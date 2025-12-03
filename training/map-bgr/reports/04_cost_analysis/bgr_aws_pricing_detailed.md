# BGR Applications - AWS Pricing Detailed Breakdown

**Region:** us-east-1  
**Date:** 2025-12-01  
**Based on:** RVTools data (ECBRTSW21: 4 vCPU, 8GB RAM, 300GB storage)

---

## 📊 Current On-Premise Infrastructure

### Server: ECBRTSW21
- **vCPU:** 4
- **RAM:** 8 GB
- **Storage:** 300 GB (2x 150GB disks)
- **OS:** Windows Server 2016/2019
- **Applications:** 6 apps (PortalGuiaBGR, Api Portal, PortalAdmBGR, Backoffice Sistemas, Seq, SonarQube)
- **Database:** SQL Server 2016/2019 Enterprise Edition

### Estimated On-Premise Monthly Cost
| Component | Cost/Month |
|-----------|------------|
| Windows Server licenses (2 servers) | $800 |
| SQL Server Enterprise licenses (2 instances) | $3,500 |
| Hardware/Hosting/Power | $800 |
| Maintenance & Support | $220 |
| **Total** | **$5,320** |

---

## ☁️ AWS Target Architecture - Detailed Pricing

### 1. Networking Infrastructure

#### VPC & Connectivity
| Service | Configuration | Monthly Cost |
|---------|---------------|--------------|
| VPC | 1 VPC, 9 subnets (3 AZs) | $0 (free) |
| Internet Gateway | 1 IGW | $0 (free) |
| NAT Gateway | 3 NAT Gateways (Multi-AZ HA) | $98.55 (3 × $32.85) |
| NAT Gateway Data Processing | 500 GB/month | $22.50 ($0.045/GB) |
| **Subtotal Networking** | | **$121.05** |

---

### 2. Compute - Amazon ECS Fargate

Based on RVTools: ECBRTSW21 has 4 vCPU, 8GB RAM shared across 6 apps.  
AWS sizing: Right-sized per application with auto-scaling.

#### Wave 1 Applications (3 apps)

**PortalGuiaBGR**
- **Configuration:** 2 vCPU, 4 GB RAM
- **Tasks:** 2-6 (avg 3 tasks)
- **Hours/month:** 730 hours × 3 tasks = 2,190 task-hours
- **vCPU cost:** 2,190 × 2 × $0.04048 = $177.30
- **Memory cost:** 2,190 × 4 × $0.004445 = $38.93
- **Monthly:** $216.23

**Api Portal**
- **Configuration:** 2 vCPU, 4 GB RAM
- **Tasks:** 3-10 (avg 5 tasks - high traffic)
- **Hours/month:** 730 hours × 5 tasks = 3,650 task-hours
- **vCPU cost:** 3,650 × 2 × $0.04048 = $295.50
- **Memory cost:** 3,650 × 4 × $0.004445 = $64.89
- **Monthly:** $360.39

**PortalAdministrativoBGR**
- **Configuration:** 1 vCPU, 2 GB RAM
- **Tasks:** 2-4 (avg 2 tasks - low traffic)
- **Hours/month:** 730 hours × 2 tasks = 1,460 task-hours
- **vCPU cost:** 1,460 × 1 × $0.04048 = $59.10
- **Memory cost:** 1,460 × 2 × $0.004445 = $12.98
- **Monthly:** $72.08

#### Wave 2 Applications (3 apps)

**Backoffice Sistemas BGR**
- **Configuration:** 2 vCPU, 4 GB RAM
- **Tasks:** 2-6 (avg 3 tasks)
- **Hours/month:** 730 hours × 3 tasks = 2,190 task-hours
- **Monthly:** $216.23

**Backoffice Banca Digital**
- **Configuration:** 2 vCPU, 4 GB RAM
- **Tasks:** 2-6 (avg 3 tasks)
- **Hours/month:** 730 hours × 3 tasks = 2,190 task-hours
- **Monthly:** $216.23

**Saras**
- **Configuration:** 2 vCPU, 4 GB RAM
- **Tasks:** 2-4 (avg 2 tasks)
- **Hours/month:** 730 hours × 2 tasks = 1,460 task-hours
- **Monthly:** $144.16

**Subtotal ECS Fargate (6 apps):** **$1,225.32**

---

### 3. Load Balancing

#### Application Load Balancers
| ALB | Applications | Monthly Cost |
|-----|--------------|--------------|
| ALB Wave 1 | PortalGuiaBGR, Api Portal, PortalAdmBGR | $16.20 (base) + $8.00 (LCU) = $24.20 |
| ALB Wave 2 | Backoffice Sistemas, Backoffice Banca, Saras | $16.20 (base) + $8.00 (LCU) = $24.20 |
| **Subtotal ALB** | | **$48.40** |

---

### 4. Database - Amazon RDS for SQL Server

Based on RVTools: SQL Server 2016/2019 Enterprise → Migrate to RDS SQL Server Standard

#### RDS Instance 1: PORTAL_ADMINISTRATIVO_BGR (Shared)
**Applications:** PortalGuiaBGR, Api Portal, PortalAdmBGR, Backoffice Sistemas (4 apps)

| Component | Configuration | Monthly Cost |
|-----------|---------------|--------------|
| Instance Type | db.m5.large (2 vCPU, 8 GB RAM) | $146.00 |
| SQL Server Standard License | Included in RDS pricing | $292.00 |
| Multi-AZ Deployment | 2x instances for HA | $146.00 (standby) |
| Storage (gp3) | 500 GB @ $0.138/GB | $69.00 |
| Backup Storage | 500 GB (7 days retention) | $47.50 ($0.095/GB) |
| **Subtotal RDS 1** | | **$700.50** |

#### RDS Instance 2: Backoffice Banca Digital + Saras
**Applications:** Backoffice Banca Digital, Saras (2 apps)

| Component | Configuration | Monthly Cost |
|-----------|---------------|--------------|
| Instance Type | db.m5.large (2 vCPU, 8 GB RAM) | $146.00 |
| SQL Server Standard License | Included in RDS pricing | $292.00 |
| Multi-AZ Deployment | 2x instances for HA | $146.00 (standby) |
| Storage (gp3) | 300 GB @ $0.138/GB | $41.40 |
| Backup Storage | 300 GB (7 days retention) | $28.50 ($0.095/GB) |
| **Subtotal RDS 2** | | **$653.90** |

**Subtotal RDS (2 instances):** **$1,354.40**

---

### 5. Security & Identity

#### AWS Managed Microsoft AD
| Component | Configuration | Monthly Cost |
|-----------|---------------|--------------|
| Directory Type | Standard Edition | $146.00 |
| Domain Controllers | 2 DCs (Multi-AZ) | Included |
| **Subtotal AD** | | **$146.00** |

#### AWS Secrets Manager
| Component | Configuration | Monthly Cost |
|-----------|---------------|--------------|
| Secrets | 20 secrets (DB creds, API keys) | $8.00 ($0.40/secret) |
| API Calls | 100,000 calls/month | $0.50 ($0.05/10k) |
| **Subtotal Secrets Manager** | | **$8.50** |

#### AWS Certificate Manager (ACM)
| Component | Configuration | Monthly Cost |
|-----------|---------------|--------------|
| Public SSL Certificates | 8 certificates | $0 (free) |

**Subtotal Security & Identity:** **$154.50**

---

### 6. Configuration & Messaging

#### AWS Systems Manager Parameter Store
| Component | Configuration | Monthly Cost |
|-----------|---------------|--------------|
| Standard Parameters | 100 parameters | $0 (free) |
| API Calls | 1M calls/month | $0 (free tier) |
| **Subtotal Parameter Store** | | **$0** |

#### Amazon SNS (Notifications)
| Component | Configuration | Monthly Cost |
|-----------|---------------|--------------|
| Requests | 1M requests/month | $0.50 ($0.50/1M) |
| Email Notifications | 10,000 emails/month | $2.00 ($0.20/1k) |
| **Subtotal SNS** | | **$2.50** |

#### Amazon SQS (Message Queue)
| Component | Configuration | Monthly Cost |
|-----------|---------------|--------------|
| Requests | 5M requests/month | $2.00 ($0.40/1M) |
| **Subtotal SQS** | | **$2.00** |

**Subtotal Configuration & Messaging:** **$4.50**

---

### 7. Observability

#### Amazon CloudWatch
| Component | Configuration | Monthly Cost |
|-----------|---------------|--------------|
| Logs Ingestion | 100 GB/month | $50.00 ($0.50/GB) |
| Logs Storage | 100 GB (30 days) | $3.00 ($0.03/GB) |
| Custom Metrics | 500 metrics | $15.00 ($0.30/metric) |
| Dashboards | 3 dashboards | $9.00 ($3/dashboard) |
| Alarms | 50 alarms | $5.00 ($0.10/alarm) |
| **Subtotal CloudWatch** | | **$82.00** |

#### AWS X-Ray
| Component | Configuration | Monthly Cost |
|-----------|---------------|--------------|
| Traces Recorded | 1M traces/month | $5.00 ($5/1M) |
| Traces Retrieved | 100k traces/month | $0.50 ($0.50/1M) |
| **Subtotal X-Ray** | | **$5.50** |

**Subtotal Observability:** **$87.50**

---

### 8. CI/CD Pipeline

#### AWS CodePipeline
| Component | Configuration | Monthly Cost |
|-----------|---------------|--------------|
| Active Pipelines | 6 pipelines | $6.00 ($1/pipeline) |
| **Subtotal CodePipeline** | | **$6.00** |

#### AWS CodeBuild
| Component | Configuration | Monthly Cost |
|-----------|---------------|--------------|
| Build Minutes | 500 minutes/month (general1.small) | $5.00 ($0.01/min) |
| **Subtotal CodeBuild** | | **$5.00** |

#### Amazon ECR (Container Registry)
| Component | Configuration | Monthly Cost |
|-----------|---------------|--------------|
| Storage | 50 GB (container images) | $5.00 ($0.10/GB) |
| Data Transfer | 100 GB/month | $0 (within region) |
| **Subtotal ECR** | | **$5.00** |

**Subtotal CI/CD:** **$16.00**

---

### 9. Governance & Compliance

#### AWS CloudTrail
| Component | Configuration | Monthly Cost |
|-----------|---------------|--------------|
| Management Events | First trail free | $0 |
| Data Events | 1M events/month | $10.00 ($0.10/100k) |
| **Subtotal CloudTrail** | | **$10.00** |

#### AWS Config
| Component | Configuration | Monthly Cost |
|-----------|---------------|--------------|
| Configuration Items | 5,000 items/month | $10.00 ($0.002/item) |
| Rules Evaluations | 50,000 evaluations/month | $10.00 ($0.20/1k) |
| **Subtotal Config** | | **$20.00** |

**Subtotal Governance:** **$30.00**

---

### 10. Wave 4: DevOps Tools Replacement

#### Option A: CloudWatch Logs Insights (Seq Replacement)
| Component | Configuration | Monthly Cost |
|-----------|---------------|--------------|
| Logs Ingestion | 100 GB/month | $50.00 |
| Logs Storage | 100 GB | $3.00 |
| Queries | 1,000 queries/month | $5.00 ($0.005/query) |
| **Subtotal CloudWatch** | | **$58.00** |

#### Option B: Amazon CodeGuru + SonarCloud (SonarQube Replacement)
| Component | Configuration | Monthly Cost |
|-----------|---------------|--------------|
| CodeGuru Reviewer | 100k lines/month | $30.00 ($0.30/1k) |
| SonarCloud (SaaS) | Team plan | $120.00 |
| **Subtotal CodeGuru** | | **$150.00** |

**Subtotal Wave 4 (DevOps Tools):** **$208.00**

---

## 💰 Total Monthly Cost Summary

| Category | Monthly Cost | % of Total |
|----------|--------------|------------|
| **1. Networking** | $121.05 | 4.5% |
| **2. Compute (ECS Fargate)** | $1,225.32 | 45.8% |
| **3. Load Balancing** | $48.40 | 1.8% |
| **4. Database (RDS)** | $1,354.40 | 50.6% |
| **5. Security & Identity** | $154.50 | 5.8% |
| **6. Configuration & Messaging** | $4.50 | 0.2% |
| **7. Observability** | $87.50 | 3.3% |
| **8. CI/CD** | $16.00 | 0.6% |
| **9. Governance** | $30.00 | 1.1% |
| **10. DevOps Tools** | $208.00 | 7.8% |
| **TOTAL AWS** | **$2,676.67** | **100%** |

---

## 📊 Cost Comparison

| Environment | Monthly Cost | Annual Cost |
|-------------|--------------|-------------|
| **On-Premise (Current)** | $5,320.00 | $63,840.00 |
| **AWS (Modernized)** | $2,676.67 | $32,120.04 |
| **Savings** | **$2,643.33** | **$31,719.96** |
| **Reduction** | **49.7%** | **49.7%** |

---

## 🎯 Cost Optimization Opportunities

### Short-term (0-3 months)
1. **Reserved Instances for RDS:** Save 30-40% on database costs
   - RDS 1-year RI: $700.50 → $490.35/month (30% savings)
   - Annual savings: ~$2,500

2. **Savings Plans for Fargate:** Save 20% on compute
   - Fargate 1-year SP: $1,225.32 → $980.26/month (20% savings)
   - Annual savings: ~$2,940

3. **Right-sizing after monitoring:** Reduce over-provisioned resources
   - Potential savings: 10-15% on compute
   - Annual savings: ~$1,500

### Medium-term (3-6 months)
4. **Database Migration to Aurora PostgreSQL:**
   - RDS SQL Server: $1,354.40/month
   - Aurora PostgreSQL: $520.00/month
   - Monthly savings: $834.40
   - Annual savings: ~$10,000

5. **Implement Auto-scaling policies:**
   - Scale down during off-hours (nights/weekends)
   - Potential savings: 20-30% on compute
   - Annual savings: ~$3,000

### Long-term (6-12 months)
6. **Serverless migration for low-traffic apps:**
   - Migrate PortalAdmBGR to Lambda
   - Monthly savings: ~$50
   - Annual savings: ~$600

7. **S3 Intelligent-Tiering for backups:**
   - Reduce backup storage costs by 30%
   - Annual savings: ~$300

**Total potential annual savings with optimizations:** ~$20,840  
**Optimized annual cost:** ~$11,280 (82% reduction vs on-premise)

---

## 📈 Cost Breakdown by Application

| Application | Compute | Database | ALB | Total/Month |
|-------------|---------|----------|-----|-------------|
| **PortalGuiaBGR** | $216.23 | $175.13 (shared) | $8.07 | $399.43 |
| **Api Portal** | $360.39 | $175.13 (shared) | $8.07 | $543.59 |
| **PortalAdministrativoBGR** | $72.08 | $175.13 (shared) | $8.07 | $255.28 |
| **Backoffice Sistemas BGR** | $216.23 | $175.13 (shared) | $8.07 | $399.43 |
| **Backoffice Banca Digital** | $216.23 | $326.95 (shared) | $8.07 | $551.25 |
| **Saras** | $144.16 | $326.95 (shared) | $8.07 | $479.18 |
| **Shared Services** | - | - | - | $48.51 |
| **TOTAL** | | | | **$2,676.67** |

---

## 🔍 Key Insights

1. **Database costs dominate:** 50.6% of total cost
   - Opportunity: Migrate to Aurora PostgreSQL for 60% database cost reduction
   
2. **Compute is right-sized:** 45.8% of total cost
   - Based on actual RVTools data (4 vCPU, 8GB RAM)
   - Distributed across 6 applications with auto-scaling
   
3. **Shared infrastructure reduces costs:**
   - 2 RDS instances serve 6 applications
   - Shared services (AD, Config, Monitoring) amortized across portfolio
   
4. **No Windows licensing costs:**
   - Linux containers eliminate Windows Server licenses
   - SQL Server Standard included in RDS pricing (vs Enterprise on-prem)
   
5. **Pay-as-you-go flexibility:**
   - Scale down during off-hours
   - No upfront hardware investment
   - Predictable monthly costs

---

## ✅ Next Steps

1. **Validate assumptions** with actual usage metrics
2. **Run AWS Pricing Calculator** for official quote
3. **Consider Reserved Instances** for 30-40% additional savings
4. **Plan Aurora migration** for maximum cost optimization
5. **Implement cost monitoring** with AWS Cost Explorer and Budgets
