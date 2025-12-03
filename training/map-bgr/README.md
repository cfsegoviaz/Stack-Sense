# Proyecto MAP-BGR

Análisis de migración a AWS para infraestructura BGR.

**Estado**: 🔄 En Progreso - Fase 1 (Discovery)  
**Progreso**: 8% completado  
**Fecha Inicio**: 2025-12-01

---

## 📋 Documentos Clave

- 📘 **[PLAN_MIGRACION.md](PLAN_MIGRACION.md)** - Plan completo con checklist
- 📊 **[PROGRESS.md](PROGRESS.md)** - Tracking de progreso
- ⚙️ **[config.json](config.json)** - Configuración del proyecto

---

## 🏗️ Estructura del Proyecto

```
map-bgr/
├── PLAN_MIGRACION.md              # Plan maestro con checklist
├── PROGRESS.md                     # Tracking de progreso
├── README.md                       # Este archivo
├── config.json                     # Configuración
├── helper.sh                       # Script de utilidades
├── RVTools_export_*.xlsm          # Datos originales
├── RVTools_export_*_csv/          # Datos convertidos (26 CSVs)
├── reports/                        # Reportes generados
├── diagrams/                       # Diagramas de arquitectura
├── docs/                           # Documentación técnica
├── templates/                      # IaC (CDK, Terraform)
│   ├── cdk/
│   └── terraform/
├── scripts/                        # Scripts de automatización
└── propuesta/                      # Propuesta comercial
```

---

## 📊 Datos Disponibles

### Ambiente Producción (Real)
- **VMs**: 383 máquinas virtuales
- **vCPUs**: 1,752 cores
- **RAM**: 5,924 GB
- **Hosts**: 14 hosts ESXi
- **Datastores**: 33 datastores
- **Fuente**: RVTools export (2025-07-09)

### Ambientes Dev y QA (Simulados)
- **Desarrollo**: ~115 VMs (30% de prod)
- **QA**: ~77 VMs (20% de prod)
- **Nota**: Mismas aplicaciones, recursos reducidos

### Aplicaciones Identificadas (8)
1. Api Portal (Alta criticidad)
2. Portal Guía BGR (Alta)
3. Sonar Qube (Media)
4. Backoffice Banca Digital (Alta)
5. Portal Adm BGR (Alta)
6. Backoffice Sistemas (Media)
7. Saras (Media)
8. Seq (Baja)

### Archivos CSV Disponibles (26)
- `vInfo.csv` - Info general de VMs (383)
- `vCPU.csv` - Configuración CPUs
- `vMemory.csv` - Configuración memoria
- `vDisk.csv` - Discos (340)
- `vPartition.csv` - Particiones (1193)
- `vNetwork.csv` - Red (151 interfaces)
- `vHost.csv` - Hosts ESXi (14)
- `vDatastore.csv` - Datastores (33)
- ... y 18 más

---

## 🚀 Quick Start

### Ver estado del proyecto
```bash
./helper.sh status
```

### Ver resumen de VMs
```bash
./helper.sh summary
```

### Ver progreso
```bash
./helper.sh progress
```

### Ver plan completo
```bash
./helper.sh plan
```

### Trabajar con Kiro CLI
```bash
cd /Users/christian/Projects/escala/stack-sense
kiro-cli chat --mcp-config ./mcp.json
```

Comandos sugeridos:
```
Analiza el inventario de producción del proyecto map-bgr
Simula inventarios de Dev y QA basados en producción
Genera recomendaciones de instancias EC2 por ambiente
Calcula costos estimados de migración a AWS
```

---

## 🎯 Objetivos del Proyecto

1. ✅ Inventario completo de 3 ambientes (Prod, Dev, QA)
2. 🔄 Mapeo de 8 aplicaciones a componentes AWS
3. ⏭️ Recomendaciones de servicios AWS por ambiente
4. ⏭️ Arquitectura target multi-cuenta en AWS
5. ⏭️ Estimación de costos y análisis TCO
6. ⏭️ Plan de migración por olas
7. ⏭️ Propuesta comercial completa

---

## 📈 Resumen Ejecutivo

### Infraestructura Actual (Producción)
- 🖥️ **383 VMs** (350 encendidas, 33 apagadas)
- 💻 **1,752 vCPUs** (promedio 4.6 por VM)
- 💾 **5,924 GB RAM** (promedio 15.5 GB por VM)
- 📦 **340 discos** configurados
- 🌐 **151 interfaces** de red

### Sistemas Operativos
- Windows Server 2016: 136 VMs (35%)
- Windows Server 2019: 53 VMs (14%)
- Windows Server 2022: 37 VMs (10%)
- ⚠️ Windows Server 2003: 38 VMs (10%) - Legacy
- Ubuntu Linux: 20 VMs (5%)
- Otros: 99 VMs (26%)

### Retos Identificados
- ⚠️ 38 VMs con Windows Server 2003 (EOL)
- 🔄 Migración sin downtime de apps críticas
- 🏗️ Arquitectura multi-ambiente en AWS
- 💰 Optimización de costos vs on-premise

---

## 📅 Cronograma

| Fase | Duración | Estado |
|------|----------|--------|
| 1. Discovery & Assessment | 2 semanas | 🔄 En progreso |
| 2. Estrategia & Diseño | 2 semanas | ⏭️ Pendiente |
| 3. Análisis de Costos | 1 semana | ⏭️ Pendiente |
| 4. Plan de Ejecución | 1 semana | ⏭️ Pendiente |
| 5. Generación Entregables | 1 semana | ⏭️ Pendiente |
| **TOTAL** | **7 semanas** | **8% completado** |

---

## 🎯 Próximos Pasos

1. ⏭️ Simular inventarios de Dev y QA
2. ⏭️ Analizar documentación HTML de aplicaciones
3. ⏭️ Mapear VMs a aplicaciones
4. ⏭️ Generar recomendaciones de instancias EC2
5. ⏭️ Calcular recursos totales por ambiente

---

**Última actualización**: 2025-12-01  
**Responsable**: Equipo Stack Sense
