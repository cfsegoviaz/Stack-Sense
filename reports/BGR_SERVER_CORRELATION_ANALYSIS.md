# Análisis de Correlación: RVTools vs Cloudamize (OLA)
## Banco General Rumiñahui - MAP-BGR
**Fecha:** 2026-01-08

---

## Resumen Ejecutivo

Este análisis correlaciona los datos de descubrimiento de VMware (RVTools) con el escaneo de Cloudamize (OLA) para identificar la cobertura real del assessment y los servidores por ambiente.

### Fuentes de Datos
| Fuente | Archivo | Descripción |
|--------|---------|-------------|
| RVTools | vInfo.csv | Export de VMware vSphere - 383 VMs |
| Cloudamize | Compute.csv | Observed Infrastructure - 122 servidores |

---

## Inventario Total

### RVTools (VMware)
| Métrica | Cantidad |
|---------|----------|
| Total VMs | 383 |
| PoweredOn | 350 |
| PoweredOff | 33 |

### Cloudamize (OLA)
| Métrica | Cantidad |
|---------|----------|
| Total Servidores | 122 |
| Con SQL Server | 36 |
| SQL Enterprise | 16 |
| SQL Standard | 18 |
| SQL Express | 2 |

---

## Correlación de Servidores

| Categoría | Cantidad | Descripción |
|-----------|----------|-------------|
| En ambos sistemas | 109 | Servidores con agente Cloudamize instalado |
| Solo en RVTools | 274 | VMs sin agente Cloudamize |
| Solo en Cloudamize | 13 | Servidores físicos o externos |

### Servidores Físicos (Solo en Cloudamize)
Estos 13 servidores fueron detectados por Cloudamize pero no existen en VMware, indicando que son servidores físicos:

1. ECBRPRAP26
2. ECBRPRAP27
3. ECBRPRAP28
4. ECBRPRAP29
5. ECBRPRAP4
6. ECBRPRB01
7. ECBRPRDP1
8. ECBRPRH04
9. ECBRPRQ73
10. ECBRPRQ74
11. ECBRPRSF1
12. ECBRPRW92
13. ECBRPRW93

---

## Distribución por Ambiente

### Convención de Nombres BGR
- **ECBRPR*** = Producción
- **ECBRTS*** = Testing
- **ECBRDR*** / **XDR** = DR/Backup
- **ECBRDV*** = Desarrollo

### RVTools por Ambiente

| Ambiente | Total | PoweredOn | PoweredOff |
|----------|-------|-----------|------------|
| Producción | 215 | 205 | 10 |
| Testing | 105 | 105 | 0 |
| POC/Piloto | 1 | 1 | 0 |
| No clasificado | 62 | 39 | 23 |
| **TOTAL** | **383** | **350** | **33** |

### Cloudamize por Ambiente

| Ambiente | Servidores | % del Total |
|----------|------------|-------------|
| Producción | 122 | 100% |
| Testing | 0 | 0% |
| Otros | 0 | 0% |
| **TOTAL** | **122** | **100%** |

### Servidores No Escaneados por Cloudamize

| Ambiente | PoweredOn | PoweredOff | Total |
|----------|-----------|------------|-------|
| Producción | 96 | 10 | 106 |
| Testing | 105 | 0 | 105 |
| No clasificado | 40 | 23 | 63 |
| **TOTAL** | **241** | **33** | **274** |

---

## Cobertura del Assessment

### Por Ambiente
| Ambiente | Total VMs | Escaneados | Cobertura |
|----------|-----------|------------|-----------|
| Producción | 215 | 109 | 51% |
| Testing | 105 | 0 | 0% |
| Otros | 63 | 0 | 0% |
| **TOTAL** | **383** | **109** | **28%** |

### Análisis de Cobertura
- **Producción**: Solo 51% de los servidores de producción fueron escaneados por Cloudamize
- **Testing**: 0% de cobertura - ningún servidor de testing tiene agente
- **Servidores físicos**: 13 servidores adicionales detectados fuera de VMware

---

## Sistemas Operativos (Cloudamize)

| Sistema Operativo | Cantidad |
|-------------------|----------|
| Windows | 88 |
| Windows (MS SQL Standard) | 18 |
| Windows (MS SQL Enterprise) | 16 |
| **TOTAL** | **122** |

---

## SQL Server (Cloudamize)

| Edición | Cantidad | Implicación de Licenciamiento |
|---------|----------|-------------------------------|
| SQL Enterprise | 16 | Alto costo - candidatos a Aurora/Babelfish |
| SQL Standard | 18 | Costo medio - evaluar RDS SQL o Aurora |
| SQL Express | 2 | Sin costo de licencia |
| **TOTAL** | **36** | |

---

## Hallazgos Clave

### ⚠️ Gaps Identificados

1. **Cobertura limitada de Cloudamize**
   - Solo 28% del total de VMs fueron escaneados
   - 51% de producción escaneado
   - 0% de testing escaneado

2. **Servidores de Testing sin assessment**
   - 105 servidores de testing no tienen datos de utilización
   - Recomendación: Instalar agente Cloudamize o usar datos de RVTools

3. **Servidores físicos no virtualizados**
   - 13 servidores físicos identificados
   - Requieren estrategia de migración específica (P2V o directo a AWS)

### ✅ Datos Confiables

1. **122 servidores con métricas de utilización**
   - CPU, memoria, storage observados
   - Datos de SQL Server y versiones de OS

2. **36 servidores SQL identificados**
   - Oportunidad de optimización de licencias
   - 16 Enterprise → candidatos a Aurora PostgreSQL + Babelfish

---

## Recomendaciones

### Corto Plazo
1. Completar instalación de agente Cloudamize en servidores de Testing
2. Validar si los 13 servidores físicos están en scope de migración
3. Documentar servidores PoweredOff (33) - ¿candidatos a decomisión?

### Para el Assessment
1. Usar datos de Cloudamize para los 122 servidores escaneados
2. Usar datos de RVTools (vCPU, vMemory) para los 274 no escaneados
3. Aplicar factor de utilización estimado (70%) para servidores sin métricas

### Para Licenciamiento SQL
1. Priorizar migración de 16 servidores SQL Enterprise a Aurora
2. Evaluar SQL Standard para RDS SQL Server o Aurora
3. Mantener SQL Express en RDS SQL Express o migrar a PostgreSQL

---

## Anexos

### Metodología
- RVTools export: vInfo.csv con 383 registros
- Cloudamize export: Compute.csv con 122 registros
- Correlación por nombre de servidor (case-insensitive)
- Clasificación de ambiente por patrón de nomenclatura BGR

### Archivos Fuente
- `/training/map-bgr/assesment/RVTools/vInfo.csv`
- `/training/map-bgr/assesment/Cloudamize/Observed-Infrastructure_csv/Compute.csv`
