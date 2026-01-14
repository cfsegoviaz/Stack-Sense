# Requirements Document - Application Analysis Workflow

## Introduction

Este documento define el flujo de trabajo repetible para analizar cada aplicación del portafolio MAP-BGR y generar su propuesta de modernización completa. El proceso se aplicará a las 44 aplicaciones identificadas en la matriz de aplicaciones.

## Glossary

- **Application_Analysis**: Proceso completo de evaluación de una aplicación para migración AWS
- **Modernization_Proposal**: Documento MD con arquitecturas AWS, costos y recomendaciones
- **Showcase_JSON**: Archivo JSON para visualización en stack-sense-showcase
- **Effort_Matrix**: Matriz de horas Escala24x7 para estimación de implementación
- **Architecture_Option**: Opción de arquitectura AWS con componentes, costos y tips

## Requirements

### Requirement 1: Infrastructure Data Collection

**User Story:** As a migration consultant, I want to collect infrastructure data from RVTools and Cloudamize, so that I can understand the current state of the application.

#### Acceptance Criteria

1. WHEN analyzing an application THEN the Analyzer SHALL extract VM specs (vCPUs, RAM, storage, OS, IP) from RVTools vInfo.csv
2. WHEN analyzing an application THEN the Analyzer SHALL extract usage metrics (CPU%, RAM%) from Cloudamize Compute.csv
3. WHEN analyzing an application THEN the Analyzer SHALL extract storage details from Cloudamize Storage.csv
4. WHEN analyzing an application THEN the Analyzer SHALL identify dependencies from matriz-aplicaciones-completa.csv

### Requirement 2: Modernization Proposal Document

**User Story:** As a migration consultant, I want to generate a comprehensive modernization proposal, so that the client can make informed migration decisions.

#### Acceptance Criteria

1. WHEN a proposal is generated THEN it SHALL include executive summary with key metrics
2. WHEN a proposal is generated THEN it SHALL include current infrastructure details (VMs, specs, usage)
3. WHEN a proposal is generated THEN it SHALL include tech stack analysis (framework, database, dependencies)
4. WHEN a proposal is generated THEN it SHALL include 3 architecture options with cost-benefit analysis
5. WHEN a proposal is generated THEN it SHALL include TCO comparison (12/24 months)
6. THE proposal SHALL be saved as `APPNAME_MODERNIZATION.md` in `/modernization-proposals/app-slug/`

### Requirement 3: Architecture Options with Tips

**User Story:** As a migration consultant, I want each architecture option to include guidance tips, so that the client can choose the best option for their situation.

#### Acceptance Criteria

1. WHEN an architecture option is defined THEN it SHALL include AWS components with pricing details
2. WHEN an architecture option is defined THEN it SHALL include implementation effort from escala24x7_effort_matrix.json
3. WHEN an architecture option is defined THEN it SHALL include a "tips" object with:
   - whenToChoose: string[] - Scenarios where this option is ideal
   - considerations: string[] - Important factors to evaluate
   - recommendations: string[] - Best practices and tips
   - idealFor: string[] - Target use cases
4. WHEN an architecture option is defined THEN it SHALL include advantages and disadvantages lists
5. THE Analyzer SHALL calculate costs using MCP aws-pricing tool

#### Tips Structure Example
```json
{
  "tips": {
    "whenToChoose": [
      "Migración urgente con timeline < 4 semanas",
      "Equipo sin experiencia en contenedores"
    ],
    "considerations": [
      "Costos de licencias Windows se mantienen",
      "Requiere VPN o Direct Connect para conectividad híbrida"
    ],
    "recommendations": [
      "Usar Reserved Instances para reducir costos 40%",
      "Implementar Auto Scaling para optimizar recursos"
    ],
    "idealFor": [
      "Aplicaciones legacy sin refactorización",
      "Cargas de trabajo con picos predecibles"
    ]
  }
}
```

### Requirement 4: Architecture Diagrams

**User Story:** As a migration consultant, I want visual architecture diagrams, so that stakeholders can understand the proposed solutions.

#### Acceptance Criteria

1. WHEN diagrams are requested THEN the Analyzer SHALL generate PNG diagrams using MCP generate_diagram
2. WHEN diagrams are generated THEN they SHALL be saved in `/modernization-proposals/app-slug/diagrams/`
3. THE Analyzer SHALL generate one diagram per architecture option
4. WHEN diagrams are generated THEN they SHALL use consistent AWS iconography

### Requirement 5: Showcase JSON Generation

**User Story:** As a migration consultant, I want to generate JSON files for the showcase app, so that results can be visualized interactively.

#### Acceptance Criteria

1. WHEN analysis completes THEN the Analyzer SHALL generate a JSON file following the Application interface in types.ts
2. THE JSON file SHALL be saved in `/apps/stack-sense-showcase/public/data/bgr/apps/{app-slug}.json`
3. WHEN JSON is generated THEN it SHALL include all architecture options with tips section
4. WHEN JSON is generated THEN the Analyzer SHALL update `/apps/stack-sense-showcase/public/data/bgr/apps/index.json`
5. THE JSON SHALL include: id, slug, name, description, currentState, techStack, architectures, owner, lastUpdated

#### Application JSON Structure
```json
{
  "id": "app-slug",
  "slug": "app-slug",
  "name": "Application Name",
  "description": "Application description",
  "clientId": "bgr",
  "waveId": "wave-N",
  "status": "planned|assessed|migrating|completed",
  "currentMonthlyCost": 1200,
  "recommendedArchitecture": "architecture-id",
  "lastUpdated": "2026-01-06",
  "owner": { "name": "", "email": "", "role": "" },
  "currentState": {
    "vms": [{ "name": "", "vCPUs": 4, "ramGB": 8, "storageGB": 200, "os": "", "ip": "", "status": "poweredOn", "environment": "prod" }],
    "totalvCPUs": 10,
    "totalRAM": 20,
    "totalStorage": 610,
    "users": 685,
    "criticality": "high"
  },
  "techStack": {
    "frontend": [],
    "backend": [],
    "database": [],
    "other": []
  },
  "architectures": [
    {
      "id": "option-id",
      "name": "Option Name",
      "strategy": "Rehost|Replatform|Refactor",
      "recommended": false,
      "monthlyCost": 500,
      "savingsPercent": 50,
      "implementationHours": 62,
      "implementationCost": 9300,
      "timeline": "2-3 semanas",
      "complexity": "low|medium|high",
      "risk": "low|medium|high",
      "description": "",
      "diagramUrl": "/diagrams/app_option.png",
      "components": [],
      "advantages": [],
      "disadvantages": [],
      "tco": { "year1Total": 15000, "yearlyRecurring": 6000 },
      "tips": {
        "whenToChoose": [],
        "considerations": [],
        "recommendations": [],
        "idealFor": []
      }
    }
  ]
}
```

### Requirement 6: Progress Tracking

**User Story:** As a migration consultant, I want to track analysis progress, so that I can monitor completion status.

#### Acceptance Criteria

1. WHEN an application is analyzed THEN the Analyzer SHALL update INDEX.md with the new application
2. WHEN an application is analyzed THEN the Analyzer SHALL update ANALYSIS_CHECKLIST.md progress (N/44)
3. THE Analyzer SHALL maintain a log of analyzed applications with dates

#### ANALYSIS_CHECKLIST.md Location
- Path: `/training/map-bgr/modernization-proposals/ANALYSIS_CHECKLIST.md`

### Requirement 7: Data Sources Configuration

**User Story:** As a migration consultant, I want clear data source paths, so that I can consistently extract infrastructure data.

#### Data Source Paths

| Source | Path | Description |
|--------|------|-------------|
| RVTools vInfo | `training/map-bgr/assesment/RVTools_export_all_250709_064325_DCP_csv/vInfo.csv` | VM specs |
| RVTools vCPU | `training/map-bgr/assesment/RVTools_export_all_250709_064325_DCP_csv/vCPU.csv` | CPU details |
| RVTools vMemory | `training/map-bgr/assesment/RVTools_export_all_250709_064325_DCP_csv/vMemory.csv` | Memory details |
| RVTools vDisk | `training/map-bgr/assesment/RVTools_export_all_250709_064325_DCP_csv/vDisk.csv` | Disk details |
| Cloudamize Compute | `training/map-bgr/assesment/Cloudamize/Observed-Infrastructure_csv/Compute.csv` | Usage metrics |
| Cloudamize Storage | `training/map-bgr/assesment/Cloudamize/Observed-Infrastructure_csv/Storage.csv` | Storage details |
| App Matrix | `training/map-bgr/applications/raw-data/matriz-aplicaciones-completa.csv` | 44 applications |
| Effort Matrix | `pricing/escala24x7_effort_matrix.json` | Implementation hours |

### Requirement 8: Output Paths Configuration

**User Story:** As a migration consultant, I want standardized output paths, so that all artifacts are organized consistently.

#### Output Paths

| Artifact | Path Pattern | Example |
|----------|--------------|---------|
| Modernization MD | `training/map-bgr/modernization-proposals/{app-slug}/{APP_NAME}_MODERNIZATION.md` | `backoffice-banca-digital/BACKOFFICE_BANCA_DIGITAL_MODERNIZATION.md` |
| Diagrams | `training/map-bgr/modernization-proposals/{app-slug}/diagrams/` | PNG files |
| Showcase JSON | `apps/stack-sense-showcase/public/data/bgr/apps/{app-slug}.json` | Individual app |
| Showcase Index | `apps/stack-sense-showcase/public/data/bgr/apps/index.json` | App listing |
| Showcase Diagrams | `apps/stack-sense-showcase/public/diagrams/` | Public diagrams |
