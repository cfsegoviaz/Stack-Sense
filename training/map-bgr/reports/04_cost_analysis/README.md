# 04. Cost Analysis

**Audiencia:** CFO, Finanzas, Procurement, Directores  
**Propósito:** Análisis detallado de costos y estimaciones

---

## 📄 Documentos

### 04_RESUMEN_COSTOS_AWS.md
**Descripción:** Resumen de costos AWS  
**Contenido:**
- Costos por aplicación
- Costos por servicio AWS
- Comparativa on-premise vs AWS

### bgr_aws_pricing_detailed.md
**Descripción:** Pricing detallado por componente  
**Contenido:**
- Desglose por servicio AWS
- Costos basados en RVTools (ECBRTSW21)
- Configuraciones específicas
- Oportunidades de optimización

### 04_estimacion_costos.json (205 KB)
**Descripción:** Estimaciones estructuradas  
**Formato:** JSON  
**Contenido:**
- Costos por aplicación
- Costos por componente
- Proyecciones mensuales/anuales

### 04_recomendaciones_ec2.csv (49 KB)
**Descripción:** Recomendaciones de instancias EC2  
**Formato:** CSV  
**Contenido:**
- Sizing por aplicación
- Tipos de instancia recomendados
- Costos estimados

### 05_optimizaciones_costos.json (2 KB)
**Descripción:** Oportunidades de optimización  
**Formato:** JSON  
**Contenido:**
- Savings Plans
- Reserved Instances
- Right-sizing opportunities

---

## 💰 Resumen de Costos

### Comparativa de Estrategias

| Estrategia | Costo Mensual | Ahorro Anual | % Ahorro |
|-----------|---------------|--------------|----------|
| **On-Premise** | $5,320 | - | - |
| **Lift & Shift** | $3,990 | $15,960 | 25% |
| **Modernización** | $2,677 | $31,720 | 49.7% |

### Desglose por Aplicación (Modernización)

| Aplicación | Costo/Mes | Ahorro vs On-Prem |
|-----------|-----------|-------------------|
| PortalGuiaBGR | $407 | 39% |
| Api Portal | $552 | 17% |
| PortalAdministrativoBGR | $263 | 60% |
| Backoffice Sistemas | $407 | 39% |
| Backoffice Banca | $559 | 16% |
| Saras | $487 | 27% |
| **TOTAL** | **$2,677** | **49.7%** |

### Desglose por Servicio AWS

| Servicio | Costo/Mes | % del Total |
|----------|-----------|-------------|
| ECS Fargate | $1,225 | 45.8% |
| RDS SQL Server | $1,354 | 50.6% |
| Networking | $121 | 4.5% |
| Otros | $177 | 6.6% |

---

## 📈 Oportunidades de Optimización

### Fase 1: Inmediata (Ahorro: $5,440/año)
- ✅ RDS Reserved Instances (1 año): 30% ahorro
- ✅ Fargate Savings Plans (1 año): 20% ahorro
- ✅ Right-sizing: 10-15% ahorro

### Fase 2: Mediano Plazo (Ahorro: $13,000/año)
- ✅ Migración a Aurora PostgreSQL: 60% ahorro en BD
- ✅ Auto-scaling policies: 20-30% ahorro en compute

### Fase 3: Largo Plazo (Ahorro: $900/año)
- ✅ Serverless para apps de bajo tráfico
- ✅ S3 Intelligent-Tiering para backups

**Ahorro Total Potencial:** $20,840/año  
**Costo Optimizado Final:** $11,280/año (82% ahorro vs on-premise)
