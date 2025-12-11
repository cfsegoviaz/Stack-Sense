# Calculadora de Costos AWS - VPN Site-to-Site

**Fecha**: 2025-12-04  
**Conectividad**: VPN Site-to-Site (implementación inmediata)

---

## 💰 Resumen Ejecutivo

| Concepto | Costo Mensual | Costo Anual |
|----------|---------------|-------------|
| **Total 4 Aplicaciones (VPN)** | **$3,410/mes** | **$40,920/año** |
| **Con Reserved Instances** | **$3,026/mes** | **$36,312/año** |
| **Ahorro vs Direct Connect** | **+$170/mes** | **+$2,040/año** |
| **Ahorro vs RDS en AWS** | **+$4,100/mes** | **+$49,200/año** |

---

## 1. Saras - Aplicación Empresarial

### Componentes AWS

| Componente | Especificación | Costo Mensual |
|------------|----------------|---------------|
| **EC2 (ASG 2/2/4)** | 2x t3.medium (On-Demand) | $120 |
| **ALB** | Application Load Balancer | $25 |
| **S3** | 50 GB storage + requests | $10 |
| **CodeDeploy + Artifacts** | Deployment | $25 |
| **CloudWatch** | Logs + Metrics + Alarms | $20 |
| **Secrets Manager** | 3 secrets | $1.20 |
| **Data Transfer** | Out to internet | $10 |
| **VPN (compartido)** | 25% del costo total | $18 |
| **Data Transfer VPN** | 25% del costo total | $10 |
| **SUBTOTAL** | | **$249/mes** |

### Con Reserved Instances (1 año)
- EC2: $120 → $80/mes (-33%)
- **Total con RI**: **$209/mes**

### Comparativa
- ❌ Con RDS + Direct Connect: $296/mes
- ✅ Con VPN: $249/mes
- **Ahorro**: $47/mes

---

## 2. SonarQube - Herramienta DevOps

### Componentes AWS

| Componente | Especificación | Costo Mensual |
|------------|----------------|---------------|
| **EC2 (ASG 2/2/4)** | 2x t3.large (On-Demand) | $300 |
| **ALB** | Application Load Balancer | $25 |
| **EFS** | 100 GB shared storage | $30 |
| **S3** | 100 GB storage + requests | $15 |
| **CodeDeploy + Artifacts** | Deployment | $25 |
| **CloudWatch** | Logs + Metrics + Alarms | $20 |
| **Secrets Manager** | 3 secrets | $1.20 |
| **Data Transfer** | Out to internet | $10 |
| **VPN (compartido)** | 25% del costo total | $18 |
| **Data Transfer VPN** | 25% del costo total | $15 |
| **SUBTOTAL** | | **$469/mes** |

### Con Reserved Instances (1 año)
- EC2: $300 → $200/mes (-33%)
- **Total con RI**: **$369/mes**

### Comparativa
- ❌ Con RDS + Direct Connect: $511/mes
- ✅ Con VPN: $469/mes
- **Ahorro**: $42/mes

---

## 3. API Portal - Alta Criticidad

### Componentes AWS

| Componente | Especificación | Costo Mensual |
|------------|----------------|---------------|
| **EC2 (ASG 2/3/8)** | 3x t3.medium (On-Demand) | $180 |
| **ALB** | Application Load Balancer | $25 |
| **ElastiCache** | Redis cache.t3.medium | $150 |
| **CloudFront** | CDN 1 TB/mes | $200 |
| **API Gateway** | 5M requests/mes | $100 |
| **WAF** | Web Application Firewall | $50 |
| **S3** | 100 GB storage + requests | $15 |
| **CodeDeploy + Artifacts** | Deployment | $30 |
| **CloudWatch + X-Ray** | Monitoring + Tracing | $30 |
| **Secrets Manager** | 5 secrets | $2 |
| **Data Transfer** | Out to internet | $30 |
| **VPN (compartido)** | 25% del costo total | $18 |
| **Data Transfer VPN** | 25% del costo total | $20 |
| **SUBTOTAL** | | **$1,345/mes** |

### Con Reserved Instances (1 año)
- EC2: $180 → $120/mes (-33%)
- ElastiCache: $150 → $100/mes (-33%)
- **Total con RI**: **$1,215/mes**

### Comparativa
- ❌ Con RDS + Direct Connect: $1,387/mes
- ✅ Con VPN: $1,345/mes
- **Ahorro**: $42/mes

---

## 4. Portal Guía BGR - Alta Criticidad

### Componentes AWS

| Componente | Especificación | Costo Mensual |
|------------|----------------|---------------|
| **EC2 (ASG 2/3/8)** | 3x t3.medium (On-Demand) | $180 |
| **ALB** | Application Load Balancer | $25 |
| **ElastiCache** | Redis Multi-AZ | $200 |
| **CloudFront** | CDN 1 TB/mes | $250 |
| **WAF** | Web Application Firewall | $50 |
| **S3** | 150 GB storage + requests | $20 |
| **CodeDeploy + Artifacts** | Deployment | $30 |
| **CloudWatch** | Monitoring | $25 |
| **Secrets Manager** | 5 secrets | $2 |
| **Data Transfer** | Out to internet | $35 |
| **VPN (compartido)** | 25% del costo total | $19 |
| **Data Transfer VPN** | 25% del costo total | $20 |
| **SUBTOTAL** | | **$1,347/mes** |

### Con Reserved Instances (1 año)
- EC2: $180 → $120/mes (-33%)
- ElastiCache: $200 → $133/mes (-33%)
- **Total con RI**: **$1,233/mes**

### Comparativa
- ❌ Con RDS + Direct Connect: $1,386/mes
- ✅ Con VPN: $1,347/mes
- **Ahorro**: $39/mes

---

## 📊 Conectividad VPN Site-to-Site (Compartida)

### Costos VPN

| Componente | Especificación | Costo Mensual |
|------------|----------------|---------------|
| **VPN Connection** | 2 túneles IPSec | $73 |
| **Data Transfer Out** | $0.09/GB (estimado 500 GB/mes) | $45 |
| **Data Transfer In** | Gratis | $0 |
| **SUBTOTAL VPN** | | **$118/mes** |

### Distribución por Aplicación (25% cada una)

| Aplicación | VPN Base | Data Transfer | Total |
|------------|----------|---------------|-------|
| Saras | $18 | $10 | $28 |
| SonarQube | $18 | $15 | $33 |
| API Portal | $18 | $20 | $38 |
| Portal Guía | $19 | $20 | $39 |
| **TOTAL** | **$73** | **$65** | **$138/mes** |

---

## 📊 Resumen Consolidado

### Costos Mensuales (On-Demand)

| Aplicación | Compute | Networking | Storage | VPN | Total |
|------------|---------|------------|---------|-----|-------|
| **Saras** | $120 | $35 | $10 | $28 | **$249** |
| **SonarQube** | $300 | $35 | $45 | $33 | **$469** |
| **API Portal** | $180 | $405 | $45 | $38 | **$1,345** |
| **Portal Guía** | $180 | $380 | $45 | $39 | **$1,347** |
| **TOTAL** | **$780** | **$855** | **$145** | **$138** | **$3,410** |

### Costos Mensuales (Reserved Instances)

| Aplicación | Ahorro RI | Total con RI |
|------------|-----------|--------------|
| **Saras** | -$40 | **$209** |
| **SonarQube** | -$100 | **$369** |
| **API Portal** | -$130 | **$1,215** |
| **Portal Guía** | -$114 | **$1,233** |
| **TOTAL** | **-$384** | **$3,026** |

### Proyección Anual

| Escenario | Mensual | Anual |
|-----------|---------|-------|
| **VPN On-Demand** | $3,410 | $40,920 |
| **VPN + RI (1 año)** | $3,026 | $36,312 |
| **VPN + RI (3 años)** | $2,480 | $29,760 |

---

## 💡 Comparativa: Direct Connect vs VPN

### Costos de Conectividad

| Concepto | Direct Connect | VPN Site-to-Site | Diferencia |
|----------|----------------|------------------|------------|
| **Setup** | $0 | $0 | $0 |
| **Port Fee** | $228/mes | $0 | -$228 |
| **VPN Connection** | $0 | $73/mes | +$73 |
| **Data Transfer** | $100/mes | $65/mes | -$35 |
| **TOTAL** | **$328/mes** | **$138/mes** | **-$190/mes** |
| **Lead Time** | 2-4 semanas | 1-3 días | **Inmediato** |

### Ahorro Anual VPN vs Direct Connect
- **Mensual**: $190/mes
- **Anual**: $2,280/año

---

## 💡 Comparativa: RDS vs On-Premise

### Costos Totales por Escenario

| Escenario | Mensual | Anual | vs RDS AWS |
|-----------|---------|-------|------------|
| **RDS en AWS** | $7,510 | $90,120 | Baseline |
| **On-Premise + Direct Connect** | $3,580 | $42,960 | -$47,160 |
| **On-Premise + VPN** | $3,410 | $40,920 | **-$49,200** |

### Ahorro Total con VPN
- **vs RDS en AWS**: $4,100/mes ($49,200/año)
- **vs Direct Connect**: $170/mes ($2,040/año)

---

## 🎯 Recomendaciones

### Implementación Inmediata (VPN)
✅ Lead time: 1-3 días  
✅ Costo: $138/mes (compartido)  
✅ Latencia: 20-50ms (aceptable)  
✅ Ancho banda: 1.25 Gbps/túnel  
✅ Sin compromiso de largo plazo  

### Optimizaciones Requeridas
1. **Connection Pooling** (obligatorio)
2. **ElastiCache** agresivo (80% hit rate)
3. **Query Optimization** (reducir round-trips)
4. **Async Operations** (background jobs)

### Upgrade a Direct Connect (Opcional)
**Evaluar después de 2-3 meses SI:**
- Latencia promedio > 40ms
- Utilización VPN > 70%
- Quejas de performance
- Queries críticas > 500ms

**Costo adicional**: +$190/mes

---

## ⚠️ Consideraciones de Performance

### Latencia Esperada con VPN
- **VPN**: 20-50ms
- **Query simple**: < 100ms total
- **Query compleja**: 200-500ms
- **Transacción**: 300-800ms

### Mitigaciones
✅ Connection pooling (Min: 10, Max: 100)  
✅ ElastiCache Redis (session + queries)  
✅ Query optimization (batch operations)  
✅ Async processing (background jobs)  
✅ Monitoring continuo (CloudWatch)  

---

## 📋 Timeline de Implementación

| Fase | Duración | Costo |
|------|----------|-------|
| **Setup VPN** | 1-3 días | $0 |
| **Migración Piloto** | 3 semanas | $3,410/mes |
| **Migración Producción** | 4 semanas | $3,410/mes |
| **Optimización** | Continuo | $3,026/mes (con RI) |

**Total**: 8 semanas vs 10-12 semanas con Direct Connect

---

**Última actualización**: 2025-12-04  
**Estado**: Calculadora VPN Site-to-Site  
**Decisión**: Implementación inmediata sin Direct Connect
