# Backoffice Banca Digital BGR - Propuesta de Modernización
## Análisis y Arquitecturas AWS

**Fecha**: 2026-01-02  
**Aplicación**: Backoffice Banca Digital  
**Estrategia Recomendada**: Replatform (Containerización)  
**Timeline**: 4-6 semanas  
**Responsable**: Erik Palma (erik.palma@bgr.com.ec) - Jefe de Arquitectura

---

## 📋 Resumen Ejecutivo

Backoffice Banca Digital es una aplicación parametrizadora para Banca Digital del BGR, desarrollada en .NET Core 8 con frontend ASP.NET C#. A diferencia de otras aplicaciones del portafolio, **ya está modernizada en .NET Core 8**, lo que la hace candidata ideal para containerización y despliegue en servicios managed de AWS.

### Hallazgos Clave

| Aspecto | Valor |
|---------|-------|
| **VMs Producción** | 2 (ECBRPRWE27, ECBRPRWE31) |
| **VMs Test** | 1 (ECBRTSW93) |
| **Total vCPUs** | 10 |
| **Total RAM** | 20 GB |
| **Framework** | .NET Core 8 ✅ (Moderno) |
| **Base de Datos** | SQL Server 2019 Enterprise + RDS existente |
| **Usuarios** | 685 colaboradores |
| **Criticidad** | Alta |

---

## 🎯 Información de la Aplicación

### Descripción
Aplicación parametrizadora para Banca Digital que permite la gestión centralizada de configuraciones, parámetros y operaciones para el ecosistema de banca digital del BGR.

### Situación Actual (On-Premise)

**Infraestructura VMware (RVTools)**:

| Servidor | vCPUs | RAM (GB) | Storage (GB) | OS | IP | Estado |
|----------|-------|----------|--------------|-----|-----|--------|
| **ECBRPRWE27** | 4 | 8 | 200 | Windows Server 2016 | 192.168.18.13 | poweredOn |
| **ECBRPRWE31** | 4 | 8 | 200 | Windows Server 2016 | 172.20.115.17 | poweredOn |
| **ECBRTSW93** | 2 | 4 | 210 | Windows Server 2016 | 172.20.41.123 | poweredOn |

**Métricas de Uso (Cloudamize)**:

| Servidor | CPU Avg (%) | RAM Avg (GB) | Network In (Mbps) | Network Out (Mbps) |
|----------|-------------|--------------|-------------------|-------------------|
| ECBRPRWE27 | 26% | 4.01 | 41.05 | 2.43 |

**Load Balancer**: drecbrprtyc.bgr.com - 172.20.115.18

### Stack Tecnológico

**Frontend**:
- ASP.NET C# (.NET Core 8) ✅
- Bootstrap
- ajaxToolkit v3.5

**Backend**:
- C# (.NET Core 8) ✅
- IIS Web Server

**Base de Datos** (Múltiples conexiones):
- SQL Server 2019 Enterprise (On-Premise)
- **RDS ya existente en AWS**: 
  - PROD: db-bancadigitalprod.cbj4jyyxsczf.us-east-1.rds.amazonaws.com
  - TEST: ecbrtsqbdaws.co04ytxx537s.us-east-1.rds.amazonaws.com
- Oracle SIGLO (On-Premise)

**Dependencias Críticas**:
- BACKOFFICE_SISTEMAS_BGR (172.20.1.128:11460)
- BGRBACKOFFICE (172.20.1.214:11443)
- CATALOGOSERVICIOSBGR (172.20.1.214:11443)
- BDD_BGR_LOGS (172.20.1.46:11463)
- PORTAL_ADMINISTRATIVO_BGR (172.20.1.215:11447)
- Oracle SIGLO (172.20.42.27:1521)
- Redis (requiere habilitar en AWS)
- Entry ID
- LDAP (Active Directory)
- Microservicio Notificador

**Servicios AWS ya en uso**:
- S3: bgrbancadigital2.s3.us-east-1.amazonaws.com (PROD)
- S3: bgrbancadigitaltest2.s3.us-east-1.amazonaws.com (TEST)
- S3: upload-templates-test.s3.us-east-1.amazonaws.com
- RDS SQL Server (ya migrado parcialmente)

**Microservicios**:
- https://MSAPIS.BGR.COM:8043 (PROD)
- https://MSAPIS-TEST.BGR.COM:8043 (TEST)
- https://ecbrprncapi.bgr.com:8043 (PROD)
- https://ecbrtsncapi.bgr.com:8043 (TEST)

**SFTP**:
- PROD: sftp://usrpbdbr@aplicativos.gen@172.20.1.15:222
- TEST: sftp://usrtbdbr@aplicativos.test.gen@172.20.41.32:222

### Usuarios y Criticidad

- **Usuarios Totales**: 685 colaboradores del BGR
- **Tipo de Usuarios**: Colaboradores internos del banco
- **Impacto de Falla**: Afectación a operaciones de Banca Digital
- **Soporte**: BGR/TCS
- **Sensibilidad a Latencia**: NO

---

## 🏗️ Arquitecturas AWS Propuestas

### Opción 1: Lift & Shift (Rehost) - Mínimo Cambio
**Complejidad**: Baja | **Timeline**: 2-3 semanas | **Costo**: $547.91/mes

Migración directa de VMs a EC2 manteniendo arquitectura actual.

![Lift & Shift](./diagrams/generated-diagrams/backoffice_banca_digital_lift_shift.png)

**Componentes**:
- 2x EC2 t3.xlarge (4 vCPU, 16 GB) - Windows Server 2016
- Application Load Balancer
- EBS gp3 (200 GB x 2)
- Direct Connect/VPN a on-premise (BDs)
- Uso de RDS existente

**Ventajas**:
- Migración rápida con AWS MGN
- Mínimo riesgo
- Sin cambios de código

**Desventajas**:
- No aprovecha .NET Core 8
- Costos de licencias Windows
- Escalabilidad limitada

---

### Opción 2: Replatform Optimizado - EC2 Linux + .NET Core
**Complejidad**: Media | **Timeline**: 3-4 semanas | **Costo**: $380.50/mes

Aprovechar .NET Core 8 para migrar a Linux y reducir costos.

![Replatform Linux](./diagrams/generated-diagrams/backoffice_banca_digital_replatform_linux.png)

**Componentes**:
- 2x EC2 t3.large (2 vCPU, 8 GB) - Amazon Linux 2023
- Application Load Balancer
- EBS gp3 (100 GB x 2)
- ElastiCache Redis
- Direct Connect/VPN

**Ventajas**:
- ~30% ahorro en costos (sin licencia Windows)
- .NET Core 8 es cross-platform
- Mejor rendimiento en Linux

**Desventajas**:
- Requiere testing exhaustivo
- Posibles ajustes de configuración

---

### Opción 3: Containerización ECS Fargate - RECOMENDADA ⭐
**Complejidad**: Media-Alta | **Timeline**: 4-6 semanas | **Costo**: $295.80/mes

Containerizar la aplicación .NET Core 8 y desplegar en ECS Fargate.

![ECS Fargate - Recomendada](./diagrams/generated-diagrams/backoffice_banca_digital_ecs_fargate.png)

**Componentes**:
- ECS Fargate (2 tasks, 2 vCPU, 4 GB cada una)
- Application Load Balancer
- ECR (Container Registry)
- ElastiCache Redis
- AWS Transfer Family (reemplazo SFTP)
- Secrets Manager
- Direct Connect/VPN

**Ventajas**:
- Sin gestión de servidores
- Auto-scaling nativo
- ~46% ahorro vs Lift & Shift
- CI/CD simplificado
- Alta disponibilidad automática

**Desventajas**:
- Requiere containerización
- Curva de aprendizaje

---

### Opción 4: Modernización Completa - ECS + Aurora + Serverless
**Complejidad**: Alta | **Timeline**: 8-12 semanas | **Costo**: $420.00/mes

Modernización completa con servicios managed.

![Modernización Completa](./diagrams/generated-diagrams/backoffice_banca_digital_modernization.png)

**Componentes**:
- ECS Fargate
- Aurora PostgreSQL (Babelfish) - migración de SQL Server
- ElastiCache Redis
- Lambda (funciones auxiliares)
- API Gateway
- EventBridge
- AWS Transfer Family

**Ventajas**:
- Arquitectura cloud-native
- Máxima escalabilidad
- Sin licencias SQL Server
- Servicios managed

**Desventajas**:
- Mayor esfuerzo de migración
- Requiere cambios en queries
- Timeline extendido

---

## 📊 Comparativa de Opciones

| Aspecto | Lift & Shift | Replatform | ECS Fargate ⭐ | Modernización |
|---------|--------------|------------|----------------|---------------|
| **Costo Mensual** | $547.91 | $380.50 | $295.80 | $420.00 |
| **Timeline** | 2-3 sem | 3-4 sem | 4-6 sem | 8-12 sem |
| **Riesgo** | Bajo | Medio | Medio | Alto |
| **Escalabilidad** | Manual | Manual | Auto | Auto |
| **Mantenimiento** | Alto | Medio | Bajo | Bajo |
| **Cambios Código** | Ninguno | Mínimos | Config | Moderados |

---

## 🎯 Recomendación: Opción 3 - ECS Fargate

### Justificación

1. **Framework Moderno**: .NET Core 8 es ideal para containers
2. **RDS Existente**: Ya tienen RDS en AWS, reduce complejidad
3. **S3 Existente**: Ya usan S3 para archivos
4. **Ahorro Significativo**: 46% menos que Lift & Shift
5. **Operaciones Simplificadas**: Sin gestión de EC2
6. **Escalabilidad**: Auto-scaling para picos de demanda

### Arquitectura Detallada ECS Fargate

![ECS Fargate - Arquitectura Recomendada](./diagrams/generated-diagrams/backoffice_banca_digital_ecs_fargate.png)

---

## 💰 Estimación de Costos - Opción Recomendada (ECS Fargate)

### Costos Mensuales Detallados

| Servicio | Configuración | Costo/Mes |
|----------|---------------|-----------|
| **ECS Fargate** | 2 tasks x 2 vCPU x 4 GB x 730h | $98.40 |
| **ALB** | 1 ALB + 10 LCU avg | $22.50 |
| **ElastiCache Redis** | cache.t3.micro (HA) | $24.82 |
| **ECR** | 10 GB storage | $1.00 |
| **CloudWatch** | Logs + Metrics | $15.00 |
| **Secrets Manager** | 5 secrets | $2.00 |
| **Data Transfer** | 100 GB/mes | $9.00 |
| **Direct Connect** | Port hour (compartido) | $50.00 |
| **NAT Gateway** | 1 NAT + 50 GB | $45.00 |
| **S3** | Ya existente | $0.00 |
| **RDS** | Ya existente | $0.00 |
| **Route 53** | 1 hosted zone | $0.50 |
| **WAF** | Basic rules | $10.00 |
| **Backup** | 50 GB | $2.50 |
| **Reserved Capacity** | -20% (1yr commit) | -$15.92 |
| **TOTAL** | | **$295.80** |

### Comparativa de Ahorro

| Escenario | Costo Mensual | Costo Anual | Ahorro vs On-Prem |
|-----------|---------------|-------------|-------------------|
| On-Premise (estimado) | $1,200.00 | $14,400.00 | - |
| Lift & Shift | $547.91 | $6,574.92 | 54% |
| **ECS Fargate** | **$295.80** | **$3,549.60** | **75%** |

---

## 📅 Plan de Migración - ECS Fargate

### Fase 1: Preparación (Semana 1)
- [ ] Crear Dockerfile para aplicación .NET Core 8
- [ ] Configurar ECR repository
- [ ] Definir task definitions
- [ ] Configurar Secrets Manager
- [ ] Provisionar ElastiCache Redis

### Fase 2: Infraestructura (Semana 2)
- [ ] Crear ECS Cluster
- [ ] Configurar ALB y Target Groups
- [ ] Configurar Security Groups
- [ ] Establecer conectividad híbrida (Direct Connect/VPN)
- [ ] Configurar CloudWatch Logs

### Fase 3: Despliegue Test (Semana 3)
- [ ] Build y push imagen a ECR
- [ ] Desplegar en ambiente Test
- [ ] Configurar conexiones a BDs on-premise
- [ ] Pruebas de conectividad
- [ ] Pruebas funcionales

### Fase 4: Despliegue Producción (Semana 4)
- [ ] Desplegar en ambiente Producción
- [ ] Configurar Auto Scaling
- [ ] Pruebas de carga
- [ ] Validación con usuarios

### Fase 5: Cutover (Semana 5-6)
- [ ] Actualizar DNS (Route 53)
- [ ] Monitoreo intensivo 48h
- [ ] Documentación final
- [ ] Handover a operaciones

---

## ⚠️ Riesgos y Mitigaciones

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| Latencia a BDs on-premise | Media | Alto | Direct Connect dedicado |
| Compatibilidad containers | Baja | Medio | Testing exhaustivo |
| Dependencias LDAP | Media | Alto | Configurar AD Connector |
| SFTP legacy | Baja | Bajo | AWS Transfer Family |
| Redis migration | Baja | Medio | ElastiCache compatible |

---

## 📋 Checklist Pre-Migración

- [ ] Validar compatibilidad .NET Core 8 con Linux containers
- [ ] Documentar todas las connection strings
- [ ] Identificar certificados SSL requeridos
- [ ] Mapear variables de ambiente
- [ ] Validar acceso a RDS existente desde nueva VPC
- [ ] Configurar peering/conectividad con VPC de RDS
- [ ] Definir estrategia de rollback

---

## 📎 Referencias

- **RVTools Export**: vInfo.csv (líneas 215-216, 317)
- **Cloudamize**: Compute.csv (línea 109)
- **Application Assessment**: G.I.-Backoffice Banca Digital.html
- **Documentación existente**: APP_Backoffice_Banca_Digital.md

---

## 📊 Diagramas de Arquitectura

### Opción 1: Lift & Shift
![Lift & Shift](./diagrams/generated-diagrams/backoffice_banca_digital_lift_shift.png)

### Opción 2: Replatform Linux
![Replatform Linux](./diagrams/generated-diagrams/backoffice_banca_digital_replatform_linux.png)

### Opción 3: ECS Fargate (Recomendada) ⭐
![ECS Fargate](./diagrams/generated-diagrams/backoffice_banca_digital_ecs_fargate.png)

### Opción 4: Modernización Completa
![Modernización](./diagrams/generated-diagrams/backoffice_banca_digital_modernization.png)

---

**Última actualización**: 2026-01-02  
**Estado**: Propuesta completa con diagramas  
**Próximo paso**: Revisión y aprobación por stakeholders
