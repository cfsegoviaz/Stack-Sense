# Aplicaciones en Stack Sense Showcase

Este documento lista todas las aplicaciones incluidas en el showcase y sus diagramas asociados.

## 📊 Resumen

- **Total de Aplicaciones**: 5
- **Ahorro Mensual Estimado**: ~$4,900 USD
- **Ahorro Anual Estimado**: ~$59,000 USD

## 🎯 Aplicaciones

### 1. Api Portal
- **Estrategia**: Refactor (Serverless)
- **Tipo de Migración**: Static Site Hosting
- **Costo Actual**: $2,000/mes
- **Costo Objetivo**: $1.50/mes
- **Ahorro**: 99.9%
- **Diagrama**: `app_apiportal.png`
- **Stack Actual**: 5 VMs Windows, 42 vCPUs, 144GB RAM
- **Stack Objetivo**: AWS Amplify, S3 + CloudFront, Azure DevOps

**Insight**: El caso de éxito financiero más impactante. Se elimina completamente el mantenimiento de SO y licencias.

---

### 2. SARAS
- **Estrategia**: Replatform (Containerization)
- **Tipo de Migración**: ECS + Babelfish
- **Costo Actual**: $1,400/mes
- **Costo Objetivo**: $904/mes
- **Ahorro**: 35%
- **Diagrama**: `app_saras.png`
- **Stack Actual**: 2 VMs Windows, SQL Server, Monolito
- **Stack Objetivo**: ECS Fargate, Aurora Babelfish (PostgreSQL), Redis

**Insight**: Babelfish es la clave aquí: permite usar PostgreSQL sin reescribir el código T-SQL existente, ahorrando meses de desarrollo.

---

### 3. SonarQube
- **Estrategia**: Replatform (Optimized)
- **Tipo de Migración**: Lift & Shift Optimizado
- **Costo Actual**: $1,500/mes
- **Costo Objetivo**: $404/mes
- **Ahorro**: 73%
- **Diagrama**: `arch_sonarqube.png`
- **Stack Actual**: 3 VMs Windows, SQL Server, Infra dispersa
- **Stack Objetivo**: 1 EC2 Linux (Rightsized), RDS PostgreSQL, EFS

**Insight**: Pasar de Windows a Linux y de SQL Server a Postgres elimina costos de licencia y reduce overhead de recursos.

---

### 4. Backoffice Sistemas
- **Estrategia**: Rehost (Hybrid)
- **Tipo de Migración**: Lift & Shift Híbrido
- **Costo Actual**: On-Premise
- **Costo Objetivo**: $402/mes (AWS) + On-Premise
- **Ahorro**: TBD (Fase 3)
- **Diagrama**: `app_backoffice_sistemas.png`
- **Stack Actual**: On-Premise Datacenter, Conectividad Local
- **Stack Objetivo**: EC2 Windows, Site-to-Site VPN, SQL Server On-Prem

**Insight**: Estrategia de menor riesgo. Permite ganar escalabilidad en la web sin enfrentar la complejidad de migrar la BD data legacy inmediatamente.

---

### 5. Seq (Logs)
- **Estrategia**: Refactor (Native)
- **Tipo de Migración**: Modernización a CloudWatch
- **Costo Actual**: $1,833/mes
- **Costo Objetivo**: $278/mes
- **Ahorro**: 85%
- **Diagrama**: `arch_seq_cloudwatch.png`
- **Stack Actual**: 3 Windows Servers, SQL Server Enterprise, Monolito .NET
- **Stack Objetivo**: CloudWatch Logs, OpenSearch, Lambda

**Insight**: Elimina un punto único de fallo y costos masivos de licenciamiento Enterprise. Pasa a un modelo "Pay-as-you-go".

---

## 📁 Diagramas Adicionales

### Arquitectura General
- **Archivo**: `bgr_aws_architecture.png`
- **Descripción**: Vista general de la arquitectura AWS para BGR

### Flujo de Migración
- **Archivo**: `migration_flow.png`
- **Descripción**: Diagrama de flujo del proceso de migración

---

## 🔄 Actualización de Contenido

Para agregar una nueva aplicación:

1. Agregar el diagrama en `public/diagrams/`
2. Actualizar `src/App.tsx` con los datos de la aplicación
3. Actualizar este documento con la información
4. Ejecutar `./sync-diagrams.sh` si el diagrama está en el proyecto principal

---

## 📝 Notas

- Los costos son estimaciones basadas en el análisis de arquitectura
- Los ahorros no incluyen costos de migración ni capacitación
- Las estrategias pueden ajustarse según las necesidades del negocio
