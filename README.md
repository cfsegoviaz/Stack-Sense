# Stack Sense

Sistema de diagnóstico y análisis para migraciones a AWS. Procesa datos de RVTools, Cloudamize, Matilda y genera recomendaciones de arquitectura y costos.

## 🎯 Objetivo

Actuar como arquitecto AWS experimentado para:
- Analizar cargas de trabajo on-premise
- Generar recomendaciones de servicios AWS
- Estimar costos de migración
- Crear diagramas de arquitectura
- Validar contra AWS Well-Architected Framework

## 🛠️ Servidores MCP Configurados

### Core
- **AWS API MCP Server**: Interacción directa con servicios AWS
- **AWS Documentation MCP Server**: Acceso a docs y best practices

### Análisis y Costos
- **AWS Pricing MCP Server**: Estimación de costos en tiempo real
- **AWS Cost Explorer MCP Server**: Análisis de costos históricos

### Arquitectura
- **AWS Diagram MCP Server**: Generación de diagramas
- **AWS CDK MCP Server**: Generación de IaC
- **AWS Well-Architected Security MCP Server**: Validación de seguridad

## 📁 Estructura del Proyecto

```
stack-sense/
├── parsers/           # Parsers para diferentes fuentes
│   ├── rvtools/      # Parser de RVTools exports
│   ├── cloudamize/   # Parser de Cloudamize
│   └── matilda/      # Parser de Matilda
├── analysis/         # Motores de análisis y recomendaciones
├── tools/            # Herramientas de conversión y utilidades
├── training/         # Proyectos de clientes
│   └── map-bgr/     # Proyecto BGR (383 VMs)
├── reports/          # Reportes generados
├── diagrams/         # Diagramas de arquitectura
├── templates/        # Templates de IaC
└── examples/         # Ejemplos de uso
```

## ⚙️ Requisitos

- ✅ uv (instalado)
- ✅ GraphViz (instalado)
- ✅ Credenciales AWS (configuradas - perfil default)
- Python 3.10+

## 🚀 Instalación

1. Instalar dependencias:
```bash
pip install -r requirements.txt
```

2. Usar con Kiro CLI:
```bash
kiro-cli chat --mcp-config ./mcp.json
```

## 💡 Uso

### Convertir RVTools a CSV
```bash
python3 tools/rvtools_to_csv.py data/rvtools_export.xlsm
```

### Convertir Cloudamize a CSV
```bash
python3 tools/cloudamize_to_csv.py data/Observed-Infrastructure.xlsx
```

### Analizar export de RVTools
```bash
python examples/analyze_rvtools.py data/rvtools_export.xlsx
```

### Con Kiro CLI
```
Analiza este export de RVTools y dame recomendaciones de instancias EC2
```

```
Genera un diagrama de arquitectura para migrar estos 50 servidores a AWS
```

```
¿Cuánto costaría mensualmente esta migración en us-east-1?
```

## 📊 Capacidades

- ✅ Parse de exports RVTools (vInfo, vCPU, vMemory, vDisk)
- ✅ Parse de Cloudamize Observed Infrastructure (Compute, Storage, Network)
- ✅ Recomendaciones de instancias EC2 basadas en specs
- ✅ Recomendaciones de almacenamiento EBS
- ✅ Cálculo de recursos totales
- 🔄 Integración con AWS Pricing API
- 🔄 Generación automática de diagramas
- 🔄 Generación de IaC (CDK/Terraform)
- 🔄 Validación Well-Architected

## 🎯 Roadmap

- [ ] Parser Cloudamize
- [ ] Parser Matilda
- [ ] Detección automática de patrones de aplicación
- [ ] Recomendaciones de servicios managed (RDS, ECS, Lambda)
- [ ] Análisis de costos comparativo on-prem vs AWS
- [ ] Generación de propuestas comerciales
