# Technical Design - Application Analysis Workflow

## Overview

Este documento define las tareas técnicas para implementar el flujo de análisis de aplicaciones del portafolio MAP-BGR. El workflow es un proceso manual asistido por Kiro CLI que genera propuestas de modernización, JSONs para showcase y diagramas de arquitectura.

## Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                        WORKFLOW DE ANÁLISIS                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐          │
│  │   INPUTS     │    │   PROCESO    │    │   OUTPUTS    │          │
│  ├──────────────┤    ├──────────────┤    ├──────────────┤          │
│  │ • vInfo.csv  │───▶│ 1. Extraer   │───▶│ • _MOD.md    │          │
│  │ • Compute.csv│    │    datos VM  │    │ • app.json   │          │
│  │ • matriz.csv │    │              │    │ • diagrams/  │          │
│  │ • effort.json│    │ 2. Generar   │    │ • index.json │          │
│  └──────────────┘    │    opciones  │    │ • checklist  │          │
│                      │              │    └──────────────┘          │
│                      │ 3. Calcular  │                              │
│                      │    costos    │    ┌──────────────┐          │
│                      │              │    │   MCP TOOLS  │          │
│                      │ 4. Generar   │◀───┤──────────────┤          │
│                      │    outputs   │    │ • aws-pricing│          │
│                      └──────────────┘    │ • diagrams   │          │
│                                          └──────────────┘          │
└─────────────────────────────────────────────────────────────────────┘
```

## Tasks

### Task 1: Update Showcase JSON Files with Tips

**Requirement:** Req 3, Req 5

**Description:** Agregar sección `tips` a los 5 JSONs existentes en showcase que no la tienen.

**Files to modify:**
- `apps/stack-sense-showcase/public/data/bgr/apps/backoffice-banca-digital.json`
- `apps/stack-sense-showcase/public/data/bgr/apps/backoffice-sistemas.json`
- `apps/stack-sense-showcase/public/data/bgr/apps/saras.json`
- `apps/stack-sense-showcase/public/data/bgr/apps/api-portal.json`
- `apps/stack-sense-showcase/public/data/bgr/apps/sonarqube.json`

**Implementation:**
Para cada arquitectura en cada JSON, agregar:
```json
"tips": {
  "whenToChoose": ["..."],
  "considerations": ["..."],
  "recommendations": ["..."],
  "idealFor": ["..."]
}
```

**Acceptance criteria:**
- Todos los JSONs tienen tips en cada arquitectura
- Tips son relevantes para cada estrategia (Rehost/Replatform/Refactor)

---

### Task 2: Create SEQ Showcase JSON

**Requirement:** Req 5

**Description:** Crear JSON para SEQ que falta en showcase (tiene propuesta MD pero no JSON).

**Files to create:**
- `apps/stack-sense-showcase/public/data/bgr/apps/seq.json`

**Files to modify:**
- `apps/stack-sense-showcase/public/data/bgr/apps/index.json`

**Data source:**
- `training/map-bgr/modernization-proposals/seq/SEQ_MODERNIZATION.md`

**Acceptance criteria:**
- JSON sigue estructura de Application interface
- index.json actualizado con SEQ
- Incluye tips en arquitecturas

---

### Task 3: Create Analysis Prompt Template

**Requirement:** Req 1, Req 2, Req 3

**Description:** Crear template de prompt reutilizable para analizar nuevas aplicaciones.

**Files to create:**
- `training/map-bgr/modernization-proposals/templates/ANALYSIS_PROMPT.md`

**Content structure:**
```markdown
# Prompt de Análisis - {APP_NAME}

## Contexto
Analiza la aplicación {APP_NAME} del portafolio BGR.

## Datos de Entrada
- Buscar en matriz: `training/map-bgr/applications/raw-data/matriz-aplicaciones-completa.csv`
- Buscar VMs en: `training/map-bgr/assesment/RVTools.../vInfo.csv`
- Buscar métricas en: `training/map-bgr/assesment/Cloudamize/...`

## Outputs Requeridos
1. Propuesta MD en: `modernization-proposals/{app-slug}/`
2. JSON showcase en: `apps/stack-sense-showcase/public/data/bgr/apps/`
3. Diagramas en: `modernization-proposals/{app-slug}/diagrams/`
4. Actualizar: ANALYSIS_CHECKLIST.md, index.json

## Arquitecturas a Evaluar
- Opción 1: Lift & Shift (Rehost)
- Opción 2: Replatform (Linux/.NET Core/Managed DB)
- Opción 3: Containers (ECS Fargate/EKS)
```

**Acceptance criteria:**
- Template es autocontenido
- Incluye todas las rutas de datos
- Especifica outputs requeridos

---

### Task 4: Update ArchitectureCard Component for Tips

**Requirement:** Req 3

**Description:** Actualizar componente React para mostrar tips de arquitectura.

**Files to modify:**
- `apps/stack-sense-showcase/src/components/applications/ArchitectureCard.tsx`

**Implementation:**
Agregar sección colapsable para tips:
```tsx
{architecture.tips && (
  <Collapsible>
    <CollapsibleTrigger>💡 Tips y Recomendaciones</CollapsibleTrigger>
    <CollapsibleContent>
      <div>Cuándo elegir: {tips.whenToChoose}</div>
      <div>Consideraciones: {tips.considerations}</div>
      <div>Recomendaciones: {tips.recommendations}</div>
      <div>Ideal para: {tips.idealFor}</div>
    </CollapsibleContent>
  </Collapsible>
)}
```

**Acceptance criteria:**
- Tips se muestran en UI cuando existen
- Sección es colapsable para no saturar vista
- Styling consistente con diseño actual

---

### Task 5: Create Diagram Templates

**Requirement:** Req 4

**Description:** Crear templates de código Python para diagramas reutilizables.

**Files to create:**
- `training/map-bgr/modernization-proposals/templates/diagrams/lift_shift_template.py`
- `training/map-bgr/modernization-proposals/templates/diagrams/ecs_fargate_template.py`
- `training/map-bgr/modernization-proposals/templates/diagrams/hybrid_template.py`

**Implementation:**
Templates parametrizables con variables:
```python
# Variables: APP_NAME, VMS, HAS_DB, HAS_CACHE
with Diagram(f"{APP_NAME} - Lift & Shift", ...):
    # Template code
```

**Acceptance criteria:**
- Templates cubren 3 estrategias principales
- Fáciles de personalizar por app
- Usan iconografía AWS consistente

---

### Task 6: Validate Effort Matrix Coverage

**Requirement:** Req 3

**Description:** Verificar que effort_matrix.json cubre todos los servicios AWS usados en arquitecturas.

**Files to review:**
- `pricing/escala24x7_effort_matrix.json`

**Services to validate:**
- EC2, ALB, NLB, ECS Fargate, EKS
- RDS, Aurora, ElastiCache, DynamoDB
- S3, EFS, EBS
- VPN, Direct Connect, Transit Gateway
- CloudWatch, WAF, Secrets Manager

**Acceptance criteria:**
- Todos los servicios tienen horas estimadas
- Documentar servicios faltantes si los hay

---

### Task 7: Create Batch Analysis Script

**Requirement:** Req 6

**Description:** Crear script helper para facilitar análisis en lote.

**Files to create:**
- `training/map-bgr/scripts/analyze_app.sh`

**Implementation:**
```bash
#!/bin/bash
# Usage: ./analyze_app.sh <app-slug>
APP_SLUG=$1
mkdir -p modernization-proposals/$APP_SLUG/diagrams
echo "Directorio creado: modernization-proposals/$APP_SLUG"
echo "Ejecuta: kiro-cli chat 'Analiza la aplicación $APP_SLUG siguiendo ANALYSIS_PROMPT.md'"
```

**Acceptance criteria:**
- Script crea estructura de directorios
- Proporciona comando de Kiro CLI a ejecutar

---

## Dependency Graph

```
Task 3 (Prompt Template)
    │
    ├──▶ Task 1 (Update JSONs with Tips) ──▶ Task 4 (UI Component)
    │
    ├──▶ Task 2 (SEQ JSON)
    │
    ├──▶ Task 5 (Diagram Templates)
    │
    └──▶ Task 6 (Validate Effort Matrix)
              │
              └──▶ Task 7 (Batch Script)
```

## Implementation Order

1. **Task 3** - Prompt Template (base para todo el workflow)
2. **Task 6** - Validar Effort Matrix (dependencia de costos)
3. **Task 1** - Actualizar JSONs existentes con tips
4. **Task 2** - Crear JSON de SEQ
5. **Task 4** - Actualizar UI para mostrar tips
6. **Task 5** - Templates de diagramas
7. **Task 7** - Script de automatización

## Estimated Effort

| Task | Effort | Priority |
|------|--------|----------|
| Task 1 | 30 min | Alta |
| Task 2 | 20 min | Alta |
| Task 3 | 15 min | Alta |
| Task 4 | 30 min | Media |
| Task 5 | 45 min | Media |
| Task 6 | 15 min | Alta |
| Task 7 | 10 min | Baja |
| **Total** | **~2.75 hrs** | |
