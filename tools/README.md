# Stack Sense Tools

Herramientas de conversión y utilidades para análisis de migraciones AWS.

## 🛠️ Herramientas Disponibles

### 1. RVTools to CSV
**Archivo**: `rvtools_to_csv.py`  
**Propósito**: Convierte exports de RVTools (XLSM/XLSX) a archivos CSV

**Uso**:
```bash
python3 tools/rvtools_to_csv.py <archivo.xlsm> [output_dir]
```

**Ejemplo**:
```bash
python3 tools/rvtools_to_csv.py data/RVTools_export.xlsm
python3 tools/rvtools_to_csv.py data/RVTools_export.xlsm output/rvtools_csv/
```

**Dependencias**: pandas, openpyxl

---

### 2. Cloudamize to CSV
**Archivo**: `cloudamize_to_csv.py`  
**Propósito**: Convierte exports de Cloudamize (XLSX) a archivos CSV

**Uso**:
```bash
python3 tools/cloudamize_to_csv.py <archivo.xlsx> [output_dir]
```

**Ejemplos**:
```bash
# Observed Infrastructure
python3 tools/cloudamize_to_csv.py Observed-Infrastructure.xlsx

# Con directorio personalizado
python3 tools/cloudamize_to_csv.py Observed-Infrastructure.xlsx output/cloudamize/

# Otros archivos de Cloudamize
python3 tools/cloudamize_to_csv.py Application-Dependencies.xlsx
python3 tools/cloudamize_to_csv.py Cost-Analysis.xlsx
```

**Dependencias**: Solo librerías estándar de Python (zipfile, xml)

---

## 📋 Comparación de Tools

| Feature | rvtools_to_csv | cloudamize_to_csv |
|---------|----------------|-------------------|
| Input | XLSM/XLSX | XLSX |
| Dependencias | pandas, openpyxl | stdlib only |
| Velocidad | Rápido | Muy rápido |
| Memoria | Media | Baja |
| Archivos grandes | ✅ | ✅ |

---

## 🚀 Uso en Proyectos

### Proyecto MAP-BGR
```bash
# RVTools
python3 tools/rvtools_to_csv.py \
  training/map-bgr/RVTools_export.xlsm \
  training/map-bgr/assesment/RVTools_csv/

# Cloudamize
python3 tools/cloudamize_to_csv.py \
  training/map-bgr/assesment/Cloudamize/Observed-Infrastructure.xlsx \
  training/map-bgr/assesment/Cloudamize/Observed-Infrastructure_csv/
```

---

## 💡 Tips

1. **Sin directorio de salida**: Se crea automáticamente con sufijo `_csv`
2. **Nombres seguros**: Los espacios y caracteres especiales se reemplazan con `_`
3. **Encoding**: Todos los CSVs se generan en UTF-8
4. **Filas vacías**: Se omiten automáticamente

---

## 🔮 Próximas Tools

- [ ] `matilda_to_csv.py` - Parser para Matilda
- [ ] `csv_analyzer.py` - Análisis rápido de CSVs
- [ ] `merge_sources.py` - Combinar datos de múltiples fuentes
- [ ] `validate_data.py` - Validación de datos extraídos
