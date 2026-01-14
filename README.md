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
├── apps/                          # Aplicaciones del ecosistema
│   └── stack-sense-showcase/      # 🎨 Capa de presentación (ver sección abajo)
├── parsers/                       # Parsers para diferentes fuentes
│   ├── rvtools/                   # Parser de RVTools exports
│   ├── cloudamize/                # Parser de Cloudamize
│   └── matilda/                   # Parser de Matilda
├── analysis/                      # Motores de análisis y recomendaciones
├── tools/                         # Herramientas de conversión y utilidades
├── pricing/                       # Matrices de precios transversales
│   └── escala24x7_effort_matrix.json
├── training/                      # Proyectos de clientes
│   └── map-bgr/                   # Proyecto BGR (383 VMs)
├── reports/                       # Reportes generados
├── docs/                          # Documentación adicional
├── templates/                     # Templates de IaC
└── examples/                      # Ejemplos de uso
```

## 🎨 Stack Sense Showcase

Aplicación web que presenta los análisis de migración generados con IA. Desplegada en AWS usando SST (Serverless Stack).

### Arquitectura

```
apps/stack-sense-showcase/
├── sst.config.ts                  # Configuración SST (Cognito, API Gateway, S3)
├── packages/
│   ├── web/                       # Frontend React + Vite
│   │   ├── src/
│   │   │   ├── pages/             # Páginas de la aplicación
│   │   │   ├── components/        # Componentes React (shadcn/ui)
│   │   │   ├── hooks/             # Custom hooks (auth, API)
│   │   │   └── lib/               # Utilidades, tipos y cliente API
│   │   └── public/
│   │       ├── diagrams/          # Diagramas de arquitectura
│   │       └── logos/             # Logos de clientes
│   └── api/                       # Backend Lambda
│       └── src/
│           ├── data/              # Datos JSON por cliente (protegidos)
│           │   └── {client}/      # Carpeta por cliente
│           ├── lib/               # Utilidades compartidas
│           └── modules/           # Módulos del API
│               ├── clients/       # GET /clients, GET /clients/{slug}
│               ├── applications/  # GET /clients/{slug}/applications
│               ├── waves/         # GET /clients/{slug}/waves
│               ├── lift-shift/    # GET /clients/{slug}/lift-shift
│               ├── assessments/   # GET /clients/{slug}/assessments/mra|ola
│               └── users/         # CRUD usuarios Cognito
```

### API Endpoints

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/clients` | Lista de clientes |
| GET | `/clients/{slug}` | Detalle del cliente |
| GET | `/clients/{slug}/waves` | Olas de migración |
| GET | `/clients/{slug}/applications` | Lista de aplicaciones |
| GET | `/clients/{slug}/applications/{app}` | Detalle de aplicación |
| GET | `/clients/{slug}/lift-shift` | Datos lift & shift |
| GET | `/clients/{slug}/assessments/mra` | MRA Assessment |
| GET | `/clients/{slug}/assessments/ola` | OLA Assessment |
| GET | `/users` | Lista usuarios Cognito |
| POST | `/users` | Crear usuario |

### Stack Tecnológico

- **Frontend**: React 18, Vite, TypeScript, Tailwind CSS, shadcn/ui
- **Backend**: AWS Lambda + API Gateway
- **Auth**: Amazon Cognito
- **Hosting**: S3 + CloudFront (StaticSite)
- **IaC**: SST v3

### Páginas Principales

| Página | Descripción |
|--------|-------------|
| `/` | Landing page |
| `/{client}` | Dashboard del cliente |
| `/{client}/applications` | Lista de aplicaciones |
| `/{client}/applications/{app}` | Detalle con arquitecturas propuestas |
| `/{client}/architectures` | Galería de arquitecturas |
| `/{client}/waves` | Olas de migración |
| `/{client}/map/{phase}` | Fases MAP (Assess, Mobilize, Migrate) |
| `/{client}/lift-shift` | Análisis Lift & Shift |
| `/{client}/mra` | Migration Readiness Assessment |
| `/{client}/ola` | Operating Level Agreement |

### Comandos

```bash
cd apps/stack-sense-showcase

# Desarrollo local
npm run dev

# Deploy a producción
npm run deploy

# Deploy a dev
npm run deploy:dev

# Eliminar stack
npm run remove
```

### Agregar Nuevo Cliente

1. Crear carpeta en `packages/api/src/data/{client-slug}/`
2. Agregar `client.json`, `waves.json`, `apps/index.json`
3. Crear JSON por cada aplicación en `apps/`
4. Agregar logo en `packages/web/public/logos/`
5. Registrar en `packages/api/src/data/clients.json`

## ⚙️ Requisitos

- Python 3.9+
- Homebrew (gestor de paquetes para macOS)
- Node.js y npm
- uv (gestor de paquetes Python para servidores MCP)
- Amazon Q CLI (Kiro CLI)
- Credenciales AWS (configuradas - perfil default)

## 🚀 Instalación

### 1. Instalar Homebrew (si no está instalado)
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Configurar Homebrew en tu PATH
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

### 2. Instalar Node.js
```bash
brew install node
```

### 3. Instalar uv (para servidores MCP)
```bash
brew install uv
```

### 4. Instalar Amazon Q CLI (Kiro CLI)
```bash
brew install --cask amazon-q

# Crear enlaces simbólicos para acceso global
sudo ln -sf "/Applications/Kiro CLI.app/Contents/MacOS/kiro-cli" /usr/local/bin/kiro-cli
sudo ln -sf "/Applications/Kiro CLI.app/Contents/MacOS/kiro-cli-chat" /usr/local/bin/kiro-cli-chat
sudo ln -sf "/Applications/Kiro CLI.app/Contents/MacOS/kiro-cli-term" /usr/local/bin/kiro-cli-term

# Verificar instalación
kiro-cli --version
```

### 5. Instalar dependencias Python del proyecto
```bash
pip3 install -r requirements.txt
```

### 6. Configurar servidores MCP
```bash
# Importar configuración MCP del proyecto
kiro-cli-chat mcp import --file ./mcp.json workspace

# Verificar servidores configurados
kiro-cli-chat mcp list
```

### 7. Configurar PATH (agregar a ~/.zshrc)
```bash
echo 'export PATH="/opt/homebrew/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

## 💡 Uso

### Iniciar chat con Kiro CLI
```bash
# Iniciar sesión interactiva con servidores MCP
kiro-cli-chat chat

# O hacer una pregunta directa
kiro-cli-chat chat "Analiza este export de RVTools y dame recomendaciones de instancias EC2"
```

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
python3 examples/analyze_rvtools.py data/rvtools_export.xlsx
```

### Ejemplos de prompts con Kiro CLI
```
Analiza este export de RVTools y dame recomendaciones de instancias EC2
```

```
Genera un diagrama de arquitectura para migrar estos 50 servidores a AWS
```

```
¿Cuánto costaría mensualmente esta migración en us-east-1?
```

### Gestionar servidores MCP
```bash
# Listar servidores configurados
kiro-cli-chat mcp list

# Ver estado de un servidor
kiro-cli-chat mcp status <nombre-servidor>

# Agregar un nuevo servidor
kiro-cli-chat mcp add <nombre-servidor>

# Eliminar un servidor
kiro-cli-chat mcp remove <nombre-servidor>
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

## 🔧 Troubleshooting

### Los servidores MCP no se cargan
Si ves errores como "No such file or directory" al iniciar el chat:
```bash
# Verificar que uv/uvx esté instalado
uvx --version

# Si no está en el PATH, agregar a ~/.zshrc
echo 'export PATH="/opt/homebrew/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### Error al importar configuración MCP
```bash
# Asegurarse de estar en el directorio del proyecto
cd /Users/migueviana/Documents/Stack-Sense

# Reimportar configuración
kiro-cli-chat mcp import --file ./mcp.json workspace --force
```

### Verificar instalación completa
```bash
# Python
python3 --version  # Debe ser 3.9+

# Node.js
node --version     # Debe ser v25+

# npm
npm --version      # Debe ser 11+

# uv
uv --version       # Debe estar instalado

# Kiro CLI
kiro-cli --version # Debe ser 1.21+

# Dependencias Python
python3 -c "import pandas; import openpyxl; import boto3; print('✅ OK')"
```

### Logs de depuración
```bash
# Ver logs detallados de Kiro CLI
KIRO_LOG_LEVEL=trace kiro-cli-chat chat

# Ubicación de logs
cat $TMPDIR/kiro-log/kiro-chat.log
```
