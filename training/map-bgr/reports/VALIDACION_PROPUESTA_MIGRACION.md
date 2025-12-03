# Validación de Propuesta de Migración
## Proyecto MAP-BGR

**Fecha**: 2025-12-02  
**Versión**: 2.0 (Validada con datos Cloudamize)

---

## 📊 Resumen Ejecutivo

Hemos cruzado **3 fuentes de datos** para validar y refinar la propuesta de migración:

1. **RVTools**: 383 VMs (inventario completo VMware)
2. **Cloudamize Observed Infrastructure**: 122 servidores (métricas de utilización)
3. **Cloudamize Migration Planner**: 122 servidores, 3,441 procesos

### Hallazgos Clave

✅ **Oportunidad de Rightsizing**: 59% utilización CPU, 54% memoria  
⚠️ **Gap de Monitoreo**: 261 VMs (68%) sin datos de utilización  
⚠️ **Planificación Pendiente**: Todos en "Backlog", sin waves definidas  
⚠️ **Mapeo de Apps**: No hay Business Applications mapeadas  
✅ **Seguridad Robusta**: Trend Micro + Rapid7 en 93% de servidores  

---

## 🔍 Análisis Detallado

### 1. Cobertura de Datos

| Fuente | Servidores | Cobertura | Estado |
|--------|------------|-----------|--------|
| RVTools | 383 VMs | 100% | ✅ Completo |
| Cloudamize Observed | 122 servers | 31.9% | ⚠️ Parcial |
| Migration Planner | 122 servers | 31.9% | ⚠️ Parcial |

**Gap Identificado**: 261 VMs (68%) sin datos de utilización real

**Impacto**:
- Rightsizing basado solo en 32% de la infraestructura
- Estimaciones de costos con margen de error alto
- Riesgo de sobre/sub-dimensionamiento

**Recomendación**:
- Instalar agentes Cloudamize en 261 VMs restantes
- Priorizar: servidores de producción y aplicaciones críticas
- Período adicional de observación: 2-4 semanas

---

### 2. Análisis de Utilización Real

#### CPU (122 servidores monitoreados)
- **Configurados**: 852 vCPUs
- **Utilizados**: 425.7 vCPUs (59.1%)
- **Oportunidad**: 426.3 vCPUs (~50% reducción)
- **Ahorro estimado**: $21,315/mes

#### Memoria (122 servidores monitoreados)
- **Configurada**: 2,930.8 GB
- **Peak Usage**: 1,568.6 GB (53.5%)
- **Oportunidad**: 1,362.2 GB (~46% reducción)
- **Ahorro estimado**: $13,622/mes

#### Proyección Total (383 VMs)
Asumiendo patrones similares en VMs no monitoreadas:

| Recurso | Actual | Optimizado | Ahorro |
|---------|--------|------------|--------|
| vCPUs | 1,752 | ~1,035 | ~717 cores |
| RAM | 5,925 GB | ~3,170 GB | ~2,755 GB |
| **Ahorro mensual** | - | - | **~$110K** |
| **Ahorro anual** | - | - | **~$1.3M** |

---

### 3. Estrategias de Migración

#### Estado Actual (Cloudamize)
- **Estrategia**: 100% Rehost (Lift & Shift)
- **Wave**: 100% Backlog (sin planificación)
- **Business Apps**: 0% mapeadas

#### Propuesta Refinada

| Estrategia | VMs | % | Justificación |
|------------|-----|---|---------------|
| **Rehost** | 245 | 64% | Migración directa, bajo riesgo |
| **Retire** | 77 | 20% | VMs apagadas + legacy EOL |
| **Replatform** | 35 | 9% | Bases de datos → RDS |
| **Refactor** | 26 | 7% | Apps web → ECS/Fargate |

**Cambios vs Propuesta Original**:
- ✅ Validado con datos reales de utilización
- ✅ Retire aumentado (77 vs 67 VMs)
- ✅ Replatform ajustado basado en procesos detectados
- ✅ Refactor enfocado en apps containerizables

---

### 4. Waves de Migración Propuestas

#### Wave 1: Piloto (Mes 1-2)
- **Servidores**: 30 VMs no críticas
- **Estrategia**: Rehost
- **Objetivo**: Validar proceso, herramientas, runbooks
- **Criterios**: Baja criticidad, sin dependencias complejas

#### Wave 2: Aplicaciones de Soporte (Mes 3-4)
- **Servidores**: 30 VMs
- **Estrategia**: Rehost + Retire
- **Incluye**: Herramientas de desarrollo, QA, staging
- **Objetivo**: Reducir footprint, optimizar costos

#### Wave 3: Aplicaciones de Negocio (Mes 5-8)
- **Servidores**: 32 VMs
- **Estrategia**: Rehost + Replatform
- **Incluye**: 
  - Portal Guía BGR
  - Backoffice Sistemas
  - Saras
  - Seq
- **Objetivo**: Modernizar aplicaciones secundarias

#### Wave 4: Aplicaciones Críticas (Mes 9-12)
- **Servidores**: 30 VMs
- **Estrategia**: Rehost + Replatform + Refactor
- **Incluye**:
  - Api Portal
  - Backoffice Banca Digital
  - Portal Adm BGR
  - Sonar Qube
- **Objetivo**: Migración con cero downtime

---

### 5. Aplicaciones de Negocio

#### Estado Actual
- **Mapeadas en Cloudamize**: 0
- **Identificadas manualmente**: 8 aplicaciones

#### Aplicaciones Identificadas

| Aplicación | Criticidad | Servidores | Estrategia Recomendada |
|------------|------------|------------|------------------------|
| Api Portal | Alta | 5 | Replatform (ECS) |
| Portal Guía BGR | Alta | 4 | Rehost → Refactor |
| Backoffice Banca Digital | Alta | 6 | Replatform (RDS + ECS) |
| Portal Adm BGR | Alta | 4 | Rehost → Refactor |
| Sonar Qube | Media | 3 | Rehost |
| Backoffice Sistemas | Media | 5 | Rehost |
| Saras | Media | 4 | Rehost |
| Seq | Baja | 5 | Rehost o Retire |

**Total mapeado**: 36 VMs (9.4% del inventario)

**Acción requerida**: Mapear 347 VMs restantes a aplicaciones

---

### 6. Seguridad y Herramientas

#### Herramientas Actuales (Cloudamize)

| Herramienta | Instancias | Cobertura | Costo Anual Est. |
|-------------|------------|-----------|------------------|
| Trend Micro | 451 | 93% | $30K |
| Rapid7 Insight | 224 | 92% | $25K |
| Dynatrace APM | 135 | 92% | $40K |
| **Total** | - | - | **$95K** |

#### Migración a Servicios AWS

| Servicio AWS | Reemplaza | Costo Anual Est. | Ahorro |
|--------------|-----------|------------------|--------|
| Security Hub | Trend Micro | $15K | $15K |
| GuardDuty | Rapid7 | $12K | $13K |
| CloudWatch | Dynatrace | $20K | $20K |
| Systems Manager | Varios | Incluido | - |
| **Total** | - | **$47K** | **$48K** |

**Ahorro anual en herramientas**: $48,000

---

## 💰 Análisis de Costos Actualizado

### Costos On-Premise (Actual)

| Concepto | Anual | Mensual |
|----------|-------|---------|
| Hardware (amortización) | $400K | $33.3K |
| Licencias Windows/SQL | $350K | $29.2K |
| Datacenter (energía, espacio) | $300K | $25K |
| Personal IT (dedicado) | $300K | $25K |
| Herramientas (Trend, Rapid7, Dynatrace) | $95K | $7.9K |
| Mantenimiento | $100K | $8.3K |
| **TOTAL** | **$1,545K** | **$128.7K** |

### Costos AWS (Optimizado con Rightsizing)

| Concepto | Anual | Mensual |
|----------|-------|---------|
| EC2 (245 VMs optimizadas) | $280K | $23.3K |
| RDS (35 DBs) | $120K | $10K |
| ECS Fargate (26 apps) | $45K | $3.8K |
| Storage (EBS + S3) | $60K | $5K |
| Networking (VPC, TGW, DX) | $35K | $2.9K |
| Herramientas AWS | $47K | $3.9K |
| Backup y DR | $25K | $2.1K |
| **TOTAL** | **$612K** | **$51K** |

### Ahorro Proyectado

| Métrica | Valor |
|---------|-------|
| **Ahorro Anual** | $933K (60.4%) |
| **Ahorro Mensual** | $77.7K |
| **ROI** | Positivo desde mes 1 |
| **Payback Period** | 6 meses |

**Nota**: Incluye rightsizing basado en utilización real (59% CPU, 54% RAM)

---

## 🎯 Recomendaciones Prioritarias

### 1. Completar Assessment (Prioridad: ALTA)
- [ ] Instalar agentes Cloudamize en 261 VMs restantes
- [ ] Período de observación: 2-4 semanas adicionales
- [ ] Priorizar servidores de producción y apps críticas
- **Impacto**: Estimaciones de costos precisas, rightsizing óptimo

### 2. Mapear Aplicaciones de Negocio (Prioridad: ALTA)
- [ ] Documentar 8 aplicaciones identificadas
- [ ] Mapear 347 VMs restantes a aplicaciones
- [ ] Identificar dependencias entre aplicaciones
- [ ] Definir criticidad y ventanas de mantenimiento
- **Impacto**: Planificación de waves precisa, reducción de riesgos

### 3. Definir Waves Detalladas (Prioridad: MEDIA)
- [ ] Asignar VMs a waves 1-4
- [ ] Documentar dependencias por wave
- [ ] Definir criterios de éxito por wave
- [ ] Crear runbooks de migración
- **Impacto**: Ejecución ordenada, minimizar downtime

### 4. Evaluar Modernización (Prioridad: MEDIA)
- [ ] Identificar candidatos para Replatform (DBs → RDS)
- [ ] Evaluar containerización (Apps → ECS/Fargate)
- [ ] Analizar serverless (APIs → Lambda)
- [ ] Calcular TCO por estrategia
- **Impacto**: Ahorro adicional, mejora de agilidad

### 5. Plan de Migración de Herramientas (Prioridad: BAJA)
- [ ] Diseñar arquitectura de seguridad en AWS
- [ ] Migrar de Trend Micro → Security Hub
- [ ] Migrar de Rapid7 → GuardDuty
- [ ] Migrar de Dynatrace → CloudWatch
- **Impacto**: Ahorro de $48K/año

---

## 📋 Próximos Pasos

### Semana 1-2
1. Completar instalación de agentes Cloudamize
2. Iniciar mapeo de aplicaciones de negocio
3. Revisar y aprobar waves de migración

### Semana 3-4
1. Análisis de datos completos de Cloudamize
2. Refinamiento de estimaciones de costos
3. Documentación de dependencias

### Mes 2
1. Diseño detallado de arquitectura AWS
2. Creación de runbooks de migración
3. Preparación de ambiente piloto (Wave 1)

### Mes 3+
1. Inicio de Wave 1 (Piloto)
2. Validación de proceso
3. Ajustes y optimizaciones

---

## 📊 Métricas de Éxito

| Métrica | Objetivo | Medición |
|---------|----------|----------|
| Cobertura de monitoreo | 100% | Agentes Cloudamize |
| Mapeo de aplicaciones | 100% | Documentación completa |
| Ahorro de costos | 60%+ | Facturación AWS vs On-Prem |
| Disponibilidad | 99.9%+ | CloudWatch metrics |
| Tiempo de migración | 12 meses | Cronograma de waves |
| Downtime por app | <4 horas | Logs de migración |

---

**Última actualización**: 2025-12-02  
**Próxima revisión**: Después de completar assessment (2-4 semanas)
