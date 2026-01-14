# Nueva Centralizada - Plan de Modernización
## Front de Configuración Centralizada BGR

**Fecha**: 2026-01-06  
**Aplicación**: Nueva Centralizada WebMasterConfiguracionBGR  
**Estrategia Recomendada**: ECS + Aurora PostgreSQL  
**Timeline**: 6 semanas

---

## 🎯 Información de la Aplicación

### Descripción
Aplicativo front de la nueva centralizada. Maneja paramétrica de configuración para sucursales BGR. Tablas tipo catálogo de configuración.

### Situación Actual

| Atributo | Valor |
|----------|-------|
| **Servidores** | ECBRPRW58, ECBRPRW59 |
| **vCPUs Totales** | 12 (6 + 6) |
| **RAM Total** | 20 GB |
| **Framework** | .NET Framework 4.7.2 |
| **Base de Datos** | SQL Server 2016 Enterprise (SEGURIDAD_OFFICE_SYSTEM) |
| **Usuarios** | Sucursales BGR |
| **Criticidad** | Baja |
| **Disponibilidad** | 0.5% (uso muy bajo) |

### ⚠️ Hallazgo Clave
- Uso muy bajo (0.5%)
- Tablas tipo catálogo (datos pequeños)
- Candidato ideal para serverless o consolidación

---

## 🏗️ Opciones de Arquitectura

### Opción 1: EC2 Lift & Shift

![Arquitectura EC2](./diagrams/generated-diagrams/nueva_centralizada_ec2.png)

| Servicio | Costo/mes |
|----------|-----------|
| EC2 t3.xlarge | $243 |
| RDS SQL Server Standard | $380 |
| ALB | $25 |
| EBS gp3 | $16 |
| CloudWatch | $10 |
| **TOTAL** | **$674/mes** |

#### 💡 Tips y Recomendaciones IA

**Cuándo elegir:**
- Migración rápida sin cambios
- Timeline agresivo
- Equipo sin experiencia en contenedores

**Consideraciones:**
- Mantiene licencias SQL Server
- Sobredimensionado para uso actual
- Sin modernización

**Recomendaciones:**
- Usar instancias más pequeñas (t3.medium)
- Evaluar Reserved Instances
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
| MGN Configuration | 2 | Infra |
| MGN Instances (2) | 2 | Infra |
| MGN Tests | 2 | Infra |
| CloudWatch Logs | 4 | Infra |
| Testing y validación | 8 | QA |
| Knowledge transfer | 4 | Infra |
| **TOTAL** | **36** | |

**Costo implementación**: 36 horas × $150/hora = **$5,400 USD**

---

### Opción 2: ECS + Aurora PostgreSQL (RECOMENDADA)

![Arquitectura ECS](./diagrams/generated-diagrams/nueva_centralizada_ecs.png)

| Servicio | Costo/mes |
|----------|-----------|
| AWS SCT | $0 |
| AWS DMS | $65 |
| ECS Fargate | $73 |
| Aurora PostgreSQL | $90 |
| ALB | $25 |
| ECR | $3 |
| Secrets Manager | $2 |
| CloudWatch | $10 |
| **TOTAL** | **$268/mes** |

#### 💡 Tips y Recomendaciones IA

**Cuándo elegir:**
- Modernización con migración a PostgreSQL
- Equipos con experiencia en contenedores
- Cuando se busca eliminar licencias

**Consideraciones:**
- BD pequeña (catálogos) - migración simple
- Aurora PostgreSQL más económico
- Escalabilidad automática

**Recomendaciones:**
- Usar Aurora Serverless v2 para más ahorro
- Containerizar a .NET Core 8
- Implementar CI/CD con CodePipeline

**Ideal para:**
- Modernización completa
- Eliminación de licencias SQL Server

#### 📋 Esfuerzo Escala24x7

| Tarea | Horas | Equipo |
|-------|-------|--------|
| VPC/Redes | 4 | Infra |
| Fargate Cluster | 2 | Infra |
| Fargate Service (2 tasks) | 8 | Infra |
| ALB | 2 | Infra |
| Aurora PostgreSQL | 2 | Infra |
| ECR | 1 | Infra |
| DMS replication instance | 4 | Data |
| DMS replication task | 4 | Data |
| Application pipeline (ECS) | 4 | Infra |
| CloudWatch Dashboard | 8 | Infra |
| Testing y validación | 16 | QA |
| Knowledge transfer | 8 | Infra |
| **TOTAL** | **63** | |

**Costo implementación**: 63 horas × $150/hora = **$9,450 USD**

---

### Opción 3: Serverless Config

![Arquitectura Serverless](./diagrams/generated-diagrams/nueva_centralizada_serverless.png)

| Servicio | Costo/mes |
|----------|-----------|
| CloudFront | $1 |
| S3 (SPA) | $0.50 |
| API Gateway | $5 |
| Lambda | $5 |
| DynamoDB | $10 |
| Secrets Manager | $2 |
| CloudWatch | $3 |
| **TOTAL** | **$26.50/mes** |

#### 💡 Tips y Recomendaciones IA

**Cuándo elegir:**
- Máxima optimización de costos
- Datos tipo catálogo (key-value)
- Equipos con experiencia serverless

**Consideraciones:**
- Cambio de SQL Server a DynamoDB
- Requiere refactoring completo
- Ideal para datos de configuración

**Recomendaciones:**
- Usar DynamoDB para catálogos
- Implementar frontend Angular/React
- Configurar caching en CloudFront

**Ideal para:**
- Máximo ahorro
- Datos de configuración simples

#### 📋 Esfuerzo Escala24x7

| Tarea | Horas | Equipo |
|-------|-------|--------|
| CloudFront Distribution | 2 | Infra |
| S3 Bucket (static) | 2 | Infra |
| API Gateway | 8 | Infra |
| Lambda Functions | 16 | Infra |
| DynamoDB Table | 2 | Infra |
| Desarrollo Lambdas | 24 | Delivery |
| Application pipeline (SAM) | 4 | Delivery |
| CloudWatch Dashboard | 8 | Infra |
| Testing y validación | 16 | QA |
| Knowledge transfer | 8 | Infra |
| **TOTAL** | **90** | |

**Costo implementación**: 90 horas × $150/hora = **$13,500 USD**

---

## 📊 Comparativa

| Criterio | EC2 Lift & Shift | ECS + Aurora | Serverless |
|----------|------------------|--------------|------------|
| **Costo/mes** | $674 | $268 | $26.50 |
| **Ahorro vs actual** | 33% | 73% | 97% |
| **Complejidad** | Baja | Media | Alta |
| **Timeline** | 2 semanas | 6 semanas | 8 semanas |
| **Recomendado** | Solo urgente | ✅ Sí | Si catálogos simples |

---

## ✅ Recomendación Final

**ECS + Aurora PostgreSQL** por:
1. Balance óptimo costo/modernización
2. Elimina licencias SQL Server
3. Escalabilidad para crecimiento
4. Migración de BD simple (catálogos)

---

**Última actualización**: 2026-01-06
