# Acciones y Accionistas - Plan de Modernización
## Gestión de Accionistas y Reportes Regulatorios

**Fecha**: 2026-01-06  
**Aplicación**: Acciones y Accionistas  
**Estrategia Recomendada**: Consolidar con Backoffice Sistemas  
**Timeline**: 1 semana

---

## 🎯 Información de la Aplicación

### Descripción
Sistema para gestión de información de accionistas (direcciones, nombres, teléfonos), transferencias de acciones y generación de reportes para la Superintendencia de Bancos.

### Situación Actual

| Atributo | Valor |
|----------|-------|
| **Servidores** | ECBRPRW44, ECBRPRW45 (compartidos con Backoffice) |
| **Framework** | .NET Framework 4.7.1 |
| **Base de Datos** | SQL Server 2016 Standard (ACCIONISTAS, ASESORES) |
| **Usuarios** | 30 |
| **Criticidad** | Media (reportes regulatorios) |
| **Disponibilidad** | 52.28% |
| **Iniciativa** | Migración BDD a PostgreSQL 2026 |

### ⚠️ Hallazgo Clave
- Comparte infraestructura con **Backoffice Sistemas**
- Genera reportes para **Superintendencia de Bancos** (regulatorio)
- BD separada (ACCIONISTAS) - puede migrarse independientemente

---

## 🏗️ Opciones de Arquitectura

### Opción 1: Consolidar con Backoffice Sistemas (RECOMENDADA)

![Arquitectura Consolidada](./diagrams/generated-diagrams/acciones_consolidate.png)

| Servicio | Costo/mes |
|----------|-----------|
| Incluido en Backoffice | $0 |
| S3 para reportes | $5 |
| CloudWatch adicional | $3 |
| **TOTAL** | **$8/mes** |

#### 💡 Tips y Recomendaciones IA

**Cuándo elegir:**
- Aplicaciones que comparten infraestructura
- Cuando la BD puede permanecer on-premise temporalmente
- Presupuesto limitado

**Consideraciones:**
- Reportes regulatorios deben generarse sin fallas
- S3 para almacenar reportes históricos
- Migración de BD puede hacerse en fase posterior

**Recomendaciones:**
- Migrar junto con Backoffice Sistemas
- Usar S3 para reportes de Superintendencia
- Planificar migración de BD ACCIONISTAS a PostgreSQL

**Ideal para:**
- Consolidación de workloads
- Migración por fases

#### 📋 Esfuerzo Escala24x7

| Tarea | Horas | Equipo |
|-------|-------|--------|
| S3 Bucket (reportes) | 2 | Infra |
| CloudWatch Logs | 4 | Infra |
| Testing integración | 4 | QA |
| Knowledge transfer | 2 | Infra |
| **TOTAL** | **12** | |

**Costo implementación**: 12 horas × $150/hora = **$1,800 USD**

---

### Opción 2: ECS + Aurora PostgreSQL

![Arquitectura ECS](./diagrams/generated-diagrams/acciones_ecs_aurora.png)

| Servicio | Costo/mes |
|----------|-----------|
| AWS SCT | $0 |
| AWS DMS | $65 |
| ECS Fargate | $73 |
| Aurora PostgreSQL | $140 |
| ALB | $25 |
| S3 | $5 |
| ECR | $3 |
| CloudWatch | $10 |
| **TOTAL** | **$321/mes** |

#### 💡 Tips y Recomendaciones IA

**Cuándo elegir:**
- Si se requiere independencia de Backoffice
- Cuando se prioriza migración a PostgreSQL
- Equipos con experiencia en contenedores

**Consideraciones:**
- BD ACCIONISTAS es pequeña (~40GB)
- Migración a PostgreSQL es directa
- Reportes regulatorios requieren alta disponibilidad

**Recomendaciones:**
- Usar AWS SCT para conversión de schema
- Implementar Multi-AZ para Aurora
- Automatizar generación de reportes con EventBridge

**Ideal para:**
- Modernización completa
- Independencia de otras aplicaciones

#### 📋 Esfuerzo Escala24x7

| Tarea | Horas | Equipo |
|-------|-------|--------|
| Fargate Cluster | 2 | Infra |
| Fargate Service | 4 | Infra |
| ALB | 2 | Infra |
| Aurora PostgreSQL | 2 | Infra |
| ECR | 1 | Infra |
| DMS replication instance | 4 | Data |
| DMS replication task | 4 | Data |
| S3 Bucket | 2 | Infra |
| Application pipeline (ECS) | 4 | Infra |
| CloudWatch Dashboard | 8 | Infra |
| Testing y validación | 16 | QA |
| Knowledge transfer | 8 | Infra |
| **TOTAL** | **57** | |

**Costo implementación**: 57 horas × $150/hora = **$8,550 USD**

---

### Opción 3: Serverless + Angular SPA

![Arquitectura Serverless](./diagrams/generated-diagrams/acciones_serverless.png)

| Servicio | Costo/mes |
|----------|-----------|
| CloudFront | $1 |
| S3 (SPA) | $0.50 |
| API Gateway | $5 |
| Lambda | $10 |
| Aurora Serverless v2 | $90 |
| S3 (Reportes) | $5 |
| CloudWatch | $5 |
| **TOTAL** | **$116.50/mes** |

#### 💡 Tips y Recomendaciones IA

**Cuándo elegir:**
- Modernización completa del frontend
- Equipos con experiencia Angular/React
- Cuando se busca máxima escalabilidad

**Consideraciones:**
- Requiere desarrollo de nuevo frontend
- Aurora Serverless escala automáticamente
- Lambda para generación de reportes

**Recomendaciones:**
- Usar AWS Amplify para desarrollo
- Implementar generación de reportes con Lambda
- Configurar EventBridge para reportes programados

**Ideal para:**
- Modernización total
- Equipos frontend modernos

#### 📋 Esfuerzo Escala24x7

| Tarea | Horas | Equipo |
|-------|-------|--------|
| CloudFront Distribution | 2 | Infra |
| S3 Bucket (SPA) | 2 | Infra |
| API Gateway | 8 | Infra |
| Lambda Functions | 16 | Infra |
| Aurora Serverless v2 | 2 | Infra |
| DMS replication instance | 4 | Data |
| DMS replication task | 4 | Data |
| Desarrollo Frontend Angular | 24 | Delivery |
| Application pipeline (S3) | 2 | Infra |
| CloudWatch Dashboard | 8 | Infra |
| Testing y validación | 16 | QA |
| Knowledge transfer | 8 | Infra |
| **TOTAL** | **96** | |

**Costo implementación**: 96 horas × $150/hora = **$14,400 USD**

---

## 📊 Comparativa

| Criterio | Consolidar | ECS + Aurora | Serverless |
|----------|------------|--------------|------------|
| **Costo/mes** | $8 | $321 | $116.50 |
| **Esfuerzo** | Ninguno | Alto | Muy Alto |
| **Timeline** | 0 | 6 semanas | 8 semanas |
| **Modernización** | Ninguna | Alta | Total |
| **Recomendado** | ✅ Sí | Si independencia | Si moderniza todo |

---

## ✅ Recomendación Final

**Consolidar con Backoffice Sistemas** por:
1. Costo mínimo ($8/mes)
2. Comparte infraestructura existente
3. Reportes regulatorios funcionan sin cambios
4. Migración de BD puede hacerse en fase posterior (2026)

---

**Última actualización**: 2026-01-06
