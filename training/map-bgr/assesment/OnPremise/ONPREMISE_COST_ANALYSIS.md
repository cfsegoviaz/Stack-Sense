# Análisis de Costos On-Premise - BGR (ACTUALIZADO)

## Resumen Ejecutivo

Este análisis identifica los costos de infraestructura on-premise relevantes para el business case de migración a AWS, basado en los contratos actualizados. Se excluyen licencias de usuario final (Office 365, M365) que no se ven afectadas por la migración.

---

## 🔍 ANÁLISIS DE IMPACTO REAL EN COSTOS

### Costos Totales Identificados: $14,457,463.18

### Categorización por Impacto en Migración

| Categoría | Costo Anual | % del Total | Impacto Migración |
|-----------|-------------|-------------|-------------------|
| **🔴 ELIMINABLES** | **$2,089,469** | **14.4%** | **Alto - Se eliminan completamente** |
| **🟡 OPTIMIZABLES** | **$1,194,051** | **8.3%** | **Medio - Se reducen significativamente** |
| **🟢 MANTENIBLES** | **$11,173,943** | **77.3%** | **Bajo - Se mantienen o son servicios** |

**Costo Mensual Infraestructura Migrable: $273,377**

---

## 🔴 COSTOS ELIMINABLES CON MIGRACIÓN ($2,089,469/año)

### Hardware y Infraestructura Física

| Proveedor | Componente | Valor Anual | Vencimiento | Impacto |
|-----------|------------|-------------|-------------|---------|
| **HP Ecuador** | Complete Care (RP4440, EVA, C7000, Blades) | **$948,868** | Abr 2026 | ✅ **NO RENOVAR** |
| **Grupo Bravco** | Equipos Red Segura (Networking DCP-DCA) | **$396,536** | May 2026 | ✅ **Reemplazar con AWS** |
| **Binaria** | SAN Switch | **$65,000** | Dic 2028 | ✅ **Reemplazar con EBS** |

### Licencias de Infraestructura Base

| Proveedor | Componente | Valor Anual | Vencimiento | Impacto |
|-----------|------------|-------------|-------------|---------|
| **Microsoft** | SQL Server Enterprise (18 cores) | **$179,388** | Ago 2026 | ✅ **BYOL o Aurora** |
| **Microsoft** | SQL Server Standard (10 cores) | **$26,480** | Ene 2027/28 | ✅ **BYOL o Aurora** |
| **Microsoft** | Windows Server/System Center | **$106,406** | Ene 2027/28 | ✅ **Incluido en EC2** |
| **Veritas** | NetBackup Respaldos | **$250,000** | Abr 2027 | ✅ **AWS Backup** |
| **Binaria** | SQL Server Enterprise Adicional | **$177,476** | Ago 2026 | ✅ **BYOL o Aurora** |

**Subtotal Eliminables: $2,089,469 (14.4% del total)**

---

## 🟡 COSTOS OPTIMIZABLES CON MIGRACIÓN ($1,194,051/año)

### Software Legado con Alternativas AWS

| Proveedor | Componente | Valor Anual | Vencimiento | Alternativa AWS |
|-----------|------------|-------------|-------------|-----------------|
| **Binaria** | TX-Series, CTG | **$108,260** | Sep 2026 | **AWS Transform for Mainframe** |
| **Micro Focus** | Server for Cobol | **$37,466** | Jul 2026 | **AWS Transform for Mainframe** |
| **BMC** | Control-M | **Variable** | Mar 2026 | **Step Functions + EventBridge** |
| **Synergy** | Arcserve | **Variable** | Sep 2026 | **AWS Backup** |
| **DOS** | Dynatrace | **$589,575** | Oct 2028 | **CloudWatch + X-Ray** |
| **TOTEM** | AFServer/AtallaServer/PIN Services | **$108,000** | Variable | **AWS HSM + KMS** |
| **IDERA** | SQL Diagnostic Manager | **$14,820** | Abr 2026 | **CloudWatch + Performance Insights** |
| **Bayteq** | MCS Switch Server | **$20,971** | Dic 2025 | **AWS API Gateway + Lambda** |
| **SoftwareOne** | SAM Simple | **$70,900** | Dic 2027 | **AWS Config + Systems Manager** |
| **MAINT** | Balanceador | **$84,877** | Jul 2028 | **Application Load Balancer** |
| **IT Era** | Google, AWS, Azure | **Variable** | Mar 2026 | **Directo con AWS** |

**Subtotal Optimizables: $1,194,051 (8.3% del total)**

---

## 🟢 COSTOS MANTENIBLES - NO AFECTADOS ($11,173,943/año)

### Servicios y Software de Negocio

| Categoría | Proveedor | Componente | Valor Anual | Razón |
|-----------|-----------|------------|-------------|-------|
| **Outsourcing** | TCS | Operaciones, Seguridad, Tecnología | **$9,920,904** | Servicios de personal |
| **Banca Digital** | VU | Banca Digital, Fraude, OnBoarding | **$604,476** | Software de negocio |
| **Comunicaciones** | Grupo Bravco | SDWAN, Enlaces LAN | **Variable** | Conectividad necesaria |
| **Notificaciones** | Infobip | SMS, Mail, WhatsApp, Push | **Variable** | Servicios de comunicación |
| **Custodia** | VISE | Traslado y custodia de cintas | **Variable** | Servicios físicos |
| **Licencias Usuario** | Microsoft | Office 365 MPSA | **$1,059,333** | Licencias de usuario final |
| **Licencias Usuario** | Microsoft | M365 E5, Office, Project, Visio | **$648,230** | Licencias de usuario final |

**Subtotal Mantenibles: $11,173,943 (77.3% del total)**

---

## � COSTOS TOTALES DE INFRAESTRUCTURA AFECTADA

### Resumen de Costos OnPremise que Impactan la Migración

| Categoría | Costo Anual | Costo Mensual | % del Total Migrable |
|-----------|-------------|---------------|---------------------|
| **Hardware y Físico** | $1,410,404 | $117,534 | 43.0% |
| **Licencias Microsoft** | $489,750 | $40,813 | 14.9% |
| **Software de Infraestructura** | $834,869 | $69,572 | 25.4% |
| **Backup y Almacenamiento** | $315,000 | $26,250 | 9.6% |
| **Monitoreo y Gestión** | $233,497 | $19,458 | 7.1% |
| **TOTAL INFRAESTRUCTURA** | **$3,283,520** | **$273,627** | **100%** |

### Detalle por Componente

#### Hardware y Físico ($1,410,404/año)
- HP Complete Care (Servidores, Storage, Blades): $948,868
- Equipos Red Segura (Networking DCP-DCA): $396,536
- SAN Switch: $65,000

#### Licencias Microsoft ($489,750/año)
- SQL Server Enterprise (18 cores): $179,388
- SQL Server Enterprise Adicional: $177,476
- SQL Server Standard (10 cores): $26,480
- Windows Server/System Center: $106,406

#### Software de Infraestructura ($834,869/año)
- Dynatrace: $589,575
- TX-Series, CTG: $108,260
- AFServer/AtallaServer/PIN Services: $108,000
- Server for Cobol: $37,466
- Control-M: Variable (estimado $50,000)
- Otros: $41,568

#### Backup y Almacenamiento ($315,000/año)
- NetBackup Respaldos: $250,000
- Arcserve: Variable (estimado $65,000)

#### Monitoreo y Gestión ($233,497/año)
- Balanceador: $84,877
- SAM Simple: $70,900
- MCS Switch Server: $20,971
- SQL Diagnostic Manager: $14,820
- IT Era (Multi-cloud): Variable (estimado $41,929)

---

## 🔄 ESCENARIOS DE MIGRACIÓN: LIFT & SHIFT vs OPTIMIZADO

### Escenario 1: LIFT & SHIFT (Migración Directa)

| Componente OnPremise | Costo Anual | Equivalente AWS | Costo AWS Anual | Ahorro/Costo |
|---------------------|-------------|-----------------|-----------------|--------------|
| **Compute (122 servidores)** | $948,868* | EC2 Instances (similar sizing) | $720,000 | -$228,868 |
| **Storage (SAN/EVA)** | $65,000 | EBS + S3 | $180,000 | -$115,000 |
| **Networking** | $396,536 | VPC + Direct Connect | $120,000 | $276,536 |
| **SQL Server BYOL** | $383,344 | RDS SQL Server BYOL | $383,344 | $0 |
| **Windows Server** | $106,406 | Incluido en EC2 Windows | $0 | $106,406 |
| **Backup** | $315,000 | AWS Backup | $60,000 | $255,000 |
| **Monitoreo** | $604,395 | CloudWatch + 3rd party | $300,000 | $304,395 |
| **Load Balancing** | $84,877 | Application Load Balancer | $24,000 | $60,877 |
| **Otros Software** | $379,114 | Mantener en EC2 | $379,114 | $0 |
| **TOTAL LIFT & SHIFT** | **$3,283,520** | | **$2,166,458** | **$1,117,062 (34%)** |

*Hardware HP incluye costo de servidores físicos

### Escenario 2: MIGRACIÓN OPTIMIZADA (Recomendado)

| Componente OnPremise | Costo Anual | Solución AWS Optimizada | Costo AWS Anual | Ahorro/Costo |
|---------------------|-------------|-------------------------|-----------------|--------------|
| **Compute Optimizado** | $948,868 | EC2 + Spot + Reserved | $480,000 | $468,868 |
| **Storage Optimizado** | $65,000 | EBS gp3 + S3 IA + Glacier | $90,000 | -$25,000 |
| **Networking** | $396,536 | VPC + Transit Gateway | $80,000 | $316,536 |
| **Aurora PostgreSQL** | $383,344 | Aurora PostgreSQL | $150,000 | $233,344 |
| **Windows → Linux** | $106,406 | Amazon Linux (gratis) | $0 | $106,406 |
| **AWS Backup** | $315,000 | AWS Backup + Lifecycle | $45,000 | $270,000 |
| **CloudWatch Native** | $604,395 | CloudWatch + X-Ray | $120,000 | $484,395 |
| **ALB + Auto Scaling** | $84,877 | Application Load Balancer | $18,000 | $66,877 |
| **Modernización** | $379,114 | Serverless + Managed Services | $123,398 | $255,716 |
| **TOTAL OPTIMIZADO** | **$3,283,520** | | **$1,106,398** | **$2,177,122 (66%)** |

### Comparativa de Escenarios

| Métrica | OnPremise | Lift & Shift | Optimizado | Diferencia |
|---------|-----------|--------------|------------|------------|
| **Costo Anual** | $3,283,520 | $2,166,458 | $1,106,398 | $1,060,060 |
| **Costo Mensual** | $273,627 | $180,538 | $92,200 | $88,338 |
| **Ahorro vs OnPrem** | - | 34% | 66% | +32% |
| **Tiempo Implementación** | - | 6-9 meses | 12-18 meses | +6-9 meses |
| **Complejidad** | - | Baja | Media-Alta | - |
| **Riesgo** | - | Bajo | Medio | - |
| **Beneficios Adicionales** | - | Limitados | Altos | - |

---

## 📊 ANÁLISIS FINANCIERO DETALLADO

### ROI por Escenario

| Escenario | Inversión Inicial | Ahorro Anual | ROI | Payback |
|-----------|------------------|--------------|-----|---------|
| **Lift & Shift** | $450,000 | $1,117,062 | 4.8 meses | 4.8 meses |
| **Optimizado** | $654,900 | $2,177,122 | 3.6 meses | 3.6 meses |

### Flujo de Caja 3 Años (Optimizado)

| Año | OnPremise | AWS Optimizado | Ahorro Anual | Ahorro Acumulado |
|-----|-----------|----------------|--------------|------------------|
| **Año 0** | $0 | -$654,900 | -$654,900 | -$654,900 |
| **Año 1** | $3,283,520 | $1,106,398 | $2,177,122 | $1,522,222 |
| **Año 2** | $3,283,520 | $1,106,398 | $2,177,122 | $3,699,344 |
| **Año 3** | $3,283,520 | $1,106,398 | $2,177,122 | $5,876,466 |

### Beneficios Adicionales del Escenario Optimizado

| Beneficio | Valor Estimado | Descripción |
|-----------|----------------|-------------|
| **Elasticidad** | $200,000/año | Auto-scaling reduce costos en períodos bajos |
| **Disponibilidad** | $500,000/año | Reducción de downtime (99.9% → 99.99%) |
| **Seguridad** | $150,000/año | Reducción de riesgos de seguridad |
| **Agilidad** | $300,000/año | Faster time-to-market para nuevos productos |
| **Innovación** | $400,000/año | Acceso a servicios de IA/ML y analytics |
| **TOTAL BENEFICIOS** | **$1,550,000/año** | **Valor adicional no cuantificado** |

### Timeline de Ahorros por Vencimientos

| Período | Contratos que Vencen | Ahorro Inmediato |
|---------|---------------------|------------------|
| **Dic 2025** | Bayteq MCS Switch | $20,971 |
| **Abr 2026** | HP Complete Care + IDERA | $963,688 |
| **May 2026** | Grupo Bravco Red Segura | $396,536 |
| **Ago 2026** | SQL Server Enterprise | $356,864 |
| **Sep 2026** | TX-Series, CTG | $108,260 |
| **Jul 2026** | Micro Focus Cobol | $37,466 |

**Ahorro acumulado primer año: $1,883,785**

---

## 🎯 RECOMENDACIÓN ESTRATÉGICA

### Enfoque Híbrido Recomendado

**Fase 1 (0-6 meses): Lift & Shift Crítico**
- Migrar infraestructura crítica antes de vencimiento HP (Abril 2026)
- Ahorro inmediato: $1,117,062/año
- Riesgo: Bajo
- Inversión: $450,000

**Fase 2 (6-18 meses): Optimización Progresiva**
- Modernizar aplicaciones y servicios
- Ahorro adicional: $1,060,060/año
- Inversión adicional: $204,900
- **Ahorro total: $2,177,122/año**

### Justificación del Enfoque Híbrido

1. **Urgencia temporal:** Contrato HP vence Abril 2026
2. **Reducción de riesgo:** Migración por fases
3. **Flujo de caja positivo:** Ahorros inmediatos financian optimización
4. **Aprendizaje organizacional:** Experiencia gradual con AWS

---

## 🎯 OPORTUNIDADES DE OPTIMIZACIÓN PRIORITARIAS

### 1. 🔥 CRÍTICO - Hardware HP ($948,868/año)
- **Vencimiento:** Abril 2026
- **Acción:** NO RENOVAR - Migrar antes del vencimiento
- **Impacto:** Ahorro inmediato del 100%
- **Riesgo:** Alto si no se migra a tiempo

### 2. 🔥 CRÍTICO - SQL Server ($356,864/año)
- **Componentes:** Enterprise (18 cores) + Standard (10 cores) + Adicional
- **Opciones:**
  - BYOL a AWS RDS (mantener licencias)
  - Migrar a Aurora PostgreSQL (eliminar licencias)
- **Recomendación:** Aurora con Babelfish para compatibilidad
- **Ahorro:** 100% de licenciamiento

### 3. 🟡 ALTO - Modernización Mainframe ($145,726/año)
- **Componentes:** TX-Series, CTG, Cobol
- **Solución:** AWS Transform for Mainframe (GRATIS)
- **Beneficios:**
  - Conversión automática COBOL → Java
  - Documentación automática
  - Eliminación de dependencias legacy
- **Ahorro:** $145,726/año + reducción mantenimiento

### 4. 🟡 MEDIO - Monitoreo y Observabilidad ($604,395/año)
- **Componentes:** Dynatrace, SQL Diagnostic Manager
- **Alternativa:** CloudWatch + X-Ray + Performance Insights
- **Ahorro estimado:** 60-70% ($362,637/año)

### 5. 🟡 MEDIO - Backup y Almacenamiento ($315,000/año)
- **Componentes:** NetBackup, Arcserve, SAN Switch
- **Alternativa:** AWS Backup + EBS
- **Ahorro estimado:** 70-80% ($220,500/año)

---

## 🚀 AWS TRANSFORM FOR MAINFRAME - OPORTUNIDAD ÚNICA

### Aplicación Específica para BGR

**Licencias actuales afectadas:**
- TX-Series, CTG: $108,260/año
- Server for Cobol: $37,466/año
- **Total:** $145,726/año

**Beneficios del servicio GRATIS:**
1. **Análisis automático** de código COBOL, JCL, BMS
2. **Documentación automática** de lógica de negocio
3. **Conversión a Java** preservando funcionalidad
4. **Generación de pruebas** automatizadas
5. **Microservicios event-driven** para aplicaciones batch

**ROI Inmediato:**
- Costo del servicio: **$0 (GRATIS)**
- Ahorro anual: **$145,726**
- Tiempo de implementación: **Meses vs años**

---

## 📈 BUSINESS CASE ACTUALIZADO

### Comparativa de Escenarios - Resumen Ejecutivo

| Métrica | OnPremise | Lift & Shift | Optimizado | Mejor Opción |
|---------|-----------|--------------|------------|--------------|
| **Costo Anual** | $3,283,520 | $2,166,458 | $1,106,398 | Optimizado |
| **Ahorro Anual** | - | $1,117,062 | $2,177,122 | Optimizado |
| **% Ahorro** | - | 34% | 66% | Optimizado |
| **ROI** | - | 4.8 meses | 3.6 meses | Optimizado |
| **Inversión** | - | $450,000 | $654,900 | Lift & Shift |
| **Riesgo** | Alto | Bajo | Medio | Lift & Shift |

### Métricas Clave del Escenario Recomendado (Optimizado)

| Concepto | Valor |
|----------|-------|
| **Costo Anual OnPremise (Infraestructura)** | $3,283,520 |
| **Costo Anual AWS Optimizado** | $1,106,398 |
| **Ahorro Anual** | **$2,177,122 (66%)** |
| **Ahorro Mensual** | **$181,427** |
| **Inversión Migración** | $654,900 |
| **ROI** | **3.6 meses** |
| **Payback Period** | **3.6 meses** |
| **Ahorro 3 años** | **$5,876,466** |

### Valor Total de la Migración (3 años)

| Concepto | Valor |
|----------|-------|
| **Ahorros Directos** | $5,876,466 |
| **Beneficios Adicionales** | $4,650,000 |
| **Valor Total** | **$10,526,466** |
| **ROI Total** | **1,608%** |

---

## 🎯 RECOMENDACIONES ESTRATÉGICAS

### Fase 1: Preparación (0-3 meses)
1. **Evaluar AWS Transform for Mainframe** para aplicaciones COBOL
2. **Planificar migración** antes de vencimiento HP (Abr 2026)
3. **Decidir estrategia SQL Server:** BYOL vs Aurora PostgreSQL
4. **Iniciar PoC** con aplicaciones críticas

### Fase 2: Migración Crítica (3-12 meses)
1. **NO RENOVAR** contrato HP Complete Care
2. **Migrar infraestructura core** antes de Abril 2026
3. **Implementar Aurora PostgreSQL** con Babelfish
4. **Modernizar aplicaciones COBOL** con AWS Transform

### Fase 3: Optimización (12-18 meses)
1. **Consolidar monitoreo** en CloudWatch
2. **Migrar backups** a AWS Backup
3. **Optimizar costos** con Reserved Instances
4. **Evaluar servicios adicionales** para optimización

### Riesgos y Mitigaciones

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| No migrar antes Abr 2026 | Media | Alto | Acelerar Wave 1-2 |
| Problemas compatibilidad SQL | Baja | Medio | PoC con Aurora Babelfish |
| Resistencia al cambio | Alta | Medio | Training y change management |
| Sobrecostos migración | Media | Medio | Monitoreo continuo de costos |

---

*Documento actualizado por Escala24x7 - Proyecto MAP BGR*  
*Fecha: Enero 2026*  
*Basado en contratos vigentes y datos actualizados*
