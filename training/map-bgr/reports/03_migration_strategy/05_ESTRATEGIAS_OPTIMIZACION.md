# Estrategias de Migración y Optimización de Costos

**Proyecto**: MAP-BGR  
**Fecha**: 2025-12-01  
**VMs Analizadas**: 383

---

## 🎯 Resumen Ejecutivo

### Clasificación por Estrategia 7R's

| Estrategia | VMs | % | Costo Mensual | Descripción |
|------------|-----|---|---------------|-------------|
| **Rehost** | 261 | 68.1% | $116,298 | Lift & Shift - Migración directa |
| **Retire** | 77 | 20.1% | $9,972 | Eliminar o consolidar |
| **Refactor** | 26 | 6.8% | $1,441 | Modernizar a serverless/containers |
| **Replatform** | 19 | 5.0% | $4,507 | Upgrade OS o migrar a managed |
| **TOTAL** | **383** | **100%** | **$132,218** | |

---

## 💰 Optimización de Costos - Roadmap

### Escenarios de Costos

| Escenario | Costo Mensual | Costo Anual | Ahorro vs On-Demand |
|-----------|---------------|-------------|---------------------|
| **On-Demand (Actual)** | $127,958 | $1,535,496 | - |
| **Reserved Instances** | $76,775 | $921,303 | 40% ($614K/año) |
| **Totalmente Optimizado** | $43,548 | $522,581 | **66% ($1.0M/año)** |

### Ahorro Total Potencial

💰 **$1,012,916 anuales** (66% de reducción)

---

## 📋 Estrategias de Optimización Detalladas

### 1. Eliminar VMs Apagadas ⚡ ACCIÓN INMEDIATA

**Impacto**: 33 VMs  
**Ahorro**: $4,260/mes | $51,115/año  
**Implementación**: Inmediata  
**Riesgo**: Bajo  

**Acciones**:
- ✅ Validar con owners si son necesarias
- ✅ Crear snapshots antes de eliminar
- ✅ Eliminar VMs y recursos asociados (EBS, NICs)
- ✅ Documentar VMs eliminadas

**Timeline**: Semana 1

---

### 2. Reserved Instances (1 año) 💎 RECOMENDADO

**Impacto**: 350 VMs  
**Ahorro**: $51,183/mes | $614,193/año  
**Implementación**: 3 meses (después de estabilización)  
**Riesgo**: Bajo  

**Acciones**:
- ✅ Identificar VMs estables (80% del inventario)
- ✅ Comprar RIs para instancias más usadas:
  - t3.xlarge (97 VMs)
  - c5.large (37 VMs)
  - t3.large (34 VMs)
- ✅ Monitorear utilización de RIs (target >80%)
- ✅ Considerar Convertible RIs para flexibilidad

**Timeline**: Mes 3-4 (después de Ola 0 y 1)

**Distribución recomendada**:
- 70% Standard RIs (máximo descuento)
- 30% Convertible RIs (flexibilidad)

---

### 3. Spot Instances para Dev/Test 🎯

**Impacto**: 70 VMs (~20% del inventario)  
**Ahorro**: $3,885/mes | $46,615/año  
**Implementación**: 2-3 meses  
**Riesgo**: Bajo  

**Acciones**:
- ✅ Identificar ambientes no productivos
- ✅ Implementar auto-restart en caso de interrupción
- ✅ Usar Spot para:
  - Ambientes de desarrollo
  - Cargas batch y procesamiento
  - Testing y QA
- ✅ Configurar Spot Fleet con diversificación

**Timeline**: Mes 2-3

**Candidatos ideales**:
- Ambientes de desarrollo
- Servidores de build/CI
- Procesamiento batch
- Análisis de datos

---

### 4. Auto Scaling 📈

**Impacto**: 105 VMs (~30% del inventario)  
**Ahorro**: $20,889/mes | $250,671/año  
**Implementación**: 3-4 meses  
**Riesgo**: Medio  

**Acciones**:
- ✅ Implementar en aplicaciones web y APIs:
  - PortalAdmBGR
  - PortalGuiaBGR
  - Api Portal
  - Backoffice apps
- ✅ Configurar políticas de scaling:
  - CPU > 70% → scale out
  - CPU < 30% → scale in
  - Requests/min como métrica
- ✅ Definir min/max instancias por aplicación
- ✅ Implementar health checks

**Timeline**: Mes 3-5

**Configuración recomendada**:
```
Min instances: 2 (HA)
Max instances: 6-10 (según carga)
Target CPU: 60-70%
Scale out: +2 instancias
Scale in: -1 instancia (gradual)
```

---

### 5. Servicios Managed (RDS, Lambda, ECS) 🚀

**Impacto**: 35 VMs (~10% del inventario)  
**Ahorro**: $4,193/mes | $50,321/año  
**Implementación**: 4-6 meses  
**Riesgo**: Alto  

**Acciones**:
- ✅ **Bases de datos → RDS/Aurora**:
  - Identificar VMs con SQL Server, PostgreSQL, MySQL
  - Migrar a RDS Multi-AZ
  - Beneficios: Backups automáticos, patching, HA
  
- ✅ **Microservicios → Lambda**:
  - APIs simples y funciones
  - Procesamiento de eventos
  - Beneficio: Pay per use, auto scaling
  
- ✅ **Aplicaciones → ECS Fargate**:
  - Containerizar aplicaciones modernas
  - Eliminar gestión de servidores
  - Beneficio: Escalado automático, menor ops

**Timeline**: Mes 4-8

**Candidatos prioritarios**:
1. Bases de datos (5-10 VMs) → RDS
2. APIs pequeñas (10-15 VMs) → Lambda
3. Apps containerizables (10-15 VMs) → ECS

---

## 📊 Estrategia 7R's Detallada

### Rehost (261 VMs - 68.1%)

**Descripción**: Lift & Shift - Migración directa a EC2

**Características**:
- OS moderno (Windows 2016+, Linux)
- Aplicaciones estables
- Complejidad baja

**Estrategia**:
1. Usar AWS Application Migration Service (MGN)
2. Migración automatizada
3. Validación post-migración
4. Comprar RIs después de 3 meses

**Timeline**: Olas 0-3 (6 meses)

**Costo optimizado**: $70,000/mes (con RIs)

---

### Retire (77 VMs - 20.1%)

**Descripción**: Eliminar o consolidar

**Categorías**:
1. **VMs apagadas** (33 VMs):
   - Acción: Validar y eliminar
   - Ahorro: $4,260/mes
   
2. **Windows 2003** (46 VMs):
   - Acción: Upgrade o retire
   - Crítico: Sin soporte desde 2015
   
3. **Duplicadas/Obsoletas**:
   - Acción: Consolidar

**Timeline**: 
- VMs apagadas: Inmediato
- Windows 2003: Mes 1-2 (antes de migración)

**Ahorro total**: $9,972/mes

---

### Refactor (26 VMs - 6.8%)

**Descripción**: Modernizar a serverless/containers

**Candidatos**:
- VMs pequeñas (≤2 vCPU, ≤4GB)
- APIs y microservicios
- Funciones específicas

**Opciones**:
1. **Lambda**: Para funciones y APIs simples
2. **ECS Fargate**: Para aplicaciones containerizadas
3. **API Gateway + Lambda**: Para APIs REST

**Timeline**: Mes 4-8

**Ahorro**: 40-60% vs EC2 tradicional

---

### Replatform (19 VMs - 5.0%)

**Descripción**: Upgrade OS o migrar a managed

**Categorías**:
1. **Windows 2008** (21 VMs):
   - Acción: Upgrade a 2019/2022 antes de migrar
   - Crítico: EOL desde 2020
   
2. **Bases de datos**:
   - Acción: Migrar a RDS/Aurora
   - Beneficio: Managed service

**Timeline**: Mes 1-3

**Costo**: Similar a Rehost, pero con mejor soporte

---

## 🎯 Plan de Implementación por Fases

### Fase 1: Quick Wins (Mes 1-2)

**Objetivo**: Ahorro inmediato

1. ✅ Eliminar 33 VMs apagadas → $4,260/mes
2. ✅ Identificar y documentar Windows 2003/2008
3. ✅ Planificar upgrades de OS

**Ahorro**: $51,115/año

---

### Fase 2: Reserved Instances (Mes 3-4)

**Objetivo**: 40% de ahorro en VMs estables

1. ✅ Completar Ola 0 y 1
2. ✅ Monitorear uso por 2-4 semanas
3. ✅ Comprar RIs para 80% de VMs
4. ✅ Implementar Spot para dev/test

**Ahorro acumulado**: $660,808/año

---

### Fase 3: Auto Scaling (Mes 4-6)

**Objetivo**: Optimizar aplicaciones web

1. ✅ Implementar auto scaling en 4 aplicaciones principales
2. ✅ Configurar políticas de scaling
3. ✅ Monitorear y ajustar

**Ahorro acumulado**: $911,479/año

---

### Fase 4: Modernización (Mes 6-12)

**Objetivo**: Servicios managed y refactoring

1. ✅ Migrar bases de datos a RDS
2. ✅ Refactorizar APIs a Lambda
3. ✅ Containerizar aplicaciones en ECS

**Ahorro acumulado**: $1,012,916/año

---

## 📈 Proyección de Costos por Fase

| Fase | Mes | Costo Mensual | Ahorro Acumulado |
|------|-----|---------------|------------------|
| Inicial | 0 | $127,958 | - |
| Quick Wins | 1-2 | $123,698 | $4,260/mes |
| Reserved Instances | 3-4 | $72,515 | $55,443/mes |
| Auto Scaling | 5-6 | $51,626 | $76,332/mes |
| Modernización | 7-12 | $43,548 | $84,410/mes |

**Ahorro final**: 66% ($84,410/mes | $1,012,916/año)

---

## 🎯 Métricas de Éxito

| KPI | Baseline | Target | Actual |
|-----|----------|--------|--------|
| Costo mensual | $127,958 | $43,548 | TBD |
| Ahorro vs On-Demand | 0% | 66% | TBD |
| Utilización RIs | - | >80% | TBD |
| VMs optimizadas | 0 | 383 | TBD |
| Tiempo de implementación | - | 12 meses | TBD |

---

## ⚠️ Riesgos y Mitigaciones

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| Subutilización de RIs | Media | Alto | Monitoreo continuo, RIs convertibles |
| Interrupciones con Spot | Media | Medio | Auto-restart, diversificación |
| Complejidad de refactoring | Alta | Alto | Empezar con apps simples, POCs |
| Resistencia al cambio | Media | Medio | Capacitación, documentación |

---

## 📋 Próximos Pasos Inmediatos

### Esta Semana
- [ ] Validar VMs apagadas con owners
- [ ] Crear snapshots de VMs a eliminar
- [ ] Documentar Windows 2003/2008 para upgrade

### Próximo Mes
- [ ] Eliminar VMs apagadas
- [ ] Iniciar Ola 0 (piloto)
- [ ] Planificar compra de RIs

### Próximos 3 Meses
- [ ] Completar Olas 0-1
- [ ] Comprar primeras RIs
- [ ] Implementar Spot para dev/test
- [ ] Iniciar auto scaling en 1-2 apps

---

## 💡 Recomendaciones Finales

### Prioridad Alta
1. ✅ **Eliminar VMs apagadas** (ahorro inmediato)
2. ✅ **Comprar Reserved Instances** (40% ahorro)
3. ✅ **Upgrade Windows 2003/2008** (seguridad crítica)

### Prioridad Media
4. ✅ **Implementar Auto Scaling** (25% ahorro adicional)
5. ✅ **Spot Instances para dev/test** (70% ahorro en esos ambientes)

### Prioridad Baja
6. ✅ **Migrar a servicios managed** (largo plazo, alto impacto)
7. ✅ **Refactoring a serverless** (modernización gradual)

---

**Archivos Relacionados:**
- `05_estrategia_7rs.csv` - Clasificación detallada por VM
- `05_optimizaciones_costos.json` - Datos de optimizaciones

**Última actualización**: 2025-12-01
