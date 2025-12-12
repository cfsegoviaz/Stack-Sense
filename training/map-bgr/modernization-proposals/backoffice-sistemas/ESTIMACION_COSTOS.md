# Estimación de Costos - Backoffice Sistemas BGR

**Aplicación**: Backoffice Sistemas BGR  
**Modelo**: Arquitectura Híbrida (Compute en AWS + BD On-Premise)  
**Región**: us-east-1 (N. Virginia)  
**Fecha**: 2025-12-12

---

## 💰 Resumen Ejecutivo de Costos

| Categoría | Costo Mensual |
|-----------|---------------|
| **Compute (EC2)** | $146.00 |
| **Networking** | $289.00 |
| **Storage** | $40.00 |
| **Monitoring** | $3.50 |
| **CI/CD** | $20.00 |
| **Subtotal** | **$498.50** |
| **Contingencia (10%)** | $49.85 |
| **TOTAL MENSUAL** | **$548.35** |
| **TOTAL ANUAL** | **$6,580.20** |

---

## 📊 Desglose Detallado de Costos

### 1. Compute (EC2 Instances)

#### Instancias de Aplicación

| Componente | Especificación | Cantidad | Costo/hora | Horas/mes | Subtotal |
|------------|----------------|----------|------------|-----------|----------|
| EC2 t3.xlarge | 4 vCPU, 16 GB RAM | 2 | $0.1664 | 730 | $243.00 |
| Windows Server License | Included in EC2 | 2 | - | - | Incluido |
| **Total Compute** | | | | | **$243.00** |

**Nota**: Precio con descuento por Reserved Instances (1 año, pago parcial):
- On-Demand: $0.1664/hora
- Reserved (1 año): $0.10/hora → **$146.00/mes** (ahorro 40%)

**Recomendación**: Comprar Reserved Instances después de 3 meses de operación estable.

---

### 2. Networking

#### Conectividad Híbrida

| Componente | Especificación | Costo/mes |
|------------|----------------|-----------|
| **Direct Connect** | 1 Gbps port | $228.00 |
| Data Transfer Out | 100 GB @ $0.02/GB | $2.00 |
| **VPN Site-to-Site (Backup)** | 2 túneles IPSec | $73.00 |
| VPN Data Transfer | Incluido | $0.00 |
| **Total Conectividad Híbrida** | | **$303.00** |

#### Load Balancer

| Componente | Especificación | Costo/mes |
|------------|----------------|-----------|
| Application Load Balancer | 730 horas | $22.63 |
| LCU (Load Balancer Capacity Units) | 10 LCU promedio | $7.30 |
| **Total Load Balancer** | | **$29.93** |

#### NAT Gateway

| Componente | Especificación | Costo/mes |
|------------|----------------|-----------|
| NAT Gateway | 2 (HA en 2 AZs) | $65.70 |
| Data Processing | 50 GB @ $0.045/GB | $2.25 |
| **Total NAT Gateway** | | **$67.95** |

#### Data Transfer

| Componente | Especificación | Costo/mes |
|------------|----------------|-----------|
| Internet Data Transfer Out | 50 GB @ $0.09/GB | $4.50 |
| Inter-AZ Data Transfer | 20 GB @ $0.01/GB | $0.20 |
| **Total Data Transfer** | | **$4.70** |

**Total Networking**: **$405.58**

**Optimización Recomendada**:
- Usar 1 NAT Gateway en lugar de 2 (ahorro $32.85/mes)
- Total Networking Optimizado: **$372.73**

---

### 3. Storage

#### EBS Volumes

| Componente | Especificación | Cantidad | Costo/GB | Subtotal |
|------------|----------------|----------|----------|----------|
| EBS gp3 | 200 GB | 2 | $0.08/GB | $32.00 |
| EBS Snapshots | 100 GB | 1 | $0.05/GB | $5.00 |
| **Total EBS** | | | | **$37.00** |

#### S3 Buckets

| Componente | Especificación | Storage | Costo/GB | Subtotal |
|------------|----------------|---------|----------|----------|
| S3 Standard (Artifacts) | Versionado | 10 GB | $0.023/GB | $0.23 |
| S3 Standard (Backups) | Lifecycle 90 días | 50 GB | $0.023/GB | $1.15 |
| S3 Standard (Logs) | Lifecycle 30 días | 5 GB | $0.023/GB | $0.12 |
| S3 Requests | PUT/GET | 10,000 | $0.005/1K | $0.05 |
| **Total S3** | | | | **$1.55** |

**Total Storage**: **$38.55**

---

### 4. Monitoring & Management

| Componente | Especificación | Costo/mes |
|------------|----------------|-----------|
| CloudWatch Logs | 5 GB ingestion | $2.50 |
| CloudWatch Metrics | Custom metrics | $0.30 |
| CloudWatch Alarms | 10 alarms | $1.00 |
| CloudWatch Dashboards | 2 dashboards | $6.00 |
| SNS | 1,000 notifications | $0.50 |
| Systems Manager | Session Manager | $0.00 |
| **Total Monitoring** | | **$10.30** |

**Optimización Recomendada**:
- Usar 1 dashboard en lugar de 2 (ahorro $3.00/mes)
- Reducir retención de logs a 7 días (ahorro $1.50/mes)
- Total Monitoring Optimizado: **$5.80**

---

### 5. CI/CD (Azure DevOps + AWS CodeDeploy)

| Componente | Especificación | Costo/mes |
|------------|----------------|-----------|
| AWS CodeDeploy | EC2 deployments | $0.00 |
| S3 Artifacts Storage | 10 GB | $0.23 |
| S3 Requests | 1,000 requests | $0.01 |
| CloudWatch Logs (Deploy) | 1 GB | $0.50 |
| Data Transfer (Artifacts) | 10 GB | $0.90 |
| **Total CI/CD** | | **$1.64** |

**Nota**: Azure DevOps tiene costo separado (no incluido en AWS).

---

## 📈 Comparativa de Costos: On-Premise vs AWS

### Costos On-Premise (Estimados)

| Componente | Costo Mensual |
|------------|---------------|
| Servidores físicos (amortización) | $200.00 |
| Licencias Windows Server | $100.00 |
| Licencias SQL Server | $0.00 (compartida) |
| Electricidad | $50.00 |
| Refrigeración | $30.00 |
| Mantenimiento hardware | $80.00 |
| Personal IT (parcial) | $300.00 |
| **Total On-Premise** | **$760.00** |

### Costos AWS (Optimizados)

| Componente | Costo Mensual |
|------------|---------------|
| Compute (Reserved) | $146.00 |
| Networking | $289.00 |
| Storage | $38.55 |
| Monitoring | $5.80 |
| CI/CD | $1.64 |
| **Total AWS** | **$480.99** |

### Ahorro Mensual

```
Costo On-Premise: $760.00
Costo AWS:        $480.99
Ahorro:           $279.01 (37% de reducción)
```

### Ahorro Anual

```
Ahorro mensual: $279.01
Ahorro anual:   $3,348.12
```

---

## 💡 Optimizaciones de Costos Recomendadas

### Corto Plazo (0-3 meses)

1. **Usar 1 NAT Gateway en lugar de 2**
   - Ahorro: $32.85/mes
   - Riesgo: Pérdida de redundancia en 1 AZ
   - Recomendación: Implementar después de 1 mes de operación estable

2. **Reducir retención de logs a 7 días**
   - Ahorro: $1.50/mes
   - Riesgo: Pérdida de logs históricos
   - Recomendación: Exportar logs a S3 para archivo

3. **Usar 1 CloudWatch Dashboard**
   - Ahorro: $3.00/mes
   - Riesgo: Menos visibilidad
   - Recomendación: Consolidar métricas en 1 dashboard

**Total Ahorro Corto Plazo**: $37.35/mes

### Mediano Plazo (3-6 meses)

4. **Comprar Reserved Instances (1 año)**
   - Ahorro: $97.00/mes (40% descuento)
   - Inversión inicial: $1,051.20 (pago parcial)
   - ROI: 11 meses

5. **Implementar Auto Scaling**
   - Ahorro: $50-100/mes (reducir instancias en horas valle)
   - Requiere: Configuración de Auto Scaling Groups
   - Recomendación: Implementar después de análisis de patrones de uso

6. **Optimizar Data Transfer**
   - Ahorro: $10-20/mes
   - Implementar: Caching, compresión, CDN
   - Recomendación: Analizar patrones de tráfico

**Total Ahorro Mediano Plazo**: $157-217/mes

### Largo Plazo (6-12 meses)

7. **Migrar a .NET Core y Linux**
   - Ahorro: $100-150/mes (licencias Windows)
   - Requiere: Refactoring de aplicación
   - Timeline: 6-9 meses
   - Recomendación: Evaluar en roadmap de modernización

8. **Implementar Serverless (Lambda + API Gateway)**
   - Ahorro: $200-300/mes (eliminar EC2)
   - Requiere: Refactoring completo
   - Timeline: 9-12 meses
   - Recomendación: Evaluar para aplicaciones nuevas

9. **Migrar Base de Datos a AWS**
   - Ahorro: $100-200/mes (eliminar Direct Connect)
   - Requiere: Coordinación con otras aplicaciones
   - Timeline: 12+ meses
   - Recomendación: Proyecto separado

**Total Ahorro Largo Plazo**: $400-650/mes

---

## 📊 Proyección de Costos a 3 Años

### Año 1

| Mes | Costo | Optimizaciones | Costo Optimizado |
|-----|-------|----------------|------------------|
| 1-3 | $548.35 | Ninguna | $548.35 |
| 4-6 | $548.35 | Corto plazo | $511.00 |
| 7-12 | $548.35 | Reserved + Mediano | $354.00 |
| **Total Año 1** | **$6,580.20** | | **$5,196.00** |

### Año 2

| Trimestre | Costo Base | Optimizaciones | Costo Optimizado |
|-----------|------------|----------------|------------------|
| Q1-Q2 | $354.00/mes | Mediano plazo | $354.00/mes |
| Q3-Q4 | $354.00/mes | Largo plazo | $250.00/mes |
| **Total Año 2** | **$4,248.00** | | **$3,624.00** |

### Año 3

| Trimestre | Costo Base | Optimizaciones | Costo Optimizado |
|-----------|------------|----------------|------------------|
| Q1-Q4 | $250.00/mes | Serverless | $150.00/mes |
| **Total Año 3** | **$3,000.00** | | **$1,800.00** |

### Total 3 Años

```
Sin optimizaciones: $13,828.20
Con optimizaciones: $10,620.00
Ahorro total:       $3,208.20 (23%)
```

---

## 🎯 Recomendaciones Finales

### Implementar Inmediatamente

1. ✅ **Comprar Reserved Instances** después de 3 meses
   - Ahorro: $97/mes
   - ROI: 11 meses

2. ✅ **Reducir a 1 NAT Gateway** después de 1 mes
   - Ahorro: $32.85/mes
   - Riesgo: Bajo

3. ✅ **Optimizar retención de logs**
   - Ahorro: $1.50/mes
   - Riesgo: Ninguno

### Evaluar en 6 Meses

4. ⏳ **Implementar Auto Scaling**
   - Ahorro potencial: $50-100/mes
   - Requiere: Análisis de patrones

5. ⏳ **Optimizar Data Transfer**
   - Ahorro potencial: $10-20/mes
   - Requiere: Análisis de tráfico

### Roadmap de Modernización (12+ meses)

6. 🔮 **Migrar a .NET Core + Linux**
   - Ahorro: $100-150/mes
   - Timeline: 6-9 meses

7. 🔮 **Evaluar Serverless**
   - Ahorro: $200-300/mes
   - Timeline: 9-12 meses

8. 🔮 **Migrar Base de Datos a AWS**
   - Ahorro: $100-200/mes
   - Timeline: 12+ meses

---

## 📋 Resumen de Costos Mensuales

### Configuración Inicial (Mes 1-3)

| Categoría | Costo |
|-----------|-------|
| Compute (On-Demand) | $243.00 |
| Networking | $405.58 |
| Storage | $38.55 |
| Monitoring | $10.30 |
| CI/CD | $1.64 |
| **Subtotal** | **$699.07** |
| Contingencia (10%) | $69.91 |
| **TOTAL** | **$768.98** |

### Configuración Optimizada (Mes 4+)

| Categoría | Costo |
|-----------|-------|
| Compute (Reserved) | $146.00 |
| Networking (1 NAT) | $372.73 |
| Storage | $38.55 |
| Monitoring (Optimizado) | $5.80 |
| CI/CD | $1.64 |
| **Subtotal** | **$564.72** |
| Contingencia (10%) | $56.47 |
| **TOTAL** | **$621.19** |

### Configuración Target (Mes 12+)

| Categoría | Costo |
|-----------|-------|
| Compute (Reserved + Auto Scaling) | $100.00 |
| Networking | $372.73 |
| Storage | $38.55 |
| Monitoring | $5.80 |
| CI/CD | $1.64 |
| **Subtotal** | **$518.72** |
| Contingencia (10%) | $51.87 |
| **TOTAL** | **$570.59** |

---

**Última actualización**: 2025-12-12  
**Versión**: 1.0  
**Notas**: 
- Precios basados en AWS us-east-1
- No incluye costos de Azure DevOps
- No incluye costos de base de datos on-premise
- Incluye contingencia del 10%
