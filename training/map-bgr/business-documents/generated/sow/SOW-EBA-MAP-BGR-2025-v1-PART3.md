# SOW EBA MAP-BGR - Parte 3
## Secciones 8-13

---

## 8. Equipo del Proyecto

### 8.1 Equipo AWS
| Rol | Nombre | Responsabilidad | Dedicación |
|-----|--------|-----------------|------------|
| AWS Account Manager | [NOMBRE_TAM] | Gestión de cuenta y programa EBA | 10% |
| AWS Solutions Architect | [NOMBRE_SA] | Diseño de arquitecturas, best practices | 50% |
| AWS Migration Specialist | [NOMBRE_MS] | Ejecución de migraciones, troubleshooting | 40% |
| AWS Training Lead | [NOMBRE_TL] | Capacitación y workshops | 20% |

### 8.2 Equipo BGR
| Rol | Nombre | Responsabilidad | Dedicación |
|-----|--------|-----------------|------------|
| Project Sponsor | [NOMBRE] | Aprobaciones ejecutivas, presupuesto | 5% |
| IT Manager | [NOMBRE] | Gestión técnica del programa | 30% |
| DevOps Lead | [NOMBRE] | Implementación, CI/CD | 80% |
| DBA | [NOMBRE] | Migración de bases de datos | 50% |
| Network Engineer | [NOMBRE] | Configuración VPN, networking | 40% |
| Application Owner - SARAS | [NOMBRE] | Validación funcional | 20% |
| Application Owner - Api Portal | [NOMBRE] | Validación funcional | 10% |
| Application Owner - Backoffice | [NOMBRE] | Validación funcional | 20% |
| Application Owner - SonarQube | [NOMBRE] | Validación funcional | 10% |

### 8.3 Partner (si aplica)
| Rol | Empresa | Responsabilidad |
|-----|---------|-----------------|
| Migration Partner | [NOMBRE_PARTNER] | Soporte en implementación |

---

## 9. Entregables

### 9.1 Documentación Técnica
- [ ] **Assessment Report**: Análisis detallado de 4 aplicaciones
- [ ] **Arquitecturas Detalladas**: Diagramas y especificaciones por aplicación
- [ ] **Planes de Migración**: Paso a paso para cada aplicación
- [ ] **Runbooks de Operación**: Procedimientos operativos estándar
- [ ] **Documentación de Configuración**: IaC, scripts, configuraciones
- [ ] **Guías de Troubleshooting**: Resolución de problemas comunes
- [ ] **Security Best Practices**: Documentación de seguridad implementada

### 9.2 Infraestructura AWS
- [ ] **4 Aplicaciones Migradas**: SARAS, Api Portal, Backoffice, SonarQube
- [ ] **VPC Configurado**: Networking completo con subnets públicas/privadas
- [ ] **Site-to-Site VPN**: Conectividad híbrida a on-premise
- [ ] **CI/CD Pipelines**: Azure DevOps integrado con AWS
- [ ] **Monitoreo Completo**: CloudWatch logs, métricas, alarmas
- [ ] **Backups Automatizados**: Estrategia de backup para todas las apps
- [ ] **Security Baseline**: IAM roles, Security Groups, Secrets Manager

### 9.3 Capacitación
- [ ] **Workshop 1**: AWS Fundamentals (4 horas) - 10 personas
- [ ] **Workshop 2**: Amazon ECS & Containers (4 horas) - 5 personas
- [ ] **Workshop 3**: Aurora PostgreSQL & Babelfish (4 horas) - 3 personas
- [ ] **Workshop 4**: DevOps & CI/CD en AWS (4 horas) - 8 personas
- [ ] **Materiales de Training**: Presentaciones, labs, documentación
- [ ] **Hands-on Labs**: Ejercicios prácticos en ambiente AWS

### 9.4 Reportes
- [ ] **Reporte de Progreso Semanal**: Status, blockers, próximos pasos
- [ ] **Reporte Mensual Ejecutivo**: Resumen para stakeholders
- [ ] **Reporte Final del Proyecto**: Resultados, métricas, lecciones aprendidas
- [ ] **Caso de Éxito**: Documentación para marketing (con aprobación BGR)
- [ ] **Recomendaciones Futuras**: Roadmap para Fase 2 (4 apps restantes)

---

## 10. Criterios de Éxito

### 10.1 Técnicos
- [ ] **4 aplicaciones funcionando** en AWS en producción
- [ ] **Disponibilidad >99.9%** para aplicaciones críticas
- [ ] **Performance igual o mejor** que on-premise
- [ ] **Zero data loss** durante todas las migraciones
- [ ] **Security compliance** validado (best practices AWS)
- [ ] **CI/CD funcionando** con deploys automatizados
- [ ] **Monitoreo completo** con CloudWatch

### 10.2 Financieros
- [ ] **Costo mensual AWS <$2,000** ($1,711.50 target)
- [ ] **Ahorro de 65%** vs on-premise ($3,188/mes)
- [ ] **ROI alcanzado** en 4.7 meses
- [ ] **Presupuesto EBA** dentro de $15,000 solicitados

### 10.3 Operacionales
- [ ] **Deploy time reducido 95%** (de 2 horas a 5 minutos)
- [ ] **MTTR reducido 60%** con rollback instantáneo
- [ ] **95% de procesos automatizados** (CI/CD, backups, scaling)
- [ ] **Equipo capacitado** y autónomo (8-10 personas)
- [ ] **Documentación completa** entregada

### 10.4 Estratégicos
- [ ] **3 estrategias validadas** (Modernización, Static Site, Lift & Shift)
- [ ] **Modelo replicable** establecido para Fase 2
- [ ] **Caso de éxito** documentado
- [ ] **Roadmap Fase 2** aprobado

---

## 11. Riesgos y Mitigaciones

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| **Latencia VPN a BD on-premise** | Media | Alto | Testing exhaustivo pre-migración, considerar Direct Connect si >50ms |
| **Incompatibilidad Babelfish** | Baja | Alto | Assessment con Babelfish Compass, testing en dev, fallback a RDS SQL Server |
| **Resistencia al cambio del equipo** | Media | Medio | Training temprano, involucrar equipo desde inicio, quick wins |
| **Problemas de performance** | Baja | Alto | Load testing pre-producción, sizing adecuado, monitoreo proactivo |
| **Sobrecosto AWS** | Baja | Medio | Monitoreo de costos semanal, AWS Cost Explorer, alertas de presupuesto |
| **Downtime durante migración** | Media | Alto | Ventanas de mantenimiento planificadas, rollback plan, blue/green deployment |
| **Falta de skills AWS en equipo** | Alta | Medio | Training intensivo, documentación detallada, soporte AWS extendido |
| **Dependencias no documentadas** | Media | Alto | Application Discovery Service, testing exhaustivo, rollback plan |

---

## 12. Términos y Condiciones

### 12.1 Duración del Programa EBA
- **Inicio**: Enero 2026
- **Fin**: Junio 2026
- **Duración**: 6 meses

### 12.2 Compromisos del Cliente (BGR)
- ✅ Asignar recursos dedicados al proyecto (9 personas con dedicación parcial)
- ✅ Proveer acceso a sistemas y datos necesarios
- ✅ Participar activamente en sesiones de training (4 workshops)
- ✅ Asumir 100% de costos AWS post-EBA ($1,711.50/mes)
- ✅ Proveer feedback continuo y participar en revisiones semanales
- ✅ Aprobar caso de éxito para uso de AWS (con revisión previa)
- ✅ Comprometerse con Fase 2 (4 aplicaciones restantes) post-EBA

### 12.3 Compromisos de AWS
- ✅ Proveer fondos EBA de $15,000 según presupuesto aprobado
- ✅ Asignar equipo técnico especializado (SA, Migration Specialist)
- ✅ Proveer 4 workshops de training (16 horas totales)
- ✅ Soporte técnico durante los 6 meses del programa
- ✅ Revisiones semanales de progreso
- ✅ Acceso a AWS Support (Business o Enterprise)
- ✅ Documentación de caso de éxito

### 12.4 Condiciones de Éxito para Continuidad
- ✅ Cumplimiento de hitos definidos (8 hitos clave)
- ✅ Adopción activa de servicios AWS (4 aplicaciones en producción)
- ✅ Feedback positivo del cliente (encuestas trimestrales)
- ✅ Caso de éxito documentable y presentable
- ✅ Compromiso con Fase 2 del programa MAP

### 12.5 Términos Financieros
- **Fondos EBA**: $15,000 USD
- **Uso**: 60% Servicios Profesionales, 40% Servicios AWS
- **Facturación**: Mensual según avance del proyecto
- **Post-EBA**: BGR asume 100% costos AWS ($1,711.50/mes)

---

## 13. Aprobaciones

### 13.1 Cliente - Banco General Rumiñahui
**Nombre**: [NOMBRE_SPONSOR]  
**Cargo**: [CARGO - ej: CIO, VP Technology]  
**Empresa**: Banco General Rumiñahui  
**País**: Ecuador  
**Firma**: _______________  
**Fecha**: _______________

### 13.2 AWS
**Nombre**: [NOMBRE_TAM]  
**Cargo**: Technical Account Manager  
**Región**: LATAM  
**Firma**: _______________  
**Fecha**: _______________

### 13.3 Partner (si aplica)
**Nombre**: [NOMBRE_PARTNER_REP]  
**Cargo**: [CARGO]  
**Empresa**: [NOMBRE_PARTNER]  
**Firma**: _______________  
**Fecha**: _______________

---

## 14. Anexos

### Anexo A: Arquitecturas Detalladas
- Diagrama SARAS (ECS Fargate + Aurora Babelfish)
- Diagrama Api Portal (Amplify + Azure DevOps)
- Diagrama Backoffice Sistemas (EC2 + VPN Híbrido)
- Diagrama SonarQube (EC2 Linux + RDS PostgreSQL)
- Diagrama de Red (VPC, Subnets, VPN, Security Groups)

**Ubicación**: `/modernization-proposals/[app]/diagrams/`

### Anexo B: Planes de Migración Detallados
- SARAS_MODERNIZATION_PLAN.md (11 semanas, 5 fases)
- API_PORTAL_AZURE_DEVOPS_AMPLIFY.md (5 días, 4 fases)
- BACKOFFICE_SISTEMAS_LIFT_SHIFT.md (3 semanas, 3 fases)
- SONARQUBE_LIFT_SHIFT.md (2 semanas, 3 fases)

**Ubicación**: `/modernization-proposals/[app]/`

### Anexo C: Presupuesto Detallado
- Desglose de costos por servicio AWS
- Comparativa on-premise vs AWS
- Proyección de costos 12 meses
- Análisis de ROI

**Ubicación**: `/project-management/costs/EBA_COST_CALCULATOR_UPDATED.csv`

### Anexo D: Assessment Data
- RVTools Export (383 VMs)
- Cloudamize Analysis
- Application Discovery Report
- Dependency Mapping

**Ubicación**: `/assesment/`

### Anexo E: Casos de Uso Específicos

#### Caso de Uso 1: SARAS - Modernización sin Cambios de Código
**Desafío**: Migrar aplicación .NET con SQL Server sin refactorizar código  
**Solución**: Aurora PostgreSQL con Babelfish (puerto 1433, protocolo TDS)  
**Beneficio**: 50% ahorro vs RDS SQL Server, sin cambios de código  

#### Caso de Uso 2: Api Portal - Arquitectura Multi-Cloud
**Desafío**: Mantener CI/CD en Azure DevOps, hosting en AWS  
**Solución**: Azure Pipelines desplegando a AWS Amplify  
**Beneficio**: Best-of-breed, no vendor lock-in, 99.9% ahorro  

#### Caso de Uso 3: Backoffice - Migración Rápida con Roadmap
**Desafío**: Migrar rápido sin mover base de datos  
**Solución**: Lift & Shift a EC2 con VPN, roadmap de modernización  
**Beneficio**: 3 semanas de migración, valor inmediato, modernización futura  

#### Caso de Uso 4: SonarQube - Optimización en Migración
**Desafío**: Reducir costos de licenciamiento  
**Solución**: Cambio de SQL Server a PostgreSQL, Windows a Linux  
**Beneficio**: 73% ahorro, mejor performance  

---

## 15. Información de Contacto

### BGR - Banco General Rumiñahui
**Dirección**: [DIRECCION]  
**Ciudad**: [CIUDAD], Ecuador  
**Teléfono**: [TELEFONO]  
**Email**: [EMAIL]  
**Website**: [WEBSITE]

### AWS LATAM
**Account Manager**: [NOMBRE_TAM]  
**Email**: [EMAIL_TAM]  
**Teléfono**: [TELEFONO_TAM]

### Partner (si aplica)
**Empresa**: [NOMBRE_PARTNER]  
**Contacto**: [NOMBRE_CONTACTO]  
**Email**: [EMAIL_PARTNER]  
**Teléfono**: [TELEFONO_PARTNER]

---

**Última actualización**: 2025-12-05  
**Versión**: 1.0  
**Estado**: DRAFT - Pendiente de Aprobación  
**Próximo paso**: Revisión con AWS TAM y aprobación de BGR

---

## Resumen Ejecutivo para Aprobación

**Proyecto**: MAP-BGR Early Business Adoption  
**Cliente**: Banco General Rumiñahui, Ecuador  
**Alcance**: 4 aplicaciones, 15 VMs, 6 meses  
**Inversión EBA**: $15,000 USD  
**Ahorro Cliente**: $3,188/mes (65%), ROI 4.7 meses  
**Innovación**: Aurora Babelfish, Multi-cloud, Arquitectura Híbrida  
**Impacto**: Modelo replicable para sector financiero LATAM  

**Recomendación**: APROBAR ✅
