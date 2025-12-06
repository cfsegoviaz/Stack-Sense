# SOW EBA MAP-BGR - Parte 3 (Actualizada)
## Secciones 8-10

---

## 8. Entregables

### 8.1 Entregables Técnicos

#### Documentación de Arquitectura
- [ ] **Diagramas de Arquitectura AWS** (4 aplicaciones)
  - Diagramas de alto nivel (L1)
  - Diagramas detallados de componentes (L2)
  - Diagramas de red y seguridad (L3)
  - Formato: Draw.io + PNG exportados

- [ ] **Architecture Decision Records (ADRs)**
  - Decisiones técnicas documentadas con contexto y rationale
  - Alternativas consideradas y descartadas
  - Implicaciones de cada decisión
  - Formato: Markdown en repositorio

- [ ] **Well-Architected Framework Review**
  - Checklist de 6 pilares por aplicación
  - Recomendaciones de mejora
  - Plan de remediación de high-risk items
  - Formato: Excel + PDF report

#### Código y Configuración

- [ ] **Infrastructure as Code (IaC)**
  - Terraform/CloudFormation templates para toda la infraestructura
  - Módulos reutilizables por tipo de recurso
  - Variables parametrizadas por ambiente
  - README con instrucciones de uso
  - Formato: Repositorio Git

- [ ] **Pipelines CI/CD**
  - Azure DevOps pipelines para Api Portal
  - GitHub Actions/CodePipeline para otras aplicaciones
  - Scripts de deployment automatizados
  - Configuración de ambientes (dev, staging, prod)
  - Formato: YAML en repositorio

- [ ] **Código de Aplicaciones Containerizadas**
  - Dockerfiles para SARAS
  - Docker Compose para desarrollo local
  - Scripts de build y push a ECR
  - Formato: Repositorio Git

- [ ] **Scripts de Migración de Datos**
  - Scripts SQL para migración a Aurora Babelfish
  - Scripts de migración SQL Server → PostgreSQL (SonarQube)
  - Scripts de validación de integridad de datos
  - Rollback scripts
  - Formato: SQL + Python scripts

#### Documentación Operacional

- [ ] **Runbooks de Deployment**
  - Procedimientos paso a paso por aplicación
  - Checklists de pre-deployment
  - Procedimientos de rollback
  - Troubleshooting común
  - Formato: Markdown + Confluence

- [ ] **Runbooks de Operación**
  - Procedimientos de monitoreo diario
  - Respuesta a alarmas de CloudWatch
  - Procedimientos de escalamiento
  - Gestión de incidentes
  - Formato: Markdown + Confluence

- [ ] **Disaster Recovery Procedures**
  - Procedimientos de backup y restore
  - Testing de DR (resultados documentados)
  - RPO/RTO por aplicación
  - Contactos de escalamiento
  - Formato: PDF + Confluence

- [ ] **Security Runbooks**
  - Procedimientos de gestión de secrets
  - Rotación de credenciales
  - Respuesta a incidentes de seguridad
  - Auditoría de accesos
  - Formato: Markdown + Confluence

#### Configuración de Monitoreo

- [ ] **CloudWatch Dashboards**
  - Dashboard por aplicación con métricas clave
  - Dashboard consolidado de todas las aplicaciones
  - Dashboard de costos AWS
  - Exportación de configuración JSON
  - Formato: JSON + Screenshots

- [ ] **CloudWatch Alarms**
  - Alarmas críticas configuradas (CPU, memoria, errores)
  - Alarmas de costos (budget alerts)
  - Integración con SNS para notificaciones
  - Documentación de umbrales y rationale
  - Formato: IaC + Excel con listado

- [ ] **Logs Centralizados**
  - Configuración de CloudWatch Logs por aplicación
  - Log groups y retention policies
  - Queries útiles guardadas (CloudWatch Insights)
  - Formato: IaC + Markdown con queries

#### Documentación de Seguridad

- [ ] **Security Baseline**
  - Configuración de Security Groups documentada
  - IAM roles y policies documentadas
  - Network ACLs y routing tables
  - Secrets Manager configuration
  - Formato: Excel + Diagrams

- [ ] **Compliance Documentation**
  - CloudTrail configurado y validado
  - AWS Config rules implementadas
  - Evidencia de controles de seguridad
  - Reporte de compliance status
  - Formato: PDF report

#### Documentación de Costos

- [ ] **Cost Analysis Report**
  - Desglose de costos por aplicación
  - Comparativa on-premise vs AWS
  - Proyecciones de costos a 12 meses
  - Recomendaciones de optimización
  - Formato: Excel + PDF

- [ ] **Cost Optimization Plan**
  - Oportunidades de reserved instances
  - Rightsizing recommendations
  - Savings Plans analysis
  - Roadmap de optimización
  - Formato: Excel + PowerPoint

### 8.2 Entregables de Gestión y Cierre

#### Documentación de Proyecto

- [ ] **Project Charter**
  - Objetivos, alcance, stakeholders
  - Roles y responsabilidades
  - Cronograma de alto nivel
  - Formato: PDF

- [ ] **Reportes de Progreso Semanales**
  - Status de hitos y entregables
  - Riesgos e issues
  - Próximos pasos
  - Formato: PowerPoint (24 reportes)

- [ ] **Risk Register**
  - Riesgos identificados con probabilidad e impacto
  - Planes de mitigación
  - Status de riesgos (abierto/cerrado)
  - Formato: Excel

- [ ] **Change Log**
  - Cambios de alcance documentados
  - Aprobaciones de cambios
  - Impacto en cronograma/presupuesto
  - Formato: Excel

#### Documentación de Capacitación

- [ ] **Training Materials**
  - Presentaciones de workshops (4 sesiones)
  - Laboratorios hands-on con instrucciones
  - Grabaciones de sesiones de training
  - Formato: PowerPoint + Videos

- [ ] **Knowledge Transfer Sessions**
  - Sesiones de transferencia por workstream
  - Documentación de Q&A
  - Contactos de soporte post-EBA
  - Formato: PowerPoint + Markdown

#### Documentación de Cierre

- [ ] **Lessons Learned Report**
  - Retrospectiva del proyecto completo
  - Qué funcionó bien / qué mejorar
  - Recomendaciones para Fase 2
  - Formato: PowerPoint + PDF

- [ ] **Project Close-out Report**
  - Resumen ejecutivo de resultados
  - Comparativa de objetivos vs logros
  - Métricas de éxito validadas
  - Próximos pasos y roadmap
  - Formato: PowerPoint + PDF

- [ ] **Case Study / Success Story**
  - Narrativa del proyecto para publicación
  - Métricas de negocio y técnicas
  - Testimoniales de BGR
  - Formato: PDF + Blog post draft

#### Entregables Financieros

- [ ] **Final Budget Report**
  - Uso de fondos EBA detallado
  - Costos AWS durante el proyecto
  - Proyección de costos post-EBA
  - Formato: Excel

- [ ] **ROI Analysis**
  - Cálculo de ROI validado
  - Ahorro mensual/anual demostrado
  - Beneficios tangibles e intangibles
  - Formato: Excel + PowerPoint

---

## 9. Cronograma / Planificación

### 9.1 Vista de Alto Nivel

| Fase | Duración | Inicio | Fin | Aplicaciones | Hitos Clave |
|------|----------|--------|-----|--------------|-------------|
| **Fase 1: Preparación y Quick Wins** | 4 semanas | Sem 1 | Sem 4 | Api Portal, SonarQube | Landing Zone, 2 apps en prod |
| **Fase 2: Arquitectura Híbrida** | 4 semanas | Sem 5 | Sem 8 | Backoffice Sistemas | VPN operativo, app híbrida |
| **Fase 3: Modernización Cloud-Native** | 12 semanas | Sem 9 | Sem 20 | SARAS | Contenedores, Aurora Babelfish |
| **Fase 4: Optimización y Cierre** | 4 semanas | Sem 21 | Sem 24 | Todas | Optimización, documentación |
| **TOTAL** | **24 semanas (6 meses)** | **Ene 2026** | **Jun 2026** | **4 aplicaciones** | **15 VMs migradas** |

### 9.2 Hitos Clave

#### Mes 1: Preparación y Quick Wins

| Semana | Hito | Descripción | Criterio de Éxito | Responsable |
|--------|------|-------------|-------------------|-------------|
| **Sem 1** | Kick-off Proyecto | Alineamiento de equipos y objetivos | Todos los stakeholders alineados | PM |
| **Sem 1** | Landing Zone Configurado | AWS accounts, VPC, subnets, security groups | Infraestructura base operativa | Workstream 3 |
| **Sem 1** | VPN Site-to-Site Operativo | Conectividad híbrida establecida | Ping exitoso on-premise ↔ AWS | Workstream 3 |
| **Sem 1** | Api Portal en Producción | Primera aplicación migrada | Sitio accesible, CI/CD funcionando | Workstream 2 |
| **Sem 3** | SonarQube en Producción | Segunda aplicación migrada | Análisis de código funcionando | Workstream 2 |
| **Sem 4** | Training Workshop 1 | AWS Fundamentals | Equipo BGR capacitado en basics | Workstream 1 |

**Entregables Mes 1**:
- ✅ 2 aplicaciones en producción (Api Portal, SonarQube)
- ✅ $3,094/mes de ahorro demostrado
- ✅ Landing Zone documentado
- ✅ Equipo BGR con conocimientos básicos AWS

#### Mes 2: Arquitectura Híbrida

| Semana | Hito | Descripción | Criterio de Éxito | Responsable |
|--------|------|-------------|-------------------|-------------|
| **Sem 5** | Inicio Migración Backoffice | Provisión de infraestructura EC2 | EC2 instances operativas | Workstream 2 |
| **Sem 6** | Testing Conectividad Híbrida | Validación de VPN bajo carga | Latencia <50ms, throughput OK | Workstream 3 |
| **Sem 7** | Backoffice en Producción | Tercera aplicación migrada | App funcionando con BD on-premise | Workstream 2 |
| **Sem 8** | Training Workshop 2 | Networking & Security | Equipo BGR capacitado en VPN/SG | Workstream 1 |

**Entregables Mes 2**:
- ✅ 3 aplicaciones en producción (+ Backoffice Sistemas)
- ✅ Arquitectura híbrida validada
- ✅ Runbook de operación híbrida
- ✅ $3,490/mes de ahorro acumulado

#### Meses 3-5: Modernización Cloud-Native

| Semana | Hito | Descripción | Criterio de Éxito | Responsable |
|--------|------|-------------|-------------------|-------------|
| **Sem 9** | Inicio Modernización SARAS | Kick-off de containerización | Plan de trabajo aprobado | Workstream 2 |
| **Sem 11** | SARAS Containerizado (Dev) | Aplicación en contenedores | Contenedor funcional en local | Workstream 2 |
| **Sem 13** | ECS Fargate Configurado | Cluster ECS operativo | Tasks ejecutándose en Fargate | Workstream 2 |
| **Sem 15** | Aurora Babelfish Provisionado | Base de datos lista | Babelfish respondiendo en puerto 1433 | Workstream 2 |
| **Sem 16** | Training Workshop 3 | ECS & Containers | Equipo BGR capacitado en ECS | Workstream 1 |
| **Sem 17** | Migración de Datos Completada | Datos en Aurora Babelfish | Validación de integridad OK | Workstream 2 |
| **Sem 18** | CI/CD Pipeline Completo | Automatización end-to-end | Deploy automatizado dev→prod | Workstream 2 |
| **Sem 19** | SARAS en Producción | Cuarta aplicación migrada | App funcionando en ECS + Aurora | Workstream 2 |
| **Sem 20** | Training Workshop 4 | DevOps & CI/CD | Equipo BGR capacitado en pipelines | Workstream 1 |

**Entregables Meses 3-5**:
- ✅ 4 aplicaciones en producción (+ SARAS)
- ✅ Arquitectura cloud-native implementada
- ✅ CI/CD completamente automatizado
- ✅ $3,188/mes de ahorro total (65% reducción)

#### Mes 6: Optimización y Cierre

| Semana | Hito | Descripción | Criterio de Éxito | Responsable |
|--------|------|-------------|-------------------|-------------|
| **Sem 21** | Rightsizing Completado | Optimización de recursos | Costos reducidos sin impacto | Workstream 2 |
| **Sem 22** | Reserved Instances Implementadas | Optimización de costos | 30-40% ahorro adicional | Workstream 1 |
| **Sem 22** | Documentación Completa | Todos los entregables listos | Documentación aprobada por BGR | Todos |
| **Sem 23** | Knowledge Transfer Completado | Transferencia final | Equipo BGR autónomo | Workstream 1 |
| **Sem 24** | Retrospectiva Final | Lecciones aprendidas | Recomendaciones para Fase 2 | PM |
| **Sem 24** | Project Close-out | Cierre formal del proyecto | Aceptación formal de BGR | PM |

**Entregables Mes 6**:
- ✅ Todas las aplicaciones optimizadas
- ✅ Documentación completa entregada
- ✅ Equipo BGR autónomo
- ✅ Caso de éxito documentado
- ✅ Roadmap para Fase 2 definido

### 9.3 Cronograma Detallado por Aplicación

#### Api Portal (Semana 1 - 5 días)
| Día | Actividad | Responsable |
|-----|-----------|-------------|
| Día 1 | Configuración de AWS Amplify + S3 | Workstream 2 |
| Día 2 | Integración Azure DevOps con AWS (OIDC) | Workstream 2 |
| Día 3 | Configuración CloudFront + Route 53 | Workstream 2 |
| Día 4 | Migración de contenido y testing | Workstream 2 |
| Día 5 | Cutover a producción y validación | Workstream 2 |

#### SonarQube (Semanas 2-3 - 2 semanas)
| Semana | Actividad | Responsable |
|--------|-----------|-------------|
| Sem 2 | Provisión EC2 + RDS PostgreSQL | Workstream 2 |
| Sem 2 | Migración SQL Server → PostgreSQL | Workstream 2 |
| Sem 3 | Configuración SonarQube + plugins | Workstream 2 |
| Sem 3 | Testing y cutover a producción | Workstream 2 |

#### Backoffice Sistemas (Semanas 5-7 - 3 semanas)
| Semana | Actividad | Responsable |
|--------|-----------|-------------|
| Sem 5 | Provisión EC2 Windows + ALB | Workstream 2 |
| Sem 6 | Migración aplicación .NET/IIS | Workstream 2 |
| Sem 6 | Testing conectividad VPN a BD | Workstream 2 |
| Sem 7 | Testing funcional y cutover | Workstream 2 |

#### SARAS (Semanas 9-19 - 11 semanas)
| Semana | Actividad | Responsable |
|--------|-----------|-------------|
| Sem 9-10 | Containerización de aplicación | Workstream 2 |
| Sem 11-12 | Setup ECS Fargate + ECR | Workstream 2 |
| Sem 13-14 | Provisión Aurora Babelfish | Workstream 2 |
| Sem 15-16 | Migración de datos | Workstream 2 |
| Sem 17 | Configuración ElastiCache Redis | Workstream 2 |
| Sem 18 | Implementación CI/CD completo | Workstream 2 |
| Sem 19 | Testing exhaustivo y cutover | Workstream 2 |

---

## 10. Dependencias del Cliente

### 10.1 Responsabilidades del Cliente – Preparación

#### Accesos y Permisos

**AWS Account**
- [ ] Crear AWS account o proveer acceso a account existente
- [ ] Configurar billing alerts y presupuestos
- [ ] Proveer acceso de administrador al equipo del partner
- [ ] Configurar MFA para usuarios privilegiados
- **Timeline**: Antes de Semana 1

**Acceso a Infraestructura On-Premise**
- [ ] Proveer acceso VPN a datacenter on-premise
- [ ] Proveer credenciales de vSphere/vCenter
- [ ] Proveer acceso a servidores de aplicaciones
- [ ] Proveer acceso a bases de datos SQL Server
- [ ] Proveer acceso a firewall para configuración VPN
- **Timeline**: Antes de Semana 1

**Acceso a Herramientas**
- [ ] Proveer acceso a Azure DevOps (si aplica)
- [ ] Proveer acceso a repositorios de código fuente
- [ ] Proveer acceso a herramientas de monitoreo existentes
- **Timeline**: Antes de Semana 1

#### Documentación y Conocimiento

**Documentación Técnica**
- [ ] Proveer documentación de arquitectura actual
- [ ] Proveer diagramas de red on-premise
- [ ] Proveer inventario de aplicaciones y dependencias
- [ ] Proveer documentación de bases de datos (schemas, tamaños)
- [ ] Proveer runbooks de deployment actuales
- **Timeline**: Antes de Semana 1

**Información de Negocio**
- [ ] Proveer SLAs de aplicaciones
- [ ] Proveer ventanas de mantenimiento permitidas
- [ ] Proveer información de usuarios y volumetría
- [ ] Proveer información de compliance y regulaciones
- **Timeline**: Antes de Semana 1

#### Recursos Humanos

**Equipo Dedicado**
- [ ] Asignar Project Sponsor con autoridad de decisión
- [ ] Asignar IT Manager como punto de contacto principal
- [ ] Asignar 8-10 personas del equipo técnico (disponibilidad 50-100%)
- [ ] Identificar Application Owners por aplicación
- [ ] Identificar Database Administrators
- [ ] Identificar Network/Security Engineers
- **Timeline**: Antes de Semana 1

**Disponibilidad del Equipo**
- [ ] Garantizar disponibilidad para daily standups (15 min/día)
- [ ] Garantizar disponibilidad para weekly status meetings (1 hora/semana)
- [ ] Garantizar disponibilidad para training workshops (4 horas/mes)
- [ ] Garantizar disponibilidad para cutover windows (4-8 horas por app)
- **Timeline**: Durante todo el proyecto

#### Infraestructura y Conectividad

**Ancho de Banda**
- [ ] Validar ancho de banda disponible (mínimo 100 Mbps)
- [ ] Coordinar con ISP si se requiere upgrade
- [ ] Validar que no hay restricciones de transferencia de datos
- **Timeline**: Antes de Semana 1

**Firewall y Seguridad**
- [ ] Aprobar reglas de firewall para VPN Site-to-Site
- [ ] Aprobar reglas de firewall para acceso a AWS services
- [ ] Coordinar con equipo de seguridad para whitelisting
- **Timeline**: Antes de Semana 2

#### Aprobaciones y Presupuesto

**Aprobaciones Internas**
- [ ] Obtener aprobación ejecutiva para el proyecto
- [ ] Obtener aprobación de seguridad/compliance
- [ ] Obtener aprobación de cambios en producción
- **Timeline**: Antes de Semana 1

**Presupuesto**
- [ ] Aprobar presupuesto para costos AWS post-EBA ($1,711.50/mes)
- [ ] Aprobar presupuesto para Fase 2 (4 aplicaciones restantes)
- [ ] Aprobar presupuesto para training adicional (si requerido)
- **Timeline**: Antes de Semana 1

### 10.2 Responsabilidades del Cliente – Durante el EBA Migration Party y Cierre

#### Participación Activa

**Sesiones de Trabajo**
- [ ] Participar activamente en daily standups
- [ ] Participar en sprint planning y retrospectivas
- [ ] Participar en architecture review sessions
- [ ] Participar en training workshops
- **Timeline**: Durante todo el proyecto

**Validaciones y Testing**
- [ ] Ejecutar testing funcional de aplicaciones migradas
- [ ] Validar performance de aplicaciones
- [ ] Validar integridad de datos migrados
- [ ] Aprobar go/no-go para cutover a producción
- **Timeline**: Según cronograma de cada aplicación

#### Soporte Operacional

**Durante Migraciones**
- [ ] Proveer soporte de aplicaciones durante cutover
- [ ] Proveer soporte de bases de datos durante migración de datos
- [ ] Proveer soporte de red durante configuración VPN
- [ ] Estar disponible para troubleshooting 24x7 durante cutover
- **Timeline**: Durante ventanas de cutover

**Post-Migración**
- [ ] Monitorear aplicaciones migradas en producción
- [ ] Reportar issues o anomalías inmediatamente
- [ ] Ejecutar runbooks de operación diaria
- [ ] Gestionar incidentes de producción
- **Timeline**: Post-cutover de cada aplicación

#### Toma de Decisiones

**Decisiones Técnicas**
- [ ] Aprobar arquitecturas propuestas
- [ ] Aprobar cambios de alcance (si aplica)
- [ ] Aprobar trade-offs técnicos
- [ ] Aprobar planes de rollback
- **Timeline**: Según necesidad durante el proyecto

**Decisiones de Negocio**
- [ ] Aprobar ventanas de mantenimiento
- [ ] Aprobar comunicaciones a usuarios
- [ ] Aprobar cambios de cronograma (si aplica)
- [ ] Aprobar presupuesto adicional (si aplica)
- **Timeline**: Según necesidad durante el proyecto

#### Documentación y Knowledge Transfer

**Colaboración en Documentación**
- [ ] Revisar y aprobar documentación técnica
- [ ] Proveer feedback en runbooks
- [ ] Validar procedimientos operacionales
- [ ] Contribuir a lecciones aprendidas
- **Timeline**: Durante todo el proyecto

**Participación en Training**
- [ ] Asistir a todos los training workshops
- [ ] Completar laboratorios hands-on
- [ ] Hacer preguntas y aclarar dudas
- [ ] Practicar procedimientos aprendidos
- **Timeline**: Según cronograma de training

#### Cierre del Proyecto

**Aceptación de Entregables**
- [ ] Revisar todos los entregables técnicos
- [ ] Revisar documentación completa
- [ ] Validar que se cumplieron objetivos
- [ ] Firmar aceptación formal del proyecto
- **Timeline**: Semana 24

**Caso de Éxito**
- [ ] Proveer testimoniales para caso de éxito
- [ ] Aprobar publicación de caso de éxito
- [ ] Participar en webinar/evento de AWS (opcional)
- [ ] Proveer métricas de negocio validadas
- **Timeline**: Semana 24

**Transición a Operación**
- [ ] Asumir operación completa de aplicaciones en AWS
- [ ] Asumir costos AWS post-EBA ($1,711.50/mes)
- [ ] Implementar mejora continua
- [ ] Planificar Fase 2 (4 aplicaciones restantes)
- **Timeline**: Post-Semana 24

---

## 11. Criterios de Éxito

### 11.1 Criterios Técnicos

| Criterio | Métrica | Target | Método de Validación |
|----------|---------|--------|----------------------|
| **Aplicaciones Migradas** | Número de apps en producción | 4/4 (100%) | Validación en AWS Console |
| **Disponibilidad** | Uptime de aplicaciones | ≥99.9% | CloudWatch metrics |
| **Performance** | Latencia de respuesta | ≤ on-premise | Load testing |
| **Integridad de Datos** | Datos migrados correctamente | 100% | Queries de validación |
| **CI/CD Funcional** | Deployments automatizados | 100% | Testing de pipelines |
| **Seguridad** | Controles implementados | 100% | Security audit |

### 11.2 Criterios de Negocio

| Criterio | Métrica | Target | Método de Validación |
|----------|---------|--------|----------------------|
| **Reducción de Costos** | Ahorro mensual | $3,188/mes (65%) | AWS Cost Explorer |
| **Time-to-Market** | Tiempo de deployment | <5 minutos (95% mejora) | Medición de pipelines |
| **ROI** | Retorno de inversión | <6 meses | Cálculo financiero |
| **Capacitación** | Personas capacitadas | 8-10 personas | Asistencia a workshops |

### 11.3 Criterios de Calidad

| Criterio | Métrica | Target | Método de Validación |
|----------|---------|--------|----------------------|
| **Documentación** | Entregables completados | 100% | Checklist de entregables |
| **Knowledge Transfer** | Autonomía del equipo BGR | 80%+ | Assessment post-training |
| **Satisfacción** | NPS del cliente | ≥8/10 | Encuesta de satisfacción |

---

## 12. Gestión de Riesgos

### 12.1 Riesgos Identificados

| ID | Riesgo | Probabilidad | Impacto | Mitigación |
|----|--------|--------------|---------|------------|
| R1 | Incompatibilidad de aplicación con Babelfish | Media | Alto | Testing exhaustivo en dev, plan B con RDS SQL Server |
| R2 | Latencia elevada en arquitectura híbrida | Media | Medio | Testing de latencia, optimización de queries |
| R3 | Falta de disponibilidad del equipo BGR | Media | Alto | Compromiso de sponsor, escalamiento temprano |
| R4 | Problemas de conectividad VPN | Baja | Alto | Redundancia de VPN, plan de rollback |
| R5 | Sobrecostos AWS por mal dimensionamiento | Media | Medio | Rightsizing continuo, alertas de costos |
| R6 | Pérdida de datos durante migración | Baja | Crítico | Backups completos, validación exhaustiva |
| R7 | Resistencia al cambio del equipo | Media | Medio | Training temprano, comunicación continua |

---

## 13. Términos y Condiciones

### 13.1 Duración del Proyecto
- **Inicio**: Enero 2026
- **Fin**: Junio 2026
- **Duración Total**: 6 meses (24 semanas)

### 13.2 Fondos EBA
- **Monto Solicitado**: $15,000 USD
- **Uso**: 60% servicios profesionales, 40% servicios AWS
- **Compromiso del Cliente**: Asumir costos AWS post-EBA ($1,711.50/mes)

### 13.3 Propiedad Intelectual
- Todo el código, documentación y entregables son propiedad de BGR
- BGR otorga permiso a AWS para documentar caso de éxito (con aprobación previa)

### 13.4 Confidencialidad
- Toda la información del proyecto es confidencial
- Se requiere NDA firmado por todas las partes

---

## 14. Aprobaciones

### 14.1 Banco General Rumiñahui

**Project Sponsor**  
Nombre: ___________________________  
Cargo: ___________________________  
Firma: ___________________________  
Fecha: ___________________________

**IT Manager**  
Nombre: ___________________________  
Cargo: ___________________________  
Firma: ___________________________  
Fecha: ___________________________

### 14.2 AWS

**Account Manager**  
Nombre: ___________________________  
Cargo: ___________________________  
Firma: ___________________________  
Fecha: ___________________________

**Solutions Architect**  
Nombre: ___________________________  
Cargo: ___________________________  
Firma: ___________________________  
Fecha: ___________________________

### 14.3 Partner (Escala 24x7)

**Project Manager**  
Nombre: ___________________________  
Cargo: ___________________________  
Firma: ___________________________  
Fecha: ___________________________

---

**FIN DEL DOCUMENTO**
