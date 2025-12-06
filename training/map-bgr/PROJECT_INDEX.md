# MAP-BGR - Índice Maestro del Proyecto
## Migration Acceleration Program - Banco General de Ruritania

**Cliente**: Banco General de Ruritania  
**Proyecto**: MAP-BGR  
**Total VMs**: 383  
**Total Aplicaciones**: 8  
**Fecha Inicio**: 2025-12-01

---

## 📁 Estructura del Proyecto

```
map-bgr/
│
├── 📄 PROJECT_INDEX.md              # Este archivo (índice maestro)
├── 📄 README.md                     # README principal del proyecto
│
├── 📁 project-management/           # Gestión del proyecto
│   ├── planning/                    # Planes de migración
│   │   └── PLAN_MIGRACION.md
│   ├── progress/                    # Seguimiento de progreso
│   │   └── PROGRESS.md
│   └── costs/                       # Calculadoras de costos
│       ├── EBA_COST_CALCULATOR.csv
│       └── EBA_COST_CALCULATOR_UPDATED.csv
│
├── 📁 applications/                 # Información de aplicaciones
│   ├── raw-data/                    # Datos originales (HTML exports)
│   │   ├── G.I.-Api Portal.html
│   │   ├── G.I.-Saras.html
│   │   ├── G.I.-Sonar Qube.html
│   │   ├── G.I.-Seq.html
│   │   ├── G.I.-Backoffice Sistemas.html
│   │   ├── G.I-PortalGuiaBGR.html
│   │   └── G.I-PortalAdmBGR.html
│   └── analysis/                    # Análisis de aplicaciones
│
├── 📁 modernization-proposals/      # Propuestas de modernización
│   ├── README.md                    # Resumen de propuestas
│   ├── INDEX.md                     # Índice de navegación
│   ├── GETTING_STARTED.md          # Guía de uso
│   ├── saras/                       # Propuesta SARAS
│   ├── api-portal/                  # Propuesta Api Portal
│   ├── backoffice-sistemas/         # Propuesta Backoffice
│   ├── sonarqube/                   # Propuesta SonarQube
│   └── templates/                   # Templates reutilizables
│
├── 📁 documentation/                # Documentación técnica
│   ├── eba-plans/                   # Planes EBA
│   │   ├── EBA_README.md
│   │   ├── EBA_PLAN.md
│   │   ├── EBA_PLAN_BABELFISH.md
│   │   └── EBA_PLAN_CONTAINERS.md
│   └── sql-analysis/                # Análisis de SQL Server
│       └── SQL_SERVER_ANALYSIS.md
│
├── 📁 assesment/                    # Assessment data
│   ├── Cloudamize/                  # Datos de Cloudamize
│   └── RVTools_export_all_*.xlsm   # Exports de RVTools
│
├── 📁 diagrams/                     # Diagramas originales
│   └── *.png                        # Diagramas de arquitectura
│
├── 📁 generated-diagrams/           # Diagramas generados
│   └── *.png                        # Diagramas auto-generados
│
├── 📁 reports/                      # Reportes del proyecto
│   ├── 01_executive_summary/
│   ├── 02_technical_analysis/
│   ├── 03_migration_strategy/
│   ├── 04_cost_analysis/
│   └── 05_architectures/
│
├── 📁 scripts/                      # Scripts de automatización
│   └── *.py                         # Scripts Python
│
├── 📁 templates/                    # Templates de IaC
│   ├── cdk/                         # AWS CDK templates
│   └── terraform/                   # Terraform templates
│
├── 📁 business-documents/           # Documentos comerciales
│   ├── templates/                   # Plantillas (SOW, propuestas, contratos)
│   │   ├── sow/                    # Statement of Work templates
│   │   ├── proposals/              # Propuestas comerciales
│   │   ├── contracts/              # Contratos
│   │   └── reports/                # Reportes ejecutivos
│   └── generated/                   # Documentos generados
│       ├── sow/                    # SOWs generados (ej: EBA)
│       ├── proposals/              # Propuestas generadas
│       ├── contracts/              # Contratos generados
│       └── reports/                # Reportes generados
│
├── 📁 propuesta/                    # Propuesta comercial (legacy)
│   ├── PROPUESTA_COMERCIAL_BGR.md
│   └── FLUJO_MIGRACION_DETALLADO.md
│
└── 📁 docs/                         # Documentación de aplicaciones
    ├── APP_Api_Portal.md
    ├── APP_Saras.md
    ├── APP_Sonar_Qube.md
    └── ...
```

---

## 🎯 Acceso Rápido

### Para Gestión del Proyecto
- **[Gestión del Proyecto](./project-management/)**: Planes, progreso, costos
- **[Plan de Migración](./project-management/planning/PLAN_MIGRACION.md)**: Plan maestro
- **[Progreso](./project-management/progress/PROGRESS.md)**: Estado actual
- **[Costos](./project-management/costs/)**: Calculadoras de costos

### Para Propuestas de Modernización
- **[Propuestas](./modernization-proposals/)**: Todas las propuestas técnicas
- **[Guía de Uso](./modernization-proposals/GETTING_STARTED.md)**: Cómo usar las propuestas
- **[Resumen](./modernization-proposals/README.md)**: Resumen ejecutivo

### Para Información de Aplicaciones
- **[Datos Originales](./applications/raw-data/)**: HTML exports de aplicaciones
- **[Documentación](./docs/)**: Fichas técnicas de aplicaciones
- **[Análisis](./applications/analysis/)**: Análisis detallados

### Para Documentación Técnica
- **[Planes EBA](./documentation/eba-plans/)**: Early Business Adoption plans
- **[Análisis SQL](./documentation/sql-analysis/)**: Análisis de SQL Server

### Para Documentos Comerciales
- **[Business Documents](./business-documents/)**: SOWs, propuestas, contratos
- **[Templates SOW](./business-documents/templates/sow/)**: Plantillas de Statement of Work
- **[SOWs Generados](./business-documents/generated/sow/)**: SOWs para EBA y otros

### Para Assessment
- **[Cloudamize](./assesment/Cloudamize/)**: Datos de assessment
- **[RVTools](./assesment/)**: Exports de RVTools

### Para Reportes
- **[Reportes](./reports/)**: Reportes ejecutivos y técnicos

---

## 📊 Estado del Proyecto

### Aplicaciones (8 total)

| # | Aplicación | VMs | Estrategia | Estado Propuesta | Estado Implementación |
|---|------------|-----|------------|------------------|----------------------|
| 1 | **SARAS** | 2 | Modernización | ✅ Completa | 📋 Pendiente |
| 2 | **Api Portal** | 5 | Static Site | ✅ Completa | 📋 Pendiente |
| 3 | **Backoffice Sistemas** | 5 | Lift & Shift | ✅ Completa | 📋 Pendiente |
| 4 | **SonarQube** | 3 | Lift & Shift | ✅ Completa | 📋 Pendiente |
| 5 | Portal Guía BGR | 4 | - | 📋 Por definir | 📋 Pendiente |
| 6 | Portal Adm BGR | 4 | - | 📋 Por definir | 📋 Pendiente |
| 7 | Backoffice Banca | 6 | - | 📋 Por definir | 📋 Pendiente |
| 8 | Seq (Logging) | 5 | - | 📋 Por definir | 📋 Pendiente |

**Progreso Propuestas**: 4/8 (50%)  
**Progreso Implementación**: 0/8 (0%)

---

## 💰 Resumen de Costos

### Aplicaciones con Propuesta

| Aplicación | Costo Actual | Costo AWS | Ahorro/mes | Ahorro % |
|------------|--------------|-----------|------------|----------|
| SARAS | $1,400 | $904 | $496 | 35% |
| Api Portal | $2,000 | $1.50 | $1,998 | 99.9% |
| Backoffice Sistemas | - | $402 | - | - |
| SonarQube | $1,500 | $404 | $1,096 | 73% |
| **TOTAL** | **$4,900** | **$1,711.50** | **$3,188.50** | **65%** |

**Ahorro Anual Proyectado**: $38,262

---

## 🚀 Roadmap

### Fase 1: Quick Wins (Mes 1)
- **Semana 1**: Api Portal (5 días) - $1,998/mes ahorro
- **Semana 2-3**: SonarQube (2 semanas) - $1,096/mes ahorro
- **Semana 4**: Documentación y lecciones aprendidas

### Fase 2: Lift & Shift (Mes 2)
- **Semana 1-3**: Backoffice Sistemas (3 semanas)
- **Semana 4**: Estabilización

### Fase 3: Modernización (Meses 3-5)
- **Semana 1-11**: SARAS (11 semanas) - $496/mes ahorro
- Containerización + Babelfish

### Fase 4: Aplicaciones Restantes (Meses 6+)
- Portal Guía BGR
- Portal Adm BGR
- Backoffice Banca
- Seq

---

## 📋 Documentos Clave

### Gestión del Proyecto
1. **[PLAN_MIGRACION.md](./project-management/planning/PLAN_MIGRACION.md)**: Plan maestro de migración
2. **[PROGRESS.md](./project-management/progress/PROGRESS.md)**: Seguimiento de progreso
3. **[Costos](./project-management/costs/)**: Calculadoras de costos

### Propuestas Técnicas
1. **[SARAS](./modernization-proposals/saras/)**: Modernización con ECS + Babelfish
2. **[Api Portal](./modernization-proposals/api-portal/)**: Static Site con Amplify
3. **[Backoffice](./modernization-proposals/backoffice-sistemas/)**: Lift & Shift híbrido
4. **[SonarQube](./modernization-proposals/sonarqube/)**: Lift & Shift optimizado

### Documentación EBA
1. **[EBA_PLAN.md](./documentation/eba-plans/EBA_PLAN.md)**: Plan EBA general
2. **[EBA_PLAN_BABELFISH.md](./documentation/eba-plans/EBA_PLAN_BABELFISH.md)**: Plan con Babelfish
3. **[EBA_PLAN_CONTAINERS.md](./documentation/eba-plans/EBA_PLAN_CONTAINERS.md)**: Plan con contenedores

### Análisis Técnico
1. **[SQL_SERVER_ANALYSIS.md](./documentation/sql-analysis/SQL_SERVER_ANALYSIS.md)**: Análisis de SQL Server
2. **[Reportes](./reports/)**: Reportes ejecutivos y técnicos

---

## 🔍 Cómo Encontrar Información

### Por Tipo de Información

#### Información de Aplicación Específica
```
1. Datos originales: applications/raw-data/G.I.-[Nombre].html
2. Ficha técnica: docs/APP_[Nombre].md
3. Propuesta: modernization-proposals/[nombre]/
```

#### Información de Gestión
```
1. Plan general: project-management/planning/
2. Progreso: project-management/progress/
3. Costos: project-management/costs/
```

#### Información Técnica
```
1. Propuestas: modernization-proposals/
2. Diagramas: diagrams/ o generated-diagrams/
3. Scripts: scripts/
4. Templates: templates/
```

### Por Fase del Proyecto

#### Assessment (Completado)
- `assesment/`: Datos de Cloudamize y RVTools
- `applications/raw-data/`: HTML exports
- `docs/`: Fichas técnicas

#### Planning (En Progreso)
- `project-management/planning/`: Planes de migración
- `modernization-proposals/`: Propuestas técnicas (4/8)
- `documentation/eba-plans/`: Planes EBA

#### Implementation (Pendiente)
- `scripts/`: Scripts de automatización
- `templates/`: Templates de IaC

#### Reporting (Continuo)
- `reports/`: Reportes del proyecto
- `project-management/progress/`: Seguimiento

---

## 🛠️ Herramientas y Scripts

### Scripts Disponibles
```bash
# Análisis de aplicaciones
scripts/analyze_applications.py

# Generación de diagramas
scripts/generate_diagrams.py

# Análisis de costos
scripts/recommend_ec2_and_costs.py

# Validación de propuestas
scripts/validate_migration_proposal.py
```

### Generación de Diagramas
```bash
# Usar Kiro CLI con generate_diagram tool
# Ver ejemplos en modernization-proposals/*/diagrams/
```

---

## 📞 Contacto y Roles

### Equipo del Proyecto
- **Project Sponsor**: [Nombre]
- **Project Manager**: [Nombre]
- **AWS Solutions Architect**: [Nombre]
- **Migration Lead**: [Nombre]
- **DevOps Engineer**: [Nombre]

### Stakeholders
- **IT Manager**: [Nombre]
- **Security Lead**: [Nombre]
- **Finance Manager**: [Nombre]

---

## 📈 Métricas del Proyecto

### KPIs Actuales
- **Aplicaciones Analizadas**: 8/8 (100%)
- **Propuestas Completadas**: 4/8 (50%)
- **Aplicaciones Migradas**: 0/8 (0%)
- **Ahorro Proyectado**: $38,262/año

### Próximos Hitos
- [ ] Completar propuestas restantes (4 aplicaciones)
- [ ] Aprobar propuestas existentes
- [ ] Iniciar implementación (Api Portal)
- [ ] Completar Fase 1 (Quick Wins)

---

## 🔄 Mantenimiento del Proyecto

### Actualizar Progreso
```bash
# Editar archivo de progreso
vim project-management/progress/PROGRESS.md

# Actualizar este índice
vim PROJECT_INDEX.md
```

### Agregar Nueva Propuesta
```bash
# Ver guía en modernization-proposals/
cat modernization-proposals/GETTING_STARTED.md
```

### Generar Reportes
```bash
# Ver estructura en reports/
ls -la reports/
```

---

## 📚 Referencias

### Documentación AWS
- [AWS Migration Hub](https://aws.amazon.com/migration-hub/)
- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)
- [6 R's of Migration](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-readiness/understanding-6rs.html)

### Herramientas
- [AWS Pricing Calculator](https://calculator.aws)
- [AWS Application Migration Service](https://aws.amazon.com/application-migration-service/)
- [Amazon Q for .NET Transform](https://aws.amazon.com/q/developer/)

---

## ✅ Checklist de Control del Proyecto

### Documentación
- [x] Estructura de directorios organizada
- [x] Índice maestro creado
- [x] Propuestas documentadas (4/8)
- [ ] Propuestas restantes (4/8)
- [ ] Reportes ejecutivos actualizados

### Gestión
- [x] Plan de migración definido
- [x] Roadmap establecido
- [x] Costos calculados
- [ ] Aprobaciones obtenidas
- [ ] Recursos asignados

### Implementación
- [ ] Ambiente AWS configurado
- [ ] Primera aplicación migrada
- [ ] Lecciones aprendidas documentadas
- [ ] Proceso repetible establecido

---

**Última actualización**: 2025-12-05  
**Versión**: 2.0  
**Estado**: En progreso - Fase de Planning
