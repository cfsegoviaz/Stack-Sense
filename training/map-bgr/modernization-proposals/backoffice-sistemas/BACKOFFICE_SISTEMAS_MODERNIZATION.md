# Backoffice Sistemas BGR - Lift & Shift a AWS
## Propuesta de Migración

**Fecha**: 2025-12-12  
**Aplicación**: Backoffice Sistemas BGR  
**Estrategia**: Lift & Shift (Rehost) con Arquitectura Híbrida  
**Timeline**: 3 semanas  
**Responsable**: Erik Palma (erik.palma@bgr.com.ec) - Jefe de Arquitectura

---

## 🎯 Información de la Aplicación

### Descripción
Aplicación parametrizadora para diversos sistemas del banco BGR. Permite la gestión centralizada de configuraciones y parámetros para múltiples aplicaciones del ecosistema bancario.

### Situación Actual (On-Premise)

**Infraestructura VMware**:
- **VMs Producción**: 2 servidores (ECBRPRW44, ECBRPRW45)
- **VMs Test**: 2 servidores (ECBRTSCC01, ECBRTSW21)
- **Base de Datos**: ECBRPRCL13 Q47 (SQL Server 2016 Enterprise)
- **Load Balancer**: ecbrprnwpc.bgr.com
- **Total vCPUs**: 12 (4 + 8)
- **Total RAM**: 40 GB (20 + 20)
- **OS**: Windows Server 2016 Standard
- **Criticidad**: ALTA (Prioridad de modernización: TRUE)

### Recursos Actuales Detallados

#### Servidores de Aplicación

| Servidor | vCPUs | RAM (GB) | Storage (GB) | OS | IP | Estado | Uso CPU (%) | Uso RAM (GB) |
|----------|-------|----------|--------------|-----|------------|--------|-------------|--------------|
| **ECBRPRW44** | 4 | 20 | 200 | Windows Server 2016 | 172.20.1.111 | poweredOn | 79% | 21.47 |
| **ECBRPRW45** | 8 | 20 | 200 | Windows Server 2016 | 172.20.1.112 | poweredOn | 45% | 21.47 |

**Fuente**: RVTools + Cloudamize Observed Infrastructure

#### Base de Datos (On-Premise)

| Servidor | vCPUs | RAM (GB) | Storage (GB) | Motor | Versión | IP |
|----------|-------|----------|--------------|-------|---------|-----|
| **ECBRPRCL13** | 24 | 80 | 7,168 | SQL Server | 2016 Enterprise SP3 | 172.20.167.59 |

**Nota Crítica**: Base de datos compartida **PORTAL_ADMINISTRATIVO_BGR** permanece on-premise según reglas del proyecto.

### Stack Tecnológico

**Frontend**:
- ASP.NET C# (.NET Framework 4.7.1) - **OBSOLETO**
- ajaxToolkit v3.5
- Bootstrap

**Backend**:
- C# (.NET Framework 4.7.1) - **OBSOLETO**
- IIS Web Server

**Base de Datos**:
- SQL Server 2016 Enterprise Edition (On-Premise)

**Dependencias**:
- **Base de datos**: PORTAL_ADMINISTRATIVO_BGR (compartida)
- **Microservicio**: BGRCELULAR (Antiguo Notificador)
- **Identidades**: Active Directory (LDAP)
- **Configuración**: Tcs.ServicioConfiguracionBGR.WS

### Usuarios y Criticidad

- **Usuarios Totales**: 685 colaboradores del BGR
- **Tipo de Usuarios**: Colaboradores internos del banco
- **Impacto de Falla**: Los colaboradores del BGR se quedarán sin poder consultar la información telefónica de sus pares en todo el BGR, ni tampoco información de contacto de los proveedores
- **Soporte**: BGR/TCS (soporte y mantenimiento)
- **Sensibilidad a Latencia**: NO (aplicación funciona en DCP del BGR)

---

## 🏗️ Arquitectura AWS Propuesta

### Modelo de Despliegue: Arquitectura Híbrida

**Componentes en AWS**:
- Servidores de aplicación (EC2)
- Load Balancer (ALB)
- Networking y seguridad

**Componentes On-Premise**:
- Base de datos SQL Server (ECBRPRCL13)
- Active Directory (LDAP)
- Microservicio Notificador

### Componentes AWS

#### 1. Compute (EC2)

**Instancias Recomendadas**:
- **Tipo**: t3.xlarge (4 vCPU, 16 GB RAM)
- **Cantidad**: 2 instancias (Alta Disponibilidad)
- **OS**: Windows Server 2016 Standard
- **Justificación**: 
  - ECBRPRW44: 79% CPU, 21.47 GB RAM → Requiere 4 vCPU, 20 GB RAM
  - ECBRPRW45: 45% CPU, 21.47 GB RAM → Requiere 8 vCPU, 20 GB RAM
  - t3.xlarge (4 vCPU, 16 GB) es suficiente con optimización
  - Burstable performance para picos de carga

**Configuración**:
```yaml
Instance Type: t3.xlarge
vCPUs: 4
RAM: 16 GB
Storage: 200 GB EBS gp3
OS: Windows Server 2016 Standard
Availability Zones: us-east-1a, us-east-1b
```

#### 2. Database (Híbrido)

**Opción Seleccionada**: Mantener on-premise con conectividad híbrida

**Razón**: 
- Base de datos compartida PORTAL_ADMINISTRATIVO_BGR
- Múltiples aplicaciones dependen de la misma instancia
- Regla del proyecto: BDs permanecen on-premise

**Conectividad Requerida**:
- AWS Direct Connect (1 Gbps) o VPN Site-to-Site
- Latencia < 10ms crítica
- Conexión redundante para HA

#### 3. Networking

**VPC Configuration**:
```yaml
VPC CIDR: 10.100.0.0/16
Public Subnet A: 10.100.1.0/24 (us-east-1a)
Public Subnet B: 10.100.2.0/24 (us-east-1b)
Private Subnet A: 10.100.10.0/24 (us-east-1a)
Private Subnet B: 10.100.11.0/24 (us-east-1b)
```

**Load Balancer**:
- **Tipo**: Application Load Balancer (ALB)
- **Scheme**: Internet-facing
- **Listeners**: HTTPS (443), HTTP (80) → redirect to HTTPS
- **Target Groups**: EC2 instances en private subnets
- **Health Checks**: HTTP /health endpoint

**Conectividad Híbrida**:
- **Virtual Private Gateway** (VGW) attached al VPC
- **Customer Gateway** en datacenter BGR
- **Direct Connect** (1 Gbps) - Recomendado
- **VPN Site-to-Site** (backup) - 2 túneles IPSec

#### 4. Storage

**EBS Volumes**:
- **Tipo**: gp3 (General Purpose SSD)
- **Tamaño**: 200 GB por instancia
- **IOPS**: 3,000 baseline
- **Throughput**: 125 MB/s

**S3 Buckets**:
- **Artifacts**: bgr-artifacts-backoffice-sistemas
- **Backups**: bgr-backups-backoffice-sistemas
- **Logs**: bgr-logs-backoffice-sistemas

#### 5. Monitoring & Management

**CloudWatch**:
- Logs de aplicación IIS
- Métricas de EC2 (CPU, RAM, Disk, Network)
- Métricas de ALB (requests, latency, errors)
- Métricas de conectividad híbrida

**SNS Topics**:
- Critical alerts → Email + SMS
- Warning alerts → Email

**Systems Manager**:
- Session Manager para acceso seguro
- Parameter Store para configuraciones
- Patch Manager para actualizaciones

#### 6. Security

**Security Groups**:

```yaml
# ALB Security Group
ALB-SG:
  Inbound:
    - Port 443: 0.0.0.0/0 (HTTPS)
    - Port 80: 0.0.0.0/0 (HTTP)
  Outbound:
    - Port 80: EC2-SG (HTTP to instances)

# EC2 Security Group
EC2-SG:
  Inbound:
    - Port 80: ALB-SG (HTTP from ALB)
    - Port 3389: Management-CIDR (RDP)
    - Port 1433: On-Premise-CIDR (SQL Server)
  Outbound:
    - Port 443: 0.0.0.0/0 (HTTPS)
    - Port 1433: On-Premise-CIDR (SQL Server)
    - Port 389: On-Premise-CIDR (LDAP)
```

**IAM Roles**:
- EC2 Instance Role (SSM, CloudWatch, S3)
- CodeDeploy Service Role
- Azure DevOps AssumeRole (OIDC)

**Secrets Manager**:
- SQL Server connection strings
- LDAP credentials
- API keys

---

## 🔄 Integración CI/CD con Azure DevOps

### Configuración Requerida

**Azure DevOps Setup**:
1. Service Connection a AWS (OIDC)
2. Azure Pipelines para build y deploy
3. Azure Repos para código fuente

**AWS CodeDeploy**:
1. Application: BGR-Backoffice-Sistemas
2. Deployment Group: Production
3. Deployment Type: Blue/Green
4. CodeDeploy Agent en EC2 instances

**S3 Artifacts**:
- Bucket: bgr-artifacts-backoffice-sistemas
- Versionado habilitado
- Lifecycle: 90 días

### Flujo de Deployment

```
Developer Push → Azure Repos
       ↓
Azure Pipeline Triggered
       ↓
Build & Test (.NET 4.7.1)
       ↓
Package Artifacts (ZIP)
       ↓
Upload to S3
       ↓
Trigger CodeDeploy
       ↓
Blue/Green Deployment
       ↓
Health Checks
       ↓
Complete or Rollback
```

---

## 📊 Diagrama de Arquitectura

### Arquitectura Híbrida Propuesta

![Arquitectura Híbrida Backoffice Sistemas BGR](./diagrams/backoffice_sistemas_hybrid_architecture.png)

### Componentes del Diagrama

**AWS Cloud (us-east-1)**:
- **Route 53**: DNS management
- **Application Load Balancer**: Distribución de tráfico HTTPS
- **EC2 Instances**: 2x t3.xlarge en diferentes AZs (Alta Disponibilidad)
- **NAT Gateways**: Salida a internet desde subnets privadas
- **Virtual Private Gateway**: Endpoint para conectividad híbrida
- **Direct Connect**: Conexión dedicada 1 Gbps a on-premise
- **VPN Site-to-Site**: Backup de conectividad
- **S3 Buckets**: Artifacts (Azure DevOps) y Backups
- **CloudWatch + SNS**: Monitoreo y alertas
- **CodeDeploy**: Deployment automatizado

**On-Premise Datacenter BGR**:
- **Customer Gateway**: Router on-premise para conectividad
- **SQL Server 2016**: Base de datos ECBRPRCL13 (24 vCPU, 80 GB)
- **Active Directory**: Autenticación LDAP
- **Microservicio Notificador**: Servicio de notificaciones

**External**:
- **Azure DevOps**: CI/CD Pipeline para build y deploy

### Flujos de Datos

1. **Tráfico de Usuarios**: Internet → Route 53 → ALB → EC2 Instances
2. **Conectividad Híbrida**: EC2 → VGW → Direct Connect/VPN → Customer Gateway → On-Premise
3. **CI/CD**: Azure DevOps → S3 → CodeDeploy → EC2 Instances
4. **Monitoreo**: EC2/ALB → CloudWatch → SNS Alerts
5. **Backups**: EC2 → S3 Backups

### 📋 Esfuerzo Escala24x7 - Opción 1 (EC2 Híbrido - RECOMENDADA)

| Tarea | Horas | Equipo |
|-------|-------|--------|
| VPC/Redes | 4 | Infra |
| EC2 Instances (2) | 4 | Infra |
| ASG Configuration | 4 | Infra |
| ALB | 2 | Infra |
| EBS Storage | 4 | Infra |
| VPN Site-to-Site | 16 | Infra |
| Direct Connect config | 16 | Infra |
| S3 Buckets (3) | 6 | Infra |
| Secrets Manager | 1 | Infra |
| Route 53 | 2 | Infra |
| CloudWatch Dashboard | 8 | Infra |
| Azure DevOps pipeline | 24 | DevOps |
| MGN Configuration | 2 | Infra |
| MGN Instances (2) | 2 | Infra |
| MGN Tests | 2 | Infra |
| Testing y validación | 16 | QA |
| Knowledge transfer | 8 | Infra |
| **TOTAL** | **121** | |

**Costo implementación**: 121 horas × $150/hora = **$18,150 USD**

---



---

# Opciones de Arquitectura Adicionales

## Opción 2: ECS Fargate Híbrido

![Arquitectura ECS Híbrido](./diagrams/generated-diagrams/backoffice_sistemas_ecs_hybrid.png)

### Descripción
Modernización a contenedores ECS Fargate manteniendo conectividad híbrida con base de datos on-premise. Combina beneficios de contenedores con arquitectura híbrida existente.

### Componentes
| Servicio | Configuración | Costo/mes |
|----------|---------------|-----------|
| ECS Fargate | 2 tasks x 2 vCPU, 4 GB RAM | $147.00 |
| Application Load Balancer | HTTPS con WAF | $35.00 |
| Amazon ECR | Registry privado | $5.00 |
| VPN Site-to-Site | 2 túneles IPSec | $36.00 |
| Direct Connect | 1 Gbps compartido | $50.00 |
| Secrets Manager | Credenciales BD | $2.00 |
| CloudWatch | Logs y métricas | $15.00 |
| **TOTAL** | | **$290/mes** |

### Ventajas
- ✅ Zero server management
- ✅ Auto-scaling nativo
- ✅ Rolling deployments sin downtime
- ✅ Mantiene BD on-premise (compliance)
- ✅ Menor costo que EC2

### Desventajas
- ❌ Requiere containerización de .NET Framework
- ❌ Latencia a BD on-premise
- ❌ Curva de aprendizaje Docker/ECS

### 💡 Tips y Recomendaciones IA

**Cuándo elegir esta opción:**
- Equipos con experiencia en contenedores
- Necesidad de deployments frecuentes
- Planificación de migración gradual a cloud

**Consideraciones importantes:**
- .NET Framework 4.7.1 requiere contenedores Windows
- Evaluar migración a .NET Core 8 para contenedores Linux
- Latencia a BD on-premise puede afectar performance

**Recomendaciones de implementación:**
- Usar Windows containers con ECS
- Configurar health checks robustos
- Implementar circuit breaker para conexión a BD

**Ideal para:**
- Organizaciones con estrategia container-first
- Equipos que planean modernizar gradualmente
- Aplicaciones con deployments frecuentes

#### 📋 Esfuerzo Escala24x7

| Tarea | Horas | Equipo |
|-------|-------|--------|
| VPC/Redes | 4 | Infra |
| Fargate Cluster | 2 | Infra |
| Fargate Service (2 tasks) | 8 | Infra |
| ALB + WAF | 6 | Infra |
| ECR | 1 | Infra |
| VPN Site-to-Site | 16 | Infra |
| Direct Connect config | 16 | Infra |
| Secrets Manager | 1 | Infra |
| DevOps Windows Container | 2 | DevOps |
| Application pipeline (ECS) | 4 | Infra |
| CloudWatch Dashboard | 8 | Infra |
| Testing y validación | 16 | QA |
| Knowledge transfer | 8 | Infra |
| **TOTAL** | **92** | |

**Costo implementación**: 92 horas × $150/hora = **$13,800 USD**

---

## Opción 3: Full Cloud con RDS SQL Server

![Arquitectura Full Cloud](./diagrams/generated-diagrams/backoffice_sistemas_full_cloud.png)

### Descripción
Migración completa a AWS incluyendo base de datos. Elimina dependencia on-premise pero requiere migración de datos compartidos.

### Componentes
| Servicio | Configuración | Costo/mes |
|----------|---------------|-----------|
| EC2 t3.xlarge | 2 instancias Windows | $243.48 |
| RDS SQL Server Standard | db.m5.large | $380.00 |
| Application Load Balancer | HTTPS | $22.50 |
| AWS DMS | Migración CDC | $130.00 |
| VPN Site-to-Site | Conectividad AD | $36.00 |
| EBS gp3 | 400 GB total | $32.00 |
| Secrets Manager | Credenciales | $2.00 |
| CloudWatch | Logs y métricas | $15.00 |
| Amazon S3 | Backups | $5.00 |
| **TOTAL** | | **$866/mes** |

### Ventajas
- ✅ Independencia de infraestructura on-premise
- ✅ Backups automáticos RDS
- ✅ Alta disponibilidad Multi-AZ
- ✅ Menor latencia (todo en AWS)
- ✅ Escalabilidad de BD

### Desventajas
- ❌ Mayor costo por licencias SQL Server
- ❌ Requiere migración de BD compartida
- ❌ Coordinación con otras aplicaciones
- ❌ Complejidad de migración de datos

### 💡 Tips y Recomendaciones IA

**Cuándo elegir esta opción:**
- Cuando se planea migrar todas las apps que comparten la BD
- Necesidad de independencia total de on-premise
- Requisitos de DR/HA avanzados

**Consideraciones importantes:**
- BD PORTAL_ADMINISTRATIVO_BGR es compartida por múltiples apps
- Requiere coordinación con otras aplicaciones dependientes
- Evaluar migración a Aurora PostgreSQL para eliminar licencias

**Recomendaciones de implementación:**
- Usar AWS DMS con CDC para migración con mínimo downtime
- Planificar migración en wave con apps dependientes
- Considerar Babelfish para eliminar licencias SQL Server

**Ideal para:**
- Migración completa del portafolio a AWS
- Organizaciones que buscan eliminar datacenter on-premise
- Aplicaciones críticas que requieren HA/DR avanzado

#### 📋 Esfuerzo Escala24x7

| Tarea | Horas | Equipo |
|-------|-------|--------|
| VPC/Redes | 4 | Infra |
| EC2 Instances (2) | 4 | Infra |
| ALB | 2 | Infra |
| RDS SQL Server | 2 | Infra |
| EBS Storage | 4 | Infra |
| VPN Site-to-Site | 16 | Infra |
| DMS replication instance | 4 | Data |
| DMS replication task | 4 | Data |
| Secrets Manager | 1 | Infra |
| S3 Bucket | 2 | Infra |
| CloudWatch Dashboard | 8 | Infra |
| Testing y validación | 24 | QA |
| Knowledge transfer | 8 | Infra |
| **TOTAL** | **83** | |

**Costo implementación**: 83 horas × $150/hora = **$12,450 USD**

---

## Comparativa de Opciones

| Criterio | EC2 Híbrido | ECS Híbrido | Full Cloud RDS |
|----------|-------------|-------------|----------------|
| **Costo/mes** | $402 | $290 | $866 |
| **Ahorro vs actual** | 45% | 60% | -19% |
| **Complejidad** | Baja | Media | Alta |
| **BD Location** | On-Premise | On-Premise | AWS |
| **Modernización** | Ninguna | Contenedores | Parcial |
| **Timeline** | 3 semanas | 5 semanas | 8 semanas |
| **Recomendado** | ✅ Sí | Para DevOps maduros | Solo si migra todo |

### Recomendación Final
**EC2 Híbrido** es la opción recomendada por:
1. Menor riesgo y complejidad
2. Mantiene BD compartida on-premise (requisito del proyecto)
3. Migración rápida con AWS MGN
4. Balance óptimo costo/beneficio
