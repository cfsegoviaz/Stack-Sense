# Estructuras de Control - Plan de Modernización
## Generación de Estructuras Regulatorias

**Fecha**: 2026-01-06  
**Aplicación**: Estructuras de Control  
**Estrategia Recomendada**: ECS + Aurora Babelfish  
**Timeline**: 10 semanas

---

## 🎯 Información de la Aplicación

### Descripción
Aplicativo para parametrización de catálogos de homologación y generación de estructuras hacia entes de control (Superintendencia de Bancos, SRI, etc.).

### Situación Actual

| Atributo | Valor |
|----------|-------|
| **Servidores** | ECBRPRW44, ECBRPRW45 (compartidos) |
| **Framework** | .NET Framework 4.7.1 |
| **Base de Datos** | SQL Server 2016 Enterprise (ESTRUCTURAS_CONTROL_BGR ~172GB) |
| **Usuarios** | 75 |
| **Criticidad** | Media (reportes regulatorios) |
| **Iniciativa** | Estructuras de Control y Regulatorios 2026 |

### ⚠️ Hallazgo Clave
- BD grande (~172GB) con datos históricos
- Genera reportes regulatorios críticos
- Tiene iniciativa de modernización 2026
- Candidato ideal para Data Lake

---

## 🏗️ Opciones de Arquitectura

### Opción 1: Consolidar con Backoffice Sistemas

![Arquitectura Consolidada](./diagrams/generated-diagrams/estructuras_consolidate.png)

| Servicio | Costo/mes |
|----------|-----------|
| Incluido en Backoffice | $0 |
| S3 para estructuras | $10 |
| CloudWatch | $5 |
| **TOTAL** | **$15/mes** |

#### 💡 Tips y Recomendaciones IA

**Cuándo elegir:**
- Migración rápida sin modernización
- Presupuesto muy limitado
- Como paso intermedio

**Consideraciones:**
- BD permanece on-premise
- Sin modernización de reportes
- Dependencia de Backoffice

**Recomendaciones:**
- Solo como paso temporal
- Planificar modernización posterior
- Usar S3 para almacenar estructuras generadas

**Ideal para:**
- Migración por fases
- Presupuesto limitado

#### 📋 Esfuerzo Escala24x7

| Tarea | Horas | Equipo |
|-------|-------|--------|
| S3 Bucket | 2 | Infra |
| CloudWatch Logs | 4 | Infra |
| Testing integración | 4 | QA |
| Knowledge transfer | 2 | Infra |
| **TOTAL** | **12** | |

**Costo implementación**: 12 horas × $150/hora = **$1,800 USD**

---

### Opción 2: ECS + Aurora Babelfish (RECOMENDADA)

![Arquitectura ECS](./diagrams/generated-diagrams/estructuras_ecs_babelfish.png)

| Servicio | Costo/mes |
|----------|-----------|
| AWS SCT | $0 |
| AWS DMS | $130 |
| ECS Fargate | $147 |
| Aurora PostgreSQL + Babelfish | $350 |
| ALB | $25 |
| S3 | $20 |
| ECR | $5 |
| CloudWatch | $15 |
| **TOTAL** | **$692/mes** |

#### 💡 Tips y Recomendaciones IA

**Cuándo elegir:**
- Alineación con iniciativa 2026
- Cuando se busca eliminar licencias SQL Server
- Modernización con compatibilidad T-SQL

**Consideraciones:**
- BD grande (~172GB) requiere planificación de migración
- Babelfish mantiene compatibilidad T-SQL
- Reportes regulatorios requieren alta disponibilidad

**Recomendaciones:**
- Usar AWS DMS con CDC para migración
- Implementar Multi-AZ para Aurora
- Automatizar generación de estructuras con EventBridge

**Ideal para:**
- Modernización alineada con iniciativa 2026
- Eliminación de licencias SQL Server

#### 📋 Esfuerzo Escala24x7

| Tarea | Horas | Equipo |
|-------|-------|--------|
| VPC/Redes | 4 | Infra |
| Fargate Cluster | 2 | Infra |
| Fargate Service (2 tasks) | 8 | Infra |
| ALB | 2 | Infra |
| Aurora PostgreSQL + Babelfish | 4 | Infra |
| ECR | 1 | Infra |
| S3 Bucket | 2 | Infra |
| DMS replication instance | 4 | Data |
| DMS replication task | 4 | Data |
| Application pipeline (ECS) | 4 | Infra |
| CloudWatch Dashboard | 8 | Infra |
| Testing y validación | 16 | QA |
| Knowledge transfer | 8 | Infra |
| **TOTAL** | **67** | |

**Costo implementación**: 67 horas × $150/hora = **$10,050 USD**

---

### Opción 3: Data Lake + Athena

![Arquitectura Data Lake](./diagrams/generated-diagrams/estructuras_datalake.png)

| Servicio | Costo/mes |
|----------|-----------|
| API Gateway | $5 |
| AWS Glue | $50 |
| Amazon Athena | $30 |
| S3 Data Lake | $40 |
| QuickSight | $24 |
| Lambda | $10 |
| CloudWatch | $10 |
| **TOTAL** | **$169/mes** |

#### 💡 Tips y Recomendaciones IA

**Cuándo elegir:**
- Cuando se busca arquitectura analítica moderna
- Equipos con experiencia en Data Lake
- Máxima flexibilidad para reportes

**Consideraciones:**
- Cambio de paradigma (OLTP a OLAP)
- Requiere rediseño de procesos
- QuickSight para dashboards interactivos

**Recomendaciones:**
- Usar Glue para ETL de datos
- Implementar particionamiento en S3
- Configurar Athena para queries ad-hoc

**Ideal para:**
- Arquitectura analítica moderna
- Máxima flexibilidad de reportes

#### 📋 Esfuerzo Escala24x7

| Tarea | Horas | Equipo |
|-------|-------|--------|
| S3 Bucket | 2 | Infra |
| Data Lake catalog (Athena/Glue) | 8 | Data |
| Data Lake ingestion (S3) | 4 | Data |
| Data Lake transform (Glue) | 8 | Data |
| Quicksight data source | 4 | Data |
| Quicksight dataset | 4 | Data |
| Quicksight dashboards | 8 | Data |
| Lambda Functions | 16 | Infra |
| CloudWatch Dashboard | 8 | Infra |
| Testing y validación | 16 | QA |
| Knowledge transfer | 8 | Data |
| **TOTAL** | **86** | |

**Costo implementación**: 86 horas × $150/hora = **$12,900 USD**

---

## 📊 Comparativa

| Criterio | Consolidar | ECS + Babelfish | Data Lake |
|----------|------------|-----------------|-----------|
| **Costo/mes** | $15 | $692 | $169 |
| **Modernización** | Ninguna | Alta | Total |
| **Timeline** | 1 semana | 10 semanas | 12 semanas |
| **Alineación 2026** | No | ✅ Sí | Parcial |
| **Recomendado** | Solo temporal | ✅ Sí | Si analítica |

---

## ✅ Recomendación Final

**ECS + Aurora Babelfish** por:
1. Alineado con iniciativa Estructuras 2026
2. Elimina licencias SQL Server Enterprise
3. Compatibilidad T-SQL con Babelfish
4. Alta disponibilidad para reportes regulatorios

---

**Última actualización**: 2026-01-06
