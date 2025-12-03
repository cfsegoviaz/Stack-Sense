# Resumen Cloudamize - Migration Planner

**Fecha de extracción**: 2025-12-02  
**Archivo fuente**: `MigrationPlanner-Server-Applications.xlsx`  
**Parser utilizado**: `parsers/cloudamize/migration_planner_parser.py`

---

## 📊 Datos Extraídos

### Server Applications (3,441 registros)
**Archivo**: `Server_Applications.csv`

**Columnas**:
- Server Group
- Server Asset
- Server Machine
- Server IP
- Server Process
- Wave
- Migration Strategy
- Business Application

---

## 🔍 Análisis Clave

### Resumen General
- **Total Registros**: 3,441 procesos/servicios
- **Servidores Únicos**: 122 servidores
- **Promedio**: ~28 procesos por servidor

### 🌊 Waves de Migración
| Wave | Servidores | Procesos |
|------|------------|----------|
| Backlog | 122 | 3,441 |

**Nota**: Todos los servidores están en Backlog - pendiente de planificación

---

### 🎯 Estrategias de Migración (7R's)
| Estrategia | Servidores | Procesos |
|------------|------------|----------|
| Rehost | 122 | 3,441 |

**Nota**: Estrategia inicial es Rehost (Lift & Shift) para todos

---

### 🏷️ Tipos de Asset (Top 5)

| Asset Type | Servidores | Procesos |
|------------|------------|----------|
| Identity and Access Management; Computer Security | 36 | 1,085 |
| Computing Workload Management | 31 | 940 |
| Software Component and API | 16 | 459 |
| Database | 12 | 250 |
| Software framework | 9 | 193 |

---

### ⚙️ Top 10 Procesos Más Comunes

| Proceso | Instancias |
|---------|------------|
| Web App (Web Services-Management) | 122 |
| Microsoft Windows Operating System | 122 |
| Trend Micro Anti-Malware Solution Platform | 115 |
| Insight Agent | 113 |
| Trend Micro Endpoint Basecamp | 113 |
| rapid7_agent_core.exe | 112 |
| rapid7_endpoint_broker.exe | 112 |
| Dynatrace | 112 |
| Trend Micro Deep Security Agent | 112 |
| Trend Micro Cloud Endpoint | 111 |

---

## 💡 Insights Clave

### Seguridad y Monitoreo
- ✅ **Trend Micro** desplegado en ~93% de servidores
- ✅ **Rapid7 Insight Agent** en ~92% de servidores
- ✅ **Dynatrace** para APM en ~92% de servidores
- ✅ Infraestructura bien monitoreada y protegida

### Aplicaciones de Negocio
- ⚠️ **No hay mapeo** de Business Applications
- ⚠️ Todos los registros muestran "-" en Business Application
- 🔄 Requiere mapeo manual o análisis adicional

### Estado de Planificación
- ⚠️ Todos en **Backlog** - sin waves definidas
- ⚠️ Todos con estrategia **Rehost** - sin análisis de modernización
- 🔄 Requiere análisis detallado para:
  - Definir waves de migración
  - Evaluar estrategias alternativas (Replatform, Refactor)
  - Mapear aplicaciones de negocio

---

## 🔗 Correlación con Otros Datos

### vs Observed Infrastructure
| Métrica | Observed Infra | Migration Planner |
|---------|----------------|-------------------|
| Servidores | 122 | 122 |
| Datos | Métricas de performance | Procesos y aplicaciones |
| Uso | Rightsizing | Planificación de migración |

**Complementariedad**:
- Observed Infrastructure → **QUÉ** migrar (specs, utilización)
- Migration Planner → **CÓMO** migrar (estrategia, waves, apps)

---

## 🎯 Próximos Pasos

1. ✅ Parser creado y funcionando
2. ⏭️ Mapear Business Applications manualmente
3. ⏭️ Definir waves de migración basadas en:
   - Dependencias entre servidores
   - Criticidad de aplicaciones
   - Complejidad técnica
4. ⏭️ Evaluar estrategias alternativas a Rehost:
   - Bases de datos → RDS (Replatform)
   - Aplicaciones web → ECS/Fargate (Refactor)
   - Servicios legacy → Modernización
5. ⏭️ Correlacionar con datos de RVTools
6. ⏭️ Generar plan de migración detallado

---

## 📁 Ubicación de Archivos

```
training/map-bgr/assesment/Cloudamize/
├── MigrationPlanner-Server-Applications.xlsx    # Original
└── MigrationPlanner_csv/                        # CSVs generados
    └── Server_Applications.csv                  # 3,441 registros
```

---

## 🔧 Herramientas

**Conversión**:
```bash
python3 tools/cloudamize_to_csv.py MigrationPlanner-Server-Applications.xlsx
```

**Análisis**:
```bash
python3 examples/analyze_migration_planner.py MigrationPlanner_csv/Server_Applications.csv
```

---

**Última actualización**: 2025-12-02
