# BGR Applications - AWS Migration Summary

**Date:** 2025-12-01  
**Project:** BGR Applications Modernization to AWS  
**Total Applications:** 8  
**Migration Duration:** 12 months

---

## 📊 Executive Summary

This document provides a comprehensive overview of the BGR applications migration to AWS, including architecture diagrams, detailed pricing based on RVTools data, and migration roadmap.

### Key Metrics

| Metric | Current (On-Premise) | Target (AWS) | Improvement |
|--------|---------------------|--------------|-------------|
| **Monthly Cost** | $5,320 | $2,677 | **49.7% reduction** |
| **Annual Cost** | $63,840 | $32,120 | **$31,720 savings** |
| **Infrastructure** | 2 physical servers | Serverless + Managed | **100% elastic** |
| **Deployment Time** | Days | Minutes | **99% faster** |
| **Availability** | Single AZ | Multi-AZ | **99.99% SLA** |

---

## 🏗️ Architecture Diagram

![BGR AWS Architecture](https://stack-sense.s3.us-east-1.amazonaws.com/map-bgr/diagrams/bgr_aws_architecture.png)

**Diagram Location:** `training/map-bgr/diagrams/bgr_aws_architecture.png`

### Architecture Highlights

1. **Multi-AZ High Availability:** All components deployed across 3 Availability Zones
2. **Containerized Applications:** 6 applications running on ECS Fargate (Linux containers)
3. **Managed Databases:** 2 RDS SQL Server instances with Multi-AZ and automated backups
4. **Shared Services:** Centralized AD, configuration, messaging, and observability
5. **CI/CD Pipeline:** Automated deployments with CodePipeline, CodeBuild, and ECR
6. **Security:** Secrets Manager, ACM, IAM, and network isolation

---

## 💰 Detailed Pricing Breakdown

**Full Pricing Document:** `training/map-bgr/reports/bgr_aws_pricing_detailed.md`

### Cost Summary by Category

| Category | Monthly Cost | % of Total |
|----------|--------------|------------|
| Compute (ECS Fargate) | $1,225.32 | 45.8% |
| Database (RDS SQL Server) | $1,354.40 | 50.6% |
| Networking (VPC, NAT, ALB) | $169.45 | 6.3% |
| Security & Identity | $154.50 | 5.8% |
| Observability | $87.50 | 3.3% |
| CI/CD | $16.00 | 0.6% |
| DevOps Tools | $208.00 | 7.8% |
| Governance | $30.00 | 1.1% |
| **TOTAL** | **$2,676.67** | **100%** |

### Pricing Based on RVTools Data

**Source Server:** ECBRTSW21
- **vCPU:** 4
- **RAM:** 8 GB
- **Storage:** 300 GB (2x 150GB disks)
- **Applications:** 6 apps sharing resources

**AWS Right-Sizing:**
- Distributed compute across 6 independent ECS Fargate tasks
- Auto-scaling: 2-10 tasks per application based on demand
- Total capacity: 12 vCPU, 24 GB RAM (elastic)
- Storage: 800 GB across 2 RDS instances with Multi-AZ

---

## 🎯 Migration Priority Matrix

| Application | Priority | Wave | Duration | Technical Debt | Complexity |
|-------------|----------|------|----------|----------------|------------|
| **PortalGuiaBGR** | P1 | Ola 1 | Months 2-3 | 🔴 High | 🟡 Medium |
| **Api Portal** | P1 | Ola 1 | Months 2-3 | 🔴 High | 🟡 Medium |
| **PortalAdministrativoBGR** | P2 | Ola 2 | Month 5 | 🔴 High | 🟢 Low |
| **Backoffice Sistemas BGR** | P2 | Ola 2 | Month 6 | 🔴 High | 🟡 Medium |
| **Backoffice Banca Digital** | P3 | Ola 3 | Months 7-8 | 🟢 Low | 🟢 Low |
| **Saras** | P3 | Ola 3 | Months 8-9 | 🟢 Low | 🟢 Low |
| **Seq** | P4 | Ola 4 | Month 10 | 🔴 High | 🟢 Low |
| **Sonar Qube** | P4 | Ola 4 | Months 11-12 | 🔴 High | 🟢 Low |

---

## 📅 Migration Timeline

```
Month 0:  ✅ Preparation - AWS Foundation Setup
          └─ VPC, IAM, Organizations, Control Tower
          
Month 1:  ✅ Ola 1 - Shared Services
          └─ Managed AD, Parameter Store, SNS/SQS, CloudWatch
          
Month 2:  ✅ Ola 1 - Database + Pilot App
          └─ RDS SQL Server + PortalGuiaBGR
          
Month 3:  ✅ Ola 1 - Validation
          └─ Performance testing, optimization
          
Month 4:  ✅ Ola 2 - Api Portal
          └─ High-traffic API gateway application
          
Month 5:  ✅ Ola 2 - PortalAdministrativoBGR
          └─ Administrative portal
          
Month 6:  ✅ Ola 2 - Backoffice Sistemas BGR
          └─ Systems backoffice application
          
Month 7:  ✅ Ola 3 - Backoffice Banca Digital
          └─ .NET Core 8 app + RDS SQL Server 2019
          
Month 8:  ✅ Ola 3 - Saras
          └─ Risk analysis application
          
Month 9:  ✅ Ola 3 - Validation
          └─ End-to-end testing
          
Month 10: ✅ Ola 4 - Seq → CloudWatch
          └─ Migrate logging to managed service
          
Month 11: ✅ Ola 4 - SonarQube → CodeGuru
          └─ Migrate code analysis to managed service
          
Month 12: ✅ Closure - Decommission On-Premise
          └─ Final cutover and infrastructure shutdown
```

---

## 🛠️ AWS Services Required

### Compute & Containers
- ✅ **Amazon ECS (Fargate)** - 6 containerized applications
- ✅ **Application Load Balancer** - 2 ALBs for traffic distribution
- ✅ **Amazon ECR** - Container image registry

### Database
- ✅ **Amazon RDS for SQL Server Standard** - 2 instances
  - Instance 1: PORTAL_ADMINISTRATIVO_BGR (shared by 4 apps)
  - Instance 2: Backoffice Banca Digital + Saras (shared by 2 apps)
- ✅ **Multi-AZ Deployment** - High availability
- ✅ **Automated Backups** - 7-day retention

### Networking
- ✅ **Amazon VPC** - Isolated network (10.0.0.0/16)
- ✅ **NAT Gateway** - 3 gateways (Multi-AZ)
- ✅ **Internet Gateway** - Public internet access
- ✅ **Subnets** - 3 public + 6 private across 3 AZs

### Security & Identity
- ✅ **AWS Managed Microsoft AD** - Active Directory replacement
- ✅ **AWS Secrets Manager** - Credentials management
- ✅ **AWS Certificate Manager** - SSL/TLS certificates
- ✅ **AWS IAM Identity Center** - SSO and access management

### DevOps & CI/CD
- ✅ **AWS CodePipeline** - Automated deployment pipelines
- ✅ **AWS CodeBuild** - Build and test automation
- ✅ **Amazon ECR** - Container registry

### Observability
- ✅ **Amazon CloudWatch** - Logs, metrics, dashboards, alarms
- ✅ **AWS X-Ray** - Distributed tracing
- ✅ **Amazon SNS** - Alerting and notifications

### Configuration & Messaging
- ✅ **AWS Systems Manager Parameter Store** - Configuration management
- ✅ **AWS AppConfig** - Dynamic configuration
- ✅ **Amazon SNS** - Pub/sub messaging
- ✅ **Amazon SQS** - Message queuing

### Governance & Compliance
- ✅ **AWS Organizations** - Multi-account management
- ✅ **AWS Control Tower** - Governance guardrails
- ✅ **AWS Config** - Resource compliance tracking
- ✅ **AWS CloudTrail** - Audit logging

---

## 💡 Cost Optimization Opportunities

### Immediate (0-3 months) - Save ~$5,440/year
1. **RDS Reserved Instances (1-year):** 30% savings on database costs
2. **Fargate Savings Plans (1-year):** 20% savings on compute costs
3. **Right-sizing after monitoring:** 10-15% reduction on over-provisioned resources

### Medium-term (3-6 months) - Save ~$13,000/year
4. **Migrate to Aurora PostgreSQL:** 60% database cost reduction
5. **Auto-scaling policies:** Scale down during off-hours (nights/weekends)

### Long-term (6-12 months) - Save ~$900/year
6. **Serverless migration:** Move low-traffic apps to Lambda
7. **S3 Intelligent-Tiering:** Optimize backup storage costs

**Total Potential Savings:** ~$20,840/year  
**Optimized Annual Cost:** ~$11,280 (82% reduction vs on-premise)

---

## 📈 Cost Breakdown by Application

| Application | Compute | Database | ALB | Shared | Total/Month |
|-------------|---------|----------|-----|--------|-------------|
| PortalGuiaBGR | $216 | $175 | $8 | $8 | **$407** |
| Api Portal | $360 | $175 | $8 | $8 | **$551** |
| PortalAdministrativoBGR | $72 | $175 | $8 | $8 | **$263** |
| Backoffice Sistemas BGR | $216 | $175 | $8 | $8 | **$407** |
| Backoffice Banca Digital | $216 | $327 | $8 | $8 | **$559** |
| Saras | $144 | $327 | $8 | $8 | **$487** |
| **Shared Infrastructure** | - | - | - | - | **$49** |
| **TOTAL** | | | | | **$2,677** |

---

## ✅ Key Benefits

### Technical Benefits
- ✅ **Eliminate Windows licensing costs** - Linux containers
- ✅ **Auto-scaling** - Handle traffic spikes automatically
- ✅ **Multi-AZ high availability** - 99.99% SLA
- ✅ **Automated backups** - Point-in-time recovery
- ✅ **Infrastructure as Code** - Repeatable deployments
- ✅ **Blue/green deployments** - Zero-downtime updates

### Operational Benefits
- ✅ **Reduced maintenance** - AWS manages infrastructure
- ✅ **Faster deployments** - Minutes vs days
- ✅ **Better observability** - Centralized logging and monitoring
- ✅ **Improved security** - Secrets management, encryption at rest/transit
- ✅ **Disaster recovery** - Multi-region capability

### Financial Benefits
- ✅ **49.7% cost reduction** - $31,720/year savings
- ✅ **No upfront investment** - Pay-as-you-go model
- ✅ **Predictable costs** - Monthly billing
- ✅ **Further optimization** - Up to 82% total reduction possible

---

## 📋 Next Steps

### Immediate Actions (Week 1-2)
1. ✅ Review architecture diagram with stakeholders
2. ✅ Validate pricing assumptions with finance team
3. ✅ Approve migration budget ($32,120/year)
4. ✅ Assign migration team (2-3 engineers + 1 architect)

### Short-term (Month 1)
5. ✅ Set up AWS Organization and accounts
6. ✅ Configure VPC and networking
7. ✅ Deploy shared services (AD, Parameter Store, CloudWatch)
8. ✅ Establish CI/CD pipelines

### Medium-term (Months 2-9)
9. ✅ Execute migration waves 1-3
10. ✅ Validate each application post-migration
11. ✅ Train operations team on AWS services
12. ✅ Implement cost monitoring and optimization

### Long-term (Months 10-12)
13. ✅ Migrate/replace DevOps tools (Wave 4)
14. ✅ Decommission on-premise infrastructure
15. ✅ Implement Reserved Instances and Savings Plans
16. ✅ Plan Aurora PostgreSQL migration

---

## 📚 Documentation References

- **Architecture Diagram:** `training/map-bgr/diagrams/bgr_aws_architecture.png`
- **Detailed Pricing:** `training/map-bgr/reports/bgr_aws_pricing_detailed.md`
- **Modernization Plan:** `training/map-bgr/reports/bgr_applications_modernization.md`
- **Application Data:** `reports/bgr_applications.json`
- **RVTools Data:** `training/map-bgr/RVTools_export_all_250709_064325_DCP_csv/`

---

## 🎯 Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Cost Reduction** | 50% | AWS Cost Explorer |
| **Deployment Frequency** | Daily | CodePipeline metrics |
| **Mean Time to Recovery** | < 15 min | CloudWatch alarms |
| **Application Availability** | 99.9% | CloudWatch uptime |
| **Database Performance** | < 100ms latency | RDS Performance Insights |
| **Migration Completion** | 12 months | Project timeline |

---

**Document Version:** 1.0  
**Last Updated:** 2025-12-01  
**Contact:** BGR Migration Team
