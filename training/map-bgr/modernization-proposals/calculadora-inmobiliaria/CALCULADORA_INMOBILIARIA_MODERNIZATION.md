# Propuesta de Modernización - Calculadora Inmobiliaria

**Fecha:** 2026-01-06  
**Aplicación:** Calculadora Inmobiliaria  
**Cliente:** BGR  
**Proveedor:** GMEDIA  
**Ponderación:** 52/100

---

## 1. Resumen Ejecutivo

| Métrica | Valor |
|---------|-------|
| VMs Actuales | 3 |
| vCPUs Totales | 12 |
| RAM Total | 24 GB |
| Storage | ~550 GB |
| Usuarios | Público (DMZ) |
| Criticidad | Baja |
| Estrategia Recomendada | **Serverless (Lambda + API Gateway)** |

**Hallazgo Clave:** Aplicación web pública para cálculo de créditos hipotecarios. Expuesta en DMZ, se comunica con MSAPI on-premise para datos. Framework .NET Core 8.0 permite migración a Linux/Serverless. Ideal para arquitectura serverless por su naturaleza stateless.

---

## 2. Estado Actual

### 2.1 Infraestructura

| VM | IP | vCPUs | RAM | Storage | OS | CPU% | RAM% |
|----|-----|-------|-----|---------|-----|------|------|
| ECBRPRKC01 | 192.168.12.10 | 4 | 8 GB | ~180 GB | Windows Server 2016 | - | - |
| ECBRPRKC02 | 172.20.115.11 | 4 | 8 GB | ~180 GB | Windows Server 2016 | - | - |
| ECBRPRKW01 | 172.20.1.140 | 4 | 8 GB | ~190 GB | Windows Server 2016 | 52% | 60% |

### 2.2 Tech Stack

| Capa | Tecnología |
|------|------------|
| Frontend | ASP.NET C#, .NET Core 8.0 |
| Backend | .NET Core 8.0, IIS |
| Database | SQL Server 2016 Enterprise |
| Auth | Proveedor (GMEDIA) |
| Ubicación | DMZ (expuesta a internet) |
| Integración | MSAPI (datos on-premise) |

### 2.3 Dependencias

- **MSAPI:** Comunicación con servicios de datos on-premise
- **Proveedor:** GMEDIA (autenticación propia)
- **Sin base de datos propia:** Consume datos vía API

---

## 3. Opciones de Arquitectura

### Opción 1: Serverless (Recomendada)

**Estrategia:** Refactor

![Diagrama Serverless](./diagrams/generated-diagrams/calculadora_inmobiliaria_serverless.png)

Migrar a arquitectura serverless aprovechando .NET Core 8.0 nativo en Lambda.

| Componente | Configuración | Costo/mes |
|------------|---------------|-----------|
| CloudFront | CDN para assets estáticos | $5 |
| S3 | Static website hosting | $1 |
| API Gateway | REST API | $3.50 |
| Lambda | 10K invocaciones, 512MB, .NET 8 | $2 |
| DynamoDB | Cache de cálculos, on-demand | $5 |
| VPN | Conectividad a MSAPI | $37 |
| **Total** | | **$53.50/mes** |

**Horas de implementación:** 48 horas  
**Timeline:** 3 semanas

#### 💡 Tips y Recomendaciones IA

**¿Cuándo elegir esta opción?**
- Aplicación stateless de cálculos
- Tráfico variable/impredecible
- Se busca eliminar gestión de servidores
- Framework .NET Core 8 compatible con Lambda

**Consideraciones importantes:**
- Requiere refactorización para modelo serverless
- Cold starts pueden afectar primeras requests
- Límite de 15 minutos por ejecución Lambda

**Recomendaciones:**
- Usar Provisioned Concurrency para eliminar cold starts
- Implementar caching en DynamoDB para cálculos frecuentes
- Separar frontend estático en S3 + CloudFront

**Ideal para:**
- Calculadoras y herramientas web públicas
- Aplicaciones con picos de tráfico
- Reducción de costos operativos

#### 📋 Esfuerzo Escala24x7

| Tarea | Horas | Equipo |
|-------|-------|--------|
| CloudFront Distribution | 2 | Infra |
| S3 Bucket (static) | 2 | Infra |
| API Gateway | 8 | Infra |
| Lambda Functions | 16 | Infra |
| DynamoDB Table | 2 | Infra |
| VPN Site-to-Site | 16 | Infra |
| Application pipeline (SAM) | 4 | Delivery |
| Desarrollo refactor | 16 | Delivery |
| CloudWatch Dashboard | 8 | Infra |
| Testing y validación | 8 | QA |
| Knowledge transfer | 4 | Infra |
| **TOTAL** | **86** | |

**Costo implementación**: 86 horas × $150/hora = **$12,900 USD**

**Ventajas:**
- Pago por uso real (sin servidores idle)
- Escalado automático ilimitado
- Sin gestión de infraestructura
- Alta disponibilidad nativa

**Desventajas:**
- Requiere refactorización
- Cold starts iniciales
- Vendor lock-in con AWS

---

### Opción 2: Lift & Shift

**Estrategia:** Rehost

![Diagrama Lift Shift](./diagrams/generated-diagrams/calculadora_inmobiliaria_lift_shift.png)

Migración directa de VMs a EC2 manteniendo arquitectura actual.

| Componente | Configuración | Costo/mes |
|------------|---------------|-----------|
| EC2 t3.medium | 2 vCPU, 4GB RAM, Windows (x2) | $121 |
| ALB | Application Load Balancer | $22.50 |
| RDS SQL Server Express | db.t3.small | $50 |
| EBS gp3 | 200 GB total | $16 |
| VPN | Site-to-Site | $37 |
| **Total** | | **$246.50/mes** |

**Horas de implementación:** 24 horas  
**Timeline:** 2 semanas

#### 💡 Tips y Recomendaciones IA

**¿Cuándo elegir esta opción?**
- Migración urgente sin cambios de código
- Equipo sin experiencia en serverless
- Se requiere compatibilidad exacta con on-premise

**Consideraciones importantes:**
- Costos de licencias Windows se mantienen
- Requiere gestión de parches y actualizaciones
- Escalado manual o con Auto Scaling

**Recomendaciones:**
- Usar Reserved Instances para reducir 40% costos
- Implementar Auto Scaling para picos de tráfico
- Considerar migración a Linux post-estabilización

**Ideal para:**
- Migraciones rápidas con bajo riesgo
- Aplicaciones con dependencias Windows específicas
- Primer paso antes de modernización

#### 📋 Esfuerzo Escala24x7

| Tarea | Horas | Equipo |
|-------|-------|--------|
| VPC/Redes | 4 | Infra |
| EC2 Instances (2) | 4 | Infra |
| ALB | 2 | Infra |
| RDS SQL Server | 2 | Infra |
| EBS Storage | 2 | Infra |
| VPN Site-to-Site | 16 | Infra |
| MGN Configuration | 2 | Infra |
| MGN Instances (2) | 2 | Infra |
| MGN Tests | 2 | Infra |
| CloudWatch Logs | 4 | Infra |
| Testing y validación | 8 | QA |
| Knowledge transfer | 4 | Infra |
| **TOTAL** | **52** | |

**Costo implementación**: 52 horas × $150/hora = **$7,800 USD**

**Ventajas:**
- Migración rápida con AWS MGN
- Sin cambios de código
- Arquitectura familiar

**Desventajas:**
- Costos más altos que serverless
- Gestión de infraestructura requerida
- No aprovecha .NET Core 8

---

### Opción 3: Containers ECS Fargate

**Estrategia:** Replatform

![Diagrama ECS](./diagrams/generated-diagrams/calculadora_inmobiliaria_ecs.png)

Containerización en ECS Fargate con Linux.

| Componente | Configuración | Costo/mes |
|------------|---------------|-----------|
| ECS Fargate | 2 tasks, 0.5 vCPU, 1GB RAM | $30 |
| ALB | Application Load Balancer | $22.50 |
| ECR | Container registry | $1 |
| RDS PostgreSQL | db.t3.micro | $15 |
| VPN | Site-to-Site | $37 |
| **Total** | | **$105.50/mes** |

**Horas de implementación:** 40 horas  
**Timeline:** 3 semanas

#### 💡 Tips y Recomendaciones IA

**¿Cuándo elegir esta opción?**
- Se busca balance entre modernización y control
- Equipo con experiencia en containers
- Se requiere portabilidad entre clouds

**Consideraciones importantes:**
- Requiere Dockerfile y pipeline CI/CD
- Migración de SQL Server a PostgreSQL
- Curva de aprendizaje en containers

**Recomendaciones:**
- Usar AWS Copilot para simplificar deployment
- Implementar health checks y auto-scaling
- Considerar Spot Fargate para reducir costos 70%

**Ideal para:**
- Estrategia de containers a largo plazo
- Aplicaciones que requieren más control que Lambda
- Equipos DevOps maduros

#### 📋 Esfuerzo Escala24x7

| Tarea | Horas | Equipo |
|-------|-------|--------|
| VPC/Redes | 4 | Infra |
| Fargate Cluster | 2 | Infra |
| Fargate Service (2 tasks) | 8 | Infra |
| ALB | 2 | Infra |
| ECR | 1 | Infra |
| RDS PostgreSQL | 2 | Infra |
| VPN Site-to-Site | 16 | Infra |
| Application pipeline (ECS) | 4 | Infra |
| CloudWatch Dashboard | 8 | Infra |
| Testing y validación | 8 | QA |
| Knowledge transfer | 4 | Infra |
| **TOTAL** | **59** | |

**Costo implementación**: 59 horas × $150/hora = **$8,850 USD**

**Ventajas:**
- Sin licencias Windows
- Escalado automático
- Portabilidad de containers

**Desventajas:**
- Requiere containerización
- Más complejo que serverless
- Gestión de imágenes Docker

---

## 4. Comparativa

| Aspecto | Opción 1: Serverless | Opción 2: Lift & Shift | Opción 3: ECS |
|---------|---------------------|------------------------|---------------|
| Costo/mes | $53.50 | $246.50 | $105.50 |
| Implementación | 48 hrs | 24 hrs | 40 hrs |
| Timeline | 3 semanas | 2 semanas | 3 semanas |
| Complejidad | Media | Baja | Media |
| Riesgo | Bajo | Bajo | Bajo |
| Escalabilidad | Automática | Manual/ASG | Automática |

---

## 5. Recomendación

**Opción 1: Serverless (Lambda + API Gateway + CloudFront)**

**Justificación:**
1. Aplicación stateless ideal para serverless
2. Ahorro de 78% vs Lift & Shift ($53 vs $246/mes)
3. .NET Core 8.0 tiene soporte nativo en Lambda
4. Tráfico público variable se beneficia de pago por uso
5. Elimina gestión de servidores Windows

**Próximos pasos:**
1. Refactorizar aplicación para modelo Lambda
2. Separar frontend estático a S3
3. Configurar API Gateway + Lambda
4. Establecer VPN para conectividad MSAPI
5. Testing de carga y optimización

---

## 6. TCO Comparativo (12 meses)

| Concepto | Serverless | Lift & Shift | ECS |
|----------|------------|--------------|-----|
| Implementación | $7,200 | $3,600 | $6,000 |
| Operación anual | $642 | $2,958 | $1,266 |
| **Total Año 1** | **$7,842** | **$6,558** | **$7,266** |
| **Total Año 2+** | **$642** | **$2,958** | **$1,266** |

> **Nota:** Serverless tiene mayor costo inicial pero ROI positivo desde mes 8.
