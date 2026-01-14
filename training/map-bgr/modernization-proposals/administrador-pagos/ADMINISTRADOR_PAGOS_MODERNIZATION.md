# Propuesta de Modernización - Administrador de Pagos

**Fecha:** 2026-01-06  
**Aplicación:** Administrador de Pagos  
**Cliente:** BGR  
**Ponderación:** 50/100  
**Criticidad:** Alta

---

## 1. Resumen Ejecutivo

| Métrica | Valor |
|---------|-------|
| VMs Actuales | 2 |
| vCPUs Totales | 12 |
| RAM Total | 40 GB |
| Storage | ~400 GB |
| TPS | 16 |
| Usuarios | Internos (LAN) |
| Criticidad | Alta |
| Estrategia Recomendada | **Modernización ECS + Aurora PostgreSQL** |

**Hallazgo Clave:** Aplicación crítica de pagos en .NET Framework 4.7.1 que requiere refactorización a .NET Core 8. La migración de SQL Server 2022 a Aurora PostgreSQL elimina costos de licenciamiento y mejora escalabilidad. Tiene 10 vulnerabilidades (3 críticas) que deben remediarse.

---

## 2. Estado Actual

### 2.1 Infraestructura

| VM | IP | vCPUs | RAM | Storage | OS | CPU% | RAM% |
|----|-----|-------|-----|---------|-----|------|------|
| ECBRPRW44 | 172.20.1.111 | 4 | 20 GB | ~200 GB | Windows Server 2016 | 79% | 48% |
| ECBRPRW45 | 172.20.1.112 | 8 | 20 GB | ~200 GB | Windows Server 2016 | 45% | 69% |

### 2.2 Tech Stack

| Capa | Tecnología |
|------|------------|
| Frontend | ASP.NET, .NET Framework 4.7.1 |
| Backend | .NET Framework 4.7.1, IIS |
| Database | SQL Server 2022 Enterprise |
| Auth | SEGUNIXORANSERVICE |
| Ubicación | LAN (interno) |

### 2.3 Dependencias

- **Bases de datos:** BGR_CELULAR, BGRNET, PRUMINAHUI, SISTEMA_MENU_CENTRALIZADO
- **Históricos:** ~312 GB (BGR_CELULAR_HISTORICO, PRUMINAHUI_HISTORICO, BGRNET_HISTORICO)
- **Servidores BD:** ECBRPRQ71, ECBRPRCL11
- **Autenticación:** SEGUNIXORANSERVICE (on-premise)
- **Vulnerabilidades:** 10 total (3 críticas, 1 alta, 6 medias)

### 2.4 Iniciativas Relacionadas

- **Iniciativa:** Migración BDD a PostgreSQL
- **Programa:** Eficiencia 2026
- **Cambios propuestos:** Migrar a .NET Core, Migrar BD a PostgreSQL, Desacoplar a MSAPI

---

## 3. Opciones de Arquitectura

### Opción 1: Modernización ECS + Aurora PostgreSQL (Recomendada)

**Estrategia:** Replatform + Refactor

![Diagrama Modernización](./diagrams/generated-diagrams/administrador_pagos_modernization.png)

Refactorizar a .NET Core 8, containerizar en ECS Fargate y migrar BD a Aurora PostgreSQL.

| Componente | Configuración | Costo/mes |
|------------|---------------|-----------|
| ECS Fargate | 2 tasks, 1 vCPU, 2GB RAM | $60 |
| ALB | Application Load Balancer | $22.50 |
| Aurora PostgreSQL | db.r6g.large, Multi-AZ | $180 |
| ElastiCache Redis | cache.t3.small | $25 |
| ECR | Container registry | $2 |
| VPN | Site-to-Site (SEGUNIX) | $37 |
| **Total** | | **$326.50/mes** |

**Horas de implementación:** 120 horas  
**Timeline:** 6 semanas

#### 💡 Tips y Recomendaciones IA

**¿Cuándo elegir esta opción?**
- Se busca eliminar licencias SQL Server Enterprise ($$$)
- Hay iniciativa de migración a PostgreSQL aprobada
- Equipo dispuesto a refactorizar código
- Se requiere alta disponibilidad Multi-AZ

**Consideraciones importantes:**
- Requiere refactorización de .NET Framework 4.7.1 a .NET Core 8
- Migración de T-SQL a PostgreSQL (usar AWS SCT)
- Remediar 10 vulnerabilidades durante refactorización
- Mantener compatibilidad con SEGUNIXORANSERVICE

**Recomendaciones:**
- Usar AWS DMS para migración de datos con CDC
- Implementar feature flags para rollback gradual
- Ejecutar pruebas de carga antes de cutover
- Considerar Aurora Serverless v2 para optimizar costos

**Ideal para:**
- Aplicaciones críticas con roadmap de modernización
- Eliminación de licencias costosas
- Alta disponibilidad requerida

#### 📋 Esfuerzo Escala24x7

| Tarea | Horas | Equipo |
|-------|-------|--------|
| VPC/Redes | 4 | Infra |
| Fargate Cluster | 2 | Infra |
| Fargate Service (2 tasks) | 8 | Infra |
| ALB | 2 | Infra |
| Aurora PostgreSQL | 2 | Infra |
| ElastiCache Cluster | 4 | Infra |
| ECR | 1 | Infra |
| VPN Site-to-Site | 16 | Infra |
| DMS replication instance | 4 | Data |
| DMS replication task | 4 | Data |
| Application pipeline (ECS) | 4 | Infra |
| Desarrollo .NET Core | 40 | Delivery |
| CloudWatch Dashboard | 8 | Infra |
| Testing y validación | 16 | QA |
| Knowledge transfer | 5 | Infra |
| **TOTAL** | **120** | |

**Costo implementación**: 120 horas × $150/hora = **$18,000 USD**

**Ventajas:**
- Elimina licencias SQL Server Enterprise (~$15K/año)
- Escalado automático con Fargate
- Alta disponibilidad Multi-AZ nativa
- Sin gestión de servidores Windows

**Desventajas:**
- Requiere refactorización significativa
- Migración de BD compleja (312 GB históricos)
- Timeline más largo

---

### Opción 2: Lift & Shift

**Estrategia:** Rehost

![Diagrama Lift Shift](./diagrams/generated-diagrams/administrador_pagos_lift_shift.png)

Migración directa a EC2 + RDS SQL Server manteniendo arquitectura actual.

| Componente | Configuración | Costo/mes |
|------------|---------------|-----------|
| EC2 t3.xlarge | 4 vCPU, 16GB, Windows (x2) | $486 |
| ALB | Application Load Balancer | $22.50 |
| RDS SQL Server | Enterprise, db.r5.large, Multi-AZ | $850 |
| EBS gp3 | 400 GB total | $32 |
| VPN | Site-to-Site | $37 |
| **Total** | | **$1,427.50/mes** |

**Horas de implementación:** 40 horas  
**Timeline:** 3 semanas

#### 💡 Tips y Recomendaciones IA

**¿Cuándo elegir esta opción?**
- Migración urgente sin tiempo para refactorización
- Se requiere compatibilidad exacta con on-premise
- No hay presupuesto para modernización

**Consideraciones importantes:**
- Costos de licencias SQL Server Enterprise muy altos
- Mantiene deuda técnica (.NET Framework 4.7.1)
- Vulnerabilidades no se remedian automáticamente

**Recomendaciones:**
- Usar AWS MGN para migración automatizada
- Planificar modernización post-migración
- Considerar BYOL si hay licencias existentes

**Ideal para:**
- Migraciones de emergencia
- Primer paso antes de modernización
- Cumplimiento de deadlines estrictos

#### 📋 Esfuerzo Escala24x7

| Tarea | Horas | Equipo |
|-------|-------|--------|
| VPC/Redes | 4 | Infra |
| EC2 Instances (2) | 4 | Infra |
| ALB | 2 | Infra |
| RDS SQL Server | 2 | Infra |
| EBS Storage | 4 | Infra |
| VPN Site-to-Site | 16 | Infra |
| MGN Configuration | 2 | Infra |
| MGN Instances (2) | 2 | Infra |
| MGN Tests | 2 | Infra |
| Testing y validación | 8 | QA |
| Knowledge transfer | 4 | Infra |
| **TOTAL** | **50** | |

**Costo implementación**: 50 horas × $150/hora = **$7,500 USD**

**Ventajas:**
- Migración rápida (3 semanas)
- Sin cambios de código
- Menor riesgo inicial

**Desventajas:**
- Costo muy alto ($1,427/mes)
- Mantiene licencias SQL Server Enterprise
- No resuelve vulnerabilidades

---

### Opción 3: Refactor Serverless

**Estrategia:** Refactor

![Diagrama Refactor](./diagrams/generated-diagrams/administrador_pagos_refactor.png)

Descomponer en microservicios serverless con Lambda + API Gateway.

| Componente | Configuración | Costo/mes |
|------------|---------------|-----------|
| API Gateway | REST API | $15 |
| Lambda | Pagos + Calendar services | $20 |
| Aurora PostgreSQL | db.r6g.medium | $120 |
| SQS | Colas de pagos | $5 |
| VPN | Site-to-Site | $37 |
| **Total** | | **$197/mes** |

**Horas de implementación:** 200 horas  
**Timeline:** 10 semanas

#### 💡 Tips y Recomendaciones IA

**¿Cuándo elegir esta opción?**
- Estrategia de microservicios a largo plazo
- Se busca máximo ahorro de costos
- Equipo con experiencia en serverless

**Consideraciones importantes:**
- Requiere rediseño completo de arquitectura
- Mayor complejidad operativa (múltiples Lambdas)
- Límite de 15 min por ejecución puede afectar procesos batch

**Recomendaciones:**
- Usar Step Functions para orquestación de pagos
- Implementar circuit breakers para resiliencia
- Considerar EventBridge para eventos de calendario

**Ideal para:**
- Visión de largo plazo en microservicios
- Equipos DevOps maduros
- Máxima optimización de costos

#### 📋 Esfuerzo Escala24x7

| Tarea | Horas | Equipo |
|-------|-------|--------|
| VPC/Redes | 4 | Infra |
| API Gateway | 8 | Infra |
| Lambda Functions (múltiples) | 32 | Infra |
| Aurora PostgreSQL | 2 | Infra |
| SQS Queues | 4 | Infra |
| VPN Site-to-Site | 16 | Infra |
| DMS replication instance | 4 | Data |
| DMS replication task | 4 | Data |
| Step Functions | 16 | Infra |
| Desarrollo Lambdas | 64 | Delivery |
| Application pipeline (SAM) | 4 | Delivery |
| CloudWatch Dashboard | 8 | Infra |
| Testing y validación | 24 | QA |
| Knowledge transfer | 10 | Infra |
| **TOTAL** | **200** | |

**Costo implementación**: 200 horas × $150/hora = **$30,000 USD**

**Ventajas:**
- Menor costo mensual ($197)
- Escalado automático por función
- Pago por uso real

**Desventajas:**
- Mayor esfuerzo de implementación (200 hrs)
- Complejidad operativa alta
- Requiere rediseño completo

---

## 4. Comparativa

| Aspecto | Opción 1: ECS + Aurora | Opción 2: Lift & Shift | Opción 3: Serverless |
|---------|------------------------|------------------------|----------------------|
| Costo/mes | $326.50 | $1,427.50 | $197 |
| Implementación | 120 hrs | 40 hrs | 200 hrs |
| Timeline | 6 semanas | 3 semanas | 10 semanas |
| Complejidad | Media | Baja | Alta |
| Riesgo | Medio | Bajo | Medio |
| Ahorro vs On-Prem | 73% | 0% | 84% |

---

## 5. Recomendación

**Opción 1: Modernización ECS + Aurora PostgreSQL**

**Justificación:**
1. Alineada con iniciativa "Migración BDD a PostgreSQL" del programa Eficiencia 2026
2. Elimina costos de licencias SQL Server Enterprise (~$15K/año)
3. Permite remediar las 10 vulnerabilidades durante refactorización
4. Balance óptimo entre costo ($326/mes) y esfuerzo (120 hrs)
5. .NET Core 8 es el camino estratégico para BGR

**Próximos pasos:**
1. Análisis de código para migración .NET Framework → .NET Core 8
2. Evaluación de compatibilidad T-SQL → PostgreSQL con AWS SCT
3. Plan de migración de datos con AWS DMS
4. Remediación de vulnerabilidades críticas
5. Pruebas de integración con SEGUNIXORANSERVICE

---

## 6. TCO Comparativo (12 meses)

| Concepto | ECS + Aurora | Lift & Shift | Serverless |
|----------|--------------|--------------|------------|
| Implementación | $18,000 | $6,000 | $30,000 |
| Operación anual | $3,918 | $17,130 | $2,364 |
| **Total Año 1** | **$21,918** | **$23,130** | **$32,364** |
| **Total Año 2+** | **$3,918** | **$17,130** | **$2,364** |

> **Nota:** ECS + Aurora tiene ROI positivo vs Lift & Shift desde mes 3 del año 2.
