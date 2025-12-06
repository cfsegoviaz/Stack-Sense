# SOW EBA MAP-BGR - Parte 2 (Actualizada)
## Secciones 4-7

---

## 4. Objetivos del Proyecto

### 4.1 Objetivo General
Acelerar la migración de 4 aplicaciones críticas del Banco General Rumiñahui desde infraestructura on-premise hacia AWS, validando arquitecturas cloud-native y híbridas que demuestren valor de negocio tangible (65% reducción de costos) y establezcan patrones replicables para las 4 aplicaciones restantes del portafolio.

### 4.2 Objetivos Específicos

#### Objetivos Técnicos
- Migrar 4 aplicaciones críticas a AWS (15 VMs) utilizando 3 estrategias diferentes
- Implementar arquitectura cloud-native con ECS Fargate y Aurora Babelfish para SARAS
- Establecer arquitectura serverless con AWS Amplify para Api Portal
- Configurar arquitectura híbrida con Site-to-Site VPN para Backoffice Sistemas
- Optimizar SonarQube mediante migración de Windows/SQL Server a Linux/PostgreSQL
- Implementar CI/CD automatizado integrando Azure DevOps con AWS
- Configurar monitoreo y observabilidad centralizada con CloudWatch
- Establecer security best practices (Secrets Manager, Security Groups, IAM)

#### Objetivos de Negocio
- Reducir costos operativos en 65% (de $4,900/mes a $1,711.50/mes)
- Mejorar time-to-market en 95% (de 2 horas a 5 minutos por deployment)
- Aumentar disponibilidad de aplicaciones a 99.9%+ mediante arquitecturas Multi-AZ
- Capacitar 8-10 personas del equipo BGR en tecnologías AWS
- Establecer modelo replicable para migración de 4 aplicaciones restantes
- Documentar caso de éxito para sector financiero en Ecuador

#### Objetivos de Capacitación
- Transferir conocimiento en arquitecturas AWS (compute, database, networking)
- Capacitar en prácticas DevOps y CI/CD
- Entrenar en operación y troubleshooting de servicios AWS
- Desarrollar autonomía del equipo BGR para futuras migraciones

---

## 5. Alcance del Trabajo

### 5.1 En Alcance para el Partner

#### Fase de Planificación y Preparación del EBA Migration Party

**Actividades de Preparación (Semanas 1-2)**
- Kick-off meeting con stakeholders de BGR y AWS
- Validación de arquitecturas propuestas para las 4 aplicaciones
- Configuración de AWS Landing Zone (cuentas, VPC, subnets, security groups)
- Establecimiento de conectividad híbrida (Site-to-Site VPN)
- Configuración de herramientas de migración (AWS MGN, Database Migration Service)
- Preparación de ambientes de desarrollo, staging y producción
- Definición de runbooks de migración por aplicación
- Configuración de pipelines CI/CD base
- Setup de monitoreo y alarmas en CloudWatch
- Preparación de materiales de training

**Entregables de Preparación**
- [ ] AWS Landing Zone configurado y validado
- [ ] Site-to-Site VPN operativo con conectividad a on-premise
- [ ] Runbooks de migración documentados
- [ ] Ambientes AWS preparados (dev, staging, prod)
- [ ] Pipelines CI/CD base configurados

#### Fase EBA Migration Party y Close-out

**Migración de Aplicaciones (Semanas 3-24)**

**Api Portal (Semana 3 - 5 días)**
- Configuración de AWS Amplify Hosting
- Integración de Azure DevOps con AWS (OIDC authentication)
- Configuración de CloudFront CDN con certificado SSL
- Migración de contenido estático a S3
- Configuración de Route 53 para DNS
- Testing de CI/CD pipeline
- Cutover a producción

**SonarQube (Semanas 4-5 - 2 semanas)**
- Provisión de EC2 Linux (t3.xlarge)
- Configuración de RDS PostgreSQL Multi-AZ
- Migración de datos de SQL Server a PostgreSQL
- Configuración de EFS para shared storage
- Setup de Application Load Balancer
- Migración de configuraciones y plugins
- Testing y validación de análisis de código
- Cutover a producción

**Backoffice Sistemas (Semanas 6-8 - 3 semanas)**
- Provisión de EC2 Windows (2x t3.xlarge)
- Configuración de conectividad VPN a SQL Server on-premise
- Migración de aplicación .NET/IIS
- Configuración de Application Load Balancer
- Testing de conectividad híbrida
- Validación de funcionalidad con BD on-premise
- Cutover a producción

**SARAS (Semanas 9-19 - 11 semanas)**
- Containerización de aplicación .NET
- Configuración de Amazon ECR (container registry)
- Setup de ECS Fargate cluster
- Provisión de Aurora PostgreSQL con Babelfish
- Migración de datos de SQL Server a Aurora Babelfish
- Configuración de ElastiCache Redis
- Setup de Application Load Balancer
- Configuración de CI/CD completo
- Testing exhaustivo de funcionalidad
- Performance tuning
- Cutover a producción

**Optimización y Cierre (Semanas 20-24)**
- Optimización de costos (rightsizing, reserved instances)
- Fine-tuning de performance
- Documentación completa de arquitecturas
- Documentación de runbooks operacionales
- Training avanzado al equipo BGR
- Retrospectiva y lecciones aprendidas
- Documentación de caso de éxito

**Entregables de Migración**
- [ ] 4 aplicaciones migradas y operativas en AWS
- [ ] Pipelines CI/CD completamente automatizados
- [ ] Documentación técnica completa
- [ ] Runbooks operacionales
- [ ] Equipo BGR capacitado y autónomo
- [ ] Caso de éxito documentado

### 5.2 Fuera de Alcance para el Partner

**Responsabilidades Excluidas**
- Desarrollo de nuevas funcionalidades en las aplicaciones
- Refactorización de código legacy (excepto containerización de SARAS)
- Migración de las 4 aplicaciones restantes (Fase 2 del programa MAP)
- Soporte 24x7 post-migración (responsabilidad de BGR)
- Gestión de licencias de software de terceros
- Migración de bases de datos on-premise a AWS (excepto las 4 aplicaciones en scope)
- Configuración de Active Directory en AWS (se mantiene on-premise con VPN)
- Implementación de soluciones de backup de terceros
- Auditorías de seguridad o compliance (se proveen best practices)
- Gestión de cambios organizacionales o procesos de negocio

**Servicios No Incluidos**
- AWS Support Plan (responsabilidad de BGR)
- Licencias de software comercial (SQL Server, Windows Server on-premise)
- Costos de ancho de banda de ISP para VPN
- Hardware on-premise
- Servicios de consultoría post-EBA

### 5.3 Supuestos

**Supuestos Técnicos**
- BGR cuenta con infraestructura VMware vSphere operativa con acceso para assessment
- Aplicaciones actuales están documentadas y se conocen sus dependencias
- Bases de datos SQL Server tienen backups recientes y consistentes
- Existe ancho de banda suficiente para transferencia de datos (mínimo 100 Mbps)
- Firewall on-premise permite configuración de VPN Site-to-Site
- Aplicaciones pueden tolerar ventana de mantenimiento para cutover (4-8 horas)
- No existen dependencias críticas no documentadas entre aplicaciones

**Supuestos de Recursos**
- BGR asignará equipo dedicado (8-10 personas) durante el proyecto
- Personal de BGR tiene conocimientos básicos de AWS (o completará training previo)
- BGR cuenta con Project Sponsor con autoridad para toma de decisiones
- Equipo de BGR estará disponible para sesiones de trabajo y validaciones
- BGR proveerá acceso a ambientes on-premise y documentación técnica

**Supuestos de Negocio**
- BGR ha obtenido aprobaciones internas necesarias para el proyecto
- BGR asumirá costos AWS post-EBA ($1,711.50/mes)
- BGR se compromete a documentar y compartir caso de éxito con AWS
- No hay restricciones regulatorias que impidan uso de AWS
- BGR cuenta con presupuesto aprobado para Fase 2 (4 aplicaciones restantes)

**Supuestos de Cronograma**
- Proyecto inicia en Enero 2026
- No hay períodos de freeze por regulación bancaria durante el proyecto
- Ventanas de mantenimiento están disponibles según cronograma acordado
- No hay cambios mayores en alcance durante ejecución

---

## 6. Metodología y Enfoque

### 6.1 Fases del Servicio

El proyecto EBA MAP-BGR se estructura en **4 fases principales** con duración total de **6 meses**:

#### Fase 1: Preparación y Quick Wins (Mes 1)
**Duración**: 4 semanas  
**Objetivo**: Establecer fundamentos AWS y demostrar valor inmediato

**Actividades Clave**:
- Kick-off y alineamiento de equipos
- Configuración de AWS Landing Zone
- Establecimiento de conectividad VPN
- Migración de Api Portal (5 días)
- Migración de SonarQube (2 semanas)

**Criterios de Éxito**:
- Landing Zone operativo
- 2 aplicaciones en producción
- $3,094/mes de ahorro demostrado
- Equipo BGR familiarizado con AWS Console

#### Fase 2: Arquitectura Híbrida (Mes 2)
**Duración**: 4 semanas  
**Objetivo**: Validar modelo híbrido on-premise + AWS

**Actividades Clave**:
- Migración de Backoffice Sistemas
- Validación de conectividad VPN bajo carga
- Testing de latencia híbrida
- Documentación de patrones híbridos

**Criterios de Éxito**:
- Backoffice Sistemas operativo con BD on-premise
- VPN estable con <50ms latencia
- Runbook híbrido documentado

#### Fase 3: Modernización Cloud-Native (Meses 3-5)
**Duración**: 12 semanas  
**Objetivo**: Implementar arquitectura moderna con contenedores

**Actividades Clave**:
- Containerización de SARAS
- Implementación de ECS Fargate
- Migración a Aurora Babelfish
- Setup de CI/CD completo
- Performance tuning

**Criterios de Éxito**:
- SARAS containerizado en producción
- Aurora Babelfish con datos migrados
- CI/CD automatizado end-to-end
- Performance igual o superior a on-premise

#### Fase 4: Optimización y Cierre (Mes 6)
**Duración**: 4 semanas  
**Objetivo**: Optimizar, documentar y transferir conocimiento

**Actividades Clave**:
- Rightsizing de recursos
- Implementación de reserved instances
- Documentación completa
- Training avanzado
- Retrospectiva y lecciones aprendidas

**Criterios de Éxito**:
- 65% reducción de costos validada
- Documentación completa entregada
- Equipo BGR autónomo
- Caso de éxito documentado

### 6.2 Principios de Trabajo

#### Principio 1: Hands-On Learning
- **Enfoque**: Aprender haciendo, no solo observando
- **Implementación**: Equipo BGR ejecuta tareas con mentoría del partner
- **Beneficio**: Transferencia efectiva de conocimiento y autonomía

#### Principio 2: Iteración Rápida
- **Enfoque**: Ciclos cortos de implementación-validación-ajuste
- **Implementación**: Sprints de 1-2 semanas con demos frecuentes
- **Beneficio**: Detección temprana de issues y ajustes ágiles

#### Principio 3: Automatización First
- **Enfoque**: Automatizar desde el inicio, no como afterthought
- **Implementación**: CI/CD desde primera migración (Api Portal)
- **Beneficio**: Escalabilidad y repetibilidad para Fase 2

#### Principio 4: Well-Architected Framework
- **Enfoque**: Aplicar pilares de excelencia operacional, seguridad, confiabilidad, eficiencia y optimización de costos
- **Implementación**: Revisión de arquitecturas contra WAF checklist
- **Beneficio**: Arquitecturas robustas y best practices desde el inicio

#### Principio 5: Documentación Continua
- **Enfoque**: Documentar mientras se construye, no al final
- **Implementación**: Runbooks, diagramas y decisiones técnicas en tiempo real
- **Beneficio**: Knowledge base completo para operación y Fase 2

#### Principio 6: Seguridad by Design
- **Enfoque**: Seguridad integrada desde arquitectura, no como capa adicional
- **Implementación**: Secrets Manager, IAM least privilege, Security Groups restrictivos
- **Beneficio**: Compliance y reducción de superficie de ataque

---

## 7. Flujos de Trabajo y Actividades Detalladas

### 7.1 Workstream 1 – Estrategia y Gobierno de Migración

**Responsable**: Project Manager + AWS Solutions Architect  
**Objetivo**: Asegurar alineamiento estratégico, gestión de riesgos y comunicación efectiva

#### Actividades Principales

**Gobernanza del Proyecto**
- Gestión de cronograma y dependencias
- Tracking de hitos y entregables
- Gestión de riesgos e issues
- Comunicación con stakeholders
- Reportes de progreso semanales

**Gestión de Cambios**
- Evaluación de change requests
- Análisis de impacto en cronograma/presupuesto
- Aprobación de cambios con sponsor
- Actualización de documentación

**Gestión Financiera**
- Tracking de uso de fondos EBA
- Monitoreo de costos AWS
- Proyecciones de costos post-EBA
- Identificación de oportunidades de optimización

**Gestión de Riesgos**
- Identificación proactiva de riesgos
- Planes de mitigación
- Escalamiento de blockers
- Contingency planning

#### Entregables del Workstream 1
- [ ] Project charter y plan de proyecto
- [ ] Reportes de progreso semanales
- [ ] Risk register actualizado
- [ ] Change log documentado
- [ ] Reporte de cierre de proyecto

### 7.2 Workstream 2 – Arquitectura y Migración de Aplicaciones

**Responsable**: AWS Solutions Architect + Migration Specialist  
**Objetivo**: Diseñar, implementar y migrar las 4 aplicaciones a AWS

#### Actividades por Aplicación

**Api Portal - Static Site (Semana 3)**
- Diseño de arquitectura serverless con Amplify
- Configuración de S3 bucket y CloudFront
- Integración de Azure DevOps con AWS
- Migración de contenido estático
- Configuración de DNS en Route 53
- Testing de CI/CD pipeline
- Cutover y validación

**SonarQube - Lift & Shift Optimizado (Semanas 4-5)**
- Diseño de arquitectura EC2 + RDS
- Provisión de infraestructura con IaC
- Migración de SQL Server a PostgreSQL
- Configuración de EFS y backups
- Testing de análisis de código
- Cutover y validación

**Backoffice Sistemas - Híbrido (Semanas 6-8)**
- Diseño de arquitectura híbrida
- Configuración de VPN Site-to-Site
- Provisión de EC2 Windows
- Migración de aplicación .NET/IIS
- Testing de conectividad a BD on-premise
- Cutover y validación

**SARAS - Modernización (Semanas 9-19)**
- Diseño de arquitectura cloud-native
- Containerización de aplicación .NET
- Setup de ECS Fargate cluster
- Provisión de Aurora Babelfish
- Migración de datos SQL Server
- Configuración de ElastiCache Redis
- Implementación de CI/CD completo
- Testing exhaustivo y performance tuning
- Cutover y validación

#### Actividades Transversales
- Revisión de arquitecturas contra Well-Architected Framework
- Documentación de diagramas de arquitectura
- Creación de runbooks de deployment
- Testing de disaster recovery
- Validación de performance y escalabilidad

#### Entregables del Workstream 2
- [ ] Diagramas de arquitectura por aplicación
- [ ] Código de infraestructura (IaC)
- [ ] Pipelines CI/CD configurados
- [ ] Runbooks de deployment
- [ ] Documentación de decisiones técnicas
- [ ] Reportes de testing y validación

### 7.3 Workstream 3 – Plataforma, Seguridad y Operaciones

**Responsable**: AWS Security Specialist + DevOps Engineer  
**Objetivo**: Establecer fundamentos de plataforma, seguridad y operaciones

#### Actividades de Plataforma

**AWS Landing Zone**
- Configuración de AWS Organizations
- Setup de cuentas (dev, staging, prod)
- Configuración de VPC, subnets, route tables
- Setup de Internet Gateway y NAT Gateways
- Configuración de Security Groups base
- Setup de Network ACLs

**Conectividad Híbrida**
- Configuración de Virtual Private Gateway
- Setup de Customer Gateway on-premise
- Establecimiento de VPN Site-to-Site
- Configuración de routing BGP
- Testing de conectividad y latencia
- Documentación de troubleshooting

#### Actividades de Seguridad

**Identity & Access Management**
- Configuración de IAM roles y policies
- Setup de least privilege access
- Configuración de MFA para usuarios
- Setup de service accounts para CI/CD
- Auditoría de permisos

**Secrets Management**
- Configuración de AWS Secrets Manager
- Migración de credenciales a Secrets Manager
- Rotación automática de secrets
- Integración con aplicaciones

**Network Security**
- Configuración de Security Groups restrictivos
- Setup de Network ACLs
- Configuración de AWS WAF (si aplica)
- Setup de VPC Flow Logs
- Configuración de GuardDuty

**Compliance & Auditing**
- Configuración de AWS CloudTrail
- Setup de AWS Config
- Configuración de compliance rules
- Documentación de controles de seguridad

#### Actividades de Operaciones

**Monitoreo y Observabilidad**
- Configuración de CloudWatch Logs
- Setup de métricas custom
- Configuración de alarmas críticas
- Setup de dashboards operacionales
- Integración con herramientas existentes

**Backup y Disaster Recovery**
- Configuración de AWS Backup
- Setup de snapshots automatizados
- Documentación de procedimientos de restore
- Testing de disaster recovery
- Definición de RPO/RTO

**Automatización Operacional**
- Configuración de AWS Systems Manager
- Setup de patch management
- Configuración de maintenance windows
- Automatización de tareas operacionales
- Documentación de runbooks

#### Entregables del Workstream 3
- [ ] AWS Landing Zone documentado
- [ ] VPN Site-to-Site operativo
- [ ] Security baseline implementado
- [ ] Secrets Manager configurado
- [ ] CloudWatch dashboards y alarmas
- [ ] Runbooks operacionales
- [ ] Documentación de DR procedures

### 7.4 Eventos y Cadencia de Trabajo

#### Eventos Recurrentes

**Daily Standup (Lunes a Viernes)**
- **Duración**: 15 minutos
- **Participantes**: Equipos técnicos BGR + Partner
- **Objetivo**: Sincronización diaria, identificación de blockers
- **Formato**: ¿Qué hice ayer? ¿Qué haré hoy? ¿Tengo blockers?

**Weekly Status Meeting (Viernes)**
- **Duración**: 1 hora
- **Participantes**: Project Manager, Tech Leads, Sponsor BGR
- **Objetivo**: Revisión de progreso, riesgos, decisiones
- **Formato**: Dashboard de hitos, risk register, action items

**Sprint Planning (Inicio de cada sprint)**
- **Duración**: 2 horas
- **Participantes**: Equipos técnicos completos
- **Objetivo**: Planificar trabajo de próximas 1-2 semanas
- **Formato**: Backlog grooming, estimación, asignación

**Sprint Review/Demo (Fin de cada sprint)**
- **Duración**: 1 hora
- **Participantes**: Equipos + Stakeholders BGR
- **Objetivo**: Demostrar progreso, obtener feedback
- **Formato**: Demo en vivo de funcionalidad migrada

**Retrospectiva (Fin de cada sprint)**
- **Duración**: 1 hora
- **Participantes**: Equipos técnicos
- **Objetivo**: Mejora continua del proceso
- **Formato**: ¿Qué funcionó bien? ¿Qué mejorar? Action items

#### Eventos Especiales

**Kick-off Meeting (Semana 1)**
- **Duración**: 4 horas
- **Participantes**: Todos los stakeholders
- **Objetivo**: Alineamiento de expectativas, roles, cronograma
- **Formato**: Presentación de proyecto, Q&A, team building

**Architecture Review Sessions (Según necesidad)**
- **Duración**: 2 horas
- **Participantes**: Arquitectos BGR + AWS
- **Objetivo**: Validar diseños contra Well-Architected Framework
- **Formato**: Presentación de arquitectura, checklist WAF, recomendaciones

**Cutover Planning Meetings (Pre-cutover)**
- **Duración**: 2 horas
- **Participantes**: Equipos técnicos + Operations BGR
- **Objetivo**: Planificar ventana de mantenimiento y rollback
- **Formato**: Runbook review, go/no-go checklist, comunicaciones

**Training Workshops (Mensual)**
- **Duración**: 4 horas
- **Participantes**: Equipo BGR
- **Objetivo**: Capacitación hands-on en tecnologías AWS
- **Formato**: Teoría + laboratorios prácticos
- **Temas**: AWS Fundamentals, ECS/Fargate, Aurora, DevOps

**Project Close-out (Semana 24)**
- **Duración**: 4 horas
- **Participantes**: Todos los stakeholders
- **Objetivo**: Cierre formal, lecciones aprendidas, próximos pasos
- **Formato**: Presentación de resultados, retrospectiva, celebración

#### Canales de Comunicación

**Slack/Teams Channel**
- Comunicación asíncrona diaria
- Resolución rápida de dudas técnicas
- Compartir documentación y links

**Email**
- Comunicaciones formales
- Reportes semanales
- Aprobaciones y decisiones

**Confluence/Wiki**
- Documentación técnica centralizada
- Runbooks y procedimientos
- Decisiones de arquitectura (ADRs)

**Jira/Azure DevOps**
- Tracking de tareas y sprints
- Gestión de bugs e issues
- Reportes de progreso

---

*Continúa en la siguiente sección...*
