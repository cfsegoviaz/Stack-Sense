# Plan de Modernización SARAS
## Contenedores ECS + Aurora PostgreSQL con Babelfish

**Fecha**: 2025-12-04  
**Aplicación**: SARAS  
**Objetivo**: Modernizar a contenedores ECS Fargate y migrar de SQL Server a Aurora PostgreSQL con Babelfish

---

## 🎯 Objetivos de Modernización

### Transformación de Infraestructura
- **De**: Servidores Windows con IIS (.NET Framework)
- **A**: Contenedores ECS Fargate (.NET Core/6+)

### Transformación de Base de Datos
- **De**: SQL Server On-Premise
- **A**: Aurora PostgreSQL con Babelfish

### Beneficios Esperados
- ✅ **Reducción de costos**: Eliminar licencias SQL Server y Windows
- ✅ **Escalabilidad automática**: ECS Fargate auto-scaling
- ✅ **Alta disponibilidad**: Multi-AZ nativo
- ✅ **Modernización**: Arquitectura cloud-native
- ✅ **Portabilidad**: Contenedores Docker
- ✅ **Mantenimiento reducido**: Serverless compute

---

## 📊 Recursos Actuales vs Propuestos

### Infraestructura Actual (On-Premise)

| Componente | Especificaciones |
|------------|------------------|
| **Servidor 1** | ecbrprw83 - 8 vCPU, 10GB RAM, Windows Server 2019 |
| **Servidor 2** | ecbrtsw98 - 4 vCPU, 8GB RAM, Windows Server 2019 |
| **Base de Datos** | SQL Server On-Premise |
| **Stack** | .NET Framework, IIS, Redis |
| **Total vCPUs** | 12 |
| **Total RAM** | 18 GB |

### Infraestructura Propuesta (AWS)

| Componente | Especificaciones | Cantidad |
|------------|------------------|----------|
| **ECS Fargate Tasks** | 2 vCPU, 4GB RAM cada uno | 2-4 (auto-scaling) |
| **Aurora PostgreSQL** | db.r5.large con Babelfish | 1 Primary + 1 Replica |
| **ElastiCache Redis** | cache.t3.medium | 1 |
| **Application Load Balancer** | ALB | 1 |
| **Amazon ECR** | Container Registry | 1 |

---

## 🏗️ Arquitectura Modernizada

![Arquitectura SARAS Modernizada](./generated-diagrams/saras_modernization_complete.png)

### Componentes Principales

#### 1. Herramientas de Migración
- **AWS Schema Conversion Tool (SCT)**: Analiza y convierte schemas de SQL Server a PostgreSQL
- **AWS Database Migration Service (DMS)**: Migra datos con Change Data Capture (CDC)

#### 2. Capa de Presentación
- **Application Load Balancer (ALB)**: Distribución de tráfico HTTPS
- **AWS WAF** (opcional): Protección contra ataques web

#### 3. Capa de Aplicación
- **ECS Fargate Cluster**: Contenedores serverless
  - Task 1: 2 vCPU, 4GB RAM
  - Task 2: 2 vCPU, 4GB RAM
  - Auto-scaling: 2-4 tasks según carga
- **Amazon ECR**: Registry privado de imágenes Docker

#### 4. Capa de Datos
- **Aurora PostgreSQL con Babelfish**
  - Primary: db.r5.large (2 vCPU, 16GB RAM)
  - Replica: Read-only para consultas
  - Puerto 1433 (TDS Protocol) para compatibilidad SQL Server
- **ElastiCache Redis**: Cache distribuido

#### 5. Storage y Seguridad
- **Amazon S3**: Backups, assets estáticos
- **AWS Secrets Manager**: Credenciales de base de datos
- **AWS KMS**: Encriptación de datos

#### 6. Monitoreo
- **CloudWatch**: Logs, métricas, alarmas
- **X-Ray** (opcional): Tracing distribuido

---

## 🔄 Proceso de Migración

### Fase 1: Assessment y Preparación (2 semanas)

#### Semana 1: Assessment de Aplicación
- [ ] Análisis de código .NET Framework
- [ ] Identificar dependencias de Windows
- [ ] Evaluar compatibilidad con .NET Core/6+
- [ ] Documentar APIs y endpoints
- [ ] Identificar configuraciones hardcoded

#### Semana 2: Assessment de Base de Datos
- [ ] Ejecutar AWS Schema Conversion Tool (SCT)
- [ ] Analizar compatibilidad con Babelfish
- [ ] Identificar stored procedures complejos
- [ ] Documentar triggers y funciones
- [ ] Evaluar tamaño de base de datos

**Entregables**:
- Reporte de compatibilidad .NET
- Reporte de compatibilidad Babelfish
- Plan de refactorización (si necesario)

---

### Fase 2: Containerización (3 semanas)

#### Semana 3: Preparación de Código
- [ ] Migrar a .NET 6+ (si es .NET Framework)
- [ ] Externalizar configuraciones a variables de entorno
- [ ] Implementar health checks
- [ ] Actualizar connection strings para Babelfish
- [ ] Testing local

#### Semana 4: Dockerización
- [ ] Crear Dockerfile optimizado
- [ ] Configurar multi-stage build
- [ ] Implementar .dockerignore
- [ ] Build y test de imagen local
- [ ] Optimizar tamaño de imagen

**Dockerfile ejemplo**:
```dockerfile
# Build stage
FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
WORKDIR /src
COPY ["SARAS.csproj", "./"]
RUN dotnet restore
COPY . .
RUN dotnet publish -c Release -o /app/publish

# Runtime stage
FROM mcr.microsoft.com/dotnet/aspnet:6.0
WORKDIR /app
COPY --from=build /app/publish .
EXPOSE 80
ENTRYPOINT ["dotnet", "SARAS.dll"]
```

#### Semana 5: Setup AWS
- [ ] Crear VPC y subnets
- [ ] Configurar Security Groups
- [ ] Crear ECR repository
- [ ] Push imagen a ECR
- [ ] Crear ECS Cluster y Task Definition

**Entregables**:
- Imagen Docker funcional
- Repositorio ECR configurado
- Infraestructura AWS base

---

### Fase 3: Migración de Base de Datos (3 semanas)

#### Semana 6: Preparación de Aurora
- [ ] Provisionar Aurora PostgreSQL con Babelfish
- [ ] Configurar Multi-AZ
- [ ] Habilitar puerto 1433 (TDS)
- [ ] Configurar Security Groups
- [ ] Testing de conectividad

#### Semana 7: Conversión de Schema
- [ ] Ejecutar SCT para conversión
- [ ] Revisar y ajustar schemas convertidos
- [ ] Migrar stored procedures
- [ ] Adaptar triggers y funciones
- [ ] Validar constraints y índices

#### Semana 8: Migración de Datos
- [ ] Configurar DMS replication instance
- [ ] Crear DMS endpoints (source y target)
- [ ] Ejecutar full load migration
- [ ] Habilitar CDC (Change Data Capture)
- [ ] Validar integridad de datos
- [ ] Testing de queries

**Entregables**:
- Aurora PostgreSQL con Babelfish operativo
- Datos migrados y validados
- Stored procedures funcionando

---

### Fase 4: Despliegue y Testing (2 semanas)

#### Semana 9: Despliegue en ECS
- [ ] Crear ECS Service
- [ ] Configurar ALB y Target Groups
- [ ] Configurar auto-scaling policies
- [ ] Integrar con Secrets Manager
- [ ] Configurar CloudWatch Logs
- [ ] Desplegar en ambiente de QA

#### Semana 10: Testing Integral
- [ ] Testing funcional completo
- [ ] Testing de performance
- [ ] Testing de carga (stress test)
- [ ] Validación de auto-scaling
- [ ] Testing de failover
- [ ] Ajustes y optimizaciones

**Entregables**:
- Aplicación desplegada en ECS
- Reportes de testing
- Documentación de operación

---

### Fase 5: Cutover a Producción (1 semana)

#### Semana 11: Go-Live
- [ ] Comunicación a usuarios
- [ ] Sincronización final de datos (DMS CDC)
- [ ] Actualizar DNS a ALB
- [ ] Monitoreo intensivo 24/7
- [ ] Validación con usuarios
- [ ] Desmantelar on-premise (después de 2 semanas)

**Entregables**:
- Aplicación en producción
- Runbook de operaciones
- Plan de rollback

---

## 🔧 Configuraciones Técnicas

### ECS Task Definition

```json
{
  "family": "saras-task",
  "networkMode": "awsvpc",
  "requiresCompatibilities": ["FARGATE"],
  "cpu": "2048",
  "memory": "4096",
  "containerDefinitions": [
    {
      "name": "saras-container",
      "image": "<account-id>.dkr.ecr.us-east-1.amazonaws.com/saras:latest",
      "portMappings": [
        {
          "containerPort": 80,
          "protocol": "tcp"
        }
      ],
      "environment": [
        {
          "name": "ASPNETCORE_ENVIRONMENT",
          "value": "Production"
        }
      ],
      "secrets": [
        {
          "name": "DB_CONNECTION_STRING",
          "valueFrom": "arn:aws:secretsmanager:us-east-1:<account-id>:secret:saras/db"
        }
      ],
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/saras",
          "awslogs-region": "us-east-1",
          "awslogs-stream-prefix": "ecs"
        }
      },
      "healthCheck": {
        "command": ["CMD-SHELL", "curl -f http://localhost/health || exit 1"],
        "interval": 30,
        "timeout": 5,
        "retries": 3
      }
    }
  ]
}
```

### Connection String para Babelfish

```csharp
// Babelfish usa el protocolo TDS de SQL Server en puerto 1433
var connectionString = "Server=aurora-babelfish.cluster-xxx.us-east-1.rds.amazonaws.com,1433;Database=saras;User Id=admin;Password=xxx;TrustServerCertificate=true;";
```

---

## 💰 Estimación de Costos Mensual

### Compute (ECS Fargate)
| Componente | Especificación | Horas/mes | Costo/hora | Subtotal |
|------------|----------------|-----------|------------|----------|
| Fargate Tasks (promedio 2) | 2 vCPU, 4GB | 1,460 | $0.08 | $117 |
| **Total Compute** | | | | **$117** |

### Database (Aurora PostgreSQL + Babelfish)
| Componente | Especificación | Horas/mes | Costo/hora | Subtotal |
|------------|----------------|-----------|------------|----------|
| Aurora Primary | db.r5.large | 730 | $0.40 | $292 |
| Aurora Replica | db.r5.large | 730 | $0.40 | $292 |
| Storage (100GB) | Aurora Storage | - | $0.10/GB | $10 |
| **Total Database** | | | | **$594** |

### Cache y Storage
| Componente | Especificación | Costo/mes |
|------------|----------------|-----------|
| ElastiCache Redis | cache.t3.medium | $60 |
| S3 Storage | 50GB | $1 |
| ECR Storage | 10GB | $1 |
| **Total Storage** | | **$62** |

### Networking
| Componente | Costo/mes |
|------------|-----------|
| Application Load Balancer | $23 |
| Data Transfer (estimado) | $20 |
| **Total Networking** | **$43** |

### Seguridad y Monitoreo
| Componente | Costo/mes |
|------------|-----------|
| Secrets Manager | $2 |
| CloudWatch Logs (5GB) | $3 |
| CloudWatch Alarms | $1 |
| **Total Monitoring** | **$6** |

### TOTAL MENSUAL

| Categoría | Costo |
|-----------|-------|
| Compute (ECS) | $117 |
| Database (Aurora + Babelfish) | $594 |
| Cache & Storage | $62 |
| Networking | $43 |
| Monitoring | $6 |
| **Subtotal** | **$822** |
| Contingencia (10%) | $82 |
| **TOTAL** | **$904/mes** |

### Comparativa vs On-Premise

| Concepto | On-Premise | AWS Modernizado | Ahorro |
|----------|------------|-----------------|--------|
| Licencias SQL Server | ~$500/mes | $0 | $500 |
| Licencias Windows | ~$200/mes | $0 | $200 |
| Hardware (amortizado) | ~$300/mes | $0 | $300 |
| Mantenimiento | ~$400/mes | Incluido | $400 |
| **Total** | **~$1,400/mes** | **$904/mes** | **$496/mes (35%)** |

---

## ⚠️ Riesgos y Mitigaciones

### Riesgo 1: Incompatibilidad de .NET Framework
**Probabilidad**: Media  
**Impacto**: Alto  
**Mitigación**:
- Assessment temprano de código
- Migración incremental a .NET 6+
- Testing exhaustivo en cada fase
- Plan B: Mantener .NET Framework en Windows Containers

### Riesgo 2: Features SQL Server no soportadas en Babelfish
**Probabilidad**: Media  
**Impacto**: Alto  
**Mitigación**:
- Assessment con Babelfish Compass
- Identificar features críticas
- Refactorizar stored procedures si necesario
- Fallback: RDS SQL Server (más costoso)

### Riesgo 3: Performance degradado
**Probabilidad**: Baja  
**Impacto**: Alto  
**Mitigación**:
- Testing de carga pre-producción
- Tuning de queries PostgreSQL
- Monitoring proactivo
- Auto-scaling configurado

### Riesgo 4: Downtime durante migración
**Probabilidad**: Media  
**Impacto**: Medio  
**Mitigación**:
- DMS con CDC para sincronización continua
- Blue/Green deployment
- Rollback plan documentado
- Ventana de mantenimiento planificada

---

## ✅ Criterios de Éxito

1. ✅ **Aplicación containerizada** funcionando en ECS Fargate
2. ✅ **Base de datos migrada** a Aurora PostgreSQL con Babelfish
3. ✅ **Costo mensual** <$1,000 USD
4. ✅ **Disponibilidad** >99.9%
5. ✅ **Performance** igual o mejor que on-premise
6. ✅ **Auto-scaling** funcionando correctamente
7. ✅ **Cero cambios** en lógica de negocio
8. ✅ **Equipo capacitado** en operación de contenedores

---

## 📚 Recursos y Documentación

### AWS Documentation
- [ECS Fargate Best Practices](https://docs.aws.amazon.com/AmazonECS/latest/bestpracticesguide/)
- [Aurora PostgreSQL Babelfish](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html)
- [AWS Schema Conversion Tool](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/)
- [AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/)

### Training Recomendado
- AWS Container Services (ECS/Fargate)
- Aurora PostgreSQL Administration
- Babelfish for SQL Server Compatibility
- Docker and Container Best Practices

---

## 👥 Equipo Necesario

### Core Team (Tiempo Completo)

#### AWS Solutions Architect (1)
**Responsabilidades**:
- Diseño de arquitectura ECS + Aurora
- Configuración de networking y seguridad
- Optimización de costos
**Duración**: 11 semanas

#### DevOps Engineer (1)
**Responsabilidades**:
- Containerización de aplicación
- CI/CD pipeline
- Configuración ECS y ECR
**Duración**: 11 semanas

#### Database Migration Specialist (1)
**Responsabilidades**:
- Migración con SCT y DMS
- Tuning de Aurora PostgreSQL
- Validación de datos
**Duración**: 8 semanas

### Support Team (Tiempo Parcial)

#### .NET Developer (1)
**Responsabilidades**: Refactorización de código si necesario  
**Duración**: 4 semanas (50%)

#### DBA SQL Server (1)
**Responsabilidades**: Validación de queries y stored procedures  
**Duración**: 4 semanas (50%)

#### QA Engineer (1)
**Responsabilidades**: Testing funcional y de performance  
**Duración**: 3 semanas (100%)

---

## 📅 Timeline Resumido

| Fase | Duración | Hitos Principales |
|------|----------|-------------------|
| **Fase 1: Assessment** | 2 semanas | Reportes de compatibilidad |
| **Fase 2: Containerización** | 3 semanas | Imagen Docker en ECR |
| **Fase 3: Migración DB** | 3 semanas | Aurora con datos migrados |
| **Fase 4: Testing** | 2 semanas | Aplicación validada en QA |
| **Fase 5: Producción** | 1 semana | Go-live exitoso |
| **TOTAL** | **11 semanas** | **Aplicación modernizada** |

---

## 🎯 Próximos Pasos

1. [ ] Aprobar plan de modernización
2. [ ] Asignar equipo de proyecto
3. [ ] Iniciar assessment de código .NET
4. [ ] Ejecutar Babelfish Compass en SQL Server
5. [ ] Crear ambiente de desarrollo en AWS
6. [ ] Kick-off del proyecto

---

**Última actualización**: 2025-12-04  
**Versión**: 1.0  
**Estado**: Propuesta para aprobación
