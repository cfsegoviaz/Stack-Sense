# Api Portal - CI/CD con Azure DevOps y AWS Amplify
## Arquitectura Multi-Cloud Moderna

**Fecha**: 2025-12-04  
**CI/CD**: Azure DevOps  
**Hosting**: AWS Amplify  
**Estrategia**: Best-of-breed multi-cloud

---

## 🎯 Arquitectura Multi-Cloud

![Arquitectura Azure DevOps + AWS](./generated-diagrams/api_portal_azure_devops_amplify.png)

### Componentes

#### Azure DevOps (CI/CD Orchestration)
- **Azure Repos**: Repositorio Git
- **Azure Pipelines**: Build y deploy automation
- **Azure Artifacts**: Package management
- **Azure Boards**: Project management

#### AWS (Hosting & CDN)
- **S3**: Almacenamiento de archivos estáticos
- **CloudFront**: CDN global (400+ edge locations)
- **Route 53**: DNS management
- **Certificate Manager**: SSL/TLS automático
- **CloudWatch**: Monitoring y logs

---

## 🔄 Pipeline CI/CD con Azure DevOps

### azure-pipelines.yml

```yaml
trigger:
  branches:
    include:
      - main
      - develop
      - staging

pool:
  vmImage: 'ubuntu-latest'

variables:
  - group: aws-credentials
  - name: AWS_REGION
    value: 'us-east-1'

stages:
  - stage: Build
    displayName: 'Build Static Site'
    jobs:
      - job: BuildJob
        displayName: 'Build and Test'
        steps:
          - task: NodeTool@0
            inputs:
              versionSpec: '18.x'
            displayName: 'Install Node.js'

          - script: |
              npm ci
              npm run build
              npm run test
            displayName: 'Install dependencies and build'

          - task: PublishBuildArtifacts@1
            inputs:
              PathtoPublish: 'dist'
              ArtifactName: 'static-site'
            displayName: 'Publish build artifacts'

  - stage: Deploy_Dev
    displayName: 'Deploy to Development'
    dependsOn: Build
    condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/develop'))
    jobs:
      - deployment: DeployDev
        displayName: 'Deploy to Dev S3'
        environment: 'development'
        strategy:
          runOnce:
            deploy:
              steps:
                - task: DownloadBuildArtifacts@0
                  inputs:
                    artifactName: 'static-site'
                    downloadPath: '$(System.ArtifactsDirectory)'

                - task: AWSCLI@1
                  inputs:
                    awsCredentials: 'aws-service-connection'
                    regionName: '$(AWS_REGION)'
                    awsCommand: 's3'
                    awsSubCommand: 'sync'
                    awsArguments: '$(System.ArtifactsDirectory)/static-site s3://api-portal-dev --delete'
                  displayName: 'Sync to S3 Dev'

                - task: AWSCLI@1
                  inputs:
                    awsCredentials: 'aws-service-connection'
                    regionName: '$(AWS_REGION)'
                    awsCommand: 'cloudfront'
                    awsSubCommand: 'create-invalidation'
                    awsArguments: '--distribution-id $(DEV_CLOUDFRONT_ID) --paths "/*"'
                  displayName: 'Invalidate CloudFront Cache'

  - stage: Deploy_Staging
    displayName: 'Deploy to Staging'
    dependsOn: Build
    condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/staging'))
    jobs:
      - deployment: DeployStaging
        displayName: 'Deploy to Staging S3'
        environment: 'staging'
        strategy:
          runOnce:
            deploy:
              steps:
                - task: DownloadBuildArtifacts@0
                  inputs:
                    artifactName: 'static-site'
                    downloadPath: '$(System.ArtifactsDirectory)'

                - task: AWSCLI@1
                  inputs:
                    awsCredentials: 'aws-service-connection'
                    regionName: '$(AWS_REGION)'
                    awsCommand: 's3'
                    awsSubCommand: 'sync'
                    awsArguments: '$(System.ArtifactsDirectory)/static-site s3://api-portal-staging --delete'
                  displayName: 'Sync to S3 Staging'

                - task: AWSCLI@1
                  inputs:
                    awsCredentials: 'aws-service-connection'
                    regionName: '$(AWS_REGION)'
                    awsCommand: 'cloudfront'
                    awsSubCommand: 'create-invalidation'
                    awsArguments: '--distribution-id $(STAGING_CLOUDFRONT_ID) --paths "/*"'
                  displayName: 'Invalidate CloudFront Cache'

  - stage: Deploy_Production
    displayName: 'Deploy to Production'
    dependsOn: Build
    condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
    jobs:
      - deployment: DeployProduction
        displayName: 'Deploy to Production S3'
        environment: 'production'
        strategy:
          runOnce:
            deploy:
              steps:
                - task: DownloadBuildArtifacts@0
                  inputs:
                    artifactName: 'static-site'
                    downloadPath: '$(System.ArtifactsDirectory)'

                - task: AWSCLI@1
                  inputs:
                    awsCredentials: 'aws-service-connection'
                    regionName: '$(AWS_REGION)'
                    awsCommand: 's3'
                    awsSubCommand: 'sync'
                    awsArguments: '$(System.ArtifactsDirectory)/static-site s3://api-portal-prod --delete'
                  displayName: 'Sync to S3 Production'

                - task: AWSCLI@1
                  inputs:
                    awsCredentials: 'aws-service-connection'
                    regionName: '$(AWS_REGION)'
                    awsCommand: 'cloudfront'
                    awsSubCommand: 'create-invalidation'
                    awsArguments: '--distribution-id $(PROD_CLOUDFRONT_ID) --paths "/*"'
                  displayName: 'Invalidate CloudFront Cache'

                - script: |
                    echo "Deployment completed successfully!"
                    echo "URL: https://api-portal.bgr.com"
                  displayName: 'Deployment Summary'
```

---

## 🔧 Configuración de Azure DevOps

### 1. Service Connections

#### AWS Service Connection
```bash
# En Azure DevOps:
# Project Settings → Service connections → New service connection → AWS

Name: aws-service-connection
Access Key ID: $(AWS_ACCESS_KEY_ID)
Secret Access Key: $(AWS_SECRET_ACCESS_KEY)
```

#### Variable Groups
```yaml
# Library → Variable groups → New variable group

Name: aws-credentials
Variables:
  - AWS_ACCESS_KEY_ID: [encrypted]
  - AWS_SECRET_ACCESS_KEY: [encrypted]
  - DEV_CLOUDFRONT_ID: E1234567890ABC
  - STAGING_CLOUDFRONT_ID: E0987654321XYZ
  - PROD_CLOUDFRONT_ID: E1122334455DEF
  - AWS_REGION: us-east-1
```

### 2. Environments

```bash
# Pipelines → Environments → New environment

Environments:
  - development (auto-approve)
  - staging (auto-approve)
  - production (manual approval required)
```

### 3. Branch Policies

```yaml
# Repos → Branches → Branch policies

main:
  - Require pull request reviews: 2
  - Require build validation
  - Require linked work items
  - No direct pushes

staging:
  - Require pull request reviews: 1
  - Require build validation

develop:
  - No restrictions (CI only)
```

---

## 🚀 Workflow de Desarrollo

### Flujo Completo

```
Developer → Azure Repos (Git Push)
              ↓
         Azure Pipelines (Build)
              ↓
         Azure Artifacts (Store)
              ↓
         Azure Pipelines (Deploy)
              ↓
         AWS S3 (Upload)
              ↓
         CloudFront (Invalidate)
              ↓
         Users (Access via CDN)
```

### Branching Strategy

```
main (production)
  ↑
staging (pre-production)
  ↑
develop (development)
  ↑
feature/* (feature branches)
```

### Proceso de Deploy

#### 1. Feature Development
```bash
# Crear feature branch
git checkout -b feature/nueva-funcionalidad

# Desarrollar y commit
git add .
git commit -m "feat: nueva funcionalidad"

# Push a Azure Repos
git push origin feature/nueva-funcionalidad

# Crear Pull Request en Azure DevOps
# → Build automático se ejecuta
# → Code review
# → Merge a develop
```

#### 2. Deploy a Development
```bash
# Merge a develop trigger auto-deploy
git checkout develop
git merge feature/nueva-funcionalidad
git push origin develop

# Azure Pipeline:
# → Build
# → Deploy to S3 Dev
# → Invalidate CloudFront
# → Available at: https://dev.api-portal.bgr.com
```

#### 3. Deploy a Staging
```bash
# Merge a staging
git checkout staging
git merge develop
git push origin staging

# Azure Pipeline:
# → Build
# → Deploy to S3 Staging
# → Invalidate CloudFront
# → Available at: https://staging.api-portal.bgr.com
```

#### 4. Deploy a Production
```bash
# Merge a main (requiere PR approval)
git checkout main
git merge staging
git push origin main

# Azure Pipeline:
# → Build
# → Wait for manual approval
# → Deploy to S3 Production
# → Invalidate CloudFront
# → Available at: https://api-portal.bgr.com
```

---

## 🛠️ Setup Inicial

### Paso 1: Configurar Azure DevOps (1 día)

#### 1.1 Crear Proyecto
```bash
# En Azure DevOps
Organization → New Project

Name: Api Portal
Visibility: Private
Version control: Git
Work item process: Agile
```

#### 1.2 Importar Código
```bash
# Repos → Import repository
Source type: Git
Clone URL: [URL del repo actual]
```

#### 1.3 Configurar Service Connection
```bash
# Project Settings → Service connections
New service connection → AWS
Name: aws-service-connection
Access Key ID: [IAM User Key]
Secret Access Key: [IAM User Secret]
```

#### 1.4 Crear Variable Group
```bash
# Pipelines → Library → Variable groups
Name: aws-credentials
Variables:
  - AWS_ACCESS_KEY_ID (secret)
  - AWS_SECRET_ACCESS_KEY (secret)
  - DEV_CLOUDFRONT_ID
  - STAGING_CLOUDFRONT_ID
  - PROD_CLOUDFRONT_ID
```

### Paso 2: Configurar AWS (1 día)

#### 2.1 Crear S3 Buckets
```bash
# Development
aws s3 mb s3://api-portal-dev --region us-east-1
aws s3 website s3://api-portal-dev --index-document index.html

# Staging
aws s3 mb s3://api-portal-staging --region us-east-1
aws s3 website s3://api-portal-staging --index-document index.html

# Production
aws s3 mb s3://api-portal-prod --region us-east-1
aws s3 website s3://api-portal-prod --index-document index.html
```

#### 2.2 Configurar Bucket Policies
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::api-portal-prod/*"
    }
  ]
}
```

#### 2.3 Crear CloudFront Distributions
```bash
# Para cada ambiente (dev, staging, prod)
aws cloudfront create-distribution \
  --origin-domain-name api-portal-prod.s3.amazonaws.com \
  --default-root-object index.html
```

#### 2.4 Configurar Route 53
```bash
# Crear hosted zone
aws route53 create-hosted-zone --name api-portal.bgr.com

# Crear records
# dev.api-portal.bgr.com → CloudFront Dev
# staging.api-portal.bgr.com → CloudFront Staging
# api-portal.bgr.com → CloudFront Prod
```

#### 2.5 Solicitar Certificados SSL
```bash
# ACM en us-east-1 (para CloudFront)
aws acm request-certificate \
  --domain-name api-portal.bgr.com \
  --subject-alternative-names *.api-portal.bgr.com \
  --validation-method DNS
```

### Paso 3: Crear Pipeline (1 día)

#### 3.1 Crear azure-pipelines.yml
```bash
# En la raíz del proyecto
touch azure-pipelines.yml
# Copiar contenido del pipeline anterior
```

#### 3.2 Configurar Pipeline en Azure DevOps
```bash
# Pipelines → New pipeline
Where is your code? → Azure Repos Git
Select repository → Api Portal
Configure → Existing Azure Pipelines YAML file
Path: /azure-pipelines.yml
```

#### 3.3 Configurar Environments
```bash
# Pipelines → Environments
Create: development (auto-approve)
Create: staging (auto-approve)
Create: production (manual approval)
```

### Paso 4: Testing (1 día)

#### 4.1 Test Build
```bash
# Push a develop
git checkout develop
git commit --allow-empty -m "test: trigger pipeline"
git push origin develop

# Verificar en Azure Pipelines
# → Build debe completarse exitosamente
```

#### 4.2 Test Deploy
```bash
# Verificar deploy a dev
# → S3 debe tener archivos
# → CloudFront debe servir contenido
# → https://dev.api-portal.bgr.com debe funcionar
```

#### 4.3 Test Full Flow
```bash
# Feature → Develop → Staging → Production
git checkout -b feature/test
# ... hacer cambios ...
git push origin feature/test
# → Crear PR a develop
# → Merge y verificar deploy a dev
# → Merge a staging y verificar
# → Merge a main (con approval) y verificar prod
```

---

## 📊 Ventajas de Azure DevOps + AWS

### Multi-Cloud Best Practices
- ✅ **Best-of-breed**: Mejor CI/CD (Azure) + Mejor CDN (AWS)
- ✅ **Vendor independence**: No lock-in a un solo proveedor
- ✅ **Flexibility**: Cambiar componentes independientemente
- ✅ **Resilience**: Diversificación de riesgos

### Azure DevOps Strengths
- ✅ **Integración con Microsoft**: Teams, Office 365, Active Directory
- ✅ **Azure Boards**: Project management integrado
- ✅ **Azure Repos**: Git enterprise-grade
- ✅ **Azure Artifacts**: Package management
- ✅ **Pricing**: Primeros 5 usuarios gratis

### AWS Strengths
- ✅ **CloudFront**: CDN más rápido y extenso
- ✅ **S3**: Storage más confiable (99.999999999%)
- ✅ **Global reach**: 400+ edge locations
- ✅ **Pricing**: Pay-as-you-go, muy económico

---

## 💰 Costos Detallados

### Azure DevOps
| Concepto | Costo |
|----------|-------|
| Basic Plan (5 usuarios) | $0/mes |
| Azure Pipelines (1 parallel job) | $0/mes (1,800 min gratis) |
| Azure Repos (ilimitado) | Incluido |
| Azure Boards | Incluido |
| **Total Azure DevOps** | **$0/mes** |

### AWS
| Concepto | Costo |
|----------|-------|
| S3 Storage (1GB) | $0.02/mes |
| S3 Requests | $0.10/mes |
| CloudFront Data Transfer (10GB) | $0.85/mes |
| CloudFront Requests | $0.03/mes |
| Route 53 Hosted Zone | $0.50/mes |
| ACM Certificate | $0/mes |
| **Total AWS** | **$1.50/mes** |

### Total Multi-Cloud
**$1.50/mes** (vs $2,000/mes actual = 99.9% ahorro)

---

## 🔒 Seguridad

### Azure DevOps Security
- ✅ **Azure AD Integration**: SSO con Active Directory
- ✅ **Branch Policies**: Protección de branches
- ✅ **Code Reviews**: Pull request obligatorios
- ✅ **Secrets Management**: Variable groups encriptados
- ✅ **Audit Logs**: Trazabilidad completa

### AWS Security
- ✅ **IAM Roles**: Least privilege access
- ✅ **S3 Encryption**: At rest y in transit
- ✅ **CloudFront**: SSL/TLS obligatorio
- ✅ **WAF** (opcional): Firewall de aplicaciones
- ✅ **CloudTrail**: Audit logs

### Best Practices
```yaml
# Secrets en Azure DevOps Variable Groups (encrypted)
# IAM User con permisos mínimos:
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:PutObject",
        "s3:GetObject",
        "s3:DeleteObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::api-portal-*",
        "arn:aws:s3:::api-portal-*/*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "cloudfront:CreateInvalidation"
      ],
      "Resource": "*"
    }
  ]
}
```

---

## 📈 Métricas y Monitoreo

### Azure DevOps Dashboards
```yaml
Widgets:
  - Build Success Rate
  - Deployment Frequency
  - Lead Time for Changes
  - Mean Time to Recovery
  - Change Failure Rate
```

### AWS CloudWatch
```yaml
Metrics:
  - CloudFront Requests
  - CloudFront Error Rate
  - S3 Bucket Size
  - CloudFront Cache Hit Rate
  
Alarms:
  - Error Rate > 1%
  - Latency > 1s
  - 4xx Errors > 100/min
  - 5xx Errors > 10/min
```

---

## ✅ Checklist de Implementación

### Azure DevOps Setup
- [ ] Proyecto creado
- [ ] Repositorio importado
- [ ] Service connection configurado
- [ ] Variable groups creados
- [ ] Environments configurados
- [ ] Branch policies aplicados
- [ ] Pipeline creado y testeado

### AWS Setup
- [ ] S3 buckets creados (dev, staging, prod)
- [ ] CloudFront distributions configuradas
- [ ] Route 53 hosted zone creada
- [ ] DNS records configurados
- [ ] ACM certificates solicitados y validados
- [ ] IAM user creado con permisos mínimos
- [ ] CloudWatch alarms configurados

### Testing
- [ ] Build pipeline funciona
- [ ] Deploy a dev funciona
- [ ] Deploy a staging funciona
- [ ] Deploy a prod funciona (con approval)
- [ ] CloudFront invalidation funciona
- [ ] Custom domains funcionan
- [ ] SSL certificates activos
- [ ] Rollback testeado

---

## 🎯 Próximos Pasos

1. [ ] Aprobar arquitectura multi-cloud
2. [ ] Configurar Azure DevOps (1 día)
3. [ ] Configurar AWS (1 día)
4. [ ] Crear pipeline (1 día)
5. [ ] Testing completo (1 día)
6. [ ] Go-live (1 día)

**Total: 5 días**

---

**Última actualización**: 2025-12-04  
**Versión**: 2.0 - Azure DevOps Integration  
**Estado**: Listo para implementación
