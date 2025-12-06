# Plan EBA - Early Business Adoption (Containers)
## Proyecto MAP-BGR - Versión Containerizada

**Fecha**: 2025-12-03  
**Objetivo**: Llevar 8 aplicaciones a producción en AWS usando **ECS Fargate**  
**Budget Target**: $5,000 USD/mes  
**Duración**: 8-10 semanas

---

## 🎯 Objetivo EBA con Containers

Validar la migración a AWS con **8 aplicaciones reales** en producción usando **contenedores (ECS Fargate)**, maximizando beneficios de modernización mientras se mantiene presupuesto de **$5,000/mes**.

### Beneficios de Containerización
- ✅ **Ahorro de costos**: $331/mes vs EC2 tradicional
- ✅ **Despliegues rápidos**: Minutos vs horas
- ✅ **Escalado automático**: Basado en métricas reales
- ✅ **Sin gestión de OS**: AWS maneja patching y actualizaciones
- ✅ **Portabilidad**: Mismo container en dev, test y prod
- ✅ **Rollback instantáneo**: Volver a versión anterior en segundos

---

## 📊 Aplicaciones Seleccionadas

| # | Aplicación | Containers | Criticidad | Estrategia |
|---|------------|------------|------------|------------|
| 1 | Seq (Logging) | 2 tasks | Baja | Containerizar |
| 2 | Sonar Qube | 2 tasks | Media | Containerizar |
| 3 | Saras | 3 tasks | Media | Containerizar |
| 4 | Backoffice Sistemas | 3 tasks | Media | Containerizar |
| 5 | Portal Guía BGR | 3 tasks | Alta | Containerizar + RDS |
| 6 | Portal Adm BGR | 3 tasks | Alta | Containerizar + RDS |
| 7 | Backoffice Banca Digital | 5 tasks | Alta | Containerizar + RDS |
| 8 | Api Portal | 5 tasks | Alta | Containerizar + RDS |
| **TOTAL** | **8 apps** | **26 tasks** | - | **ECS Fargate** |

---

## 🏗️ Arquitectura EBA con Containers

### Diagrama General
![Arquitectura Containers](https://stack-sense-bgr-reports.s3.us-east-1.amazonaws.com/diagrams/eba/eba_containers_general.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIASSLOFJES2FJA3T5Y%2F20251203%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20251203T152044Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLWVhc3QtMSJIMEYCIQCuHq38A%2BjKkrJEkgi0St8Y%2BlUZGvu8krkpMhCexGURWAIhAPvjgTJRXD2XGR6pjPw77ovQ2EC95AhfCHn8rRpQ2JFhKqADCDAQABoMMTc2ODYxNTYzMTczIgyG%2F5Q74YFg87ZaFU4q%2FQIiOE7HP8HrUrPtjdsfw8AT7beO%2FVFAQhHWk8O20rCfxtHI8j8G%2BFCK1d6ejnkMtBroK1yfrRha7lJHezk9ffWVhlxH9NuotOJhVSlrqBieHhbePUs8vIMrGVXYogyI%2F5YC9CJDlDXNeRWsmQkoJgRNkJIAAzsiQZZtLe7KeYCFxaAVARhOyuLua%2FFaxqRah%2FdMimoOgoGWR%2FstZZncCI%2FZiFlEZsEYM5pk%2FLq9LFcav%2BOpvGOax2SPhlxqgGzFOzNBnkmhy9IFY7N%2BhRZ9baIxVqaiiYTu3ai1dbTQkL7itgjdwdgdHBc0tClcQfHA8ITUXxFKX79a0EBlu5EmuJWxOS%2BRbRDYYSQT37EbuJ5yOTSFp1t2zqeTpfyeG5ELNveDov3r9%2BeREk0nt1meM6RB6%2BDji656gp5sSIOsJGaM%2FN7zst7q93YzKwHvU5p0Mt5cf166u2BW2uuEGDeNX1DuVWtu1770BCmywFxwSV%2FXr7CTmLfGYpfDSey52Ykw5KjByQY6owGWhEVJG692m6MFDJwRT04tWh7PZKPAa%2FnOwG%2BhulhdtLt4%2BHAlN6Klpm5VMuQvu4fN0UKqdQwdnFuDHNgHeAPpKDlb%2B49bmI7XN4fHwqLkNziKFFNmX%2B9tcKYi8JTaheetA6VxkpqDxWlmLmzupt8Nd8Jg0Y2tmWkcJrO539kQ3YecBSX8N8I1lcw22Tn6vutO7ixQy%2BX1T1NRFR%2F%2BnbGu%2Bm7c&X-Amz-Signature=e867cf0004c531de39684a66d898b0dea941369804d8ef7cb9841a5235a28153)

Vista completa de las 8 aplicaciones containerizadas en ECS Fargate con VPC, ALBs, RDS databases y servicios compartidos.

### Api Portal Containerizado
![Api Portal Containers](https://stack-sense-bgr-reports.s3.us-east-1.amazonaws.com/diagrams/eba/eba_containers_api_portal.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIASSLOFJES2FJA3T5Y%2F20251203%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20251203T152044Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLWVhc3QtMSJIMEYCIQCuHq38A%2BjKkrJEkgi0St8Y%2BlUZGvu8krkpMhCexGURWAIhAPvjgTJRXD2XGR6pjPw77ovQ2EC95AhfCHn8rRpQ2JFhKqADCDAQABoMMTc2ODYxNTYzMTczIgyG%2F5Q74YFg87ZaFU4q%2FQIiOE7HP8HrUrPtjdsfw8AT7beO%2FVFAQhHWk8O20rCfxtHI8j8G%2BFCK1d6ejnkMtBroK1yfrRha7lJHezk9ffWVhlxH9NuotOJhVSlrqBieHhbePUs8vIMrGVXYogyI%2F5YC9CJDlDXNeRWsmQkoJgRNkJIAAzsiQZZtLe7KeYCFxaAVARhOyuLua%2FFaxqRah%2FdMimoOgoGWR%2FstZZncCI%2FZiFlEZsEYM5pk%2FLq9LFcav%2BOpvGOax2SPhlxqgGzFOzNBnkmhy9IFY7N%2BhRZ9baIxVqaiiYTu3ai1dbTQkL7itgjdwdgdHBc0tClcQfHA8ITUXxFKX79a0EBlu5EmuJWxOS%2BRbRDYYSQT37EbuJ5yOTSFp1t2zqeTpfyeG5ELNveDov3r9%2BeREk0nt1meM6RB6%2BDji656gp5sSIOsJGaM%2FN7zst7q93YzKwHvU5p0Mt5cf166u2BW2uuEGDeNX1DuVWtu1770BCmywFxwSV%2FXr7CTmLfGYpfDSey52Ykw5KjByQY6owGWhEVJG692m6MFDJwRT04tWh7PZKPAa%2FnOwG%2BhulhdtLt4%2BHAlN6Klpm5VMuQvu4fN0UKqdQwdnFuDHNgHeAPpKDlb%2B49bmI7XN4fHwqLkNziKFFNmX%2B9tcKYi8JTaheetA6VxkpqDxWlmLmzupt8Nd8Jg0Y2tmWkcJrO539kQ3YecBSX8N8I1lcw22Tn6vutO7ixQy%2BX1T1NRFR%2F%2BnbGu%2Bm7c&X-Amz-Signature=693ad2cdb8fe139170bdf66952aa8dd0948f9d2ffa73af36e90989fd97b7d9af)

Detalle de aplicación crítica con ECS Fargate tasks, Auto Scaling, ECR, RDS Multi-AZ y servicios de management.

### Comparativa EC2 vs Containers
![Comparativa](https://stack-sense-bgr-reports.s3.us-east-1.amazonaws.com/diagrams/eba/eba_containers_comparison.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIASSLOFJES2FJA3T5Y%2F20251203%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20251203T152044Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLWVhc3QtMSJIMEYCIQCuHq38A%2BjKkrJEkgi0St8Y%2BlUZGvu8krkpMhCexGURWAIhAPvjgTJRXD2XGR6pjPw77ovQ2EC95AhfCHn8rRpQ2JFhKqADCDAQABoMMTc2ODYxNTYzMTczIgyG%2F5Q74YFg87ZaFU4q%2FQIiOE7HP8HrUrPtjdsfw8AT7beO%2FVFAQhHWk8O20rCfxtHI8j8G%2BFCK1d6ejnkMtBroK1yfrRha7lJHezk9ffWVhlxH9NuotOJhVSlrqBieHhbePUs8vIMrGVXYogyI%2F5YC9CJDlDXNeRWsmQkoJgRNkJIAAzsiQZZtLe7KeYCFxaAVARhOyuLua%2FFaxqRah%2FdMimoOgoGWR%2FstZZncCI%2FZiFlEZsEYM5pk%2FLq9LFcav%2BOpvGOax2SPhlxqgGzFOzNBnkmhy9IFY7N%2BhRZ9baIxVqaiiYTu3ai1dbTQkL7itgjdwdgdHBc0tClcQfHA8ITUXxFKX79a0EBlu5EmuJWxOS%2BRbRDYYSQT37EbuJ5yOTSFp1t2zqeTpfyeG5ELNveDov3r9%2BeREk0nt1meM6RB6%2BDji656gp5sSIOsJGaM%2FN7zst7q93YzKwHvU5p0Mt5cf166u2BW2uuEGDeNX1DuVWtu1770BCmywFxwSV%2FXr7CTmLfGYpfDSey52Ykw5KjByQY6owGWhEVJG692m6MFDJwRT04tWh7PZKPAa%2FnOwG%2BhulhdtLt4%2BHAlN6Klpm5VMuQvu4fN0UKqdQwdnFuDHNgHeAPpKDlb%2B49bmI7XN4fHwqLkNziKFFNmX%2B9tcKYi8JTaheetA6VxkpqDxWlmLmzupt8Nd8Jg0Y2tmWkcJrO539kQ3YecBSX8N8I1lcw22Tn6vutO7ixQy%2BX1T1NRFR%2F%2BnbGu%2Bm7c&X-Amz-Signature=074fe54f01793b80216910ac8ec10df6bef3f633226cc21a8a6f2fe763af1ef8)

Comparación de costos y beneficios entre EC2 tradicional y ECS Fargate.

---

## 💰 Calculadora de Costos EBA Containers

### Desglose Mensual

#### 1. Compute (ECS Fargate)
| Aplicación | vCPU | RAM (GB) | Tasks | Horas/mes | Precio/hora | Subtotal |
|------------|------|----------|-------|-----------|-------------|----------|
| Seq | 0.5 | 1 | 2 | 730 | $0.0495 | $72 |
| SonarQube | 0.5 | 1 | 2 | 730 | $0.0495 | $72 |
| Saras | 0.5 | 1 | 3 | 730 | $0.0495 | $108 |
| Backoffice Sistemas | 0.5 | 1 | 3 | 730 | $0.0495 | $108 |
| Portal Guía BGR | 1 | 2 | 3 | 730 | $0.0865 | $190 |
| Portal Adm BGR | 1 | 2 | 3 | 730 | $0.0865 | $190 |
| Backoffice Banca | 1 | 2 | 5 | 730 | $0.0865 | $316 |
| Api Portal | 1 | 2 | 5 | 730 | $0.0865 | $316 |
| **Total ECS Fargate** | - | - | **26** | - | - | **$1,372** |

**Ahorro vs EC2**: $1,579 - $1,372 = **$207/mes**

#### 2. Container Registry (ECR)
| Concepto | Cantidad | Precio | Subtotal |
|----------|----------|--------|----------|
| Storage | 50 GB | $0.10/GB | $5 |
| Data Transfer | Incluido | $0 | $0 |
| **Total ECR** | - | - | **$5** |

#### 3. Database (RDS) - Sin cambios
| Aplicación | Tipo | Edición | Multi-AZ | Subtotal |
|------------|------|---------|----------|----------|
| Portal Guía | db.t3.medium | SQL Web | No | $121 |
| Portal Adm | db.t3.medium | SQL Web | No | $121 |
| Backoffice Banca | db.m5.large | SQL Standard | Sí | $397 |
| Api Portal | db.m5.xlarge | SQL Enterprise | Sí | $1,340 |
| **Total RDS** | - | - | - | **$1,980** |

#### 4. Storage, Networking, Monitoring - Reducidos
| Categoría | Costo EC2 | Costo Containers | Ahorro |
|-----------|-----------|------------------|--------|
| Storage (EBS + S3) | $176 | $150 | $26 |
| Networking | $206 | $190 | $16 |
| Monitoring | $154 | $130 | $24 |
| Backup | $75 | $60 | $15 |
| Security | $32 | $32 | $0 |

### TOTAL MENSUAL EBA CONTAINERS

| Categoría | Costo Mensual |
|-----------|---------------|
| Compute (ECS Fargate) | $1,372 |
| Container Registry (ECR) | $5 |
| Database (RDS) | $1,980 |
| Storage | $150 |
| Networking | $190 |
| Monitoring | $130 |
| Backup | $60 |
| Security | $32 |
| **Subtotal** | **$3,919** |
| Contingencia (10%) | $392 |
| **TOTAL** | **$4,311** |

**Comparativa con EC2**:
- Costo EC2: $4,587/mes
- Costo Containers: $4,311/mes
- **Ahorro**: $276/mes (6%)
- **Margen vs $5K**: $689 (14%)

---

## 🚀 Beneficios de Containerización

### 1. Operacionales
- ✅ **Sin gestión de OS**: AWS maneja patching, actualizaciones, seguridad
- ✅ **Despliegues rápidos**: 2-3 minutos vs 15-20 minutos con EC2
- ✅ **Rollback instantáneo**: Volver a versión anterior en <1 minuto
- ✅ **Escalado automático**: Basado en CPU, memoria, requests
- ✅ **Alta disponibilidad**: Tasks distribuidas en múltiples AZs

### 2. Desarrollo
- ✅ **Portabilidad**: Mismo container en dev, test, prod
- ✅ **Consistencia**: Elimina "funciona en mi máquina"
- ✅ **CI/CD nativo**: Integración con CodePipeline, GitHub Actions
- ✅ **Versionado**: Imágenes taggeadas en ECR
- ✅ **Testing**: Containers idénticos para QA

### 3. Costos
- ✅ **Pay-per-use**: Solo pagas por recursos consumidos
- ✅ **Sin over-provisioning**: Rightsizing automático
- ✅ **Ahorro en management**: Menos horas de DevOps
- ✅ **Spot Fargate**: Hasta 70% descuento (futuro)

### 4. Seguridad
- ✅ **Aislamiento**: Cada task en su propio entorno
- ✅ **Secrets Manager**: Integración nativa
- ✅ **IAM roles**: Por task, no por instancia
- ✅ **Scanning**: ECR escanea vulnerabilidades automáticamente

---

## 📅 Cronograma EBA Containers (10 Semanas)

### Fase 1: Preparación (Semanas 1-2)

**Semana 1**:
- [ ] Kick-off del proyecto
- [ ] Setup de cuentas AWS
- [ ] Creación de VPC y subnets
- [ ] Setup de ECR (Container Registry)
- [ ] Creación de ECS Cluster

**Semana 2**:
- [ ] Containerización de aplicaciones (Dockerfiles)
- [ ] Build y push de imágenes a ECR
- [ ] Configuración de task definitions
- [ ] Setup de CloudWatch Logs
- [ ] Training del equipo en containers

---

### Fase 2: Migración Apps No Críticas (Semanas 3-4)

**Semana 3**:
- [ ] Deploy Seq (2 tasks)
- [ ] Deploy SonarQube (2 tasks)
- [ ] Configuración de ALB
- [ ] Testing funcional
- [ ] Ajuste de auto scaling

**Semana 4**:
- [ ] Deploy Saras (3 tasks)
- [ ] Deploy Backoffice Sistemas (3 tasks)
- [ ] Testing de integración
- [ ] Monitoreo y optimización

---

### Fase 3: Migración Apps Críticas (Semanas 5-8)

**Semana 5-6**:
- [ ] Deploy Portal Guía BGR (3 tasks + RDS)
- [ ] Deploy Portal Adm BGR (3 tasks + RDS)
- [ ] Configuración de service discovery
- [ ] Testing exhaustivo
- [ ] Performance tuning

**Semana 7-8**:
- [ ] Deploy Backoffice Banca (5 tasks + RDS)
- [ ] Deploy Api Portal (5 tasks + RDS)
- [ ] Testing de carga
- [ ] Security assessment
- [ ] Disaster recovery testing

---

### Fase 4: Estabilización (Semanas 9-10)

**Semana 9**:
- [ ] Monitoreo y ajustes
- [ ] Optimización de costos
- [ ] Configuración de CI/CD pipelines
- [ ] Documentación de runbooks

**Semana 10**:
- [ ] Validación final con stakeholders
- [ ] Handover a operaciones
- [ ] Training a equipo de soporte
- [ ] Retrospectiva del proyecto

---

## 👥 Equipos Necesarios

### Core Team (Tiempo Completo)

#### AWS Solutions Architect (1)
**Responsabilidades**:
- Diseño de arquitectura ECS
- Definición de task definitions
- Configuración de networking
- Optimización de costos

**Duración**: 10 semanas

---

#### Container Engineers (2)
**Responsabilidades**:
- Containerización de aplicaciones
- Build de imágenes Docker
- Push a ECR
- Troubleshooting de containers

**Duración**: 8 semanas

---

#### DevOps Engineer (1)
**Responsabilidades**:
- Setup de CI/CD pipelines
- Configuración de auto scaling
- Monitoring y alerting
- Infrastructure as Code (Terraform/CDK)

**Duración**: 8 semanas

---

### Support Team (Tiempo Parcial)

#### Database Administrator (1)
**Responsabilidades**: Migración de DBs a RDS  
**Duración**: 4 semanas (50%)

#### Security Engineer (1)
**Responsabilidades**: Security groups, IAM, scanning  
**Duración**: 3 semanas (50%)

#### Application Owners (8)
**Responsabilidades**: Validación funcional  
**Duración**: 2 semanas cada uno (25%)

#### Project Manager (1)
**Responsabilidades**: Coordinación y seguimiento  
**Duración**: 10 semanas (50%)

#### Technical Lead (1)
**Responsabilidades**: Liderazgo técnico  
**Duración**: 10 semanas

---

## 🛠️ Herramientas y Tecnologías

### Containerización
- **Docker**: Build de imágenes
- **Amazon ECR**: Container registry
- **ECS Fargate**: Serverless containers

### CI/CD
- **AWS CodePipeline**: Pipelines de despliegue
- **AWS CodeBuild**: Build de imágenes
- **GitHub Actions**: Alternativa

### Infrastructure as Code
- **Terraform**: Provisión de infraestructura
- **AWS CDK**: Alternativa para ECS

### Monitoring
- **CloudWatch Container Insights**: Métricas de containers
- **CloudWatch Logs**: Logs centralizados
- **X-Ray**: Tracing distribuido

---

## 📊 KPIs y Métricas de Éxito

### Técnicos
| KPI | Objetivo | Medición |
|-----|----------|----------|
| Disponibilidad | >99.9% | CloudWatch |
| Tiempo de despliegue | <5 min | CodePipeline |
| Tiempo de rollback | <2 min | ECS |
| CPU utilization | 60-80% | Container Insights |
| Memory utilization | 60-80% | Container Insights |

### Operacionales
| KPI | Objetivo | Medición |
|-----|----------|----------|
| Tiempo de scaling | <2 min | ECS metrics |
| MTTR | <1 hora | Incident logs |
| Despliegues/semana | >5 | CI/CD metrics |

### Financieros
| KPI | Objetivo | Medición |
|-----|----------|----------|
| Costo mensual | <$5,000 | AWS Cost Explorer |
| Ahorro vs EC2 | >5% | Comparativa |

---

## ⚠️ Riesgos y Mitigaciones

### Riesgo 1: Curva de aprendizaje de containers
**Probabilidad**: Media  
**Impacto**: Medio  
**Mitigación**:
- Training previo del equipo
- Documentación detallada
- Soporte de AWS
- Empezar con apps no críticas

### Riesgo 2: Problemas de compatibilidad
**Probabilidad**: Media  
**Impacto**: Alto  
**Mitigación**:
- Testing exhaustivo en dev
- Containerización incremental
- Rollback plan documentado
- Mantener EC2 como fallback

### Riesgo 3: Performance degradado
**Probabilidad**: Baja  
**Impacto**: Alto  
**Mitigación**:
- Sizing adecuado de tasks
- Testing de carga pre-producción
- Monitoring proactivo
- Auto scaling configurado

---

## ✅ Criterios de Éxito

1. ✅ **8 aplicaciones** containerizadas y en producción
2. ✅ **Costo mensual** <$5,000 USD
3. ✅ **Disponibilidad** >99.9%
4. ✅ **Tiempo de despliegue** <5 minutos
5. ✅ **Cero incidentes** críticos post-migración
6. ✅ **Equipo capacitado** en containers
7. ✅ **CI/CD pipelines** funcionando
8. ✅ **Stakeholders satisfechos**

---

## 🚀 Próximos Pasos

### Inmediatos (Esta semana)
1. Aprobar plan EBA Containers
2. Asignar equipo
3. Provisionar cuentas AWS
4. Kick-off meeting

### Corto plazo (Próximas 2 semanas)
1. Setup de ECS Cluster y ECR
2. Containerización de aplicaciones
3. Build de imágenes Docker
4. Training del equipo

### Mediano plazo (Semanas 3-10)
1. Ejecución de migraciones
2. Testing y validación
3. Setup de CI/CD
4. Handover

---

## 📋 Comparativa: EC2 vs Containers

| Aspecto | EC2 (Plan Original) | ECS Fargate (Propuesta) |
|---------|---------------------|-------------------------|
| **Costo mensual** | $4,587 | $4,311 (-6%) |
| **Instancias/Tasks** | 36 EC2 | 26 Fargate tasks |
| **Tiempo despliegue** | 15-20 min | 2-5 min |
| **Tiempo rollback** | 10-15 min | <2 min |
| **Gestión de OS** | Manual | Automático |
| **Patching** | Manual | Automático |
| **Escalado** | Manual/ASG | Automático |
| **Portabilidad** | Baja | Alta |
| **CI/CD** | Complejo | Nativo |
| **Margen vs $5K** | $413 (8%) | $689 (14%) |

---

**Aprobaciones requeridas**:
- [ ] Sponsor ejecutivo
- [ ] Gerente de IT
- [ ] Gerente de Seguridad
- [ ] Gerente Financiero
- [ ] Arquitecto de Soluciones

**Fecha límite aprobación**: 2025-12-10

---

**Última actualización**: 2025-12-03  
**Versión**: 2.0 - Containerizada
