# Cuadre y Compensación ATMs - Plan de Modernización

**Fecha**: 2026-01-06  
**Aplicación**: Cuadre y Compensación ATMs  
**Estrategia Recomendada**: Replatform (ECS + Aurora Babelfish)  
**Timeline**: 8 semanas

---

## 🎯 Información de la Aplicación

### Descripción
Sistema de cuadre y compensación de cajeros automáticos. Procesa archivos emitidos por ATMs, Host, Banred y Mastercard para conciliación de transacciones.

### Situación Actual (On-Premise)

| Atributo | Valor |
|----------|-------|
| **Servidores App** | ECBRPRW47, ECBRPRW48 |
| **Servidor Legacy** | ECBRPRW30 (Windows 2003 ⚠️) |
| **vCPUs Totales** | 9 (4 + 4 + 1) |
| **RAM Total** | 18 GB |
| **Storage** | ~200 GB |
| **OS** | Windows Server 2016 / 2003 |
| **Framework** | .NET Framework 4.7.1 |
| **Base de Datos** | SQL Server 2016 Enterprise (ATM_HIS ~100GB) |
| **Usuarios** | 50 (operadores ATM) |
| **Criticidad** | Media |
| **Disponibilidad** | 99.43% |

### Stack Tecnológico

- **Frontend**: ASP.NET Web Forms
- **Backend**: C# .NET Framework 4.7.1
- **Database**: SQL Server 2016 Enterprise (ATM_HIS)
- **Integraciones**: Banred, Mastercard, Host bancario

---

## 🏗️ Opciones de Arquitectura

### Opción 1: ECS Fargate + Aurora Babelfish (RECOMENDADA)

![Arquitectura ECS Babelfish](./diagrams/generated-diagrams/cuadre_atms_ecs_babelfish.png)

#### Componentes
| Servicio | Configuración | Costo/mes |
|----------|---------------|-----------|
| AWS SCT | Schema Conversion Tool | $0 |
| AWS DMS | CDC Replication | $130 |
| ECS Fargate | 2 tasks x 2 vCPU, 4 GB | $147 |
| Aurora PostgreSQL + Babelfish | db.r6g.large | $280 |
| Application Load Balancer | HTTPS | $25 |
| Amazon ECR | Registry | $5 |
| Amazon S3 | Archivos ATM/Banred | $10 |
| CloudWatch | Logs y métricas | $15 |
| **TOTAL** | | **$612/mes** |

#### Ventajas
- ✅ Elimina licencias SQL Server Enterprise (~$15K/año)
- ✅ Babelfish mantiene compatibilidad T-SQL
- ✅ Auto-scaling para picos de procesamiento
- ✅ Alta disponibilidad Multi-AZ

#### Desventajas
- ❌ Requiere containerización
- ❌ Migración de BD compleja
- ❌ Timeline más largo

#### 💡 Tips y Recomendaciones IA

**Cuándo elegir:**
- Equipos con experiencia en contenedores
- Cuando se busca eliminar licencias SQL Server
- Proyectos con presupuesto para modernización

**Consideraciones:**
- Babelfish soporta ~95% de T-SQL
- Usar AWS SCT para análisis de compatibilidad
- Planificar ventana de migración con DMS CDC

**Recomendaciones:**
- Ejecutar assessment con SCT primero
- Containerizar .NET a .NET Core 8
- Configurar auto-scaling para fin de mes

**Ideal para:**
- Modernización completa del stack
- Eliminación de costos de licenciamiento

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

### Opción 2: EC2 Lift & Shift

![Arquitectura EC2](./diagrams/generated-diagrams/cuadre_atms_ec2_lift_shift.png)

#### Componentes
| Servicio | Configuración | Costo/mes |
|----------|---------------|-----------|
| EC2 t3.large | 2 instancias Windows | $152 |
| RDS SQL Server Standard | db.m5.large | $380 |
| Application Load Balancer | HTTPS | $25 |
| EBS gp3 | 200 GB | $16 |
| Amazon S3 | Archivos | $10 |
| CloudWatch | Logs | $10 |
| **TOTAL** | | **$593/mes** |

#### 💡 Tips y Recomendaciones IA

**Cuándo elegir:**
- Migración urgente con mínimo riesgo
- Equipo sin experiencia en contenedores
- Timeline agresivo

**Consideraciones:**
- Mantiene costos de licencias SQL Server
- Sin modernización del stack
- Requiere mantenimiento de servidores

**Recomendaciones:**
- Usar AWS MGN para migración automatizada
- Configurar Multi-AZ para RDS
- Planificar modernización posterior

**Ideal para:**
- Migraciones rápidas
- Equipos tradicionales

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

![Arquitectura Serverless](./diagrams/generated-diagrams/cuadre_atms_serverless.png)

#### Componentes
| Servicio | Configuración | Costo/mes |
|----------|---------------|-----------|
| API Gateway | REST API | $5 |
| AWS Lambda | 3 funciones | $20 |
| Step Functions | Orquestador | $25 |
| Amazon S3 | Input/Output | $15 |
| DynamoDB | Resultados | $30 |
| Amazon SQS | Cola de procesamiento | $5 |
| CloudWatch | Logs | $10 |
| **TOTAL** | | **$110/mes** |

#### 💡 Tips y Recomendaciones IA

**Cuándo elegir:**
- Procesamiento batch sin interacción en tiempo real
- Equipos con experiencia serverless
- Máxima optimización de costos

**Consideraciones:**
- Requiere refactoring completo
- Lambda tiene límite de 15 min
- Cambio de paradigma de BD relacional a NoSQL

**Recomendaciones:**
- Evaluar si el proceso es realmente batch
- Usar Step Functions para orquestación
- Implementar DLQ para manejo de errores

**Ideal para:**
- Procesos batch puros
- Máximo ahorro de costos

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
| Desarrollo Lambdas | 48 | Delivery |
| Application pipeline (SAM) | 4 | Delivery |
| CloudWatch Dashboard | 8 | Infra |
| Testing y validación | 24 | QA |
| Knowledge transfer | 10 | Infra |
| **TOTAL** | **156** | |

**Costo implementación**: 156 horas × $150/hora = **$23,400 USD**

---

## 📊 Comparativa

| Criterio | ECS + Babelfish | EC2 Lift & Shift | Serverless |
|----------|-----------------|------------------|------------|
| **Costo/mes** | $612 | $593 | $110 |
| **Ahorro vs actual** | 59% | 60% | 93% |
| **Complejidad** | Alta | Baja | Muy Alta |
| **Timeline** | 8 semanas | 3 semanas | 12 semanas |
| **Modernización** | Alta | Ninguna | Total |
| **Recomendado** | ✅ Sí | Solo urgente | Si es batch puro |

---

## ✅ Recomendación Final

**ECS + Aurora Babelfish** por:
1. Elimina licencias SQL Server Enterprise
2. Compatibilidad T-SQL con Babelfish
3. Escalabilidad para picos de fin de mes
4. Alineado con iniciativa Cámara de Compensación 2028

---

**Última actualización**: 2026-01-06
