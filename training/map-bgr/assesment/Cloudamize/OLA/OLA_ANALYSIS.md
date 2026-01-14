# OLA (Optimization and Licensing Assessment) - BGR

## 📋 Resumen Ejecutivo

**Cliente:** Banco General Rumiñahui S.A.  
**Fecha Assessment:** 29 de Octubre, 2025  
**Período de Recolección:** 15-26 de Octubre, 2025 (11 días)  
**Equipo:** Cloudamize TAM (Nick Nendel), AWS OLA EM (Valerie Rosenfield), Escala24x7

---

## 🖥️ Infraestructura Evaluada

| Métrica | Valor |
|---------|-------|
| **Servidores Totales** | 122 |
| **Windows Servers** | 122 |
| **Linux Servers** | 0 |
| **Almacenamiento Total** | 101.8 TB |
| **Almacenamiento Utilizado** | 44.7 TB (44%) |
| **Aplicaciones Descubiertas** | 848 |
| **Servidores Zombie** | 3 |

### SQL Server Overview

| Edición | Cantidad | Cores On-Prem | Cores AWS Optimizado |
|---------|----------|---------------|----------------------|
| Enterprise | 16 | 184 | 126 |
| Standard | 18 | 146 | 86 |
| **Total** | **34** | **330** | **212** |

**Reducción de Cores SQL:** 118 cores (36% menos)

---

## 💰 Análisis Financiero

### Comparativa de Costos Anuales

| Escenario | Costo Anual | Ahorro vs Lift & Shift |
|-----------|-------------|------------------------|
| **Lift & Shift (On-Demand)** | $883K | - |
| **Right-Sized (On-Demand)** | $514K | 42% |
| **1-Year RI (No Upfront)** | $433K | 51% |
| **3-Year RI (No Upfront)** | $380K | **57%** |

### Desglose de Costos (Right-Sized)

| Componente | Lift & Shift | Optimizado | Ahorro |
|------------|--------------|------------|--------|
| Compute | $707K | $272K | 62% |
| Storage | $125K | $58K | 54% |
| Network | $51K | $51K | 0% |

### Opciones de Licenciamiento SQL

| Modelo | Costo Anual | Ahorro Total |
|--------|-------------|--------------|
| **SQL BYOL** | $380K | $503K (57%) |
| **SQL License Included** | $941K | $503K (35%) |

---

## 📊 Optimización de Infraestructura

### Restricciones de Sizing

| Tipo de Restricción | Servidores |
|---------------------|------------|
| CPU Constrained | 42 |
| Memory Constrained | 72 |
| CPU & Memory | 0 |

### Reducción de Almacenamiento

- **Capacidad Total:** 101.8 TB
- **Ocupación Real:** 44.7 TB
- **Recomendado AWS:** 45.0 TB
- **Reducción:** 56%

### Oportunidad FSx

| Componente | Costo Actual | Con FSx | Ahorro |
|------------|--------------|---------|--------|
| EC2 Compute | $6K | - | - |
| EC2 Storage | $9K | - | - |
| FSx (2 shares) | - | $10K | - |
| **Total** | $15K | $10K | **33%** |

---

## ⚠️ End-of-Life (EOL) Assessment

### Windows Server

| Versión | Cantidad | Estado | Fin Soporte Ext. | Riesgo |
|---------|----------|--------|------------------|--------|
| ≤ 2012 R2 | 12 | ❌ Sin Soporte | Oct 2023 | 🔴 Alto |
| 2016 | 64 | ⚠️ Soporte Extendido | Ene 2027 | 🟡 Medio |
| 2019 | 27 | ⚠️ Soporte Extendido | Ene 2029 | 🟡 Medio |
| 2022 | 18 | ✅ Soportado | Oct 2031 | 🟢 Bajo |
| 2025 | 1 | ✅ Soportado | Oct 2034 | 🟢 Bajo |

### SQL Server

| Versión | Cantidad | Estado | Fin Soporte Ext. | Riesgo |
|---------|----------|--------|------------------|--------|
| ≤ 2014 | 5 | ❌ Sin Soporte | Jul 2024 | 🔴 Alto |
| 2016 | 16 | ⚠️ Soporte Extendido | Jul 2026 | 🟡 Medio |
| 2019 | 6 | ⚠️ Soporte Extendido | Ene 2030 | 🟡 Medio |
| 2022 | 7 | ✅ Soportado | Ene 2033 | 🟢 Bajo |

### Resumen EOL

| Categoría | Servidores | % del Total |
|-----------|------------|-------------|
| 🔴 Riesgo Alto (Sin Soporte) | 17 | 14% |
| 🟡 Riesgo Medio (Soporte Extendido) | 113 | 93% |
| 🟢 Riesgo Bajo (Soportado) | 26 | 21% |

---

## 💡 Oportunidades de Ahorro SQL

### BYOL (Bring Your Own License)

| Métrica | Standard | Enterprise | Total |
|---------|----------|------------|-------|
| Ahorro SA Anual | $22K | $81K | **$103K** |
| Valor Licencias Reutilizables (MSRP) | $118K | $439K | **$557K** |

### License Included

| Métrica | Standard | Enterprise | Total |
|---------|----------|------------|-------|
| Ahorro por Right-Sizing | $13K | $66K | **$78K** |

---

## 🔄 Opciones de Modernización

### RDS como Alternativa

| Métrica | Standard | Enterprise | Total |
|---------|----------|------------|-------|
| Servidores | 18 | 16 | 34 |
| Costo EC2 | $202K | $606K | $808K |
| Costo RDS | $292K | $1M | $1.3M |

**Nota:** RDS tiene mayor costo pero ofrece:
- Gestión automatizada
- Alta disponibilidad
- Backups automáticos
- Patching automático

### Servidores Zombie

| Métrica | Valor |
|---------|-------|
| Servidores < 20% uso | 3 |
| Ahorro Potencial | $4K/año |

---

## 📈 Savings Plan Comparison

| Plan | Ahorro Adicional |
|------|------------------|
| 1 YR NURI | $81K |
| 1 YR AURI | $91K |
| 3 YR NURI | $133K |
| 3 YR AURI | $147K |

---

## ✅ Recomendaciones Escala24x7

### Prioridad Alta (Inmediato)
1. **Migrar servidores EOL** - 17 servidores sin soporte (Windows ≤2012 R2, SQL ≤2014)
2. **Implementar Right-Sizing** - Ahorro inmediato de 42%
3. **Optimizar cores SQL** - Reducción de 330 a 212 cores

### Prioridad Media (3-6 meses)
4. **Evaluar BYOL vs License Included** - Decisión basada en contratos Microsoft existentes
5. **Consolidar File Servers con FSx** - 33% ahorro en 2 servidores
6. **Eliminar servidores Zombie** - $4K ahorro anual

### Prioridad Baja (6-12 meses)
7. **Evaluar RDS para SQL críticos** - Mayor costo pero menor gestión
8. **Implementar Savings Plans 3YR** - 57% ahorro total
9. **Considerar Graviton** - No aplica (0 servidores Linux)

---

## 📊 Resumen de Ahorros

| Categoría | Ahorro Anual |
|-----------|--------------|
| Infrastructure Right-Sizing | $370K |
| SQL Core Optimization | $103K (BYOL) |
| Savings Plan 3YR NURI | $133K |
| FSx Migration | $5K |
| Zombie Servers | $4K |
| **Total Potencial** | **$615K** |

### ROI Proyectado

- **Costo Actual Estimado:** $883K/año
- **Costo Optimizado AWS:** $380K/año
- **Ahorro Anual:** $503K (57%)
- **Ahorro 3 Años:** $1.5M

---

## 📎 Anexos

- [Cloudamize Assessment Summary PDF](./Cloudamize_Assessment_Summary.pdf)
- [Observed Infrastructure Excel](../Observed-Infrastructure.xlsx)
- [Detailed Server List](../server-inventory.xlsx)

---

*Documento generado por Escala24x7 como parte del proyecto MAP-BGR*
