# Arquitectura Detallada - Backoffice Sistemas BGR

**Aplicación**: Backoffice Sistemas BGR  
**Modelo**: Arquitectura Híbrida  
**Fecha**: 2025-12-12

---

## 📊 Diagrama de Arquitectura

![Arquitectura Híbrida Backoffice Sistemas BGR](./diagrams/backoffice_sistemas_hybrid_architecture.png)

---

## 🏗️ Componentes de la Arquitectura

### 1. Capa de Usuarios

#### Colaboradores BGR (685 usuarios)
- **Tipo**: Usuarios internos del banco
- **Acceso**: Navegador web (HTTPS)
- **Ubicación**: Oficinas BGR en Ecuador
- **Autenticación**: Active Directory (LDAP)

---

### 2. AWS Cloud (us-east-1)

#### 2.1 DNS y Enrutamiento

**Route 53**
- **Función**: DNS management y routing
- **Configuración**:
  - Hosted Zone: backoffice-sistemas.bgr.com
  - Record Type: A (Alias a ALB)
  - TTL: 300 segundos
  - Health Checks: Habilitados
- **Failover**: Configurado para alta disponibilidad

#### 2.2 VPC (10.100.0.0/16)

**Subnets Públicas**:
- **Public Subnet A**: 10.100.1.0/24 (us-east-1a)
- **Public Subnet B**: 10.100.2.0/24 (us-east-1b)
- **Componentes**: ALB, NAT Gateways

**Subnets Privadas**:
- **Private Subnet A**: 10.100.10.0/24 (us-east-1a)
- **Private Subnet B**: 10.100.11.0/24 (us-east-1b)
- **Componentes**: EC2 Instances

#### 2.3 Load Balancing

**Application Load Balancer (ALB)**
- **Tipo**: Internet-facing
- **Scheme**: HTTPS (443) + HTTP (80)
- **Listeners**:
  - Port 443: SSL/TLS termination
  - Port 80: Redirect to 443
- **Target Groups**:
  - Protocol: HTTP
  - Port: 80
  - Health Check: /health
  - Healthy Threshold: 2
  - Unhealthy Threshold: 3
  - Timeout: 5s
  - Interval: 30s
- **Sticky Sessions**: Habilitadas (1 hora)
- **Cross-Zone Load Balancing**: Habilitado

#### 2.4 Compute

**EC2 Instance 1 (AZ us-east-1a)**
- **Instance Type**: t3.xlarge
- **vCPUs**: 4
- **RAM**: 16 GB
- **OS**: Windows Server 2016 Standard
- **Storage**: 200 GB EBS gp3
- **Software**:
  - IIS Web Server
  - .NET Framework 4.7.1
  - CloudWatch Agent
  - SSM Agent
  - CodeDeploy Agent
- **Security Group**: EC2-SG
- **IAM Role**: EC2-Instance-Role

**EC2 Instance 2 (AZ us-east-1b)**
- **Configuración**: Idéntica a Instance 1
- **Propósito**: Alta disponibilidad y distribución de carga

#### 2.5 Conectividad Híbrida

**Virtual Private Gateway (VGW)**
- **Función**: Endpoint AWS para conectividad on-premise
- **Attached to**: VPC 10.100.0.0/16
- **BGP ASN**: 65000 (AWS)
- **Route Propagation**: Habilitada

**Direct Connect (1 Gbps)**
- **Tipo**: Dedicated Connection
- **Bandwidth**: 1 Gbps
- **Location**: Datacenter BGR
- **VLAN**: 100
- **BGP**: Habilitado
- **Latencia**: < 5ms
- **SLA**: 99.95%
- **Costo**: $228/mes (port) + $0.02/GB transfer

**VPN Site-to-Site (Backup)**
- **Tipo**: IPSec VPN
- **Túneles**: 2 (redundancia)
- **Bandwidth**: 1.25 Gbps por túnel
- **Encryption**: AES-256
- **IKE Version**: IKEv2
- **DPD**: Habilitado
- **Failover**: Automático desde Direct Connect
- **Costo**: $36.50/mes por túnel

#### 2.6 NAT Gateways

**NAT Gateway 1 (AZ us-east-1a)**
- **Función**: Salida a internet desde private subnet A
- **Elastic IP**: Asignada
- **Bandwidth**: 45 Gbps
- **Costo**: $32.85/mes + data processing

**NAT Gateway 2 (AZ us-east-1b)**
- **Función**: Salida a internet desde private subnet B
- **Configuración**: Idéntica a NAT Gateway 1
- **Propósito**: Alta disponibilidad

#### 2.7 Storage

**S3 Bucket - Artifacts**
- **Nombre**: bgr-artifacts-backoffice-sistemas
- **Región**: us-east-1
- **Versionado**: Habilitado
- **Encryption**: AES-256 (SSE-S3)
- **Lifecycle**: 90 días
- **Propósito**: Almacenar artifacts de Azure DevOps
- **Acceso**: IAM Role (CodeDeploy)

**S3 Bucket - Backups**
- **Nombre**: bgr-backups-backoffice-sistemas
- **Región**: us-east-1
- **Versionado**: Habilitado
- **Encryption**: AES-256 (SSE-S3)
- **Lifecycle**: 
  - 30 días: Transition to S3-IA
  - 90 días: Transition to Glacier
  - 365 días: Delete
- **Propósito**: Backups de aplicación y configuraciones

#### 2.8 Monitoring

**CloudWatch**
- **Logs**:
  - IIS Access Logs
  - IIS Error Logs
  - Application Logs
  - CodeDeploy Logs
- **Metrics**:
  - EC2: CPU, Memory, Disk, Network
  - ALB: Requests, Latency, Errors, Targets
  - Direct Connect: ConnectionState, Bandwidth
  - VPN: TunnelState, TunnelDataIn, TunnelDataOut
- **Dashboards**:
  - Application Performance
  - Infrastructure Health
- **Retention**: 7 días (logs), 15 meses (metrics)

**SNS Topics**
- **Critical Alerts**:
  - EC2 CPU > 80%
  - ALB Unhealthy Targets > 0
  - Direct Connect Down
  - VPN Tunnels Down
  - Delivery: Email + SMS
- **Warning Alerts**:
  - EC2 CPU > 60%
  - ALB Latency > 2s
  - Delivery: Email

#### 2.9 CI/CD

**CodeDeploy**
- **Application**: BGR-Backoffice-Sistemas
- **Deployment Group**: Production
- **Deployment Type**: Blue/Green
- **Deployment Config**: CodeDeployDefault.AllAtOnce
- **Rollback**: Automático en caso de fallo
- **Service Role**: CodeDeploy-Service-Role
- **Triggers**: SNS notification

---

### 3. On-Premise Datacenter BGR

#### 3.1 Conectividad

**Customer Gateway**
- **Función**: Router on-premise para AWS
- **IP Pública**: 200.115.34.x (BGR)
- **BGP ASN**: 65001 (BGR)
- **Routing**: BGP dinámico
- **Firewall**: Configurado para AWS traffic

#### 3.2 Base de Datos

**SQL Server 2016 Enterprise (ECBRPRCL13)**
- **Servidor**: ECBRPRCL13
- **IP**: 172.20.167.59
- **vCPUs**: 24
- **RAM**: 80 GB
- **Storage**: 7,168 GB
- **Versión**: SQL Server 2016 Enterprise SP3 (13.3.6300.2)
- **Base de Datos**: PORTAL_ADMINISTRATIVO_BGR (compartida)
- **Instancias**: Q47
- **Backup**: Diario (on-premise)
- **HA**: Cluster SQL Server
- **Licenciamiento**: Enterprise (Core-based)

**Conexión desde AWS**:
- **Protocol**: TDS (TCP/1433)
- **Encryption**: TLS 1.2
- **Authentication**: SQL Server Authentication
- **Connection String**: Almacenado en AWS Secrets Manager
- **Connection Pooling**: 
  - Min Pool Size: 5
  - Max Pool Size: 100
  - Connection Timeout: 30s
  - Command Timeout: 30s

#### 3.3 Active Directory

**Active Directory (LDAP)**
- **Función**: Autenticación de usuarios
- **Protocol**: LDAP (TCP/389) + LDAPS (TCP/636)
- **Domain**: bgr.com
- **Base DN**: DC=bgr,DC=com
- **Encryption**: LDAPS (SSL/TLS)
- **Connection**: Desde EC2 instances
- **Timeout**: 10s
- **Retry**: 3 intentos

#### 3.4 Microservicio Notificador

**BGRCELULAR (Antiguo Notificador)**
- **Función**: Envío de notificaciones
- **Protocol**: HTTP/HTTPS
- **Endpoint**: http://notificador.bgr.com/api
- **Authentication**: API Key
- **Timeout**: 15s
- **Retry**: 2 intentos

---

### 4. External Services

#### Azure DevOps

**CI/CD Pipeline**
- **Función**: Build, test y deploy
- **Repos**: Azure Repos (Git)
- **Pipelines**: Azure Pipelines
- **Artifacts**: Azure Artifacts
- **Service Connection**: AWS (OIDC)
- **Triggers**: Push to main branch
- **Stages**:
  1. Build (.NET Framework 4.7.1)
  2. Test (Unit tests)
  3. Package (ZIP)
  4. Upload to S3
  5. Trigger CodeDeploy
  6. Validate deployment

---

## 🔄 Flujos de Datos

### Flujo 1: Tráfico de Usuarios

```
Usuario → Internet → Route 53 → ALB → EC2 Instance → VGW → Direct Connect → Customer Gateway → SQL Server
                                                                                                  ↓
                                                                                          Active Directory
```

**Latencia Total**: < 100ms
- Route 53: < 5ms
- ALB: < 10ms
- EC2 Processing: < 50ms
- Direct Connect: < 5ms
- SQL Server: < 30ms

### Flujo 2: CI/CD Deployment

```
Developer → Azure Repos → Azure Pipeline → Build → Package → S3 Artifacts → CodeDeploy → EC2 Instances
                                                                                              ↓
                                                                                        Health Check
                                                                                              ↓
                                                                                    Complete or Rollback
```

**Tiempo Total**: 5-10 minutos
- Build: 2-3 min
- Package: 1 min
- Upload S3: 30s
- CodeDeploy: 2-5 min
- Health Check: 1 min

### Flujo 3: Monitoreo

```
EC2 Instances → CloudWatch Logs → CloudWatch Metrics → CloudWatch Alarms → SNS → Email/SMS
ALB → CloudWatch Metrics → CloudWatch Alarms → SNS → Email/SMS
Direct Connect → CloudWatch Metrics → CloudWatch Alarms → SNS → Email/SMS
```

**Frecuencia**:
- Logs: Real-time
- Metrics: 1 minuto
- Alarms: Evaluación cada 1 minuto

### Flujo 4: Backup

```
EC2 Instances → EBS Snapshots → S3 (automated)
EC2 Instances → Application Backup → S3 Backups → Lifecycle → Glacier
```

**Frecuencia**:
- EBS Snapshots: Diario (automated)
- Application Backup: Semanal
- Retention: 90 días (S3) → 365 días (Glacier)

---

## 🔒 Seguridad

### Security Groups

**ALB-SG**:
```yaml
Inbound:
  - Port 443: 0.0.0.0/0 (HTTPS from Internet)
  - Port 80: 0.0.0.0/0 (HTTP from Internet)
Outbound:
  - Port 80: EC2-SG (HTTP to instances)
```

**EC2-SG**:
```yaml
Inbound:
  - Port 80: ALB-SG (HTTP from ALB)
  - Port 3389: 10.0.0.0/8 (RDP from management)
  - Port 1433: 172.20.0.0/16 (SQL from on-premise)
  - Port 389: 172.20.0.0/16 (LDAP from on-premise)
Outbound:
  - Port 443: 0.0.0.0/0 (HTTPS to Internet)
  - Port 1433: 172.20.167.59/32 (SQL to on-premise)
  - Port 389: 172.20.0.0/16 (LDAP to on-premise)
```

### IAM Roles

**EC2-Instance-Role**:
- CloudWatch Logs: Write
- CloudWatch Metrics: Write
- S3 Backups: Read/Write
- Secrets Manager: Read
- SSM: Managed Instance

**CodeDeploy-Service-Role**:
- EC2: Describe, Start, Stop
- S3 Artifacts: Read
- CloudWatch Logs: Write
- SNS: Publish

**Azure-DevOps-Role** (OIDC):
- S3 Artifacts: Write
- CodeDeploy: Create Deployment
- CloudWatch Logs: Read

### Encryption

**In Transit**:
- Internet → ALB: TLS 1.2
- ALB → EC2: HTTP (internal VPC)
- EC2 → SQL Server: TLS 1.2
- EC2 → LDAP: LDAPS (SSL/TLS)
- Direct Connect: MACsec (opcional)
- VPN: IPSec (AES-256)

**At Rest**:
- EBS Volumes: AES-256 (AWS managed)
- S3 Buckets: AES-256 (SSE-S3)
- Secrets Manager: AES-256 (AWS managed)

---

## 📈 Escalabilidad

### Auto Scaling (Futuro)

**Auto Scaling Group**:
- Min Instances: 2
- Max Instances: 6
- Desired Capacity: 2
- Scale Out: CPU > 70% por 5 min
- Scale In: CPU < 30% por 10 min
- Cooldown: 300s

**Estimación de Ahorro**:
- Horas valle (22:00-06:00): 2 instances
- Horas pico (08:00-18:00): 4-6 instances
- Ahorro: $50-100/mes

---

## 🎯 Alta Disponibilidad

### Componentes Redundantes

1. **EC2 Instances**: 2 en diferentes AZs
2. **NAT Gateways**: 2 en diferentes AZs
3. **Direct Connect + VPN**: Failover automático
4. **ALB**: Multi-AZ por defecto
5. **SQL Server**: Cluster on-premise

### SLAs

| Componente | SLA | Downtime/mes |
|------------|-----|--------------|
| EC2 | 99.99% | 4.3 min |
| ALB | 99.99% | 4.3 min |
| Direct Connect | 99.95% | 21.6 min |
| VPN | 99.95% | 21.6 min |
| S3 | 99.99% | 4.3 min |
| **Total Estimado** | **99.9%** | **43 min** |

---

## 💡 Optimizaciones Futuras

### Corto Plazo (3 meses)
1. Implementar Auto Scaling
2. Optimizar connection pooling
3. Implementar caching (ElastiCache)

### Mediano Plazo (6 meses)
1. Migrar a .NET Framework 4.8
2. Implementar CDN (CloudFront)
3. Optimizar queries SQL

### Largo Plazo (12 meses)
1. Migrar a .NET Core + Linux
2. Evaluar contenedores (ECS/EKS)
3. Migrar BD a AWS (RDS)

---

**Última actualización**: 2025-12-12  
**Versión**: 1.0  
**Diagrama generado con**: AWS Diagrams MCP Server
