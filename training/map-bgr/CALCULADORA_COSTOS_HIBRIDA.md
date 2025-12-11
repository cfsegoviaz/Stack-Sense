# Calculadora de Costos AWS - Arquitectura Híbrida BGR

**Fecha**: 2025-12-04  
**Modelo**: Bases de Datos On-Premise + Compute en AWS

---

## 💰 Resumen Ejecutivo

| Concepto | Costo Mensual | Costo Anual |
|----------|---------------|-------------|
| **Total 4 Aplicaciones** | **$3,580/mes** | **$42,960/año** |
| **Con Reserved Instances** | **$2,650/mes** | **$31,800/año** |
| **Ahorro vs RDS en AWS** | **+$1,680/mes** | **+$20,160/año** |

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
| **Data Transfer** | Out to internet | $20 |
| **Direct Connect (compartido)** | 25% del costo total | $57 |
| **VPN Backup (compartido)** | 25% del costo total | $18 |
| **SUBTOTAL** | | **$296/mes** |

### Con Reserved Instances (1 año)
- EC2: $120 → $80/mes (-33%)
- **Total con RI**: **$256/mes**

### Comparativa
- ❌ Antes (con RDS): $625/mes
- ✅ Ahora (BD on-premise): $296/mes
- **Ahorro**: $329/mes

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
| **Data Transfer** | Out to internet | $20 |
| **Direct Connect (compartido)** | 25% del costo total | $57 |
| **VPN Backup (compartido)** | 25% del costo total | $18 |
| **SUBTOTAL** | | **$511/mes** |

### Con Reserved Instances (1 año)
- EC2: $300 → $200/mes (-33%)
- **Total con RI**: **$411/mes**

### Comparativa
- ❌ Antes (con RDS): $1,225/mes
- ✅ Ahora (BD on-premise): $511/mes
- **Ahorro**: $714/mes

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
| **Data Transfer** | Out to internet | $50 |
| **Direct Connect (compartido)** | 25% del costo total | $57 |
| **VPN Backup (compartido)** | 25% del costo total | $18 |
| **SUBTOTAL** | | **$1,387/mes** |

### Con Reserved Instances (1 año)
- EC2: $180 → $120/mes (-33%)
- ElastiCache: $150 → $100/mes (-33%)
- **Total con RI**: **$1,257/mes**

### Comparativa
- ❌ Antes (con RDS): $2,830/mes
- ✅ Ahora (BD on-premise): $1,387/mes
- **Ahorro**: $1,443/mes

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
| **Shield Advanced** | DDoS Protection (opcional) | $0 |
| **S3** | 150 GB storage + requests | $20 |
| **CodeDeploy + Artifacts** | Deployment | $30 |
| **CloudWatch** | Monitoring | $25 |
| **Secrets Manager** | 5 secrets | $2 |
| **Data Transfer** | Out to internet | $75 |
| **Direct Connect (compartido)** | 25% del costo total | $57 |
| **VPN Backup (compartido)** | 25% del costo total | $18 |
| **SUBTOTAL** | | **$1,386/mes** |

### Con Reserved Instances (1 año)
- EC2: $180 → $120/mes (-33%)
- ElastiCache: $200 → $133/mes (-33%)
- **Total con RI**: **$1,272/mes**

### Comparativa
- ❌ Antes (con RDS): $2,830/mes
- ✅ Ahora (BD on-premise): $1,386/mes
- **Ahorro**: $1,444/mes

---

## 📊 Conectividad Híbrida (Compartida)

### Direct Connect

| Componente | Especificación | Costo Mensual |
|------------|----------------|---------------|
| **Port Fee** | 1 Gbps Dedicated | $228 |
| **Data Transfer Out** | $0.02/GB (estimado 5 TB/mes) | $100 |
| **SUBTOTAL Direct Connect** | | **$328/mes** |

### VPN Site-to-Site (Backup)

| Componente | Especificación | Costo Mensual |
|------------|----------------|---------------|
| **VPN Connection** | 2 túneles IPSec | $73 |
| **SUBTOTAL VPN** | | **$73/mes** |

### Total Conectividad Híbrida
- **Direct Connect**: $228/mes
- **VPN Backup**: $73/mes
- **Data Transfer**: $100/mes
- **Total**: **$401/mes**

**Distribución por aplicación** (25% cada una):
- Saras: $100/mes
- SonarQube: $100/mes
- API Portal: $100/mes
- Portal Guía: $101/mes

---

## 📊 Resumen Consolidado

### Costos Mensuales (On-Demand)

| Aplicación | Compute | Networking | Storage | Híbrido | Total |
|------------|---------|------------|---------|---------|-------|
| **Saras** | $120 | $45 | $10 | $75 | **$296** |
| **SonarQube** | $300 | $45 | $45 | $75 | **$511** |
| **API Portal** | $180 | $425 | $45 | $75 | **$1,387** |
| **Portal Guía** | $180 | $400 | $45 | $76 | **$1,386** |
| **TOTAL** | **$780** | **$915** | **$145** | **$301** | **$3,580** |

### Costos Mensuales (Reserved Instances)

| Aplicación | Ahorro RI | Total con RI |
|------------|-----------|--------------|
| **Saras** | -$40 | **$256** |
| **SonarQube** | -$100 | **$411** |
| **API Portal** | -$130 | **$1,257** |
| **Portal Guía** | -$114 | **$1,272** |
| **TOTAL** | **-$384** | **$3,196** |

### Proyección Anual

| Escenario | Mensual | Anual |
|-----------|---------|-------|
| **On-Demand** | $3,580 | $42,960 |
| **Reserved Instances (1 año)** | $3,196 | $38,352 |
| **Reserved Instances (3 años)** | $2,650 | $31,800 |

---

## 💡 Comparativa: RDS vs On-Premise

### Costos Eliminados (RDS)

| Aplicación | RDS Eliminado | Ahorro |
|------------|---------------|--------|
| Saras | SQL Server t3.medium Multi-AZ | -$180/mes |
| SonarQube | PostgreSQL t3.large Multi-AZ | -$350/mes |
| API Portal | SQL Server t3.large Multi-AZ | -$700/mes |
| Portal Guía | SQL Server t3.xlarge + Replica | -$900/mes |
| **TOTAL AHORRADO** | | **-$2,130/mes** |

### Costos Agregados (Híbrido)

| Componente | Costo |
|------------|-------|
| Direct Connect 1 Gbps | +$228/mes |
| VPN Site-to-Site | +$73/mes |
| Data Transfer | +$100/mes |
| **TOTAL AGREGADO** | **+$401/mes** |

### Balance Neto

```
Ahorro RDS:        -$2,130/mes
Costo Híbrido:     +$401/mes
─────────────────────────────
Balance Neto:      -$1,729/mes de ahorro
```

**Ahorro Anual**: **$20,748/año**

---

## 🎯 Recomendaciones de Optimización

### Corto Plazo (Mes 1-3)

1. **Reserved Instances (1 año)**
   - Ahorro: $384/mes
   - ROI inmediato

2. **Auto Scaling Optimizado**
   - Scheduled scaling en horarios no laborales
   - Ahorro estimado: $200-300/mes

3. **CloudFront Optimization**
   - Compression habilitado
   - Cache policies optimizadas
   - Ahorro: $50-100/mes

### Medio Plazo (Mes 6-12)

4. **Reserved Instances (3 años)**
   - Ahorro adicional: $546/mes vs 1 año
   - Total: $2,650/mes

5. **Direct Connect 10 Gbps**
   - Si el tráfico crece
   - Mejor costo por GB

6. **ElastiCache Optimization**
   - Ajustar tamaño según uso real
   - Ahorro potencial: $100/mes

### Largo Plazo (Año 2+)

7. **Evaluar Migración BD a AWS**
   - Si dependencias on-premise se resuelven
   - Aurora PostgreSQL/MySQL
   - Eliminar costos de conectividad híbrida

8. **Containerización (ECS/EKS)**
   - Mejor utilización de recursos
   - Ahorro: 30-40%

---

## ⚠️ Consideraciones Importantes

### Latencia
- **Direct Connect**: < 10ms (excelente)
- **VPN**: 20-50ms (aceptable)
- **Crítico para**: Queries frecuentes a BD

### Ancho de Banda
- **1 Gbps**: Suficiente para 4 aplicaciones
- **Monitorear**: Utilización > 70% → upgrade a 10 Gbps

### Alta Disponibilidad
- Direct Connect como primario
- VPN como backup automático
- Failover < 1 minuto

### Seguridad
- Tráfico encriptado (IPSec/MACsec)
- Security Groups restrictivos
- VPC Flow Logs habilitados
- Secrets Manager para credenciales

---

## 📋 Próximos Pasos

1. ✅ Arquitectura híbrida definida
2. ⏳ Solicitar Direct Connect (lead time: 2-4 semanas)
3. ⏳ Configurar VPN Site-to-Site (backup)
4. ⏳ Provisionar infraestructura AWS
5. ⏳ Probar conectividad y latencia
6. ⏳ Migrar aplicaciones piloto (Saras, SonarQube)
7. ⏳ Validar performance con BD on-premise
8. ⏳ Migrar aplicaciones críticas (API Portal, Portal Guía)

---

**Última actualización**: 2025-12-04  
**Estado**: Calculadora actualizada - Arquitectura Híbrida
