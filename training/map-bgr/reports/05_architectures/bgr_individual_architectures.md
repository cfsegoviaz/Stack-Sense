# BGR Applications - Individual Target Architectures

**Project:** BGR Applications Modernization to AWS  
**Date:** 2025-12-01  
**Document Type:** Technical Architecture Specifications

---

## 📋 Table of Contents

1. [PortalGuiaBGR](#1-portalguiabgr)
2. [Api Portal](#2-api-portal)
3. [PortalAdministrativoBGR](#3-portaladministrativobgr)
4. [Backoffice Sistemas BGR](#4-backoffice-sistemas-bgr)
5. [Backoffice Banca Digital](#5-backoffice-banca-digital)
6. [Saras](#6-saras)

---

## 1. PortalGuiaBGR

### Overview
**Description:** Guía telefónica del banco  
**Users:** Bank Employees  
**Priority:** P1 - Wave 1  
**Migration:** Months 2-3

### Current State
- **Stack:** .NET Framework 4.7.1 (Obsolete)
- **Server:** ECBRTSW21 (shared)
- **Database:** SQL Server 2016 Enterprise
- **OS:** Windows Server 2016

### Target Architecture

![PortalGuiaBGR Architecture](https://stack-sense.s3.us-east-1.amazonaws.com/map-bgr/diagrams/app_portalguiabgr.png)

### AWS Components

#### Compute Layer
- **Service:** Amazon ECS with Fargate
- **Configuration:** 
  - 2 vCPU, 4 GB RAM per task
  - Auto-scaling: 2-6 tasks
  - Average: 3 tasks running
- **Container:** .NET 8 on Linux
- **Cost:** $216.23/month

#### Database Layer
- **Service:** Amazon RDS for SQL Server Standard
- **Configuration:**
  - Instance: db.m5.large (2 vCPU, 8 GB RAM)
  - Multi-AZ deployment
  - Storage: 500 GB gp3 (shared)
  - Automated backups (7 days)
- **Cost:** $175.13/month (shared with 3 other apps)

#### Networking
- **DNS:** Route 53 (guiabgr.bgr.com)
- **Load Balancer:** Application Load Balancer
- **SSL/TLS:** AWS Certificate Manager
- **Cost:** $8.07/month

#### Security & Identity
- **Authentication:** AWS Managed Microsoft AD
- **Secrets:** AWS Secrets Manager
- **Configuration:** Systems Manager Parameter Store

#### Observability
- **Logs:** CloudWatch Logs
- **Metrics:** CloudWatch Metrics
- **Tracing:** AWS X-Ray
- **Alerts:** Amazon SNS

### Technical Specifications

| Component | Specification |
|-----------|--------------|
| **Availability** | 99.99% (Multi-AZ) |
| **Scalability** | Auto-scale 2-6 tasks |
| **Deployment** | Blue/green via CodePipeline |
| **Backup** | Automated daily, 7-day retention |
| **Monitoring** | CloudWatch + X-Ray |
| **Security** | TLS 1.3, Secrets Manager, IAM |

### Monthly Cost Breakdown

| Component | Cost |
|-----------|------|
| ECS Fargate (3 tasks avg) | $216.23 |
| RDS SQL Server (shared) | $175.13 |
| Application Load Balancer | $8.07 |
| Shared Services | $8.00 |
| **Total** | **$407.43** |

### Migration Strategy

**Phase 1: Code Modernization (4 weeks)**
- Migrate .NET Framework 4.7.1 → .NET 8
- Remove ajaxToolkit dependencies
- Implement dependency injection
- Add health check endpoints

**Phase 2: Containerization (2 weeks)**
- Create Dockerfile (Linux base)
- Build CI/CD pipeline
- Deploy to dev environment
- Performance testing

**Phase 3: Database Migration (2 weeks)**
- Migrate to RDS SQL Server
- Configure Multi-AZ
- Test failover scenarios
- Optimize queries

**Phase 4: Cutover (1 week)**
- Blue/green deployment
- DNS cutover
- Monitor and validate
- Decommission old infrastructure

---

## 2. Api Portal

### Overview
**Description:** Portal estático de APIs que define entrada y salida de peticiones  
**Users:** API Clients (Mobile, Web, 3rd Party)  
**Priority:** P1 - Wave 1  
**Migration:** Months 2-3

### Current State
- **Stack:** .NET Framework 4.7.1 (Obsolete)
- **Server:** ECBRTSW21 (shared)
- **Database:** SQL Server 2016 Enterprise
- **OS:** Windows Server 2016

### Target Architecture

![Api Portal Architecture](https://stack-sense.s3.us-east-1.amazonaws.com/map-bgr/diagrams/app_apiportal.png)

### AWS Components

#### Compute Layer
- **Service:** Amazon ECS with Fargate
- **Configuration:** 
  - 2 vCPU, 4 GB RAM per task
  - Auto-scaling: 3-10 tasks (high traffic)
  - Average: 5 tasks running
- **Container:** .NET 8 API on Linux
- **Cost:** $360.39/month

#### Database Layer
- **Service:** Amazon RDS for SQL Server Standard
- **Configuration:**
  - Instance: db.m5.large
  - Multi-AZ deployment
  - Storage: 500 GB gp3 (shared)
- **Cost:** $175.13/month (shared)

#### Networking
- **DNS:** Route 53 (api.bgr.com)
- **Load Balancer:** Application Load Balancer with rate limiting
- **SSL/TLS:** AWS Certificate Manager
- **Cost:** $8.07/month

#### API Management
- **Rate Limiting:** ALB rules
- **Authentication:** API Keys via Managed AD
- **Throttling:** ALB + CloudWatch alarms

#### Security & Identity
- **Authentication:** AWS Managed Microsoft AD
- **API Keys:** Secrets Manager
- **Configuration:** Parameter Store

#### Observability
- **API Metrics:** CloudWatch custom metrics
- **Logs:** CloudWatch Logs with insights
- **Tracing:** X-Ray for request tracing
- **Alerts:** SNS for API errors/latency

### Technical Specifications

| Component | Specification |
|-----------|--------------|
| **Availability** | 99.99% (Multi-AZ) |
| **Scalability** | Auto-scale 3-10 tasks |
| **Max Throughput** | 10,000 req/sec |
| **Avg Latency** | < 100ms |
| **Rate Limit** | 1,000 req/min per client |
| **Security** | TLS 1.3, API Keys, WAF |

### Monthly Cost Breakdown

| Component | Cost |
|-----------|------|
| ECS Fargate (5 tasks avg) | $360.39 |
| RDS SQL Server (shared) | $175.13 |
| Application Load Balancer | $8.07 |
| Shared Services | $8.00 |
| **Total** | **$551.59** |

### Migration Strategy

**Phase 1: API Modernization (4 weeks)**
- Migrate to .NET 8 Web API
- Implement OpenAPI/Swagger
- Add versioning support
- Implement rate limiting

**Phase 2: Containerization (2 weeks)**
- Create optimized Dockerfile
- Configure auto-scaling policies
- Load testing (10k req/sec)
- Performance optimization

**Phase 3: Database & Integration (2 weeks)**
- Migrate to RDS
- Configure connection pooling
- Test high-load scenarios
- Optimize database queries

**Phase 4: Production Deployment (1 week)**
- Gradual traffic shift (10% → 100%)
- Monitor API metrics
- Validate SLAs
- Complete cutover

---

## 3. PortalAdministrativoBGR

### Overview
**Description:** Permite realizar tareas de desbloqueo y deslogueo de usuarios  
**Users:** IT Administrators  
**Priority:** P2 - Wave 2  
**Migration:** Month 5

### Current State
- **Stack:** .NET Framework 4.7.1 (Obsolete)
- **Database:** SQL Server 2016 Enterprise
- **OS:** Windows Server 2016

### Target Architecture

![PortalAdministrativoBGR Architecture](https://stack-sense.s3.us-east-1.amazonaws.com/map-bgr/diagrams/app_portaladministrativo.png)

### AWS Components

#### Compute Layer
- **Service:** Amazon ECS with Fargate
- **Configuration:** 
  - 1 vCPU, 2 GB RAM per task (low traffic)
  - Auto-scaling: 2-4 tasks
  - Average: 2 tasks running
- **Container:** .NET 8 on Linux
- **Cost:** $72.08/month

#### Database Layer
- **Service:** Amazon RDS for SQL Server Standard
- **Configuration:**
  - Instance: db.m5.large (shared)
  - Multi-AZ deployment
- **Cost:** $175.13/month (shared)

#### Networking
- **DNS:** Route 53 (admin.bgr.com)
- **Load Balancer:** Application Load Balancer
- **SSL/TLS:** AWS Certificate Manager
- **Cost:** $8.07/month

#### Security & Identity
- **Authentication:** AWS Managed Microsoft AD (admin access)
- **Secrets:** Secrets Manager
- **Configuration:** Parameter Store

#### Observability
- **Logs:** CloudWatch Logs
- **Metrics:** CloudWatch Metrics
- **Alerts:** SNS for admin actions

### Technical Specifications

| Component | Specification |
|-----------|--------------|
| **Availability** | 99.9% |
| **Scalability** | Auto-scale 2-4 tasks |
| **Users** | ~50 IT admins |
| **Security** | MFA required, audit logs |
| **Compliance** | All actions logged to CloudTrail |

### Monthly Cost Breakdown

| Component | Cost |
|-----------|------|
| ECS Fargate (2 tasks avg) | $72.08 |
| RDS SQL Server (shared) | $175.13 |
| Application Load Balancer | $8.07 |
| Shared Services | $8.00 |
| **Total** | **$263.28** |

### Migration Strategy

**Phase 1: Modernization (3 weeks)**
- Migrate to .NET 8
- Implement MFA
- Add audit logging
- Security hardening

**Phase 2: Deployment (1 week)**
- Containerize application
- Deploy to AWS
- Admin user testing
- Production cutover

---

## 4. Backoffice Sistemas BGR

### Overview
**Description:** Aplicación parametrizadora para diversos sistemas del banco  
**Users:** Bank Staff  
**Priority:** P2 - Wave 2  
**Migration:** Month 6

### Current State
- **Stack:** .NET Framework 4.7.1 (Obsolete)
- **Server:** ECBRTSW21 (shared)
- **Database:** SQL Server 2016 Enterprise
- **OS:** Windows Server 2016

### Target Architecture

![Backoffice Sistemas BGR Architecture](https://stack-sense.s3.us-east-1.amazonaws.com/map-bgr/diagrams/app_backoffice_sistemas.png)

### AWS Components

#### Compute Layer
- **Service:** Amazon ECS with Fargate
- **Configuration:** 
  - 2 vCPU, 4 GB RAM per task
  - Auto-scaling: 2-6 tasks
  - Average: 3 tasks running
- **Container:** .NET 8 on Linux
- **Cost:** $216.23/month

#### Database Layer
- **Service:** Amazon RDS for SQL Server Standard
- **Configuration:**
  - Instance: db.m5.large (shared)
  - Multi-AZ deployment
- **Cost:** $175.13/month (shared)

#### Networking
- **DNS:** Route 53 (backoffice.bgr.com)
- **Load Balancer:** Application Load Balancer
- **SSL/TLS:** AWS Certificate Manager
- **Cost:** $8.07/month

#### Security & Identity
- **Authentication:** AWS Managed Microsoft AD
- **Secrets:** Secrets Manager
- **Configuration:** Parameter Store (system configs)

#### Observability
- **Logs:** CloudWatch Logs
- **Metrics:** CloudWatch Metrics
- **Alerts:** SNS for system changes

### Technical Specifications

| Component | Specification |
|-----------|--------------|
| **Availability** | 99.99% (Multi-AZ) |
| **Scalability** | Auto-scale 2-6 tasks |
| **Users** | ~200 bank staff |
| **Security** | Role-based access control |
| **Audit** | All config changes logged |

### Monthly Cost Breakdown

| Component | Cost |
|-----------|------|
| ECS Fargate (3 tasks avg) | $216.23 |
| RDS SQL Server (shared) | $175.13 |
| Application Load Balancer | $8.07 |
| Shared Services | $8.00 |
| **Total** | **$407.43** |

### Migration Strategy

**Phase 1: Modernization (4 weeks)**
- Migrate to .NET 8
- Implement RBAC
- Add configuration versioning
- Audit trail implementation

**Phase 2: Deployment (2 weeks)**
- Containerization
- Deploy to AWS
- User acceptance testing
- Production cutover

---

## 5. Backoffice Banca Digital

### Overview
**Description:** Aplicación parametrizadora para Banca Digital  
**Users:** Digital Banking Team  
**Priority:** P3 - Wave 3  
**Migration:** Months 7-8

### Current State
- **Stack:** .NET Core 8 ✅ (Modern)
- **Database:** SQL Server 2019 Enterprise
- **OS:** Windows Server 2019

### Target Architecture

![Backoffice Banca Digital Architecture](https://stack-sense.s3.us-east-1.amazonaws.com/map-bgr/diagrams/app_backoffice_banca.png)

### AWS Components

#### Compute Layer
- **Service:** Amazon ECS with Fargate
- **Configuration:** 
  - 2 vCPU, 4 GB RAM per task
  - Auto-scaling: 2-6 tasks
  - Average: 3 tasks running
- **Container:** .NET 8 on Linux (already modern!)
- **Cost:** $216.23/month

#### Database Layer
- **Service:** Amazon RDS for SQL Server 2019 Standard
- **Configuration:**
  - Instance: db.m5.large
  - Multi-AZ deployment
  - Storage: 300 GB gp3
- **Cost:** $326.95/month (shared with Saras)

#### Networking
- **DNS:** Route 53 (banca.bgr.com)
- **Load Balancer:** Application Load Balancer
- **SSL/TLS:** AWS Certificate Manager
- **Cost:** $8.07/month

#### Security & Identity
- **Authentication:** Amazon Cognito User Pool (modern auth)
- **Secrets:** Secrets Manager
- **Configuration:** Parameter Store

#### Observability
- **Logs:** CloudWatch Logs
- **Metrics:** CloudWatch Metrics
- **Tracing:** X-Ray

### Technical Specifications

| Component | Specification |
|-----------|--------------|
| **Availability** | 99.99% (Multi-AZ) |
| **Scalability** | Auto-scale 2-6 tasks |
| **Users** | ~100 digital banking staff |
| **Security** | Cognito MFA, OAuth 2.0 |
| **Modern Stack** | .NET 8, no code migration needed |

### Monthly Cost Breakdown

| Component | Cost |
|-----------|------|
| ECS Fargate (3 tasks avg) | $216.23 |
| RDS SQL Server 2019 (shared) | $326.95 |
| Application Load Balancer | $8.07 |
| Shared Services | $8.00 |
| **Total** | **$559.25** |

### Migration Strategy

**Phase 1: Containerization Only (2 weeks)**
- Create Dockerfile (no code changes!)
- Configure CI/CD pipeline
- Deploy to dev/staging
- Performance validation

**Phase 2: Database Migration (2 weeks)**
- Migrate to RDS SQL Server 2019
- Configure Multi-AZ
- Test and validate
- Optimize performance

**Phase 3: Production Deployment (1 week)**
- Blue/green deployment
- Monitor and validate
- Complete cutover

**Note:** Fast migration due to modern stack (.NET 8)

---

## 6. Saras

### Overview
**Description:** Aplicación para análisis de riesgo ambiental y social  
**Users:** Risk Analysts  
**Priority:** P3 - Wave 3  
**Migration:** Months 8-9

### Current State
- **Stack:** .NET Core 8 ✅ (Modern)
- **Database:** SQL Server 2019 Enterprise
- **OS:** Windows Server 2019

### Target Architecture

![Saras Architecture](https://stack-sense.s3.us-east-1.amazonaws.com/map-bgr/diagrams/app_saras.png)

### AWS Components

#### Compute Layer
- **Service:** Amazon ECS with Fargate
- **Configuration:** 
  - 2 vCPU, 4 GB RAM per task
  - Auto-scaling: 2-4 tasks
  - Average: 2 tasks running
- **Container:** .NET 8 on Linux (already modern!)
- **Cost:** $144.16/month

#### Database Layer
- **Service:** Amazon RDS for SQL Server 2019 Standard
- **Configuration:**
  - Instance: db.m5.large (shared with Banca Digital)
  - Multi-AZ deployment
  - Storage: 300 GB gp3 (shared)
- **Cost:** $326.95/month (shared)

#### Networking
- **DNS:** Route 53 (saras.bgr.com)
- **Load Balancer:** Application Load Balancer
- **SSL/TLS:** AWS Certificate Manager
- **Cost:** $8.07/month

#### Security & Identity
- **Authentication:** Amazon Cognito User Pool
- **Secrets:** Secrets Manager
- **Configuration:** Parameter Store

#### Observability
- **Logs:** CloudWatch Logs
- **Metrics:** CloudWatch Metrics
- **Tracing:** X-Ray

### Technical Specifications

| Component | Specification |
|-----------|--------------|
| **Availability** | 99.99% (Multi-AZ) |
| **Scalability** | Auto-scale 2-4 tasks |
| **Users** | ~50 risk analysts |
| **Security** | Cognito MFA, OAuth 2.0 |
| **Modern Stack** | .NET 8, no code migration needed |

### Monthly Cost Breakdown

| Component | Cost |
|-----------|------|
| ECS Fargate (2 tasks avg) | $144.16 |
| RDS SQL Server 2019 (shared) | $326.95 |
| Application Load Balancer | $8.07 |
| Shared Services | $8.00 |
| **Total** | **$487.18** |

### Migration Strategy

**Phase 1: Containerization Only (2 weeks)**
- Create Dockerfile (no code changes!)
- Configure CI/CD pipeline
- Deploy to dev/staging
- Performance validation

**Phase 2: Database Migration (1 week)**
- Share RDS instance with Banca Digital
- Migrate data
- Test and validate

**Phase 3: Production Deployment (1 week)**
- Blue/green deployment
- Monitor and validate
- Complete cutover

**Note:** Fast migration due to modern stack (.NET 8)

---

## 📊 Comparative Summary

### Cost Comparison by Application

| Application | Current (On-Prem) | AWS Target | Savings | % Reduction |
|-------------|-------------------|------------|---------|-------------|
| PortalGuiaBGR | $665 | $407 | $258 | 39% |
| Api Portal | $665 | $552 | $113 | 17% |
| PortalAdministrativoBGR | $665 | $263 | $402 | 60% |
| Backoffice Sistemas BGR | $665 | $407 | $258 | 39% |
| Backoffice Banca Digital | $665 | $559 | $106 | 16% |
| Saras | $665 | $487 | $178 | 27% |
| **TOTAL (6 apps)** | **$3,990** | **$2,675** | **$1,315** | **33%** |

### Technical Debt Summary

| Application | Code Migration | Complexity | Duration |
|-------------|----------------|------------|----------|
| PortalGuiaBGR | .NET 4.7.1 → 8 | Medium | 9 weeks |
| Api Portal | .NET 4.7.1 → 8 | Medium | 9 weeks |
| PortalAdministrativoBGR | .NET 4.7.1 → 8 | Low | 4 weeks |
| Backoffice Sistemas BGR | .NET 4.7.1 → 8 | Medium | 6 weeks |
| Backoffice Banca Digital | None (.NET 8) | Low | 5 weeks |
| Saras | None (.NET 8) | Low | 4 weeks |

### Architecture Patterns

**All applications share:**
- ✅ Multi-AZ high availability
- ✅ Auto-scaling compute (ECS Fargate)
- ✅ Managed databases (RDS Multi-AZ)
- ✅ SSL/TLS encryption (ACM)
- ✅ Centralized logging (CloudWatch)
- ✅ Secrets management (Secrets Manager)
- ✅ Infrastructure as Code (CDK/Terraform)
- ✅ CI/CD automation (CodePipeline)

---

## ✅ Next Steps

### For Each Application

1. **Review architecture diagram** with application team
2. **Validate technical specifications** and sizing
3. **Approve migration timeline** and resources
4. **Assign development team** for modernization
5. **Set up AWS environments** (dev, staging, prod)
6. **Execute migration plan** per wave schedule
7. **Validate post-migration** performance and costs
8. **Optimize and tune** based on actual usage

### Documentation

- Architecture diagrams: `training/map-bgr/diagrams/app_*.png`
- Detailed pricing: `training/map-bgr/reports/bgr_aws_pricing_detailed.md`
- Migration plan: `training/map-bgr/reports/bgr_applications_modernization.md`

---

**Document Version:** 1.0  
**Last Updated:** 2025-12-01  
**Maintained by:** BGR Migration Team
