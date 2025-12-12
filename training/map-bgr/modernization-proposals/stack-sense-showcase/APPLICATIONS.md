# Aplicaciones en Stack Sense Showcase

Este documento lista todas las aplicaciones incluidas en el showcase y sus diagramas asociados.

## 📊 Resumen

- **Total de Aplicaciones**: 5
- **Ahorro Mensual Estimado**: ~$5,179 USD
- **Ahorro Anual Estimado**: ~$62,148 USD

**Desglose de Ahorros**:
- Api Portal: $1,998.50/mes (99.9%)
- SARAS: $496/mes (35%)
- SonarQube: $1,096/mes (73%)
- Backoffice Sistemas: $279/mes (37%)
- Seq: $1,555/mes (85%)

**Inversión Inicial Estimada**:
- Direct Connect Setup: $2,500 (one-time)
- Migración y Testing: $15,000 - $25,000
- Training: $5,000
- **Total**: $22,500 - $32,500

**ROI**: 4-6 meses

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
- **Costo Actual**: $760/mes (On-Premise)
- **Costo Objetivo**: $481/mes (AWS Optimizado)
- **Ahorro**: 37% ($279/mes)
- **Diagrama**: `backoffice_sistemas_hybrid_architecture.png`
- **Stack Actual**: 2 VMs Windows (12 vCPUs, 40GB RAM), SQL Server 2016 Enterprise On-Prem, Load Balancer On-Prem
- **Stack Objetivo**: 2x EC2 t3.xlarge (Multi-AZ), ALB, Direct Connect (1 Gbps) + VPN Backup, SQL Server On-Prem, Azure DevOps CI/CD

**Detalles Técnicos**:
- **Usuarios**: 685 colaboradores BGR
- **Criticidad**: ALTA
- **Timeline**: 3 semanas
- **Stack**: .NET Framework 4.7.1 (Obsoleto)
- **Dependencias**: Active Directory (LDAP), Microservicio Notificador, BD Compartida (PORTAL_ADMINISTRATIVO_BGR)
- **SLA Target**: 99.9%
- **Conectividad**: Direct Connect 1 Gbps (latencia <10ms) + VPN Site-to-Site (backup)

**Insight**: Arquitectura híbrida de menor riesgo. Permite escalabilidad cloud sin migrar BD compartida por múltiples aplicaciones. Direct Connect garantiza latencia <10ms crítica para performance. Ahorro de $3,348/año (37%) vs on-premise. Base de datos permanece on-premise según reglas del proyecto BGR.

**Fases Futuras**:
- Fase 2 (6 meses): Migrar a .NET Core + Linux (ahorro adicional $100-150/mes)
- Fase 3 (12 meses): Evaluar migración BD a AWS RDS (ahorro adicional $100-200/mes)

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
