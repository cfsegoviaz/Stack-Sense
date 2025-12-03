# 05. Architectures

**Audiencia:** Arquitectos, Ingenieros, Equipo de Desarrollo  
**Propósito:** Arquitecturas detalladas y especificaciones técnicas

---

## 📄 Documentos

### ARCHITECTURE_CATALOG.md
**Descripción:** Catálogo completo de arquitecturas  
**Contenido:**
- Índice de 7 diagramas
- Matriz comparativa de arquitecturas
- Patrones comunes compartidos
- Guía de uso por audiencia

### bgr_individual_architectures.md
**Descripción:** Arquitecturas individuales detalladas  
**Contenido:**
- 6 arquitecturas por aplicación
- Especificaciones técnicas (vCPU, RAM, storage)
- Componentes AWS específicos
- Costos por aplicación
- Estrategia de migración por app

---

## 🎨 Diagramas Disponibles

**Ubicación:** `../../diagrams/`

### Diagrama General
**Archivo:** `bgr_aws_architecture.png` (321 KB)  
**Contenido:**
- Arquitectura completa AWS
- 6 aplicaciones en ECS Fargate
- 2 instancias RDS Multi-AZ
- Servicios compartidos
- CI/CD pipeline

### Diagrama de Migración
**Archivo:** `migration_flow.png` (321 KB)  
**Contenido:**
- Flujo origen → destino
- Nombres de servidores on-premise
- Servicios AWS target
- Código de colores por tipo de migración

### Diagramas Individuales (6 aplicaciones)

1. **app_portalguiabgr.png** (228 KB)
   - 3 tasks ECS Fargate (2 vCPU, 4GB)
   - RDS SQL Server compartido
   - Managed AD + SNS

2. **app_apiportal.png** (269 KB)
   - 5 tasks ECS Fargate (2 vCPU, 4GB)
   - Auto-scaling 3-10 tasks
   - Rate limiting + API metrics

3. **app_portaladministrativo.png** (186 KB)
   - 2 tasks ECS Fargate (1 vCPU, 2GB)
   - Admin auth + MFA
   - Audit logging

4. **app_backoffice_sistemas.png** (223 KB)
   - 3 tasks ECS Fargate (2 vCPU, 4GB)
   - RBAC + Config versioning
   - System parameters

5. **app_backoffice_banca.png** (193 KB)
   - 3 tasks ECS Fargate (.NET 8)
   - Cognito authentication
   - SQL Server 2019

6. **app_saras.png** (175 KB)
   - 2 tasks ECS Fargate (.NET 8)
   - Cognito authentication
   - Risk analysis

---

## 🏗️ Patrones de Arquitectura

### Todos los Componentes Comparten:

✅ **Alta Disponibilidad**
- Multi-AZ deployment (3 AZs)
- Auto-scaling compute
- RDS Multi-AZ databases
- 99.99% SLA

✅ **Seguridad**
- TLS 1.3 encryption
- AWS Secrets Manager
- Certificate Manager (ACM)
- IAM role-based access

✅ **Observabilidad**
- CloudWatch Logs
- CloudWatch Metrics
- AWS X-Ray tracing
- SNS alerting

✅ **Networking**
- Route 53 DNS
- Application Load Balancer
- Private subnets (compute/data)
- Public subnets (ALB)

✅ **Configuration**
- Parameter Store
- Environment-based configs
- Centralized management

✅ **CI/CD**
- CodePipeline automation
- CodeBuild for containers
- ECR for images
- Blue/green deployments

---

## 📊 Especificaciones por Aplicación

| Aplicación | Compute | Database | Auth | Costo/Mes |
|-----------|---------|----------|------|-----------|
| PortalGuiaBGR | 3 tasks (2v/4GB) | SQL Shared | Managed AD | $407 |
| Api Portal | 5 tasks (2v/4GB) | SQL Shared | Managed AD | $552 |
| PortalAdministrativo | 2 tasks (1v/2GB) | SQL Shared | Managed AD | $263 |
| Backoffice Sistemas | 3 tasks (2v/4GB) | SQL Shared | Managed AD | $407 |
| Backoffice Banca | 3 tasks (2v/4GB) | SQL 2019 | Cognito | $559 |
| Saras | 2 tasks (2v/4GB) | SQL 2019 | Cognito | $487 |

---

## 🎯 Servicios AWS Utilizados

### Compute & Containers
- Amazon ECS (Fargate)
- Application Load Balancer
- Amazon ECR

### Database
- Amazon RDS for SQL Server Standard (2 instancias)
- Multi-AZ deployment
- Automated backups

### Networking
- Amazon VPC
- NAT Gateway (3 AZs)
- Internet Gateway
- Route 53

### Security & Identity
- AWS Managed Microsoft AD
- Amazon Cognito
- AWS Secrets Manager
- AWS Certificate Manager
- AWS IAM

### DevOps & CI/CD
- AWS CodePipeline
- AWS CodeBuild
- Amazon ECR

### Observability
- Amazon CloudWatch
- AWS X-Ray
- Amazon SNS

### Configuration
- AWS Systems Manager Parameter Store
- AWS AppConfig
- Amazon SQS

**Total:** 22 servicios AWS
