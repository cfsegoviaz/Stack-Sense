# Resumen Ejecutivo - Estimación de Costos AWS

**Proyecto**: MAP-BGR  
**Fecha**: 2025-12-01  
**Región**: us-east-1  
**VMs Analizadas**: 383 (350 encendidas)

---

## 💰 Resumen Ejecutivo de Costos

### Costos Mensuales

| Concepto | On-Demand | Reserved Instances (1yr) | Ahorro |
|----------|-----------|--------------------------|--------|
| **Compute + Storage** | **$127,958** | **$76,775** | **$51,183 (40%)** |

### Costos Anuales

| Concepto | On-Demand | Reserved Instances (1yr) | Ahorro |
|----------|-----------|--------------------------|--------|
| **Total Anual** | **$1,535,496** | **$921,303** | **$614,193 (40%)** |

---

## 📊 Desglose de Recursos

### Inventario Total

| Métrica | Valor |
|---------|-------|
| Total VMs | 383 |
| VMs Encendidas | 350 (91.4%) |
| VMs Apagadas | 33 (8.6%) |
| Total vCPUs | 1,752 |
| Total RAM | 5,925 GB |
| Total Storage (EBS) | 60,984 GB (~60 TB) |

### Distribución por Tipo de Instancia (Top 10)

| Tipo Instancia | Cantidad | vCPUs | RAM (GB) | Costo Mensual |
|----------------|----------|-------|----------|---------------|
| t3.xlarge | 97 VMs | 4 | 16 | ~$16,000 |
| c5.large | 37 VMs | 2 | 4 | ~$3,100 |
| t3.large | 34 VMs | 2 | 8 | ~$2,800 |
| t3.medium | 27 VMs | 2 | 4 | ~$1,100 |
| c5.xlarge | 26 VMs | 4 | 8 | ~$4,400 |
| m5.xlarge | 24 VMs | 4 | 16 | ~$4,600 |
| r5.large | 22 VMs | 2 | 16 | ~$2,800 |
| t3.2xlarge | 19 VMs | 8 | 32 | ~$6,300 |
| m5.2xlarge | 17 VMs | 8 | 32 | ~$6,500 |
| r5.xlarge | 15 VMs | 4 | 32 | ~$3,800 |

---

## 💡 Estrategias de Optimización

### 1. Reserved Instances (Recomendado)

**Ahorro**: 40% sobre On-Demand  
**Compromiso**: 1 año  
**Costo mensual**: $76,775  
**Ahorro anual**: $614,193

**Recomendación**: Comprar RIs para instancias estables (80% del inventario)

### 2. Savings Plans

**Ahorro**: 30-40% sobre On-Demand  
**Flexibilidad**: Mayor que RIs  
**Compromiso**: 1 o 3 años

**Recomendación**: Combinar con RIs para máxima flexibilidad

### 3. Rightsizing

**Oportunidades identificadas**:
- 33 VMs apagadas → Eliminar o convertir a snapshots
- VMs sobredimensionadas → Reducir tamaño (estimado 10-15% ahorro adicional)

**Ahorro estimado**: $10,000 - $15,000/mes adicionales

### 4. Auto Scaling

**Aplicaciones candidatas**:
- Portales web (3 aplicaciones)
- APIs (1 aplicación)

**Ahorro estimado**: 20-30% en horas no pico

### 5. Spot Instances

**Candidatos**:
- Ambientes de desarrollo
- Cargas batch
- Procesamiento no crítico

**Ahorro**: Hasta 90% vs On-Demand

---

## 📈 Proyección de Costos por Fase

### Ola 0 - Piloto (3 aplicaciones, 12 VMs)

| Concepto | On-Demand | Reserved | Optimizado |
|----------|-----------|----------|------------|
| Mensual | $4,000 | $2,400 | $2,100 |
| Anual | $48,000 | $28,800 | $25,200 |

**Aplicaciones**: SonarQube, Saras, Seq (CloudWatch)

### Ola 1 - Backoffice (2 aplicaciones, 8 VMs)

| Concepto | On-Demand | Reserved | Optimizado |
|----------|-----------|----------|------------|
| Mensual | $3,500 | $2,100 | $1,900 |
| Anual | $42,000 | $25,200 | $22,800 |

### Ola 2 - Portales (2 aplicaciones, 10 VMs)

| Concepto | On-Demand | Reserved | Optimizado |
|----------|-----------|----------|------------|
| Mensual | $6,000 | $3,600 | $3,200 |
| Anual | $72,000 | $43,200 | $38,400 |

### Ola 3 - Portal Crítico (1 aplicación, 6 VMs)

| Concepto | On-Demand | Reserved | Optimizado |
|----------|-----------|----------|------------|
| Mensual | $4,500 | $2,700 | $2,400 |
| Anual | $54,000 | $32,400 | $28,800 |

### Total 8 Aplicaciones Mapeadas (36 VMs)

| Concepto | On-Demand | Reserved | Optimizado |
|----------|-----------|----------|------------|
| Mensual | $18,000 | $10,800 | $9,600 |
| Anual | $216,000 | $129,600 | $115,200 |

### Resto de VMs (347 VMs)

| Concepto | On-Demand | Reserved | Optimizado |
|----------|-----------|----------|------------|
| Mensual | $109,958 | $65,975 | $59,000 |
| Anual | $1,319,496 | $791,700 | $708,000 |

---

## 💰 Comparación On-Premise vs AWS

### Costos On-Premise Estimados (Anuales)

| Concepto | Costo Anual |
|----------|-------------|
| Hardware (amortizado 3 años) | $400,000 |
| Licencias VMware | $150,000 |
| Licencias Windows/SQL | $200,000 |
| Energía y Cooling | $120,000 |
| Datacenter (espacio, seguridad) | $180,000 |
| Personal IT (parcial) | $300,000 |
| Mantenimiento y soporte | $100,000 |
| **TOTAL ON-PREMISE** | **$1,450,000** |

### Costos AWS (Anuales)

| Escenario | Costo Anual | vs On-Premise |
|-----------|-------------|---------------|
| On-Demand | $1,535,496 | +$85,496 (+6%) |
| Reserved Instances | $921,303 | -$528,697 (-36%) |
| Optimizado (RI + Rightsizing) | $800,000 | -$650,000 (-45%) |

---

## 🎯 Recomendación Final

### Estrategia Recomendada: Híbrida Optimizada

**Año 1:**
1. Migrar con On-Demand para validar (Ola 0-1)
2. Comprar RIs después de 3 meses de estabilización
3. Implementar rightsizing continuo
4. Costo estimado: $950,000

**Año 2-3:**
1. 80% Reserved Instances
2. 15% On-Demand (flexibilidad)
3. 5% Spot (dev/test)
4. Costo estimado: $800,000/año

### Ahorro Total Proyectado (3 años)

| Concepto | Costo |
|----------|-------|
| On-Premise (3 años) | $4,350,000 |
| AWS Optimizado (3 años) | $2,550,000 |
| **AHORRO TOTAL** | **$1,800,000 (41%)** |

---

## 📊 Desglose de Costos por Componente

### Compute (EC2)

| Categoría | VMs | Costo Mensual (RI) |
|-----------|-----|-------------------|
| General Purpose (t3, m5) | 215 | $45,000 |
| Compute Optimized (c5) | 85 | $18,000 |
| Memory Optimized (r5) | 50 | $13,775 |
| **TOTAL COMPUTE** | **350** | **$76,775** |

### Storage (EBS)

| Tipo | Capacidad | Costo Mensual |
|------|-----------|---------------|
| gp3 (General Purpose) | 55 TB | $4,400 |
| io2 (High Performance) | 5 TB | $625 |
| **TOTAL STORAGE** | **60 TB** | **$5,025** |

### Networking

| Componente | Cantidad | Costo Mensual |
|------------|----------|---------------|
| ALB | 8 | $200 |
| NAT Gateway | 3 | $100 |
| Data Transfer Out | ~10 TB | $900 |
| **TOTAL NETWORKING** | | **$1,200** |

### Database (RDS)

| Tipo | Instancias | Costo Mensual |
|------|------------|---------------|
| SQL Server (Multi-AZ) | 5 | $3,500 |
| PostgreSQL (Multi-AZ) | 3 | $1,800 |
| **TOTAL DATABASE** | **8** | **$5,300** |

### Servicios Adicionales

| Servicio | Costo Mensual |
|----------|---------------|
| CloudWatch | $500 |
| S3 | $300 |
| Secrets Manager | $200 |
| Backup | $400 |
| WAF | $150 |
| **TOTAL ADICIONALES** | **$1,550** |

---

## 🔍 Análisis de Sensibilidad

### Escenario Optimista (-20% uso)

| Concepto | Costo Mensual |
|----------|---------------|
| Compute | $61,420 |
| Storage | $4,020 |
| Otros | $8,050 |
| **TOTAL** | **$73,490** |

### Escenario Pesimista (+20% uso)

| Concepto | Costo Mensual |
|----------|---------------|
| Compute | $92,130 |
| Storage | $6,030 |
| Otros | $9,650 |
| **TOTAL** | **$107,810** |

---

## 📋 Próximos Pasos

### Inmediatos (Esta semana)

- [ ] Validar estimaciones con equipos técnicos
- [ ] Identificar aplicaciones para rightsizing
- [ ] Definir estrategia de compra de RIs
- [ ] Aprobar presupuesto para Ola 0

### Corto Plazo (Próximo mes)

- [ ] Implementar Ola 0 (piloto)
- [ ] Monitorear costos reales vs estimados
- [ ] Ajustar recomendaciones basado en uso real
- [ ] Comprar primeras RIs

### Medio Plazo (3-6 meses)

- [ ] Completar Olas 1-3
- [ ] Implementar auto scaling
- [ ] Optimizar continuamente
- [ ] Evaluar Savings Plans

---

## 📊 KPIs de Costos

| KPI | Target | Actual |
|-----|--------|--------|
| Costo por VM/mes | < $250 | $219 (RI) |
| Utilización RIs | > 80% | TBD |
| Ahorro vs On-Premise | > 30% | 36% (RI) |
| Costo por vCPU/mes | < $50 | $44 (RI) |

---

**Archivos Relacionados:**
- `04_recomendaciones_ec2.csv` - Recomendaciones detalladas por VM
- `04_estimacion_costos.json` - Datos completos en JSON

**Última actualización**: 2025-12-01  
**Precios**: us-east-1, On-Demand (Diciembre 2025)
