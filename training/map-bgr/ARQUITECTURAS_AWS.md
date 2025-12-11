# Arquitecturas AWS Híbridas - Aplicaciones BGR

**Fecha**: 2025-12-04  
**Aplicaciones**: Saras, SonarQube, API Portal, Portal Guía BGR  
**Modelo**: **Bases de Datos On-Premise + Compute en AWS**

---

## ⚠️ REGLA CRÍTICA: Bases de Datos On-Premise

**BGR ha manifestado que las bases de datos deberán continuar on-premise por temas de dependencias.**

### Implicaciones:
- ✅ Compute (EC2) en AWS
- ✅ Storage (S3, EFS) en AWS
- ✅ Cache (ElastiCache) en AWS
- ❌ Bases de datos permanecen on-premise
- ✅ Conectividad híbrida: Direct Connect + VPN

---

## 1. Saras - Aplicación Empresarial

### 📊 Recursos Actuales
- **VMs**: 2
- **vCPUs**: 12
- **RAM**: 18 GB
- **Stack**: .NET/IIS + SQL Server

### 🏗️ Arquitectura AWS Híbrida Propuesta

![Saras Architecture](diagrams/saras_architecture.png)

#### Componentes Principales

**Compute (AWS)**
- Auto Scaling Group: Min 2, Desired 2, Max 4
- EC2 t3.medium (2 vCPU, 4 GB RAM)
- Application Load Balancer (ALB) para distribución de tráfico
- Multi-AZ deployment (us-east-1a, us-east-1b)
- Target Tracking: CPU 50%

**Database (On-Premise)**
- SQL Server (permanece on-premise)
- Conectividad vía Direct Connect + VPN backup
- Latencia < 10ms

**Conectividad Híbrida**
- AWS Direct Connect 1 Gbps (compartido)
- VPN Site-to-Site (backup automático)
- Virtual Private Gateway en VPC
- Customer Gateway on-premise

**Database**
- RDS SQL Server Multi-AZ (t3.medium)
- Automated backups (7 días retención)
- Encryption at rest con KMS

**Storage**
- EBS gp3 para discos de aplicación (100 GB por instancia)
- S3 para backups y archivos estáticos

**Security**
- AWS Secrets Manager para credenciales
- Security Groups con least privilege
- VPC con subnets públicas y privadas

**Monitoring**
- CloudWatch Logs y Metrics
- CloudWatch Alarms para CPU, memoria, disco
- SNS para notificaciones de alertas

#### Flujo de Tráfico
```
Usuarios Internos → Route 53 → ALB → EC2 Instances (AZ1/AZ2) → RDS SQL Server
                                  ↓
                            Secrets Manager
                                  ↓
                            CloudWatch → SNS
```

### 💰 Estimación de Costos (us-east-1)
- **Compute (EC2)**: ~$120/mes
- **Load Balancer**: ~$25/mes
- **Storage (S3)**: ~$10/mes
- **Data Transfer**: ~$20/mes
- **CI/CD (CodeDeploy + S3 artifacts)**: ~$25/mes
- **Monitoring (CloudWatch)**: ~$20/mes
- **Conectividad Híbrida (25% compartido)**: ~$75/mes
- **Total**: **~$296/mes**
- **Con Reserved Instances**: **~$256/mes**

**Ahorro vs RDS en AWS**: +$329/mes (eliminado RDS SQL Server $180/mes, agregado híbrido $75/mes)

---

## 2. SonarQube - Herramienta DevOps

### 📊 Recursos Actuales
- **VMs**: 5 (1 restore backup)
- **vCPUs**: 42
- **RAM**: 144 GB
- **Stack**: .NET/IIS + SQL Server

### 🏗️ Arquitectura AWS Propuesta

![SonarQube Architecture](diagrams/sonarqube_architecture.png)

#### Componentes Principales

**Compute**
- Auto Scaling Group: Min 2, Desired 2, Max 4
- EC2 t3.large (2 vCPU, 8 GB RAM)
- Application Load Balancer (ALB)
- Multi-AZ deployment (us-east-1a, us-east-1b)
- Target Tracking: CPU 50%
- Sticky Sessions: 1 hora (session affinity)

**Database**
- RDS PostgreSQL Multi-AZ (t3.large)
- Automated backups (14 días retención)
- Encryption at rest

**Storage**
- EFS para datos compartidos entre instancias
- S3 para reportes de análisis y backups
- EBS gp3 para discos locales

**CI/CD Integration**
- Integración con CodeBuild
- Integración con CodeCommit
- Webhooks para análisis automático

**Security & Monitoring**
- Secrets Manager para tokens y credenciales
- CloudWatch para logs y métricas
- Security Groups restrictivos

#### Flujo de Tráfico
```
Developers → Route 53 → ALB → SonarQube Instances → RDS PostgreSQL
                                      ↓
                                    EFS (shared data)
                                      ↓
                                S3 (analysis reports)
                                      ↓
CodeBuild/CodeCommit → ALB (webhooks)
```

### 💰 Estimación de Costos (us-east-1)
- **Compute (EC2)**: ~$300/mes
- **Database (RDS)**: ~$350/mes
- **Storage (EFS + S3 + EBS)**: ~$200/mes
- **Load Balancer**: ~$25/mes
- **Data Transfer**: ~$25/mes
- **CI/CD (CodeDeploy + S3 artifacts)**: ~$25/mes
- **Total**: **~$1,225/mes**

---

## 3. API Portal - Portal Web de Alta Criticidad

### 📊 Recursos Actuales
- **VMs**: 5
- **vCPUs**: 42
- **RAM**: 144 GB
- **Stack**: .NET/IIS + SQL Server

### 🏗️ Arquitectura AWS Propuesta

![API Portal Architecture](diagrams/api_portal_architecture.png)

#### Componentes Principales

**Edge & Security**
- CloudFront para CDN global
- AWS WAF para protección contra ataques
- API Gateway para gestión de APIs

**Compute**
- Auto Scaling Group: Min 2, Desired 3, Max 8
- EC2 t3.medium (2 vCPU, 4 GB RAM)
- Application Load Balancer (ALB)
- Multi-AZ deployment (us-east-1a, us-east-1b)
- Target Tracking: CPU 50% + Request Count 1000/target
- Scheduled Scaling: 4 instancias en horario laboral, 2 fuera de horario

**Database**
- RDS SQL Server Multi-AZ (t3.large)
- Read replicas para consultas
- Automated backups (30 días)

**Cache Layer**
- ElastiCache for Redis (cache.t3.medium)
- Session management
- API response caching

**Storage**
- S3 para assets estáticos
- CloudFront integration
- Versioning habilitado

**Monitoring & Tracing**
- CloudWatch Logs y Metrics
- X-Ray para distributed tracing
- CloudWatch Alarms
- Secrets Manager para credenciales

#### Flujo de Tráfico
```
External Users → Route 53 → WAF → CloudFront → API Gateway → ALB
                                                                ↓
                                                    EC2 Auto Scaling Group
                                                                ↓
                                                    ElastiCache (Redis)
                                                                ↓
                                                    RDS SQL Server
                                                                ↓
                                                    X-Ray → CloudWatch
```

### 💰 Estimación de Costos (us-east-1)
- **Compute (EC2 Auto Scaling)**: ~$600/mes
- **Database (RDS + Replicas)**: ~$700/mes
- **Cache (ElastiCache)**: ~$150/mes
- **CDN (CloudFront)**: ~$200/mes
- **API Gateway**: ~$100/mes
- **WAF**: ~$50/mes
- **Load Balancer**: ~$25/mes
- **Storage & Transfer**: ~$75/mes
- **CI/CD (CodeDeploy + S3 artifacts)**: ~$30/mes
- **Total**: **~$2,830/mes**

---

## 4. Portal Guía BGR - Portal Web de Alta Criticidad

### 📊 Recursos Actuales
- **VMs**: 5
- **vCPUs**: 42
- **RAM**: 144 GB
- **Stack**: .NET/IIS + SQL Server

### 🏗️ Arquitectura AWS Propuesta

![Portal Guía Architecture](diagrams/portal_guia_architecture.png)

#### Componentes Principales

**Edge & Security**
- CloudFront para CDN global
- AWS WAF para protección DDoS y OWASP Top 10
- AWS Shield Advanced para protección DDoS avanzada

**Compute**
- Auto Scaling Group: Min 2, Desired 3, Max 8
- EC2 t3.medium (2 vCPU, 4 GB RAM)
- Application Load Balancer (ALB)
- Multi-AZ deployment (us-east-1a, us-east-1b)
- Target Tracking: CPU 50% + Request Count 1000/target
- Scheduled Scaling: 4 instancias en horario laboral, 2 fuera de horario

**Database**
- RDS SQL Server Multi-AZ (t3.xlarge)
- Read Replica para consultas de solo lectura
- Automated backups (30 días)
- Point-in-time recovery

**Cache Layer**
- ElastiCache for Redis (cache.t3.medium)
- Session management
- Page caching
- Multi-AZ deployment

**Storage**
- S3 para contenido estático (imágenes, CSS, JS)
- S3 para backups con lifecycle policies
- CloudFront integration
- Versioning y MFA Delete habilitado

**Security & Monitoring**
- Secrets Manager para credenciales
- CloudWatch Logs y Metrics
- CloudWatch Alarms para métricas críticas
- Security Groups con least privilege
- VPC Flow Logs

#### Flujo de Tráfico
```
Clientes BGR → Route 53 → Shield Advanced → WAF → CloudFront → ALB
                                                                  ↓
                                                      EC2 Auto Scaling Group
                                                                  ↓
                                                      ElastiCache (Redis)
                                                                  ↓
                                                      RDS SQL Server ← Read Replica
                                                                  ↓
                                                            CloudWatch
CloudFront → S3 (static content)
```

### 💰 Estimación de Costos (us-east-1)
- **Compute (EC2 Auto Scaling)**: ~$600/mes
- **Database (RDS + Read Replica)**: ~$900/mes
- **Cache (ElastiCache Multi-AZ)**: ~$200/mes
- **CDN (CloudFront)**: ~$250/mes
- **WAF**: ~$50/mes
- **Shield Advanced**: ~$3,000/mes (opcional)
- **Load Balancer**: ~$25/mes
- **Storage & Transfer**: ~$75/mes
- **CI/CD (CodeDeploy + S3 artifacts)**: ~$30/mes
- **Total sin Shield**: **~$2,830/mes**
- **Total con Shield**: **~$5,830/mes**

---

## 📊 Comparativa de Arquitecturas

| Aplicación | Criticidad | ASG (Min/Des/Max) | Tipo EC2 | RDS | Cache | CDN | WAF | CI/CD | Costo Mensual |
|------------|------------|-------------------|----------|-----|-------|-----|-----|-------|---------------|
| **Saras** | Media | 2/2/4 | t3.medium | SQL Server t3.medium | No | No | No | Azure DevOps | $625 |
| **SonarQube** | Media | 2/2/4 | t3.large | PostgreSQL t3.large | No | No | No | Azure DevOps | $1,225 |
| **API Portal** | Alta | 2/3/8 | t3.medium | SQL Server t3.large | Redis | Sí | Sí | Azure DevOps | $2,830 |
| **Portal Guía** | Alta | 2/3/8 | t3.medium | SQL Server t3.xlarge | Redis | Sí | Sí | Azure DevOps | $2,830 |

**Notas**:
- Todos los deployments se realizan mediante **Azure DevOps** con integración a AWS CodeDeploy
- ASG configurado con Target Tracking (CPU 50%) y Scheduled Scaling
- Multi-AZ deployment en todas las aplicaciones
- Health checks configurados en ALB y ASG

---

## 🎯 Características Comunes

### Todas las Arquitecturas Incluyen:

✅ **Alta Disponibilidad**
- Multi-AZ deployment
- Application Load Balancer
- RDS Multi-AZ con automated backups

✅ **Seguridad**
- VPC con subnets públicas y privadas
- Security Groups con least privilege
- AWS Secrets Manager para credenciales
- Encryption at rest (EBS, RDS, S3)
- Encryption in transit (TLS/SSL)

✅ **Monitoring & Observability**
- CloudWatch Logs y Metrics
- CloudWatch Alarms
- SNS para notificaciones

✅ **Backup & Recovery**
- Automated RDS backups
- S3 backups con lifecycle policies
- Point-in-time recovery

✅ **CI/CD con Azure DevOps** ⚠️ **REGLA OBLIGATORIA**
- AWS CodeDeploy para deployment
- S3 para artifacts de Azure DevOps
- CodeDeploy Agent en todas las EC2 instances
- IAM Roles para integración Azure DevOps → AWS
- Systems Manager (SSM) para gestión de instancias
- CloudWatch Logs para deployment logs

### Diferencias por Criticidad:

**Media Criticidad (Saras, SonarQube)**
- Arquitectura más simple
- Sin CDN ni WAF
- Menor capacidad de auto-scaling
- Costos optimizados

**Alta Criticidad (API Portal, Portal Guía)**
- CloudFront + WAF
- Auto Scaling más agresivo
- ElastiCache para performance
- Read Replicas para escalabilidad
- Shield Advanced (opcional)
- X-Ray para tracing (API Portal)

---

## 🔄 Estrategia de Migración

### Fase 1: Piloto (Saras + SonarQube)
- Arquitecturas más simples
- Menor riesgo
- Validar proceso de migración
- **Duración**: 4-6 semanas

### Fase 2: Aplicaciones Críticas (API Portal + Portal Guía)
- Arquitecturas más complejas
- Mayor preparación
- Cutover planificado
- **Duración**: 8-12 semanas

---

## 💡 Recomendaciones

### Optimización de Costos
1. **Reserved Instances**: 30-40% ahorro en EC2 y RDS
2. **Savings Plans**: Flexibilidad con descuentos
3. **Auto Scaling**: Ajustar capacidad según demanda
4. **S3 Lifecycle Policies**: Mover backups antiguos a Glacier

### Seguridad
1. **AWS Config**: Compliance continuo
2. **GuardDuty**: Detección de amenazas
3. **Security Hub**: Vista centralizada de seguridad
4. **Patch Manager**: Automatizar parches de SO

### Performance
1. **CloudFront**: Reducir latencia global
2. **ElastiCache**: Reducir carga en BD
3. **Read Replicas**: Escalar lecturas
4. **Auto Scaling**: Manejar picos de tráfico

### Modernización Futura
1. **Containers (ECS/EKS)**: Mayor eficiencia
2. **Serverless (Lambda)**: Para APIs simples
3. **Aurora**: Migrar de SQL Server a PostgreSQL compatible
4. **AppSync**: GraphQL APIs

---

## 📋 Próximos Pasos

1. ✅ Arquitecturas definidas
2. ⏳ Provisionar infraestructura base (VPC, subnets, security groups)
3. ⏳ Configurar servicios compartidos (Route 53, Secrets Manager)
4. ⏳ **Configurar integración Azure DevOps → AWS**
   - Crear Service Connection en Azure DevOps
   - Configurar IAM Roles con OIDC
   - Setup CodeDeploy Applications
   - Crear S3 bucket para artifacts
5. ⏳ Migrar Saras (piloto)
6. ⏳ Migrar SonarQube (piloto)
7. ⏳ Validar y ajustar
8. ⏳ Migrar API Portal
9. ⏳ Migrar Portal Guía BGR

---

## 🔄 CI/CD con Azure DevOps

### Arquitectura de Deployment

```
Azure DevOps Pipeline
        ↓
    Build & Test
        ↓
    Package Artifacts
        ↓
    AWS S3 (artifacts bucket)
        ↓
    AWS CodeDeploy
        ↓
    EC2 Instances (Blue/Green)
        ↓
    Health Checks
        ↓
    Complete o Rollback
```

### Componentes Requeridos

**Azure DevOps:**
- Azure Pipelines (Build & Deploy)
- Azure Repos (Source Control)
- Service Connection a AWS

**AWS:**
- CodeDeploy (Applications + Deployment Groups)
- S3 Bucket para artifacts
- IAM Roles (Azure DevOps + CodeDeploy + EC2)
- Systems Manager (SSM Agent)
- CloudWatch Logs

### Flujo por Aplicación

1. **Developer** push código → Azure Repos
2. **Azure Pipeline** triggered automáticamente
3. **Build** en Azure DevOps (compile, test, package)
4. **Upload** artifacts → S3
5. **Trigger** CodeDeploy deployment
6. **CodeDeploy** distribuye a EC2 instances
7. **Health checks** automáticos
8. **Complete** deployment o **Rollback** si falla

### Configuración Requerida

Cada aplicación necesita:
- `appspec.yml` en el repositorio
- Scripts de deployment (start/stop/validate)
- Azure Pipeline YAML
- CodeDeploy Application en AWS
- Deployment Group configurado

**Ver detalles completos en**: `REGLAS_PROYECTO_BGR.md`

---

**Última actualización**: 2025-12-03  
**Estado**: Arquitecturas definidas con integración Azure DevOps
