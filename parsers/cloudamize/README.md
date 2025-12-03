# Cloudamize Parsers

Parsers para diferentes archivos de Cloudamize OLA (Online Assessment).

## Parsers Disponibles

### 1. Observed Infrastructure Parser
**Archivo**: `observed_infrastructure_parser.py`  
**Input**: `Observed-Infrastructure.xlsx`  
**Output**: 3 archivos CSV

#### Pestañas Procesadas
- **Compute** - Información de servidores (CPU, RAM, OS)
- **Storage** - Información de almacenamiento
- **Network** - Información de red

#### Uso
```bash
python3 parsers/cloudamize/observed_infrastructure_parser.py <archivo.xlsx> [output_dir]
```

#### Datos Extraídos (Compute)
- Group Name, Asset, Server Name, IP Address
- OS / OS Version
- MS SQL Edition / SQL Version
- On Time (%), Observed vCPU
- Current CPU Utilization (%)
- Observed Memory Provisioned (GB)
- Peak Memory Used (GB)

---

### 2. Migration Planner Parser ⭐ NUEVO
**Archivo**: `migration_planner_parser.py`  
**Input**: `MigrationPlanner-Server-Applications.xlsx`  
**Output**: 1 archivo CSV

#### Pestañas Procesadas
- **Server Applications** - Mapeo de servidores, procesos y aplicaciones

#### Uso
```bash
python3 parsers/cloudamize/migration_planner_parser.py <archivo.xlsx> [output_dir]
```

#### Datos Extraídos
- Server Group, Server Asset
- Server Machine, Server IP
- Server Process
- Wave (ola de migración)
- Migration Strategy (7R's)
- Business Application

#### Análisis Disponible
```bash
python3 examples/analyze_migration_planner.py <Server_Applications.csv>
```

**Output del análisis**:
- Resumen general (servidores únicos, registros)
- Análisis por Wave
- Estrategias de migración (7R's)
- Aplicaciones de negocio
- Tipos de Asset
- Top procesos más comunes

---

## Próximos Parsers

- [ ] Application Dependencies Parser
- [ ] Cost Analysis Parser
- [ ] Performance Metrics Parser
- [ ] Migration Recommendations Parser

## Notas

- Los parsers usan solo librerías estándar de Python (no requieren pandas/openpyxl)
- Procesan archivos .xlsx usando zipfile y xml.etree
- Generan CSVs limpios para análisis posterior
