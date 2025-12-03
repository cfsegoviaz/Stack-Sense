# Stack Sense - Guía de Herramientas

Guía rápida de uso de las herramientas disponibles en Stack Sense.

## 🔧 Herramientas de Conversión

### 1. RVTools to CSV
Convierte exports de VMware RVTools a archivos CSV.

```bash
python3 tools/rvtools_to_csv.py <archivo.xlsm> [output_dir]
```

**Ejemplo**:
```bash
python3 tools/rvtools_to_csv.py data/RVTools_export.xlsm
# Genera: data/RVTools_export_csv/
```

---

### 2. Cloudamize to CSV ⭐ NUEVO
Convierte exports de Cloudamize a archivos CSV.

```bash
python3 tools/cloudamize_to_csv.py <archivo.xlsx> [output_dir]
```

**Ejemplos**:
```bash
# Observed Infrastructure
python3 tools/cloudamize_to_csv.py Observed-Infrastructure.xlsx

# Con directorio personalizado
python3 tools/cloudamize_to_csv.py Observed-Infrastructure.xlsx output/

# Resultado:
# - Compute.csv (servidores)
# - Storage.csv (discos)
# - Network.csv (interfaces)
```

**Características**:
- ✅ Sin dependencias externas (solo stdlib)
- ✅ Rápido y eficiente
- ✅ Maneja archivos grandes
- ✅ Soporta cualquier archivo Excel de Cloudamize

---

## 📊 Scripts de Análisis

### 1. Analizar RVTools
```bash
python3 examples/analyze_rvtools.py data/RVTools_export.xlsx
```

### 2. Analizar Cloudamize Observed Infrastructure ⭐
```bash
python3 examples/analyze_cloudamize.py data/Observed-Infrastructure_csv/
```

**Output**:
```
📊 COMPUTE ANALYSIS
- Total Servers
- Total vCPUs
- Total Memory
- Avg CPU Utilization
- OS Distribution

💾 STORAGE ANALYSIS
- Total Disks
- Total Capacity
- Total Used (%)
- Total Peak IOPS

🌐 NETWORK ANALYSIS
- Total Interfaces
- Total Outbound/Inbound
- Total Traffic
```

### 3. Analizar Cloudamize Migration Planner ⭐ NUEVO
```bash
python3 examples/analyze_migration_planner.py data/MigrationPlanner_csv/Server_Applications.csv
```

**Output**:
```
📊 RESUMEN GENERAL
- Total Registros
- Servidores Únicos

🌊 ANÁLISIS POR WAVE
- Distribución por olas

🎯 ESTRATEGIAS DE MIGRACIÓN (7R's)
- Rehost, Replatform, etc.

💼 APLICACIONES DE NEGOCIO
- Mapeo de aplicaciones

🏷️ TIPOS DE ASSET
- Categorización de servicios

⚙️ TOP PROCESOS
- Procesos más comunes
```

---

## 🚀 Workflow Completo

### Para Proyecto MAP-BGR

1. **Convertir RVTools**:
```bash
python3 tools/rvtools_to_csv.py \
  training/map-bgr/RVTools_export.xlsm \
  training/map-bgr/assesment/RVTools_csv/
```

2. **Convertir Cloudamize Observed Infrastructure**:
```bash
python3 tools/cloudamize_to_csv.py \
  training/map-bgr/assesment/Cloudamize/Observed-Infrastructure.xlsx \
  training/map-bgr/assesment/Cloudamize/Observed-Infrastructure_csv/
```

3. **Convertir Cloudamize Migration Planner**:
```bash
python3 tools/cloudamize_to_csv.py \
  training/map-bgr/assesment/Cloudamize/MigrationPlanner-Server-Applications.xlsx \
  training/map-bgr/assesment/Cloudamize/MigrationPlanner_csv/
```

4. **Analizar datos**:
```bash
# RVTools
python3 examples/analyze_rvtools.py \
  training/map-bgr/assesment/RVTools_csv/

# Cloudamize Observed Infrastructure
python3 examples/analyze_cloudamize.py \
  training/map-bgr/assesment/Cloudamize/Observed-Infrastructure_csv/

# Cloudamize Migration Planner
python3 examples/analyze_migration_planner.py \
  training/map-bgr/assesment/Cloudamize/MigrationPlanner_csv/Server_Applications.csv
```

---

## 💡 Tips y Mejores Prácticas

### Conversión de Archivos
- Si no especificas `output_dir`, se crea automáticamente con sufijo `_csv`
- Los nombres de archivos se sanitizan (espacios → `_`)
- Todos los CSVs usan encoding UTF-8

### Análisis de Datos
- Los CSVs de Cloudamize tienen 2 filas de headers (se manejan automáticamente)
- Los scripts de análisis son ejemplos - personalízalos según necesites
- Usa los CSVs generados con cualquier herramienta (Excel, pandas, SQL, etc.)

### Performance
- `cloudamize_to_csv.py` es más rápido que `rvtools_to_csv.py` (no usa pandas)
- Para archivos muy grandes (>100MB), considera procesar por partes
- Los CSVs ocupan menos espacio que los Excel originales

---

## 🔮 Próximas Herramientas

- [ ] `matilda_to_csv.py` - Parser para Matilda
- [ ] `merge_sources.py` - Combinar RVTools + Cloudamize
- [ ] `validate_data.py` - Validación de datos
- [ ] `generate_report.py` - Reportes automáticos

---

## 📚 Documentación Adicional

- **Tools README**: `tools/README.md`
- **Parsers README**: `parsers/cloudamize/README.md`
- **Examples**: `examples/`

---

**Última actualización**: 2025-12-02
