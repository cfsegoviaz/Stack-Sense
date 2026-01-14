# BGRTuCuenta - Plan de Modernización
## Portal de Cargas Masivas para Creación de Cuentas

**Fecha**: 2026-01-06  
**Aplicación**: BGRTuCuenta  
**Estrategia Recomendada**: ECS + Aurora Babelfish  
**Timeline**: 8 semanas

---

## 🎯 Información de la Aplicación

### Descripción
Portal donde se realizan cargas masivas para creación de cuentas bancarias. Procesa archivos bulk con datos de clientes para apertura automatizada de cuentas.

### Situación Actual

| Atributo | Valor |
|----------|-------|
| **Servidores** | ECBRPRWE27, ECBRPRWE31 |
| **vCPUs Totales** | 8 (4 + 4) |
| **RAM Total** | 16 GB |
| **Framework** | .NET Framework 4.7.1 |
| **Base de Datos** | SQL Server 2016 Enterprise (BDD_BGR_PRODUCTOS, CATALOGOSERVICIOSBGR) |
| **Usuarios** | 75 operadores |
| **Criticidad** | Baja |
| **Iniciativa** | Generador de Plantillas y Contratos 2027 |

---

## 🏗️ Opciones de Arquitectura

### Opción 1: ECS + Aurora Babelfish (RECOMENDADA)

![Arquitectura ECS](./diagrams/generated-diagrams/bgr_tucuenta_ecs.png)

| Servicio | Configuración | Costo/mes |
|----------|---------------|-----------|
| AWS SCT | Schema Conversion | $0 |
| AWS DMS | CDC Replication | $130 |
| ECS Fargate | 2 tasks x 2 vCPU, 4 GB | $147 |
| Aurora PostgreSQL + Babelfish | db.r6g.large | $280 |
| Application Load Balancer | HTTPS | $25 |
| Amazon S3 | Bulk files | $10 |
| Amazon SQS | Processing queue | $5 |
| Amazon ECR | Registry | $5 |
| CloudWatch | Logs | $15 |
| **TOTAL** | | **$617/mes** |

#### 💡 Tips y Recomendaciones IA

**Cuándo elegir:**
- Procesamiento batch con picos de carga
- Cuando se busca eliminar licencias SQL Server
- Alineación con iniciativa 2027

**Consideraciones:**
- Babelfish mantiene compatibilidad T-SQL
- SQS para desacoplar procesamiento batch
- Auto-scaling para picos de carga masiva

**Recomendaciones:**
- Usar S3 para upload de archivos bulk
- Implementar SQS para cola de procesamiento
- Configurar auto-scaling basado en cola

**Ideal para:**
- Modernización con compatibilidad SQL
- Procesamiento batch escalable

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
| SQS Queue | 4 | Infra |
| DMS replication instance | 4 | Data |
| DMS replication task | 4 | Data |
| Application pipeline (ECS) | 4 | Infra |
| CloudWatch Dashboard | 8 | Infra |
| Testing y validación | 16 | QA |
| Knowledge transfer | 8 | Infra |
| **TOTAL** | **71** | |

**Costo implementación**: 71 horas × $150/hora = **$10,650 USD**

---

### Opción 2: EC2 Lift & Shift

![Arquitectura EC2](./diagrams/generated-diagrams/bgr_tucuenta_ec2.png)

| Servicio | Configuración | Costo/mes |
|----------|---------------|-----------|
| EC2 t3.large | 2 instancias Windows | $152 |
| RDS SQL Server Standard | db.m5.large | $380 |
| Application Load Balancer | HTTPS | $25 |
| Amazon S3 | Bulk files | $10 |
| EBS gp3 | 200 GB | $16 |
| CloudWatch | Logs | $10 |
| **TOTAL** | | **$593/mes** |

#### 💡 Tips y Recomendaciones IA

**Cuándo elegir:**
- Migración rápida con mínimo riesgo
- Timeline agresivo
- Equipo sin experiencia en contenedores

**Consideraciones:**
- Mantiene licencias SQL Server
- Sin modernización del stack
- Migración simple con AWS MGN

**Recomendaciones:**
- Usar AWS MGN para migración
- Configurar S3 para archivos bulk
- Planificar modernización posterior

**Ideal para:**
- Migraciones rápidas
- Paso intermedio

#### 📋 Esfuerzo Escala24x7

| Tarea | Horas | Equipo |
|-------|-------|--------|
| VPC/Redes | 4 | Infra |
| EC2 Instances (2) | 4 | Infra |
| ALB | 2 | Infra |
| RDS SQL Server | 2 | Infra |
| EBS Storage | 2 | Infra |
| S3 Bucket | 2 | Infra |
| MGN Configuration | 2 | Infra |
| MGN Instances (2) | 2 | Infra |
| MGN Tests | 2 | Infra |
| CloudWatch Logs | 4 | Infra |
| Testing y validación | 8 | QA |
| Knowledge transfer | 4 | Infra |
| **TOTAL** | **38** | |

**Costo implementación**: 38 horas × $150/hora = **$5,700 USD**

---

### Opción 3: Serverless Batch Processing

![Arquitectura Serverless](./diagrams/generated-diagrams/bgr_tucuenta_serverless.png)

| Servicio | Configuración | Costo/mes |
|----------|---------------|-----------|
| API Gateway | REST API | $5 |
| AWS Lambda | 3 funciones | $25 |
| Step Functions | Workflow | $30 |
| Amazon S3 | Bulk files | $15 |
| DynamoDB | Accounts data | $40 |
| Amazon SQS | Queue | $5 |
| Amazon SNS | Notifications | $3 |
| CloudWatch | Logs | $10 |
| **TOTAL** | | **$133/mes** |

#### 💡 Tips y Recomendaciones IA

**Cuándo elegir:**
- Procesamiento batch puro
- Máxima optimización de costos
- Equipos con experiencia serverless

**Consideraciones:**
- Requiere refactoring completo
- Cambio de SQL Server a DynamoDB
- Lambda límite 15 min por ejecución

**Recomendaciones:**
- Usar Step Functions para orquestación
- Particionar archivos grandes
- Implementar DLQ para errores

**Ideal para:**
- Máximo ahorro
- Procesamiento event-driven

#### 📋 Esfuerzo Escala24x7

| Tarea | Horas | Equipo |
|-------|-------|--------|
| VPC/Redes | 4 | Infra |
| API Gateway | 8 | Infra |
| Lambda Functions (3) | 24 | Infra |
| Step Functions | 16 | Infra |
| S3 Bucket | 2 | Infra |
| DynamoDB Tables | 4 | Infra |
| SQS Queue | 4 | Infra |
| SNS Topic | 4 | Infra |
| Desarrollo Lambdas | 48 | Delivery |
| Application pipeline (SAM) | 4 | Delivery |
| CloudWatch Dashboard | 8 | Infra |
| Testing y validación | 24 | QA |
| Knowledge transfer | 10 | Infra |
| **TOTAL** | **160** | |

**Costo implementación**: 160 horas × $150/hora = **$24,000 USD**

---

## 📊 Comparativa

| Criterio | ECS + Babelfish | EC2 Lift & Shift | Serverless |
|----------|-----------------|------------------|------------|
| **Costo/mes** | $617 | $593 | $133 |
| **Ahorro vs actual** | 59% | 60% | 91% |
| **Complejidad** | Alta | Baja | Muy Alta |
| **Timeline** | 8 semanas | 3 semanas | 12 semanas |
| **Recomendado** | ✅ Sí | Solo urgente | Si es batch puro |

---

## ✅ Recomendación Final

**ECS + Aurora Babelfish** por:
1. Elimina licencias SQL Server Enterprise
2. Escalabilidad para cargas masivas
3. Alineado con iniciativa Generador Plantillas 2027
4. Compatibilidad T-SQL con Babelfish

---

**Última actualización**: 2026-01-06
