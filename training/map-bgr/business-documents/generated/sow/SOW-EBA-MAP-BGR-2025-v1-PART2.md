# SOW EBA MAP-BGR - Parte 2
## Secciones 4-7

---

## 4. Objetivos y Beneficios

### 4.1 Objetivos Técnicos
- [ ] Migrar 4 aplicaciones críticas a AWS (15 VMs)
- [ ] Implementar 3 estrategias de migración diferentes (Modernización, Static Site, Lift & Shift)
- [ ] Establecer CI/CD automatizado con Azure DevOps + AWS
- [ ] Configurar monitoreo y observabilidad con CloudWatch
- [ ] Implementar security best practices (Secrets Manager, Security Groups, IAM)
- [ ] Configurar conectividad híbrida (Site-to-Site VPN)
- [ ] Establecer disaster recovery con backups automatizados

### 4.2 Objetivos de Negocio
- [ ] Reducir costos operativos en 65% ($3,188/mes ahorro)
- [ ] Mejorar time-to-market en 95% (de 2 horas a 5 minutos)
- [ ] Aumentar disponibilidad a 99.9%+
- [ ] Reducir incidentes operacionales en 80%
- [ ] Capacitar 8-10 personas del equipo BGR en AWS
- [ ] Establecer modelo replicable para 4 aplicaciones restantes

### 4.3 Beneficios Esperados

#### Financieros
- **Reducción de Costos**: $3,188.50/mes (65% ahorro)
- **ROI Esperado**: 4.7 meses
- **Ahorro Anual**: $38,262
- **Eliminación de Licencias**: SQL Server, Windows Server

#### Técnicos
- **Escalabilidad**: Auto-scaling automático (ECS, Amplify)
- **Disponibilidad**: 99.9%+ uptime con Multi-AZ
- **Performance**: 10x mejora en latencia global (CloudFront CDN)
- **Seguridad**: Compliance con best practices AWS

#### Operacionales
- **Deploy Time**: De 2 horas a 5 minutos (24x más rápido)
- **MTTR**: Reducción de 60% con rollback instantáneo
- **Automatización**: 95% de procesos automatizados
- **Monitoreo**: Observabilidad completa con CloudWatch

---

## 5. Arquitectura Propuesta

### 5.1 Servicios AWS a Utilizar

#### Compute
- **Amazon ECS Fargate**: Contenedores serverless para SARAS
- **Amazon EC2**: Instancias para Backoffice Sistemas y SonarQube
- **AWS Amplify**: Hosting serverless para Api Portal

#### Database
- **Amazon Aurora PostgreSQL con Babelfish**: Para SARAS (compatibilidad SQL Server)
- **Amazon RDS PostgreSQL**: Para SonarQube
- **Conectividad Híbrida**: VPN a SQL Server on-premise (Backoffice Sistemas)

#### Networking
- **Application Load Balancer**: Distribución de tráfico HTTPS
- **Amazon CloudFront**: CDN global para Api Portal
- **Site-to-Site VPN**: Conectividad híbrida a on-premise
- **Amazon Route 53**: DNS management

#### Storage
- **Amazon S3**: Backups, assets estáticos, container registry
- **Amazon EBS**: Discos para EC2 instances
- **Amazon EFS**: Shared storage para SonarQube

#### Security
- **AWS Secrets Manager**: Gestión de credenciales
- **AWS Certificate Manager**: Certificados SSL/TLS gratuitos
- **AWS IAM**: Control de acceso granular
- **Security Groups**: Firewall a nivel de instancia

#### Monitoring & DevOps
- **Amazon CloudWatch**: Logs, métricas, alarmas
- **AWS Systems Manager**: Gestión de instancias
- **Amazon ECR**: Container registry
- **Azure DevOps**: CI/CD orchestration (integración multi-cloud)

### 5.2 Arquitecturas por Aplicación

#### SARAS - Modernización Cloud-Native
```
Users → ALB → ECS Fargate (2-4 tasks)
                ↓
         Aurora PostgreSQL + Babelfish (Multi-AZ)
                ↓
         ElastiCache Redis + S3 + CloudWatch
```

**Innovación**: Aurora Babelfish permite migrar de SQL Server sin cambios de código

#### Api Portal - Static Site Serverless
```
Developer → Azure DevOps → AWS S3
                              ↓
Users → Route 53 → CloudFront CDN → S3 Origin
```

**Innovación**: Arquitectura multi-cloud (Azure DevOps + AWS Amplify)

#### Backoffice Sistemas - Híbrido
```
Users → ALB → EC2 (Private Subnet)
                ↓
         Site-to-Site VPN
                ↓
         SQL Server On-Premise
```

**Innovación**: Migración rápida manteniendo BD on-premise, con roadmap de modernización

#### SonarQube - Lift & Shift Optimizado
```
Developers → ALB → EC2 Linux
                      ↓
                RDS PostgreSQL (Multi-AZ)
                      ↓
                EFS + S3 + CloudWatch
```

**Innovación**: Cambio de SQL Server a PostgreSQL y Windows a Linux (73% ahorro)

### 5.3 Innovación y Diferenciadores

#### Aurora PostgreSQL con Babelfish
- **Qué es**: Capa de compatibilidad SQL Server en PostgreSQL
- **Beneficio**: Migración sin cambios de código (puerto 1433, protocolo TDS)
- **Ahorro**: 50% vs RDS SQL Server
- **Caso de uso**: SARAS migra de SQL Server a Babelfish sin refactorización

#### Arquitectura Multi-Cloud
- **Qué es**: CI/CD con Azure DevOps + Hosting en AWS
- **Beneficio**: Best-of-breed (mejor CI/CD + mejor CDN)
- **Flexibilidad**: No vendor lock-in
- **Caso de uso**: Api Portal con Azure Pipelines desplegando a AWS Amplify

#### Estrategia Híbrida con Roadmap
- **Qué es**: Lift & Shift inicial con plan de modernización futura
- **Beneficio**: Migración rápida (3 semanas) + valor inmediato
- **Roadmap**: Amazon Q for .NET Transform para modernización automatizada
- **Caso de uso**: Backoffice Sistemas migra rápido, moderniza después

---

## 6. Plan de Implementación

### 6.1 Fases del Proyecto

#### Fase 1: Quick Wins (Mes 1)
**Objetivos**:
- Migrar Api Portal (5 días)
- Migrar SonarQube (2 semanas)
- Demostrar valor inmediato ($3,094/mes ahorro)

**Entregables**:
- [ ] Api Portal en AWS Amplify con CI/CD
- [ ] SonarQube en EC2 + RDS PostgreSQL
- [ ] Documentación de lecciones aprendidas

#### Fase 2: Lift & Shift Híbrido (Mes 2)
**Objetivos**:
- Migrar Backoffice Sistemas (3 semanas)
- Establecer conectividad híbrida VPN
- Validar arquitectura híbrida

**Entregables**:
- [ ] Backoffice Sistemas en EC2
- [ ] Site-to-Site VPN configurado
- [ ] Runbooks de operación híbrida

#### Fase 3: Modernización Cloud-Native (Meses 3-5)
**Objetivos**:
- Modernizar SARAS (11 semanas)
- Containerización con ECS Fargate
- Migración a Aurora Babelfish

**Entregables**:
- [ ] SARAS containerizado en ECS
- [ ] Aurora Babelfish con datos migrados
- [ ] CI/CD pipeline completo

#### Fase 4: Estabilización y Optimización (Mes 6)
**Objetivos**:
- Optimización de costos
- Fine-tuning de performance
- Documentación completa
- Training avanzado

**Entregables**:
- [ ] Todas las aplicaciones optimizadas
- [ ] Documentación completa
- [ ] Equipo capacitado y autónomo
- [ ] Caso de éxito documentado

### 6.2 Timeline Detallado

| Fase | Aplicación | Inicio | Fin | Duración |
|------|------------|--------|-----|----------|
| **Mes 1** | Api Portal | Sem 1 | Sem 1 | 5 días |
| | SonarQube | Sem 2 | Sem 3 | 2 semanas |
| **Mes 2** | Backoffice Sistemas | Sem 5 | Sem 7 | 3 semanas |
| **Mes 3-5** | SARAS | Sem 9 | Sem 19 | 11 semanas |
| **Mes 6** | Optimización | Sem 20 | Sem 24 | 4 semanas |
| **TOTAL** | 4 aplicaciones | | | **6 meses** |

### 6.3 Hitos Clave

| Hito | Fecha | Criterio de Éxito |
|------|-------|-------------------|
| Kick-off Proyecto | Sem 1 | Equipo alineado, ambiente AWS configurado |
| Api Portal en Producción | Sem 1 | Sitio accesible, CI/CD funcionando |
| SonarQube en Producción | Sem 3 | Análisis de código funcionando |
| VPN Híbrido Operativo | Sem 7 | Conectividad a on-premise validada |
| Backoffice en Producción | Sem 7 | Aplicación funcionando con BD on-premise |
| SARAS Containerizado | Sem 15 | Contenedores en ECS funcionando |
| SARAS en Producción | Sem 19 | Aplicación con Aurora Babelfish |
| Proyecto Completado | Sem 24 | 4 apps en producción, equipo capacitado |

---

## 7. Presupuesto y Uso de Fondos EBA

### 7.1 Desglose de Costos AWS (Mensual Post-EBA)

#### Por Aplicación
| Aplicación | Estrategia | Costo/mes |
|------------|------------|-----------|
| SARAS | Modernización | $904 |
| Api Portal | Static Site | $1.50 |
| Backoffice Sistemas | Lift & Shift | $402 |
| SonarQube | Lift & Shift | $404 |
| **TOTAL AWS** | | **$1,711.50** |

#### Desglose por Servicio
| Servicio | Uso | Costo/mes |
|----------|-----|-----------|
| **Compute** | | |
| ECS Fargate | SARAS (2-4 tasks) | $117 |
| EC2 Instances | Backoffice (2x t3.xlarge) | $243 |
| EC2 Instance | SonarQube (1x t3.xlarge) | $121 |
| AWS Amplify | Api Portal | $1.50 |
| **Subtotal Compute** | | **$482.50** |
| **Database** | | |
| Aurora Babelfish | SARAS (db.r5.large Multi-AZ) | $594 |
| RDS PostgreSQL | SonarQube (db.t3.large Multi-AZ) | $158 |
| **Subtotal Database** | | **$752** |
| **Networking** | | |
| ALB | 3 load balancers | $69 |
| NAT Gateway | 2 NAT gateways | $66 |
| Site-to-Site VPN | 1 VPN connection | $36 |
| Data Transfer | Estimado | $34 |
| **Subtotal Networking** | | **$205** |
| **Storage & Other** | | |
| EBS, S3, EFS | Varios | $60 |
| CloudWatch, Secrets Manager | Monitoreo | $12 |
| **Subtotal Storage** | | **$72** |
| **TOTAL MENSUAL** | | **$1,711.50** |

### 7.2 Solicitud de Fondos EBA

#### Servicios AWS Durante EBA (6 meses)
| Concepto | Costo/mes | Meses | Total |
|----------|-----------|-------|-------|
| Servicios AWS | $1,711.50 | 6 | $10,269 |

#### Servicios Profesionales AWS
| Servicio | Horas | Costo/hora | Total |
|----------|-------|------------|-------|
| AWS Solutions Architect | 40 | $200 | $8,000 |
| AWS Migration Specialist | 30 | $180 | $5,400 |
| AWS Training (workshops) | 16 | $150 | $2,400 |
| **Subtotal Servicios** | | | **$15,800** |

#### Resumen Total
| Concepto | Monto |
|----------|-------|
| Servicios AWS (6 meses) | $10,269 |
| Servicios Profesionales AWS | $15,800 |
| **Subtotal** | **$26,069** |
| Descuento EBA (40%) | -$10,428 |
| **TOTAL SOLICITADO EBA** | **$15,641** |
| **Redondeado** | **$15,000** |

### 7.3 Uso de Fondos EBA
Los fondos EBA se utilizarán para:
- ✅ **60% Servicios Profesionales**: Arquitectura, migración, training
- ✅ **40% Servicios AWS**: Costos de infraestructura durante período EBA
- ✅ **Training**: 4 workshops (AWS fundamentals, ECS, Aurora, DevOps)
- ✅ **Soporte**: Acompañamiento técnico durante 6 meses

**Compromiso del Cliente**:
- BGR asumirá 100% de costos AWS post-EBA ($1,711.50/mes)
- BGR ha aprobado presupuesto para Fase 2 (4 aplicaciones restantes)
- BGR se compromete a documentar caso de éxito

---

*Continúa en la siguiente sección...*
