# Propuesta de Modernización - Visor Histórico de Cheques

**Fecha:** 2026-01-06  
**Aplicación:** Visor Histórico de Cheques  
**Cliente:** BGR  
**Ponderación:** 52/100

---

## 1. Resumen Ejecutivo

| Métrica | Valor |
|---------|-------|
| VMs Actuales | 1 (compartida con Backoffice Sistemas) |
| vCPUs | 8 |
| RAM | 10 GB |
| Storage | ~200 GB |
| Usuarios | 2 |
| Criticidad | Baja |
| Estrategia Recomendada | **Consolidar con Backoffice Sistemas** |

**Hallazgo Clave:** Esta aplicación es un **componente acoplado** de Backoffice Sistemas BGR. Comparte el mismo servidor (ECBRPRW83) y bases de datos. La recomendación es migrarla junto con Backoffice Sistemas, no de forma independiente.

---

## 2. Estado Actual

### 2.1 Infraestructura

| VM | IP | vCPUs | RAM | Storage | OS | CPU% | RAM% |
|----|-----|-------|-----|---------|-----|------|------|
| ECBRPRW83 | 172.20.1.76 | 8 | 10 GB | ~200 GB | Windows Server 2019 | 41% | 85% |

### 2.2 Tech Stack

| Capa | Tecnología |
|------|------------|
| Frontend | ASP.NET C#, .NET Core 8.0 |
| Backend | .NET Core 8.0, IIS |
| Database | SQL Server (CANJE, CANJE_HIST) - compartida |
| Auth | Active Directory |
| Ubicación | LAN (no expuesta a DMZ) |

### 2.3 Dependencias

- **Servidor compartido:** ECBRPRW83 (mismo que Backoffice Sistemas)
- **Bases de datos:** 
  - BACKOFFICE_SISTEMAS_BGR
  - CANJE / CANJE_HIST (~31 GB históricos)
  - PORTAL_ADMINISTRATIVO_BGR
- **Servidores BD:** ECBRPRCL19, ECBRPRCL13, ECBRPRQ45

---

## 3. Opciones de Arquitectura

### Opción 1: Consolidar con Backoffice Sistemas (Recomendada)

**Estrategia:** Rehost consolidado

![Diagrama Consolidar](./diagrams/generated-diagrams/visor_historico_cheques_consolidate.png)

Esta aplicación ya está desplegada en el mismo servidor que Backoffice Sistemas. La migración debe hacerse como parte del proyecto de Backoffice Sistemas.

| Componente | Configuración | Costo Incremental |
|------------|---------------|-------------------|
| EC2 (compartido) | Configuración en servidor existente | $0 |
| Storage adicional | +50 GB EBS gp3 para históricos | $4/mes |
| **Total Incremental** | | **$4/mes** |

**Horas de implementación:** 4 horas
**Timeline:** 1 semana

#### 💡 Tips y Recomendaciones IA

**¿Cuándo elegir esta opción?**
- Aplicación acoplada a otro sistema
- Comparte servidor y base de datos
- Bajo número de usuarios (2)

**Consideraciones importantes:**
- No tiene sentido migrar independientemente
- Depende de migración de Backoffice Sistemas
- Históricos de CANJE pueden crecer

**Recomendaciones:**
- Migrar junto con Backoffice Sistemas
- Considerar archivado de históricos a S3 Glacier
- Evaluar si se puede desacoplar en el futuro

**Ideal para:**
- Componentes acoplados
- Aplicaciones con pocos usuarios

#### 📋 Esfuerzo Escala24x7

| Tarea | Horas | Equipo |
|-------|-------|--------|
| CloudWatch Logs | 4 | Infra |
| Testing integración | 4 | QA |
| Knowledge transfer | 2 | Infra |
| **TOTAL** | **10** | |

**Costo implementación**: 10 horas × $150/hora = **$1,500 USD**
- Funcionalidad de consulta read-only

**Ventajas:**
- Sin costo adicional significativo
- Migración simplificada (ya incluida)
- Mantiene arquitectura actual

**Desventajas:**
- Permanece acoplado a Backoffice Sistemas
- No aprovecha modernización independiente

---

### Opción 2: Desacoplar como Microservicio

**Estrategia:** Refactor

Separar el visor como un servicio independiente con su propia API.

| Componente | Configuración | Costo/mes |
|------------|---------------|-----------|
| Lambda | 1000 invocaciones/mes, 512MB | $0.50 |
| API Gateway | REST API | $3.50 |
| RDS SQL Server | db.t3.micro (read replica) | $25 |
| S3 | Históricos archivados | $2 |
| **Total** | | **$31/mes** |

**Horas de implementación:** 40 horas

#### 💡 Tips y Recomendaciones IA

**¿Cuándo elegir esta opción?**
- Se requiere escalar independientemente
- Hay planes de exponer como API
- Se quiere desacoplar de Backoffice

**Consideraciones importantes:**
- Requiere refactorización de código
- Necesita nueva autenticación (Cognito/AD)
- Mayor complejidad operativa

**Recomendaciones:**
- Solo si hay roadmap de desacoplamiento
- Usar read replica para no afectar producción
- Implementar caching para consultas frecuentes

**Ideal para:**
- Estrategia de microservicios
- APIs públicas o internas

#### 📋 Esfuerzo Escala24x7

| Tarea | Horas | Equipo |
|-------|-------|--------|
| VPC/Redes | 4 | Infra |
| Fargate Cluster | 2 | Infra |
| Fargate Service | 4 | Infra |
| ALB | 2 | Infra |
| Aurora PostgreSQL | 2 | Infra |
| ECR | 1 | Infra |
| DMS replication instance | 4 | Data |
| DMS replication task | 4 | Data |
| Application pipeline (ECS) | 4 | Infra |
| CloudWatch Dashboard | 8 | Infra |
| Testing y validación | 16 | QA |
| Knowledge transfer | 8 | Infra |
| **TOTAL** | **59** | |

**Costo implementación**: 59 horas × $150/hora = **$8,850 USD**
- Alta demanda de consultas

**Ventajas:**
- Independencia de Backoffice Sistemas
- Escalabilidad serverless
- Costos por uso

**Desventajas:**
- Requiere refactorización
- Mayor complejidad
- Overkill para 2 usuarios

---

### Opción 3: Archivar Históricos en S3

**Estrategia:** Optimización de datos

Mover datos históricos de CANJE_HIST a S3 + Athena para consultas.

| Componente | Configuración | Costo/mes |
|------------|---------------|-----------|
| S3 Standard | 50 GB datos | $1.15 |
| S3 Glacier | Archivos >1 año | $0.20 |
| Athena | Consultas esporádicas | $2 |
| Glue Catalog | Metadatos | $1 |
| **Total** | | **$4.35/mes** |

**Horas de implementación:** 24 horas

#### 💡 Tips y Recomendaciones IA

**¿Cuándo elegir esta opción?**
- Históricos crecen significativamente
- Consultas son esporádicas
- Se quiere reducir costo de SQL Server

**Consideraciones importantes:**
- Requiere ETL para migrar datos
- Latencia mayor que SQL Server
- Cambio en patrón de consultas

**Recomendaciones:**
- Mantener últimos 6 meses en SQL Server
- Archivar resto en S3/Glacier
- Usar Athena para consultas ad-hoc

**Ideal para:**
- Datos históricos de compliance
- Consultas infrecuentes

#### 📋 Esfuerzo Escala24x7

| Tarea | Horas | Equipo |
|-------|-------|--------|
| S3 Bucket | 2 | Infra |
| Data Lake catalog (Athena/Glue) | 8 | Data |
| Data Lake ingestion (S3) | 4 | Data |
| Data Lake transform (Glue) | 8 | Data |
| Lambda Functions | 8 | Infra |
| CloudWatch Dashboard | 8 | Infra |
| Migración datos | 16 | Data |
| Testing y validación | 8 | QA |
| Knowledge transfer | 4 | Data |
| **TOTAL** | **66** | |

**Costo implementación**: 66 horas × $150/hora = **$9,900 USD**
- Optimización de costos de BD

---

## 4. Comparativa

| Aspecto | Opción 1: Consolidar | Opción 2: Microservicio | Opción 3: S3 Archive |
|---------|---------------------|------------------------|---------------------|
| Costo/mes | $4 | $31 | $4.35 |
| Implementación | 4 hrs | 40 hrs | 24 hrs |
| Complejidad | Baja | Alta | Media |
| Riesgo | Bajo | Medio | Bajo |
| Independencia | No | Sí | Parcial |

---

## 5. Recomendación

**Opción 1: Consolidar con Backoffice Sistemas**

**Justificación:**
1. La aplicación es un componente acoplado, no una aplicación independiente
2. Solo tiene 2 usuarios
3. Ya está incluida en la migración de Backoffice Sistemas
4. Costo incremental mínimo ($4/mes)
5. No justifica inversión de desacoplamiento

**Próximos pasos:**
1. ✅ Documentar como parte de Backoffice Sistemas
2. Migrar junto con Backoffice Sistemas (ya planificado)
3. Evaluar archivado de históricos post-migración

---

## 6. TCO Comparativo (12 meses)

| Concepto | Opción 1 | Opción 2 | Opción 3 |
|----------|----------|----------|----------|
| Implementación | $600 | $6,000 | $3,600 |
| Operación anual | $48 | $372 | $52 |
| **Total Año 1** | **$648** | **$6,372** | **$3,652** |
