# Análisis de Aplicaciones BGR para Modernización AWS

**Fecha:** 2025-12-01
**Total de aplicaciones:** 8

## 📊 Resumen Ejecutivo

- **Aplicaciones .NET:** 6/8
- **Stack obsoleto:** 6/8
- **Arquitectura predominante:** Capas (N-Tier)
- **Base de datos:** SQL Server 2016 Enterprise

### Recomendación General

Todas las aplicaciones requieren modernización. Estrategias recomendadas:

1. **Replatform:** Migrar a .NET 6/8 + contenedores (ECS/EKS)
2. **Database:** Migrar a Amazon RDS for SQL Server o Aurora PostgreSQL
3. **Infraestructura:** Eliminar dependencia de Windows Server
4. **Servicios Managed:** Reemplazar componentes con servicios AWS

---

## 📋 Detalle por Aplicación

### 1. PortalAdministrativoBGR

**Descripción:** Permite realizar tareas de desbloqueo y deslogueo de usuarios de siglo 21

#### Stack Técnico Actual

| Componente | Tecnología | Versión | Estado |
|------------|------------|---------|--------|
| Frontend | ASP.NET C# | .NET Framework 4.7.1 | ⚠️ Obsoleto |
| Backend | C# | .NET Framework 4.7.1 | ⚠️ Obsoleto |
| Base de Datos | Microsoft SQL Server | 2016 ENTERPRISE EDITION | ⚠️ Soporte extendido |
| SO | Windows Server 2016 STANDARD EDITION | - | ⚠️ Windows |

**Arquitectura:** N/A

#### 🎯 Estrategia de Modernización Recomendada

**Fase 1: Modernización de Código**
- Migrar de .NET Framework 4.7.1 a .NET 8
- Refactorizar dependencias obsoletas (ajaxToolkit → componentes modernos)
- Implementar arquitectura de microservicios si aplica

**Fase 2: Containerización**
- Dockerizar aplicación (.NET 8 en Linux containers)
- Desplegar en Amazon ECS con Fargate o EKS
- Implementar Application Load Balancer

**Fase 3: Base de Datos**
- Opción A: Amazon RDS for SQL Server (compatibilidad total)
- Opción B: Migrar a Amazon Aurora PostgreSQL (mayor ahorro)
- Implementar backups automáticos y Multi-AZ

**Fase 4: Servicios Managed**
- Active Directory → AWS Managed Microsoft AD o Amazon Cognito
- Configuración centralizada → AWS Systems Manager Parameter Store
- Notificaciones → Amazon SNS/SQS

---

### 2. PortalGuiaBGR

**Descripción:** Es la guía telefónica del banco

#### Stack Técnico Actual

| Componente | Tecnología | Versión | Estado |
|------------|------------|---------|--------|
| Frontend | ASP.NET C# | .NET Framework 4.7.1 | ⚠️ Obsoleto |
| Backend | C# | .NET Framework 4.7.1 | ⚠️ Obsoleto |
| Base de Datos | Microsoft SQL Server | 2016 ENTERPRISE EDITION | ⚠️ Soporte extendido |
| SO | Windows Server 2016 STANDARD EDITION | - | ⚠️ Windows |

**Arquitectura:** Capas

**Servidores:** ECBRTSW21

**Dependencias:**
- Base de datos: PORTAL_ADMINISTRATIVO_BGR
- Microservicio: BGRCELULAR (Antiguo Notificador)
- Identidades: Active Directory
- Configuración centralizada: Tcs.ServicioConfiguracionBGR.WS

#### 🎯 Estrategia de Modernización Recomendada

**Fase 1: Modernización de Código**
- Migrar de .NET Framework 4.7.1 a .NET 8
- Refactorizar dependencias obsoletas (ajaxToolkit → componentes modernos)
- Implementar arquitectura de microservicios si aplica

**Fase 2: Containerización**
- Dockerizar aplicación (.NET 8 en Linux containers)
- Desplegar en Amazon ECS con Fargate o EKS
- Implementar Application Load Balancer

**Fase 3: Base de Datos**
- Opción A: Amazon RDS for SQL Server (compatibilidad total)
- Opción B: Migrar a Amazon Aurora PostgreSQL (mayor ahorro)
- Implementar backups automáticos y Multi-AZ

**Fase 4: Servicios Managed**
- Active Directory → AWS Managed Microsoft AD o Amazon Cognito
- Configuración centralizada → AWS Systems Manager Parameter Store
- Notificaciones → Amazon SNS/SQS

---

### 3. Api Portal

**Descripción:** Portal estatico de apis que define la entrada y salida de peticiones

#### Stack Técnico Actual

| Componente | Tecnología | Versión | Estado |
|------------|------------|---------|--------|
| Frontend | ASP.NET C# | .NET Framework 4.7.1 | ⚠️ Obsoleto |
| Backend | C# | .NET Framework 4.7.1 | ⚠️ Obsoleto |
| Base de Datos | Microsoft SQL Server | 2016 ENTERPRISE EDITION | ⚠️ Soporte extendido |
| SO | Windows Server 2016 STANDARD EDITION | - | ⚠️ Windows |

**Arquitectura:** Capas

**Servidores:** ECBRTSW21

**Dependencias:**
- Base de datos: PORTAL_ADMINISTRATIVO_BGR
- Microservicio: BGRCELULAR (Antiguo Notificador)
- Identidades: Active Directory
- Configuración centralizada: Tcs.ServicioConfiguracionBGR.WS

#### 🎯 Estrategia de Modernización Recomendada

**Fase 1: Modernización de Código**
- Migrar de .NET Framework 4.7.1 a .NET 8
- Refactorizar dependencias obsoletas (ajaxToolkit → componentes modernos)
- Implementar arquitectura de microservicios si aplica

**Fase 2: Containerización**
- Dockerizar aplicación (.NET 8 en Linux containers)
- Desplegar en Amazon ECS con Fargate o EKS
- Implementar Application Load Balancer

**Fase 3: Base de Datos**
- Opción A: Amazon RDS for SQL Server (compatibilidad total)
- Opción B: Migrar a Amazon Aurora PostgreSQL (mayor ahorro)
- Implementar backups automáticos y Multi-AZ

**Fase 4: Servicios Managed**
- Active Directory → AWS Managed Microsoft AD o Amazon Cognito
- Configuración centralizada → AWS Systems Manager Parameter Store
- Notificaciones → Amazon SNS/SQS

---

### 4. Backoffice Banca Digital

**Descripción:** Aplicación parametrizadora para Banca Digital

#### Stack Técnico Actual

| Componente | Tecnología | Versión | Estado |
|------------|------------|---------|--------|
| Frontend | ASP.NET C# | .NET Core 8 | ✅ |
| Backend | N/A | N/A | ✅ |
| Base de Datos | Microsoft SQL Server | 2019 ENTERPRISE EDITION | ✅ |
| SO | Windows Server 2019 STANDARD EDITION | - | ⚠️ Windows |

**Arquitectura:** N/A

#### 🎯 Estrategia de Modernización Recomendada

---

### 5. Backoffice Sistemas BGR

**Descripción:** Aplicación parametrizadora para diversos sistemas del banco

#### Stack Técnico Actual

| Componente | Tecnología | Versión | Estado |
|------------|------------|---------|--------|
| Frontend | ASP.NET C# | .NET Framework 4.7.1 | ⚠️ Obsoleto |
| Backend | C# | .NET Framework 4.7.1 | ⚠️ Obsoleto |
| Base de Datos | Microsoft SQL Server | 2016 ENTERPRISE EDITION | ⚠️ Soporte extendido |
| SO | Windows Server 2016 STANDARD EDITION | - | ⚠️ Windows |

**Arquitectura:** Capas

**Servidores:** ECBRTSW21

**Dependencias:**
- Base de datos: PORTAL_ADMINISTRATIVO_BGR
- Microservicio: BGRCELULAR (Antiguo Notificador)
- Identidades: Active Directory
- Configuración centralizada: Tcs.ServicioConfiguracionBGR.WS

#### 🎯 Estrategia de Modernización Recomendada

**Fase 1: Modernización de Código**
- Migrar de .NET Framework 4.7.1 a .NET 8
- Refactorizar dependencias obsoletas (ajaxToolkit → componentes modernos)
- Implementar arquitectura de microservicios si aplica

**Fase 2: Containerización**
- Dockerizar aplicación (.NET 8 en Linux containers)
- Desplegar en Amazon ECS con Fargate o EKS
- Implementar Application Load Balancer

**Fase 3: Base de Datos**
- Opción A: Amazon RDS for SQL Server (compatibilidad total)
- Opción B: Migrar a Amazon Aurora PostgreSQL (mayor ahorro)
- Implementar backups automáticos y Multi-AZ

**Fase 4: Servicios Managed**
- Active Directory → AWS Managed Microsoft AD o Amazon Cognito
- Configuración centralizada → AWS Systems Manager Parameter Store
- Notificaciones → Amazon SNS/SQS

---

### 6. Saras

**Descripción:** Aplicación para analisis de riesgo ambiental y social

#### Stack Técnico Actual

| Componente | Tecnología | Versión | Estado |
|------------|------------|---------|--------|
| Frontend | ASP.NET C# | .NET Core 8 | ✅ |
| Backend | N/A | N/A | ✅ |
| Base de Datos | Microsoft SQL Server | 2019 ENTERPRISE EDITION | ✅ |
| SO | Windows Server 2019 STANDARD EDITION | - | ⚠️ Windows |

**Arquitectura:** N/A

#### 🎯 Estrategia de Modernización Recomendada

---

### 7. Seq

**Descripción:** Plataforma autohosteable que funciona como servidor de logs

#### Stack Técnico Actual

| Componente | Tecnología | Versión | Estado |
|------------|------------|---------|--------|
| Frontend | ASP.NET C# | .NET Framework 4.7.1 | ⚠️ Obsoleto |
| Backend | C# | .NET Framework 4.7.1 | ⚠️ Obsoleto |
| Base de Datos | Microsoft SQL Server | 2016 ENTERPRISE EDITION | ⚠️ Soporte extendido |
| SO | Windows Server 2016 STANDARD EDITION | - | ⚠️ Windows |

**Arquitectura:** Capas

**Servidores:** ECBRTSW21

**Dependencias:**
- Base de datos: PORTAL_ADMINISTRATIVO_BGR
- Microservicio: BGRCELULAR (Antiguo Notificador)
- Identidades: Active Directory
- Configuración centralizada: Tcs.ServicioConfiguracionBGR.WS

#### 🎯 Estrategia de Modernización Recomendada

**Fase 1: Modernización de Código**
- Migrar de .NET Framework 4.7.1 a .NET 8
- Refactorizar dependencias obsoletas (ajaxToolkit → componentes modernos)
- Implementar arquitectura de microservicios si aplica

**Fase 2: Containerización**
- Dockerizar aplicación (.NET 8 en Linux containers)
- Desplegar en Amazon ECS con Fargate o EKS
- Implementar Application Load Balancer

**Fase 3: Base de Datos**
- Opción A: Amazon RDS for SQL Server (compatibilidad total)
- Opción B: Migrar a Amazon Aurora PostgreSQL (mayor ahorro)
- Implementar backups automáticos y Multi-AZ

**Fase 4: Servicios Managed**
- Active Directory → AWS Managed Microsoft AD o Amazon Cognito
- Configuración centralizada → AWS Systems Manager Parameter Store
- Notificaciones → Amazon SNS/SQS

---

### 8. Sonar Qube

**Descripción:** Plataforma diseñada para realizar analisis estatico de código fuente

#### Stack Técnico Actual

| Componente | Tecnología | Versión | Estado |
|------------|------------|---------|--------|
| Frontend | ASP.NET C# | .NET Framework 4.7.1 | ⚠️ Obsoleto |
| Backend | C# | .NET Framework 4.7.1 | ⚠️ Obsoleto |
| Base de Datos | Microsoft SQL Server | 2016 ENTERPRISE EDITION | ⚠️ Soporte extendido |
| SO | Windows Server 2016 STANDARD EDITION | - | ⚠️ Windows |

**Arquitectura:** Capas

**Servidores:** ECBRTSW21

**Dependencias:**
- Base de datos: PORTAL_ADMINISTRATIVO_BGR
- Microservicio: BGRCELULAR (Antiguo Notificador)
- Identidades: Active Directory
- Configuración centralizada: Tcs.ServicioConfiguracionBGR.WS

#### 🎯 Estrategia de Modernización Recomendada

**Fase 1: Modernización de Código**
- Migrar de .NET Framework 4.7.1 a .NET 8
- Refactorizar dependencias obsoletas (ajaxToolkit → componentes modernos)
- Implementar arquitectura de microservicios si aplica

**Fase 2: Containerización**
- Dockerizar aplicación (.NET 8 en Linux containers)
- Desplegar en Amazon ECS con Fargate o EKS
- Implementar Application Load Balancer

**Fase 3: Base de Datos**
- Opción A: Amazon RDS for SQL Server (compatibilidad total)
- Opción B: Migrar a Amazon Aurora PostgreSQL (mayor ahorro)
- Implementar backups automáticos y Multi-AZ

**Fase 4: Servicios Managed**
- Active Directory → AWS Managed Microsoft AD o Amazon Cognito
- Configuración centralizada → AWS Systems Manager Parameter Store
- Notificaciones → Amazon SNS/SQS

---

## 💰 Estimación de Costos (por aplicación)

### Opción 1: Lift & Shift (EC2 + RDS SQL Server)
- **Compute:** 2x t3.large (Windows) = ~$240/mes
- **Database:** RDS SQL Server Standard (db.m5.large) = ~$400/mes
- **Load Balancer:** ALB = ~$25/mes
- **Total estimado:** ~$665/mes por aplicación

### Opción 2: Modernización (ECS + RDS SQL Server)
- **Compute:** ECS Fargate (2 vCPU, 4GB) = ~$60/mes
- **Database:** RDS SQL Server Standard (db.m5.large) = ~$400/mes
- **Load Balancer:** ALB = ~$25/mes
- **Total estimado:** ~$485/mes por aplicación (27% ahorro)

### Opción 3: Modernización Completa (ECS + Aurora PostgreSQL)
- **Compute:** ECS Fargate (2 vCPU, 4GB) = ~$60/mes
- **Database:** Aurora PostgreSQL (db.r5.large) = ~$180/mes
- **Load Balancer:** ALB = ~$25/mes
- **Total estimado:** ~$265/mes por aplicación (60% ahorro)

**Ahorro anual estimado (8 aplicaciones, Opción 3):** ~$38,400 USD

---

## 🎯 Matriz de Priorización de Migración

| Aplicación | Deuda Técnica | Complejidad | Impacto Negocio | Dependencias | Prioridad | Ola |
|------------|---------------|-------------|-----------------|--------------|-----------|-----|
| **PortalGuiaBGR** | 🔴 Alta | 🟡 Media | 🟢 Baja | 4 deps | **P1** | **Ola 1** |
| **Api Portal** | 🔴 Alta | 🟡 Media | 🔴 Alta | 4 deps | **P1** | **Ola 1** |
| **PortalAdministrativoBGR** | 🔴 Alta | 🟢 Baja | 🟡 Media | 0 deps | **P2** | **Ola 2** |
| **Backoffice Sistemas BGR** | 🔴 Alta | 🟡 Media | 🔴 Alta | 4 deps | **P2** | **Ola 2** |
| **Backoffice Banca Digital** | 🟢 Baja | 🟢 Baja | 🔴 Alta | 0 deps | **P3** | **Ola 3** |
| **Saras** | 🟢 Baja | 🟢 Baja | 🟡 Media | 0 deps | **P3** | **Ola 3** |
| **Seq** | 🔴 Alta | 🟢 Baja | 🟢 Baja | 4 deps | **P4** | **Ola 4** |
| **Sonar Qube** | 🔴 Alta | 🟢 Baja | 🟢 Baja | 4 deps | **P4** | **Ola 4** |

### Criterios de Priorización

**Deuda Técnica:**
- 🔴 Alta: .NET Framework 4.7.1 + SQL Server 2016 + Windows Server 2016
- 🟢 Baja: .NET Core 8 + SQL Server 2019 + Windows Server 2019

**Complejidad:**
- 🟢 Baja: Sin dependencias críticas, arquitectura simple
- 🟡 Media: Múltiples dependencias compartidas
- 🔴 Alta: Arquitectura compleja, integraciones críticas

**Impacto Negocio:**
- 🔴 Alta: Aplicaciones core de negocio
- 🟡 Media: Aplicaciones administrativas
- 🟢 Baja: Herramientas de soporte/desarrollo

### Estrategia por Ola

**Ola 1 (Meses 1-3):** Aplicaciones con alta deuda técnica y dependencias compartidas
- Establece infraestructura base AWS
- Migra servicios compartidos (AD, Config, Notificaciones)
- Valida patrones de modernización

**Ola 2 (Meses 4-6):** Aplicaciones críticas con deuda técnica
- Aplica patrones validados en Ola 1
- Migra aplicaciones administrativas core

**Ola 3 (Meses 7-9):** Aplicaciones modernas (.NET Core 8)
- Containerización directa sin refactoring
- Migración rápida

**Ola 4 (Meses 10-12):** Herramientas de desarrollo
- Evaluar alternativas managed (CloudWatch, CodeGuru)
- Migración o reemplazo

---

## 🏗️ Plan Extendido de Migración y Modernización

### Fase 0: Preparación (Mes 0)

#### Infraestructura Base AWS

**Networking:**
- VPC con 3 AZs (us-east-1a, us-east-1b, us-east-1c)
- Subnets públicas (3) y privadas (6)
- NAT Gateways (3 para HA)
- Internet Gateway
- Route Tables y Security Groups

**Servicios Fundacionales:**
- AWS Organizations + Control Tower
- AWS IAM Identity Center (SSO)
- AWS Config + CloudTrail
- AWS Systems Manager Session Manager
- AWS Secrets Manager
- AWS Certificate Manager (ACM)

**Costo estimado Fase 0:** ~$350/mes

---

### Ola 1: Servicios Compartidos + Aplicaciones Piloto (Meses 1-3)

#### 1.1 Servicios Compartidos (Mes 1)

**Active Directory:**
- AWS Managed Microsoft AD (Standard Edition)
- 2 domain controllers en Multi-AZ
- Integración con AD on-premise via VPN/Direct Connect
- **Costo:** ~$146/mes

**Configuración Centralizada:**
- AWS Systems Manager Parameter Store (Standard)
- AWS AppConfig para configuración dinámica
- **Costo:** ~$5/mes

**Notificaciones (BGRCELULAR):**
- Amazon SNS para notificaciones push
- Amazon SQS para cola de mensajes
- AWS Lambda para procesamiento
- **Costo:** ~$20/mes

**Observabilidad:**
- Amazon CloudWatch Logs
- Amazon CloudWatch Metrics
- AWS X-Ray para tracing
- **Costo:** ~$50/mes

**Total Servicios Compartidos:** ~$221/mes

#### 1.2 Base de Datos Compartida (Mes 1-2)

**PORTAL_ADMINISTRATIVO_BGR:**
- Amazon RDS for SQL Server Standard Edition
- Instance: db.m5.large (2 vCPU, 8 GB RAM)
- Multi-AZ para HA
- Storage: 500 GB gp3
- Automated backups (7 días)
- **Costo:** ~$580/mes

#### 1.3 Aplicación Piloto: PortalGuiaBGR (Mes 2-3)

**Compute:**
- Amazon ECS Cluster (Fargate)
- Task Definition: 2 vCPU, 4 GB RAM
- Auto Scaling: 2-6 tasks
- Application Load Balancer
- **Costo:** ~$85/mes

**CI/CD:**
- AWS CodePipeline
- AWS CodeBuild
- Amazon ECR (Container Registry)
- **Costo:** ~$30/mes

**Total Ola 1:** ~$916/mes

---

### Ola 2: Aplicaciones Core (Meses 4-6)

#### 2.1 Api Portal (Mes 4)

**Compute:**
- Amazon ECS Fargate (2 vCPU, 4 GB)
- Auto Scaling: 3-10 tasks (alta demanda)
- Application Load Balancer
- Amazon API Gateway (opcional, para gestión APIs)
- **Costo:** ~$150/mes

#### 2.2 PortalAdministrativoBGR (Mes 5)

**Compute:**
- Amazon ECS Fargate (1 vCPU, 2 GB)
- Auto Scaling: 2-4 tasks
- Application Load Balancer
- **Costo:** ~$60/mes

**Base de Datos:**
- Usa RDS compartido PORTAL_ADMINISTRATIVO_BGR
- **Costo:** $0 (ya provisionado)

#### 2.3 Backoffice Sistemas BGR (Mes 6)

**Compute:**
- Amazon ECS Fargate (2 vCPU, 4 GB)
- Auto Scaling: 2-6 tasks
- Application Load Balancer
- **Costo:** ~$85/mes

**Total Ola 2:** ~$295/mes (incremental)

---

### Ola 3: Aplicaciones Modernas (Meses 7-9)

#### 3.1 Backoffice Banca Digital (Mes 7-8)

**Compute:**
- Amazon ECS Fargate (2 vCPU, 4 GB)
- Auto Scaling: 2-6 tasks
- Application Load Balancer
- **Costo:** ~$85/mes

**Base de Datos:**
- Amazon RDS for SQL Server 2019 Standard
- Instance: db.m5.large
- Multi-AZ
- Storage: 300 GB gp3
- **Costo:** ~$580/mes

#### 3.2 Saras (Mes 8-9)

**Compute:**
- Amazon ECS Fargate (2 vCPU, 4 GB)
- Auto Scaling: 2-4 tasks
- Application Load Balancer
- **Costo:** ~$70/mes

**Base de Datos:**
- Comparte RDS SQL Server 2019 con Backoffice Banca Digital
- **Costo:** $0 (ya provisionado)

**Total Ola 3:** ~$735/mes (incremental)

---

### Ola 4: Herramientas DevOps (Meses 10-12)

#### 4.1 Seq → Amazon CloudWatch Logs Insights (Mes 10)

**Reemplazo con Servicio Managed:**
- Amazon CloudWatch Logs (ingesta y almacenamiento)
- CloudWatch Logs Insights (queries)
- CloudWatch Dashboards
- **Costo:** ~$80/mes (basado en 100 GB/mes logs)

**Alternativa (si se requiere Seq):**
- Amazon ECS Fargate (1 vCPU, 2 GB)
- Amazon EFS para almacenamiento persistente
- **Costo:** ~$90/mes

#### 4.2 SonarQube → AWS CodeGuru + SonarCloud (Mes 11-12)

**Opción A - Reemplazo Managed:**
- Amazon CodeGuru Reviewer (análisis estático)
- SonarCloud (SaaS)
- **Costo:** ~$150/mes

**Opción B - Self-Hosted:**
- Amazon ECS Fargate (2 vCPU, 4 GB)
- Amazon RDS PostgreSQL (db.t3.medium)
- **Costo:** ~$180/mes

**Total Ola 4:** ~$230/mes (incremental, opción managed)

---

## 📊 Resumen de Servicios AWS Requeridos

### Compute & Containers
- ✅ Amazon ECS (Fargate) - 8 aplicaciones
- ✅ Application Load Balancer - 8 ALBs
- ✅ Amazon ECR - Registry de imágenes

### Database
- ✅ Amazon RDS for SQL Server Standard - 2 instancias
  - PORTAL_ADMINISTRATIVO_BGR (compartida por 6 apps)
  - Backoffice Banca Digital + Saras (compartida)

### Networking
- ✅ Amazon VPC
- ✅ NAT Gateway (3 AZs)
- ✅ AWS PrivateLink (para servicios AWS)

### Security & Identity
- ✅ AWS Managed Microsoft AD
- ✅ AWS Secrets Manager
- ✅ AWS Certificate Manager
- ✅ AWS IAM Identity Center

### DevOps & CI/CD
- ✅ AWS CodePipeline
- ✅ AWS CodeBuild
- ✅ AWS CodeDeploy
- ✅ Amazon ECR

### Observability
- ✅ Amazon CloudWatch (Logs, Metrics, Dashboards)
- ✅ AWS X-Ray
- ✅ Amazon SNS (alertas)

### Configuration & Messaging
- ✅ AWS Systems Manager Parameter Store
- ✅ AWS AppConfig
- ✅ Amazon SNS
- ✅ Amazon SQS

### Governance
- ✅ AWS Organizations
- ✅ AWS Control Tower
- ✅ AWS Config
- ✅ AWS CloudTrail

---

## 💰 Costo Total Mensual por Fase

| Fase | Componentes | Costo Mensual | Costo Acumulado |
|------|-------------|---------------|-----------------|
| **Fase 0** | Infraestructura base | $350 | $350 |
| **Ola 1** | Servicios compartidos + 1 app | $916 | $1,266 |
| **Ola 2** | 3 aplicaciones core | $295 | $1,561 |
| **Ola 3** | 2 aplicaciones modernas | $735 | $2,296 |
| **Ola 4** | Herramientas DevOps | $230 | $2,526 |

**Costo mensual final (8 aplicaciones):** ~$2,526/mes (~$30,312/año)

**Costo on-premise estimado actual:** ~$5,320/mes (~$63,840/año)
- 8 Windows Server licenses
- SQL Server Enterprise licenses
- Hardware/hosting

**Ahorro anual estimado:** ~$33,528 USD (52% reducción)

---

## 📅 Timeline de Migración

```
Mes 0:  [Preparación] Infraestructura base AWS
Mes 1:  [Ola 1] Servicios compartidos
Mes 2:  [Ola 1] Base de datos + PortalGuiaBGR
Mes 3:  [Ola 1] Validación y optimización
Mes 4:  [Ola 2] Api Portal
Mes 5:  [Ola 2] PortalAdministrativoBGR
Mes 6:  [Ola 2] Backoffice Sistemas BGR
Mes 7:  [Ola 3] Backoffice Banca Digital
Mes 8:  [Ola 3] Saras
Mes 9:  [Ola 3] Validación
Mes 10: [Ola 4] Seq → CloudWatch
Mes 11: [Ola 4] SonarQube → CodeGuru
Mes 12: [Cierre] Desmantelamiento on-premise
```

**Duración total:** 12 meses

---

## ✅ Próximos Pasos

1. **Validar priorización** con stakeholders de negocio
2. **Aprobar presupuesto** de infraestructura AWS (~$30K/año)
3. **Establecer equipo de migración** (2-3 ingenieros + 1 arquitecto)
4. **Configurar entorno AWS** (Fase 0)
5. **Iniciar Ola 1** con aplicación piloto
6. **Establecer métricas de éxito** (performance, costos, disponibilidad)

