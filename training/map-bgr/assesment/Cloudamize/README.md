# Cloudamize Assessment - Proyecto MAP-BGR

Datos de assessment de Cloudamize para el proyecto de migración BGR.

---

## 📁 Archivos Disponibles

### 1. Observed Infrastructure
**Archivo**: `Observed-Infrastructure.xlsx`  
**Descripción**: Métricas observadas de infraestructura (CPU, RAM, Storage, Network)  
**Período**: Datos recolectados durante el assessment  
**Servidores**: 122

**CSVs Generados**:
- `Compute.csv` - 122 servidores
- `Storage.csv` - 470 discos
- `Network.csv` - 122 interfaces

**Resumen**: Ver `RESUMEN_CLOUDAMIZE.md`

---

### 2. Migration Planner - Server Applications
**Archivo**: `MigrationPlanner-Server-Applications.xlsx`  
**Descripción**: Mapeo de servidores, procesos, aplicaciones y estrategias de migración  
**Registros**: 3,441 procesos/servicios  
**Servidores**: 122

**CSVs Generados**:
- `Server_Applications.csv` - 3,441 registros

**Resumen**: Ver `RESUMEN_MIGRATION_PLANNER.md`

---

## 🔧 Conversión a CSV

### Usando la tool general
```bash
# Observed Infrastructure
python3 tools/cloudamize_to_csv.py Observed-Infrastructure.xlsx

# Migration Planner
python3 tools/cloudamize_to_csv.py MigrationPlanner-Server-Applications.xlsx
```

### Usando parsers específicos
```bash
# Observed Infrastructure
python3 parsers/cloudamize/observed_infrastructure_parser.py \
  Observed-Infrastructure.xlsx \
  Observed-Infrastructure_csv/

# Migration Planner
python3 parsers/cloudamize/migration_planner_parser.py \
  MigrationPlanner-Server-Applications.xlsx \
  MigrationPlanner_csv/
```

---

## 📊 Análisis Rápido

### Observed Infrastructure
```bash
python3 examples/analyze_cloudamize.py Observed-Infrastructure_csv/
```

**Métricas**:
- 122 servidores
- 852 vCPUs totales
- 2,930 GB RAM total
- 59% utilización promedio CPU
- 104 TB capacidad storage
- 51 TB/mes tráfico de red

### Migration Planner
```bash
python3 examples/analyze_migration_planner.py \
  MigrationPlanner_csv/Server_Applications.csv
```

**Insights**:
- 3,441 procesos identificados
- Todos en Wave "Backlog"
- Estrategia inicial: Rehost
- Top assets: Security (36 servers), Workload Mgmt (31 servers)
- Trend Micro + Rapid7 en ~93% servidores

---

## 🔗 Correlación de Datos

### Observed Infrastructure vs Migration Planner

| Aspecto | Observed Infrastructure | Migration Planner |
|---------|------------------------|-------------------|
| **Propósito** | Métricas de performance | Planificación de migración |
| **Datos** | CPU, RAM, IOPS, Network | Procesos, Apps, Estrategias |
| **Uso** | Rightsizing de instancias | Definición de waves |
| **Servidores** | 122 | 122 |
| **Granularidad** | Por servidor | Por proceso |

**Complementariedad**:
- Observed Infrastructure → **Dimensionamiento** (¿qué tamaño de instancia?)
- Migration Planner → **Estrategia** (¿cómo migrar? ¿cuándo?)

---

## 💡 Insights Clave del Assessment

### Infraestructura
- ✅ 122 servidores bien monitoreados
- ✅ Utilización promedio 59% CPU (oportunidad de rightsizing)
- ✅ 44% ocupación de storage (bien dimensionado)
- ⚠️ 261 servidores adicionales en RVTools no monitoreados por Cloudamize

### Seguridad y Monitoreo
- ✅ Trend Micro desplegado en 93% de servidores
- ✅ Rapid7 Insight Agent en 92%
- ✅ Dynatrace APM en 92%
- ✅ Infraestructura enterprise-grade

### Planificación de Migración
- ⚠️ Todos los servidores en "Backlog" - sin waves definidas
- ⚠️ Estrategia inicial "Rehost" para todos - sin análisis de modernización
- ⚠️ No hay mapeo de Business Applications
- 🔄 Requiere análisis adicional para optimizar estrategia

---

## 🎯 Recomendaciones

### Inmediatas
1. **Mapear Business Applications** manualmente
2. **Definir waves** de migración basadas en:
   - Dependencias entre servidores
   - Criticidad de aplicaciones
   - Complejidad técnica
3. **Correlacionar** con datos de RVTools (383 VMs vs 122 monitoreadas)

### Análisis Adicional
1. **Evaluar estrategias alternativas**:
   - Bases de datos → RDS (Replatform)
   - Aplicaciones web → ECS/Fargate (Refactor)
   - Servicios legacy → Modernización
2. **Rightsizing** basado en utilización real:
   - CPU promedio 59% → oportunidad de optimización
   - Memoria peak vs provisioned
3. **Análisis de costos** con datos reales de utilización

---

## 📁 Estructura de Archivos

```
Cloudamize/
├── README.md                                    # Este archivo
├── RESUMEN_CLOUDAMIZE.md                       # Resumen Observed Infrastructure
├── RESUMEN_MIGRATION_PLANNER.md                # Resumen Migration Planner
├── Observed-Infrastructure.xlsx                # Original
├── MigrationPlanner-Server-Applications.xlsx   # Original
├── Observed-Infrastructure_csv/                # CSVs generados
│   ├── Compute.csv
│   ├── Storage.csv
│   └── Network.csv
└── MigrationPlanner_csv/                       # CSVs generados
    └── Server_Applications.csv
```

---

**Última actualización**: 2025-12-02  
**Assessment realizado por**: Cloudamize  
**Proyecto**: MAP-BGR - Migración a AWS
