# Stack Sense - Reglas del Proyecto

## 🎯 Propósito

Stack Sense es un sistema de diagnóstico y análisis para migraciones AWS. Genera análisis detallados de aplicaciones y servidores, y los presenta en un dashboard interactivo (stack-sense-showcase).

## 📁 Estructura de Datos

### Flujo de Datos

```
training/{cliente}/          →  Análisis con IA  →  apps/stack-sense-showcase/packages/api/src/data/{cliente}/
(RVTools, Cloudamize, MRA)      (Kiro CLI)           (JSONs tipados para API)
```

### Ubicación de Archivos

| Tipo | Ubicación | Descripción |
|------|-----------|-------------|
| Datos fuente | `training/{cliente}/` | RVTools, Cloudamize, documentos MRA/OLA |
| Análisis MD | `training/{cliente}/modernization-proposals/` | Análisis detallado por aplicación |
| JSONs API | `apps/stack-sense-showcase/packages/api/src/data/{cliente}/` | Datos para el showcase |
| Tipos TS | `apps/stack-sense-showcase/packages/api/src/types/index.ts` | Definición de tipos |

## 🔧 Arquitectura del Showcase

### Stack Tecnológico

- **Frontend**: React + Vite + TypeScript + Tailwind + shadcn/ui
- **Backend**: Hono (Lambda Function URL)
- **Auth**: Amazon Cognito
- **IaC**: SST v3
- **Datos**: JSON estáticos servidos por API

### Estructura de Carpetas

```
apps/stack-sense-showcase/
├── packages/
│   ├── api/                    # Backend Hono
│   │   ├── src/
│   │   │   ├── data/           # JSONs por cliente
│   │   │   │   ├── clients.json
│   │   │   │   └── {cliente}/
│   │   │   │       ├── client.json
│   │   │   │       ├── waves.json
│   │   │   │       ├── lift-and-shift.json
│   │   │   │       ├── apps/
│   │   │   │       │   ├── index.json
│   │   │   │       │   └── {app-slug}.json
│   │   │   │       └── map-steps/
│   │   │   │           ├── mra-assessment.json
│   │   │   │           └── ola-assessment.json
│   │   │   ├── modules/        # Rutas por dominio
│   │   │   ├── types/          # Tipos TypeScript
│   │   │   └── index.ts        # Entry point Hono
│   │   └── package.json
│   └── web/                    # Frontend React
│       ├── src/
│       │   ├── pages/
│       │   ├── components/
│       │   └── hooks/
│       └── package.json
└── sst.config.ts
```

## 📋 Tipos de Datos (OBLIGATORIO)

Al crear JSONs para el showcase, **SIEMPRE** usar los tipos definidos en:
`packages/api/src/types/index.ts`

### Tipos Principales

```typescript
// Cliente
interface Client {
  id: string;
  name: string;
  slug: string;
  project: ProjectInfo;
  assessment: AssessmentSummary;
  costs: CostSummary;
  implementation: ImplementationSummary;
  waves: WaveSummary[];
  strategies: Record<string, number>;
  liftAndShift: LiftAndShiftSummary;
}

// Aplicación
interface Application {
  id: string;
  slug: string;
  name: string;
  description: string;
  waveId: string;
  status: ApplicationStatus;
  currentMonthlyCost: number;
  recommendedArchitecture: string;
  owner: ContactInfo;
  currentState: CurrentState;
  techStack: TechStack;
  architectures: ArchitectureOption[];
}

// Wave de Migración
interface MigrationWave {
  id: string;
  name: string;
  description: string;
  status: WaveStatus;
  startDate: string;
  endDate: string;
  applications: string[];
  totalVMs: number;
  currentMonthlyCost: number;
  estimatedMonthlyCost: number;
  savingsPercent: number;
  implementationHours: number;
}

// Lift & Shift
interface LiftAndShift {
  totalServers: number;
  totalvCPUs: number;
  totalRAM: number;
  serversWithSql: number;
  serversWithoutSql: number;
  estimatedMonthlyCost: number;
  implementationHours: number;
  servers: LiftShiftServer[];
}

// MRA Assessment
interface MRAAssessment {
  executiveSummary: MRAExecutiveSummary;
  radarChart: RadarChart;
  findings: MRAFindings;
  recommendations: MRARecommendations;
  riskMatrix: RiskMatrixItem[];
}

// OLA Assessment
interface OLAAssessment {
  currentState: OLACurrentState;
  financialSummary: OLAFinancialSummary;
  sqlOptimization: SQLOptimization;
  eolAssessment: EOLAssessment;
  recommendations: OLARecommendations;
}
```

## 🔄 Proceso de Análisis

### 1. Preparación de Datos Fuente

```bash
training/{cliente}/
├── assesment/
│   ├── Cloudamize/
│   │   ├── Observed-Infrastructure.xlsx
│   │   ├── MigrationPlanner-Server-Applications.xlsx
│   │   └── OLA/
│   │       └── Cloudamize_Assessment_Summary.pdf
│   └── MRA/
│       └── [Cliente]Informe MRA.pdf
├── rvtools/
│   └── RVTools_export.xlsx
└── modernization-proposals/
    └── {app}/
        └── {APP}_MODERNIZATION.md
```

### 2. Análisis con Kiro CLI

Para cada aplicación:
1. Analizar VMs del RVTools/Cloudamize
2. Identificar stack tecnológico
3. Proponer 2-3 arquitecturas AWS
4. Calcular costos y ahorros
5. Generar diagrama de arquitectura
6. Crear MD de análisis detallado

### 3. Exportación a Showcase

```bash
# Estructura de salida
apps/stack-sense-showcase/packages/api/src/data/{cliente}/
├── client.json              # Resumen del cliente
├── waves.json               # Waves de migración
├── lift-and-shift.json      # Servidores sin app asignada
├── apps/
│   ├── index.json           # Lista de apps
│   └── {app-slug}.json      # Detalle por app
└── map-steps/
    ├── mra-assessment.json  # Assessment MRA
    └── ola-assessment.json  # Assessment OLA
```

## ✅ Checklist de Validación

Antes de considerar un análisis completo:

### Por Aplicación
- [ ] JSON válido (validar con `python3 -m json.tool`)
- [ ] Campos obligatorios: id, slug, name, waveId, currentMonthlyCost
- [ ] Al menos 2 arquitecturas propuestas
- [ ] recommendedArchitecture apunta a un id válido
- [ ] Costos calculados (monthlyCost, implementationHours)
- [ ] Diagrama generado (diagramUrl)

### Por Cliente
- [ ] client.json con totales correctos
- [ ] waves.json con todas las apps asignadas
- [ ] lift-and-shift.json con servidores restantes
- [ ] Assessments MRA y OLA si aplica
- [ ] Suma de apps en waves = total de apps

### Cálculos
- [ ] savingsPercent = (1 - awsCost/currentCost) * 100
- [ ] implementationCost = hours * hourlyRate ($150)
- [ ] annualSavings = monthlySavings * 12

## 🚀 Comandos Útiles

```bash
# Validar todos los JSONs de un cliente
for f in apps/stack-sense-showcase/packages/api/src/data/{cliente}/apps/*.json; do
  python3 -m json.tool "$f" > /dev/null && echo "✅ $f" || echo "❌ $f"
done

# Calcular totales desde apps
python3 << 'EOF'
import json, os
apps_dir = 'apps/stack-sense-showcase/packages/api/src/data/{cliente}/apps'
total_cost = 0
total_hours = 0
for f in os.listdir(apps_dir):
    if f.endswith('.json') and f != 'index.json':
        with open(os.path.join(apps_dir, f)) as file:
            app = json.load(file)
            # ... calcular totales
EOF

# Desarrollo local
cd apps/stack-sense-showcase && npx sst dev
```

## 📝 Convenciones de Nombres

| Elemento | Formato | Ejemplo |
|----------|---------|---------|
| App ID/Slug | kebab-case | `backoffice-banca-digital` |
| Wave ID | wave-N | `wave-1`, `wave-2` |
| Arquitectura ID | kebab-case | `ecs-aurora-babelfish` |
| Archivos JSON | kebab-case.json | `lift-and-shift.json` |
| Archivos MD | UPPER_SNAKE.md | `APP_MODERNIZATION.md` |

## ⚠️ Reglas Importantes

1. **NUNCA** crear JSONs sin validar contra los tipos de `types/index.ts`
2. **SIEMPRE** incluir implementationHours y monthlyCost en arquitecturas
3. **SIEMPRE** asignar waveId a cada aplicación
4. **SIEMPRE** actualizar waves.json cuando cambian apps
5. **SIEMPRE** incluir servidores no asignados en lift-and-shift.json
6. Los diagramas van en `packages/web/public/diagrams/{app-slug}/`
7. Usar español para descripciones y nombres visibles al usuario
8. Usar inglés para IDs, slugs y campos técnicos

## 🔗 Referencias

- Tipos completos: `packages/api/src/types/index.ts`
- API README: `packages/api/README.md`
- Showcase README: `apps/stack-sense-showcase/README.md`
- Proyecto principal: `README.md`
