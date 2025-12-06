# Statement of Work (SOW) - AWS Early Business Adoption (EBA)
## MAP-BGR - Migration Acceleration Program

**Fecha**: 2025-12-05  
**Versión**: 1.0  
**Solicitante**: Banco General Rumiñahui (BGR)  
**País**: Ecuador  
**AWS Account Manager**: [NOMBRE_TAM]  
**Partner**: [NOMBRE_PARTNER]

---

## 1. Executive Summary

### 1.1 Propósito
Este Statement of Work (SOW) describe el alcance, objetivos y entregables para el programa de Early Business Adoption (EBA) de AWS para el proyecto MAP-BGR (Migration Acceleration Program) del Banco General Rumiñahui en Ecuador.

### 1.2 Objetivos del Programa EBA
- Acelerar la migración de 4 aplicaciones críticas de BGR desde on-premise a AWS
- Validar arquitecturas cloud-native y híbridas en producción
- Demostrar valor de negocio tangible con reducción de costos del 65%
- Establecer best practices replicables para las 4 aplicaciones restantes
- Capacitar al equipo de BGR en tecnologías AWS modernas

### 1.3 Solicitud de Fondos
**Monto Solicitado**: $15,000 USD  
**Duración**: 6 meses  
**Fecha Inicio Propuesta**: Enero 2026  
**Fecha Fin Propuesta**: Junio 2026

---

## 2. Información del Proyecto

### 2.1 Contexto del Cliente
**Cliente**: Banco General Rumiñahui (BGR)  
**Industria**: Servicios Financieros - Banca  
**Tamaño**: Banco regional con presencia en Ecuador  
**Ubicación**: Ecuador

**Situación Actual**:
- Infraestructura on-premise con 383 VMs en datacenter local
- 8 aplicaciones críticas de negocio ejecutándose en Windows Server 2016/2019
- Costos operativos elevados por licenciamiento (Windows, SQL Server)
- Limitaciones de escalabilidad y disponibilidad
- Procesos de deployment manuales (2+ horas por release)
- Falta de disaster recovery robusto

**Desafíos Actuales**:
- Alto costo de mantenimiento de infraestructura física
- Dificultad para escalar recursos según demanda
- Tiempo prolongado para implementar nuevas funcionalidades
- Riesgos de disponibilidad por infraestructura única
- Complejidad en gestión de actualizaciones y parches

**Motivación para AWS**:
- Reducir costos operativos y de licenciamiento
- Mejorar agilidad y time-to-market
- Implementar arquitecturas resilientes y escalables
- Adoptar prácticas DevOps y CI/CD
- Prepararse para transformación digital del sector financiero

### 2.2 Alcance del Proyecto
**Aplicaciones en Scope**: 4 aplicaciones (Fase 1 de 8 totales)  
**VMs a Migrar**: 15 VMs  
**Usuarios Impactados**: ~500 usuarios internos  
**Criticidad**: Media-Alta

**Aplicaciones Incluidas en EBA**:

1. **SARAS** (2 VMs)
   - Aplicación empresarial .NET/IIS con SQL Server
   - Estrategia: Modernización completa (ECS Fargate + Aurora Babelfish)
   - Timeline: 11 semanas
   - Costo AWS: $904/mes

2. **Api Portal** (5 VMs)
   - Portal web estático (HTML, CSS, JS)
   - Estrategia: Static Site Hosting (AWS Amplify + Azure DevOps CI/CD)
   - Timeline: 5 días
   - Costo AWS: $1.50/mes

3. **Backoffice Sistemas** (5 VMs)
   - Aplicación backoffice .NET/IIS
   - Estrategia: Lift & Shift híbrido (EC2 + VPN a BD on-premise)
   - Timeline: 3 semanas
   - Costo AWS: $402/mes

4. **SonarQube** (3 VMs)
   - Herramienta DevOps de análisis de código
   - Estrategia: Lift & Shift optimizado (EC2 Linux + RDS PostgreSQL)
   - Timeline: 2 semanas
   - Costo AWS: $404/mes

---

## 3. Descripción del Cliente

### 3.1 Perfil del Banco General Rumiñahui (BGR)

BGR es una institución financiera establecida en Ecuador que ofrece servicios bancarios integrales a clientes corporativos y retail. Como banco regional, BGR ha mantenido una infraestructura tecnológica tradicional basada en datacenters on-premise, lo cual ha sido suficiente para sus operaciones históricas pero presenta limitaciones significativas para su estrategia de transformación digital.

### 3.2 Situación Tecnológica Actual

#### Infraestructura On-Premise
BGR opera un datacenter local con:
- **383 máquinas virtuales** ejecutándose en VMware vSphere
- **1,752 vCPUs** y **5,924 GB de RAM** totales
- **14 hosts ESXi** con **33 datastores**
- Predominantemente **Windows Server 2016/2019**
- Múltiples instancias de **SQL Server** para bases de datos

#### Portafolio de Aplicaciones
El banco mantiene **8 aplicaciones críticas** que soportan operaciones diarias:

1. **SARAS**: Sistema empresarial para gestión de operaciones internas
2. **Api Portal**: Portal de APIs para integraciones externas
3. **Backoffice Sistemas**: Sistema de backoffice para operaciones administrativas
4. **SonarQube**: Plataforma de análisis de calidad de código
5. **Portal Guía BGR**: Portal de autoservicio para clientes
6. **Portal Administrativo BGR**: Portal de administración interna
7. **Backoffice Banca Digital**: Sistema de gestión de banca digital
8. **Seq**: Sistema centralizado de logging y monitoreo

#### Stack Tecnológico Predominante
- **Aplicaciones**: .NET Framework en IIS (Windows Server)
- **Bases de Datos**: Microsoft SQL Server
- **Infraestructura**: VMware vSphere
- **Deployment**: Procesos manuales (2+ horas por release)
- **Monitoreo**: Herramientas tradicionales on-premise

### 3.3 Desafíos de Negocio

#### Costos Operativos Elevados
- **Licenciamiento**: Costos significativos de Windows Server y SQL Server
- **Hardware**: Inversión continua en renovación de servidores físicos
- **Mantenimiento**: Personal dedicado a gestión de infraestructura física
- **Energía y Refrigeración**: Costos operativos del datacenter
- **Estimado actual**: ~$4,900/mes solo para las 4 aplicaciones en scope

#### Limitaciones de Escalabilidad
- Capacidad fija de recursos (no elastic)
- Tiempo prolongado para provisionar nuevos recursos (semanas)
- Dificultad para manejar picos de demanda
- Subutilización de recursos en períodos de baja demanda

#### Agilidad y Time-to-Market
- Deployments manuales que toman 2+ horas
- Falta de ambientes de desarrollo/staging consistentes
- Procesos de testing limitados
- Ciclos de release lentos (mensual o trimestral)

#### Riesgos Operacionales
- Datacenter único (sin disaster recovery robusto)
- Dependencia de hardware físico (single point of failure)
- Backups tradicionales con RPO/RTO elevados
- Dificultad para cumplir con SLAs de disponibilidad

### 3.4 Visión y Objetivos Estratégicos

#### Transformación Digital
BGR ha identificado la necesidad de modernizar su infraestructura tecnológica como parte de su estrategia de transformación digital. Los objetivos clave incluyen:

1. **Reducción de Costos**: Disminuir gastos operativos mediante eliminación de licencias y optimización de recursos
2. **Mejora de Agilidad**: Implementar prácticas DevOps y CI/CD para acelerar time-to-market
3. **Escalabilidad**: Adoptar arquitecturas elásticas que se adapten a la demanda
4. **Resiliencia**: Mejorar disponibilidad y disaster recovery
5. **Innovación**: Habilitar adopción de tecnologías modernas (contenedores, serverless, AI/ML)

#### Programa MAP (Migration Acceleration Program)
BGR ha iniciado un programa estructurado de migración a AWS con las siguientes fases:

**Fase 1 (EBA)**: Migrar 4 aplicaciones piloto (15 VMs)
- Validar estrategias de migración
- Establecer best practices
- Capacitar equipo interno
- Demostrar valor de negocio

**Fase 2**: Migrar 4 aplicaciones restantes (20 VMs)
- Replicar estrategias validadas
- Escalar capacidades del equipo
- Optimizar costos continuamente

**Fase 3**: Modernización continua
- Refactorizar aplicaciones legacy
- Adoptar servicios managed de AWS
- Implementar arquitecturas cloud-native

### 3.5 Caso de Negocio

#### Beneficios Financieros Proyectados (Fase 1 - EBA)
- **Costo Actual On-Premise**: $4,900/mes
- **Costo Proyectado AWS**: $1,711.50/mes
- **Ahorro Mensual**: $3,188.50 (65% reducción)
- **Ahorro Anual**: $38,262
- **ROI**: 4.7 meses

#### Beneficios Técnicos
- **Disponibilidad**: De 99.5% a 99.9%+
- **Deploy Time**: De 2 horas a 5 minutos (24x más rápido)
- **Escalabilidad**: Auto-scaling automático vs manual
- **Disaster Recovery**: RPO/RTO de minutos vs horas

#### Beneficios Operacionales
- **Automatización**: CI/CD completamente automatizado
- **Monitoreo**: Observabilidad integrada con CloudWatch
- **Seguridad**: Security best practices de AWS
- **Compliance**: Facilita cumplimiento regulatorio

### 3.6 Preparación para AWS

#### Assessment Completado
BGR ha completado un assessment exhaustivo utilizando:
- **RVTools**: Export completo de infraestructura VMware (383 VMs)
- **Cloudamize**: Análisis de utilización y recomendaciones
- **Application Discovery**: Mapeo de dependencias

#### Propuestas Técnicas Desarrolladas
Se han desarrollado propuestas detalladas para las 4 aplicaciones:
- Arquitecturas AWS específicas con diagramas
- Planes de migración paso a paso
- Estimaciones de costos detalladas
- Análisis de riesgos y mitigaciones
- Criterios de éxito definidos

#### Equipo Preparado
- **Project Sponsor**: Comprometido con la transformación
- **IT Manager**: Liderando el programa MAP
- **DevOps Team**: Identificado y disponible para capacitación
- **Application Owners**: Involucrados en el proceso

#### Compromiso Ejecutivo
La dirección de BGR ha aprobado:
- Presupuesto para el programa MAP
- Asignación de recursos dedicados
- Compromiso de asumir costos AWS post-EBA
- Visión de largo plazo para modernización completa

### 3.7 Alineación con Programa EBA

Este proyecto es ideal para el programa EBA de AWS porque:

✅ **Validación en Producción**: 4 aplicaciones reales con usuarios activos  
✅ **Diversidad de Estrategias**: Modernización, Static Site, Lift & Shift  
✅ **Tecnologías Innovadoras**: ECS Fargate, Aurora Babelfish, Amplify  
✅ **Caso de Éxito Replicable**: Modelo para sector financiero en Ecuador  
✅ **Compromiso del Cliente**: Equipo dedicado y presupuesto aprobado  
✅ **Impacto Medible**: Métricas claras de éxito (costos, performance, agilidad)  
✅ **Escalabilidad**: Base para migrar 4 aplicaciones adicionales  

---

*Continúa en la siguiente sección...*
