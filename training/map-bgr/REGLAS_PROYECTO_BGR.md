# Reglas del Proyecto BGR

**Fecha**: 2025-12-04  
**Cliente**: BGR

---

## 🎯 Reglas de Arquitectura y Despliegue

### 1. CI/CD - Azure DevOps

**REGLA OBLIGATORIA**: El despliegue se realiza por **Azure DevOps**

#### Implicaciones en Arquitectura AWS:

**Conectividad**
- Azure DevOps debe tener conectividad con AWS
- Usar AWS IAM roles para autenticación desde Azure DevOps
- Configurar Service Connections en Azure DevOps para AWS

**Pipelines**
- Azure Pipelines para build y deploy
- Azure Repos para código fuente
- Azure Artifacts para paquetes

**Integración AWS**
- AWS CodeDeploy como target de deployment
- EC2 instances con CodeDeploy Agent instalado
- S3 para almacenar artifacts de deployment
- Systems Manager (SSM) para gestión de instancias

**Arquitectura de Deployment**
```
Azure DevOps Pipeline → AWS S3 (artifacts) → AWS CodeDeploy → EC2 Instances
                              ↓
                        CloudWatch Logs
```

---

### 2. Bases de Datos On-Premise ⚠️ **REGLA CRÍTICA**

**REGLA OBLIGATORIA**: Las bases de datos permanecen **on-premise** por dependencias existentes.

#### Implicaciones en Arquitectura:

**Conectividad Híbrida Requerida**
- AWS Direct Connect (recomendado) o VPN Site-to-Site
- Baja latencia crítica para aplicaciones
- Conexión redundante para alta disponibilidad

**Componentes AWS Necesarios**
1. **Virtual Private Gateway (VGW)**
   - Attached al VPC de AWS
   - Endpoint para conexión on-premise

2. **Customer Gateway**
   - Representa el router on-premise
   - IP pública del datacenter BGR

3. **Direct Connect (Recomendado)**
   - 1 Gbps o 10 Gbps
   - Latencia < 10ms
   - SLA 99.95%
   - Backup con VPN

4. **VPN Site-to-Site (Alternativa/Backup)**
   - 2 túneles IPSec
   - Hasta 1.25 Gbps por túnel
   - Latencia variable

**Arquitectura de Conectividad**
```
AWS VPC (EC2 Instances)
        ↓
Private Subnets → Virtual Private Gateway
        ↓
Direct Connect / VPN
        ↓
Customer Gateway (On-Premise)
        ↓
On-Premise Datacenter (SQL Server, PostgreSQL)
```

**Seguridad**
- Tráfico encriptado (IPSec para VPN, MACsec para Direct Connect)
- Security Groups permitiendo solo tráfico de DB desde EC2
- Network ACLs restrictivas
- Secrets Manager para credenciales de BD

**Consideraciones de Performance**
- Latencia: < 10ms (Direct Connect) vs 20-50ms (VPN)
- Ancho de banda: Dimensionar según carga de aplicaciones
- Connection pooling en aplicaciones
- Caching agresivo (ElastiCache) para reducir queries

**Monitoreo**
- CloudWatch Metrics para conexión híbrida
- VPC Flow Logs
- Alarmas de latencia y packet loss
- Network Performance Monitor

#### Bases de Datos Afectadas:

| Aplicación | Base de Datos | Ubicación | Conectividad |
|------------|---------------|-----------|--------------|
| Saras | SQL Server | On-Premise | Direct Connect/VPN |
| SonarQube | PostgreSQL | On-Premise | Direct Connect/VPN |
| API Portal | SQL Server | On-Premise | Direct Connect/VPN |
| Portal Guía | SQL Server | On-Premise | Direct Connect/VPN |

**Eliminado de Arquitectura AWS**:
- ❌ RDS SQL Server
- ❌ RDS PostgreSQL
- ❌ RDS Multi-AZ
- ❌ RDS Read Replicas
- ❌ Database Subnet Groups

**Agregado a Arquitectura AWS**:
- ✅ Virtual Private Gateway
- ✅ Direct Connect Connection
- ✅ VPN Site-to-Site (backup)
- ✅ Customer Gateway
- ✅ Route Tables para on-premise
- ✅ Security Groups para DB traffic

---

## 💰 Impacto en Costos

### Costos Eliminados (por mantener BD on-premise):
```
Saras: -$180/mes (RDS SQL Server)
SonarQube: -$350/mes (RDS PostgreSQL)
API Portal: -$700/mes (RDS SQL Server + Replica)
Portal Guía: -$900/mes (RDS SQL Server + Read Replica)

Total ahorrado: -$2,130/mes
```

### Costos Agregados (conectividad híbrida):
```
Direct Connect (1 Gbps): +$228/mes (port) + $0.02/GB transfer
VPN Site-to-Site (backup): +$73/mes (2 túneles)
Data Transfer Out: +$100-200/mes (estimado)

Total agregado: +$400-500/mes
```

### Balance Neto:
```
Ahorro: $2,130/mes
Costo híbrido: -$450/mes
Balance: +$1,680/mes de ahorro
```

---

## 📋 Checklist de Implementación

### Conectividad Híbrida
- [ ] Solicitar Direct Connect (lead time: 2-4 semanas)
- [ ] Configurar Customer Gateway on-premise
- [ ] Crear Virtual Private Gateway en AWS
- [ ] Establecer VPN Site-to-Site (backup)
- [ ] Configurar BGP routing
- [ ] Probar conectividad y latencia
- [ ] Configurar monitoring

### Seguridad
- [ ] Security Groups para tráfico DB
- [ ] Network ACLs
- [ ] Secrets Manager para credenciales
- [ ] Encriptación en tránsito
- [ ] VPC Flow Logs

### Aplicaciones
- [ ] Connection strings apuntando a on-premise
- [ ] Connection pooling configurado
- [ ] Timeouts apropiados
- [ ] Retry logic
- [ ] Circuit breakers

### Azure DevOps Setup
- [ ] Crear Service Connection a AWS
- [ ] Configurar IAM Role con OIDC
- [ ] Crear Azure Pipelines por aplicación
- [ ] Configurar Azure Repos
- [ ] Setup Azure Artifacts (si aplica)

### AWS Setup
- [ ] Crear S3 bucket para artifacts
- [ ] Configurar CodeDeploy Applications
- [ ] Crear Deployment Groups
- [ ] Configurar IAM Roles
- [ ] Instalar CodeDeploy Agent en EC2
- [ ] Configurar CloudWatch Logs

---

**Última actualización**: 2025-12-04  
**Estado**: Reglas actualizadas - BD on-premise


#### Componentes AWS Adicionales Requeridos:

1. **AWS CodeDeploy**
   - Application y Deployment Groups por aplicación
   - Blue/Green o In-place deployment
   - Rollback automático en caso de fallo

2. **S3 Buckets**
   - Bucket para artifacts de Azure DevOps
   - Versionado habilitado
   - Lifecycle policies

3. **IAM Roles**
   - Role para Azure DevOps (AssumeRole con OIDC)
   - Role para EC2 instances (CodeDeploy Agent)
   - Role para CodeDeploy service

4. **Systems Manager**
   - SSM Agent en todas las EC2 instances
   - Parameter Store para configuraciones
   - Session Manager para acceso seguro

5. **CloudWatch**
   - Logs de deployments
   - Métricas de CodeDeploy
   - Alarms para fallos de deployment

#### Flujo de Deployment:

```
1. Developer push → Azure Repos
2. Azure Pipeline triggered
3. Build & Test en Azure DevOps
4. Package artifacts
5. Upload artifacts → S3
6. Trigger CodeDeploy
7. CodeDeploy → EC2 instances
8. Health checks
9. Complete deployment o Rollback
```

---

## 📋 Checklist de Implementación

### Azure DevOps Setup
- [ ] Crear Service Connection a AWS
- [ ] Configurar IAM Role con OIDC
- [ ] Crear Azure Pipelines por aplicación
- [ ] Configurar Azure Repos
- [ ] Setup Azure Artifacts (si aplica)

### AWS Setup
- [ ] Crear S3 bucket para artifacts
- [ ] Configurar CodeDeploy Applications
- [ ] Crear Deployment Groups
- [ ] Configurar IAM Roles
- [ ] Instalar CodeDeploy Agent en EC2
- [ ] Configurar CloudWatch Logs

### Seguridad
- [ ] Least privilege IAM policies
- [ ] Encriptar artifacts en S3
- [ ] Secrets en AWS Secrets Manager
- [ ] Audit logs habilitados

---

## 🔧 Configuración por Aplicación

### Todas las Aplicaciones Requieren:

**En EC2 Instances:**
```bash
# CodeDeploy Agent
sudo yum install -y ruby wget
wget https://aws-codedeploy-us-east-1.s3.amazonaws.com/latest/install
chmod +x ./install
sudo ./install auto

# SSM Agent (pre-instalado en AMIs recientes)
sudo systemctl enable amazon-ssm-agent
sudo systemctl start amazon-ssm-agent
```

**appspec.yml** (en cada repositorio):
```yaml
version: 0.0
os: windows
files:
  - source: /
    destination: C:\inetpub\wwwroot\app
hooks:
  BeforeInstall:
    - location: scripts\stop-service.ps1
      timeout: 300
  AfterInstall:
    - location: scripts\start-service.ps1
      timeout: 300
  ApplicationStop:
    - location: scripts\stop-service.ps1
      timeout: 300
  ApplicationStart:
    - location: scripts\start-service.ps1
      timeout: 300
  ValidateService:
    - location: scripts\validate-service.ps1
      timeout: 300
```

**Azure Pipeline YAML** (ejemplo):
```yaml
trigger:
  - main

pool:
  vmImage: 'windows-latest'

variables:
  AWS_REGION: 'us-east-1'
  S3_BUCKET: 'bgr-artifacts'
  CODEDEPLOY_APP: 'BGR-Saras'
  DEPLOYMENT_GROUP: 'Production'

stages:
- stage: Build
  jobs:
  - job: BuildJob
    steps:
    - task: DotNetCoreCLI@2
      inputs:
        command: 'build'
        projects: '**/*.csproj'
    
    - task: DotNetCoreCLI@2
      inputs:
        command: 'publish'
        publishWebProjects: true
        arguments: '--output $(Build.ArtifactStagingDirectory)'
    
    - task: PublishBuildArtifacts@1
      inputs:
        PathtoPublish: '$(Build.ArtifactStagingDirectory)'
        ArtifactName: 'drop'

- stage: Deploy
  dependsOn: Build
  jobs:
  - deployment: DeployAWS
    environment: 'Production'
    strategy:
      runOnce:
        deploy:
          steps:
          - task: AWSCLI@1
            inputs:
              awsCredentials: 'AWS-BGR-Connection'
              regionName: '$(AWS_REGION)'
              awsCommand: 's3'
              awsSubCommand: 'cp'
              awsArguments: '$(Pipeline.Workspace)/drop/app.zip s3://$(S3_BUCKET)/$(Build.BuildId)/'
          
          - task: AWSCLI@1
            inputs:
              awsCredentials: 'AWS-BGR-Connection'
              regionName: '$(AWS_REGION)'
              awsCommand: 'deploy'
              awsSubCommand: 'create-deployment'
              awsArguments: '--application-name $(CODEDEPLOY_APP) --deployment-group-name $(DEPLOYMENT_GROUP) --s3-location bucket=$(S3_BUCKET),key=$(Build.BuildId)/app.zip,bundleType=zip'
```

---

## 💰 Costos Adicionales por Azure DevOps Integration

**AWS Services:**
- CodeDeploy: Gratis para EC2
- S3 Storage: ~$5-10/mes
- Data Transfer: ~$10-20/mes
- CloudWatch Logs: ~$5/mes

**Total adicional**: ~$20-35/mes por aplicación

---

## 🎯 Próximos Pasos

1. [ ] Documentar credenciales AWS para Azure DevOps
2. [ ] Crear Service Connection en Azure DevOps
3. [ ] Configurar IAM Roles con OIDC
4. [ ] Crear pipelines base por aplicación
5. [ ] Probar deployment en ambiente de desarrollo
6. [ ] Validar rollback automático
7. [ ] Documentar proceso de deployment

---

**Última actualización**: 2025-12-03  
**Estado**: Regla documentada
