# Plan EBA - Early Business Adoption
## Proyecto MAP-BGR

**Fecha**: 2025-12-02  
**Objetivo**: Llevar 8 aplicaciones a producción en AWS  
**Budget Target**: $5,000 USD/mes  
**Duración**: 8-10 semanas

---

## 🎯 Objetivo EBA

Validar la migración a AWS con **8 aplicaciones reales** en producción, minimizando modernización y manteniendo presupuesto de **$5,000/mes**.

### Beneficios
- ✅ Validación técnica con cargas reales
- ✅ Experiencia práctica del equipo
- ✅ Identificación temprana de riesgos
- ✅ Ajuste de procesos y herramientas
- ✅ Quick wins para stakeholders

---

## 📊 Aplicaciones Seleccionadas

| # | Aplicación | Servidores | Criticidad | Estrategia EBA |
|---|------------|------------|------------|----------------|
| 1 | Seq (Logging) | 5 | Baja | Rehost → EC2 |
| 2 | Sonar Qube | 3 | Media | Rehost → EC2 |
| 3 | Saras | 4 | Media | Rehost → EC2 |
| 4 | Backoffice Sistemas | 5 | Media | Rehost → EC2 |
| 5 | Portal Guía BGR | 4 | Alta | Rehost → EC2 + RDS |
| 6 | Portal Adm BGR | 4 | Alta | Rehost → EC2 + RDS |
| 7 | Backoffice Banca Digital | 6 | Alta | Rehost → EC2 + RDS |
| 8 | Api Portal | 5 | Alta | Rehost → EC2 + RDS |
| **TOTAL** | **8 apps** | **36 VMs** | - | **Lift & Shift** |

---

## 🏗️ Arquitectura EBA

### Principios de Diseño
1. **Mínima modernización**: Lift & Shift prioritario
2. **Servicios managed**: Solo RDS para bases de datos
3. **Alta disponibilidad**: Multi-AZ solo para apps críticas
4. **Optimización de costos**: Instancias rightsized
5. **Seguridad**: VPC, Security Groups, IAM

### Componentes AWS

#### Networking
- **1 VPC** (10.0.0.0/16)
  - 2 Subnets públicas (us-east-1a, us-east-1b)
  - 2 Subnets privadas (us-east-1a, us-east-1b)
  - 1 Internet Gateway
  - 1 NAT Gateway (single AZ para EBA)
  - Route Tables

#### Compute
- **36 EC2 instances** (rightsized)
  - Apps no críticas: t3.medium (2 vCPU, 4 GB)
  - Apps críticas: t3.large (2 vCPU, 8 GB)
  - Auto Scaling (solo apps críticas)

#### Database
- **4 RDS instances** (Multi-AZ solo críticas)
  - Portal Guía BGR: db.t3.medium
  - Portal Adm BGR: db.t3.medium
  - Backoffice Banca: db.t3.large
  - Api Portal: db.t3.large

#### Storage
- **EBS**: gp3 volumes (optimizado)
- **S3**: Backups y logs

#### Load Balancing
- **2 ALB** (Application Load Balancers)
  - 1 para apps públicas
  - 1 para apps internas

#### Security & Monitoring
- **Security Groups**: Por aplicación
- **CloudWatch**: Métricas y logs
- **Systems Manager**: Gestión de instancias
- **Secrets Manager**: Credenciales

---

## 💰 Calculadora de Costos EBA

### Desglose Mensual

#### 1. Compute (EC2)
| Tipo | Cantidad | vCPU | RAM | Precio/hora | Horas/mes | Subtotal |
|------|----------|------|-----|-------------|-----------|----------|
| t3.medium | 20 | 2 | 4 GB | $0.0416 | 730 | $607 |
| t3.large | 16 | 2 | 8 GB | $0.0832 | 730 | $972 |
| **Total EC2** | **36** | - | - | - | - | **$1,579** |

#### 2. Database (RDS)
| Aplicación | Tipo | Edición | Multi-AZ | Precio/hora | Horas/mes | Subtotal |
|------------|------|---------|----------|-------------|-----------|----------|
| Portal Guía | db.t3.medium | SQL Web | No | $0.166 | 730 | $121 |
| Portal Adm | db.t3.medium | SQL Web | No | $0.166 | 730 | $121 |
| Backoffice Banca | db.m5.large | **SQL Standard** | Sí | $0.544 | 730 | $397 |
| Api Portal | db.m5.xlarge | **SQL Enterprise** | Sí | $1.836 | 730 | $1,340 |
| **Total RDS** | **4** | - | - | - | - | **$1,980** |

**Nota**: Precios incluyen licenciamiento de SQL Server
- **Web Edition**: Para aplicaciones web estándar
- **Standard Edition**: Para Backoffice Banca (HA con RDS Multi-AZ)
- **Enterprise Edition**: Para Api Portal (Always On, compresión, particionamiento)

#### 3. Storage
| Servicio | Capacidad | Precio | Subtotal |
|----------|-----------|--------|----------|
| EBS gp3 | 2 TB | $0.08/GB | $164 |
| S3 Standard | 500 GB | $0.023/GB | $12 |
| **Total Storage** | - | - | **$176** |

#### 4. Networking
| Servicio | Cantidad | Precio | Subtotal |
|----------|----------|--------|----------|
| NAT Gateway | 1 | $0.045/hora + data | $33 + $50 |
| ALB | 2 | $0.0225/hora | $33 |
| Data Transfer Out | 1 TB | $0.09/GB | $90 |
| **Total Networking** | - | - | **$206** |

#### 5. Monitoring & Security
| Servicio | Descripción | Subtotal |
|----------|-------------|----------|
| CloudWatch | Logs + Metrics | $150 |
| Systems Manager | Incluido | $0 |
| Secrets Manager | 10 secrets | $4 |
| **Total Monitoring** | - | **$154** |

#### 6. Backup & DR
| Servicio | Descripción | Subtotal |
|----------|-------------|----------|
| AWS Backup | 1 TB | $50 |
| Snapshots EBS | 500 GB | $25 |
| **Total Backup** | - | **$75** |

### TOTAL MENSUAL EBA

| Categoría | Costo Mensual |
|-----------|---------------|
| Compute (EC2) | $1,579 |
| Database (RDS) | $1,980 |
| Storage | $176 |
| Networking | $206 |
| Monitoring | $154 |
| Backup | $75 |
| **Contingencia (10%)** | $417 |
| **TOTAL** | **$4,587** |

**Margen disponible**: $413 para ajustes y crecimiento (8% bajo presupuesto)

---

## 📐 Diagramas de Arquitectura

### Arquitectura General EBA
![Arquitectura General](https://stack-sense-bgr-reports.s3.us-east-1.amazonaws.com/diagrams/eba/eba_general_architecture.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIASSLOFJESQ4CXORPN%2F20251202%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20251202T151805Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLWVhc3QtMSJGMEQCIHP21iWjCbS47KlE%2B0hchpxjdosSkIPPz2n1TNS0lkTcAiBYJ8cF1ubsqvJlj%2Bt%2FHw7ag3CLGAuRzZV580NkilymmyqgAwgYEAAaDDE3Njg2MTU2MzE3MyIMj35euxSTDV01odYVKv0CPZ9Uq0HMWxO31EzAhCUPeVBpcSj2fdbFNTY93Uj%2FCGy%2FJWum7duKFVAFLxIDxZ%2BfQdiQ5D1z6FTnxYo%2ByY7BV2yDOMHtSndN70TcLjLLNAqBn6f4KjFwUQqOJLDyNVHXYLzi7Vn6DYdnUJa456vi%2BZzz5YfxiiRkakhphtBx7aM0bs5TwaxUMcO5NUcZdzB4VqesgMa7jV2wEXAU8ThrmW8vlnpipvPq8QfNci%2FfEtnwFcgy%2BIqjCTxksgEYISOTl7P3a9NiWv9XSKkS7IKl7hbdoYg4lIQ7pPzrhgx0DP8cNc8Jr4rtCZgBoDJxlvoeiNBLXCZGq%2B7z6ulRWQcW9wUQl65%2Bn%2Fa8Mebp0NGN6HtcA8tiIGBsfMs4BYKAl9CTtpfctrGSId%2BdzKytq5bosj6TZAVRQRLZWBQbDmGh59eQiaTwfizc%2FcVqaS55hcs4DguYPiaMKP%2BNqJz8F6YZ0Ffnkgv%2B%2FMgQkyT%2BeOZkMfBHtiMOdUAHrKFWxT6dMOuEvMkGOqUBpc6ADV7FuQhax3TUL8uH4zwox90lkYZksHP0t%2BDC%2BzI4ExeuNzolj7jSkMv8%2BoapYSiXbUmti9OuB81dDWbS59w7aJgO0f8By0acKL8fdegIxHdzQbr1GoF7ERhqgPY23XKkPU3UHhQaOnZ1UxaP4e2%2B3WS6meNti9O0y2MAt30%2BJ8AADTweJFUJ%2Fxv4wro7RR0qTzHoAlOJzgHMPCHq8dmm8uOu&X-Amz-Signature=6b0652ffc54aed9f4f1a9a81913e9ebe5d0735a6df93569a49b5ea5cdcfe24be)

Vista completa de las 8 aplicaciones en AWS con VPC, subnets, ALBs, EC2 instances, RDS databases y servicios compartidos.

### Arquitectura de Red
![Arquitectura de Red](https://stack-sense-bgr-reports.s3.us-east-1.amazonaws.com/diagrams/eba/eba_network_architecture.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIASSLOFJESQ4CXORPN%2F20251202%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20251202T151806Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLWVhc3QtMSJGMEQCIHP21iWjCbS47KlE%2B0hchpxjdosSkIPPz2n1TNS0lkTcAiBYJ8cF1ubsqvJlj%2Bt%2FHw7ag3CLGAuRzZV580NkilymmyqgAwgYEAAaDDE3Njg2MTU2MzE3MyIMj35euxSTDV01odYVKv0CPZ9Uq0HMWxO31EzAhCUPeVBpcSj2fdbFNTY93Uj%2FCGy%2FJWum7duKFVAFLxIDxZ%2BfQdiQ5D1z6FTnxYo%2ByY7BV2yDOMHtSndN70TcLjLLNAqBn6f4KjFwUQqOJLDyNVHXYLzi7Vn6DYdnUJa456vi%2BZzz5YfxiiRkakhphtBx7aM0bs5TwaxUMcO5NUcZdzB4VqesgMa7jV2wEXAU8ThrmW8vlnpipvPq8QfNci%2FfEtnwFcgy%2BIqjCTxksgEYISOTl7P3a9NiWv9XSKkS7IKl7hbdoYg4lIQ7pPzrhgx0DP8cNc8Jr4rtCZgBoDJxlvoeiNBLXCZGq%2B7z6ulRWQcW9wUQl65%2Bn%2Fa8Mebp0NGN6HtcA8tiIGBsfMs4BYKAl9CTtpfctrGSId%2BdzKytq5bosj6TZAVRQRLZWBQbDmGh59eQiaTwfizc%2FcVqaS55hcs4DguYPiaMKP%2BNqJz8F6YZ0Ffnkgv%2B%2FMgQkyT%2BeOZkMfBHtiMOdUAHrKFWxT6dMOuEvMkGOqUBpc6ADV7FuQhax3TUL8uH4zwox90lkYZksHP0t%2BDC%2BzI4ExeuNzolj7jSkMv8%2BoapYSiXbUmti9OuB81dDWbS59w7aJgO0f8By0acKL8fdegIxHdzQbr1GoF7ERhqgPY23XKkPU3UHhQaOnZ1UxaP4e2%2B3WS6meNti9O0y2MAt30%2BJ8AADTweJFUJ%2Fxv4wro7RR0qTzHoAlOJzgHMPCHq8dmm8uOu&X-Amz-Signature=1546e7c6bb313971d92dd0c595ff0e56da2444ca8c756204b2df296623e6cc1f)

Detalle de VPC con subnets públicas y privadas en 2 Availability Zones, Internet Gateway, NAT Gateway y RDS Multi-AZ.

### Api Portal (Aplicación Crítica)
![Api Portal](https://stack-sense-bgr-reports.s3.us-east-1.amazonaws.com/diagrams/eba/eba_api_portal_detailed.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIASSLOFJESQ4CXORPN%2F20251202%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20251202T151805Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLWVhc3QtMSJGMEQCIHP21iWjCbS47KlE%2B0hchpxjdosSkIPPz2n1TNS0lkTcAiBYJ8cF1ubsqvJlj%2Bt%2FHw7ag3CLGAuRzZV580NkilymmyqgAwgYEAAaDDE3Njg2MTU2MzE3MyIMj35euxSTDV01odYVKv0CPZ9Uq0HMWxO31EzAhCUPeVBpcSj2fdbFNTY93Uj%2FCGy%2FJWum7duKFVAFLxIDxZ%2BfQdiQ5D1z6FTnxYo%2ByY7BV2yDOMHtSndN70TcLjLLNAqBn6f4KjFwUQqOJLDyNVHXYLzi7Vn6DYdnUJa456vi%2BZzz5YfxiiRkakhphtBx7aM0bs5TwaxUMcO5NUcZdzB4VqesgMa7jV2wEXAU8ThrmW8vlnpipvPq8QfNci%2FfEtnwFcgy%2BIqjCTxksgEYISOTl7P3a9NiWv9XSKkS7IKl7hbdoYg4lIQ7pPzrhgx0DP8cNc8Jr4rtCZgBoDJxlvoeiNBLXCZGq%2B7z6ulRWQcW9wUQl65%2Bn%2Fa8Mebp0NGN6HtcA8tiIGBsfMs4BYKAl9CTtpfctrGSId%2BdzKytq5bosj6TZAVRQRLZWBQbDmGh59eQiaTwfizc%2FcVqaS55hcs4DguYPiaMKP%2BNqJz8F6YZ0Ffnkgv%2B%2FMgQkyT%2BeOZkMfBHtiMOdUAHrKFWxT6dMOuEvMkGOqUBpc6ADV7FuQhax3TUL8uH4zwox90lkYZksHP0t%2BDC%2BzI4ExeuNzolj7jSkMv8%2BoapYSiXbUmti9OuB81dDWbS59w7aJgO0f8By0acKL8fdegIxHdzQbr1GoF7ERhqgPY23XKkPU3UHhQaOnZ1UxaP4e2%2B3WS6meNti9O0y2MAt30%2BJ8AADTweJFUJ%2Fxv4wro7RR0qTzHoAlOJzgHMPCHq8dmm8uOu&X-Amz-Signature=b06277cfdc39f1f8a5bfd51f1385c23444f4b6b2721a39a631b025588e58bd84)

Arquitectura de aplicación crítica con ALB, Auto Scaling Group, capa de servicios, RDS Multi-AZ y servicios de management.

### SonarQube (Aplicación No Crítica)
![SonarQube](https://stack-sense-bgr-reports.s3.us-east-1.amazonaws.com/diagrams/eba/eba_sonarqube_detailed.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIASSLOFJESQ4CXORPN%2F20251202%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20251202T151807Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLWVhc3QtMSJGMEQCIHP21iWjCbS47KlE%2B0hchpxjdosSkIPPz2n1TNS0lkTcAiBYJ8cF1ubsqvJlj%2Bt%2FHw7ag3CLGAuRzZV580NkilymmyqgAwgYEAAaDDE3Njg2MTU2MzE3MyIMj35euxSTDV01odYVKv0CPZ9Uq0HMWxO31EzAhCUPeVBpcSj2fdbFNTY93Uj%2FCGy%2FJWum7duKFVAFLxIDxZ%2BfQdiQ5D1z6FTnxYo%2ByY7BV2yDOMHtSndN70TcLjLLNAqBn6f4KjFwUQqOJLDyNVHXYLzi7Vn6DYdnUJa456vi%2BZzz5YfxiiRkakhphtBx7aM0bs5TwaxUMcO5NUcZdzB4VqesgMa7jV2wEXAU8ThrmW8vlnpipvPq8QfNci%2FfEtnwFcgy%2BIqjCTxksgEYISOTl7P3a9NiWv9XSKkS7IKl7hbdoYg4lIQ7pPzrhgx0DP8cNc8Jr4rtCZgBoDJxlvoeiNBLXCZGq%2B7z6ulRWQcW9wUQl65%2Bn%2Fa8Mebp0NGN6HtcA8tiIGBsfMs4BYKAl9CTtpfctrGSId%2BdzKytq5bosj6TZAVRQRLZWBQbDmGh59eQiaTwfizc%2FcVqaS55hcs4DguYPiaMKP%2BNqJz8F6YZ0Ffnkgv%2B%2FMgQkyT%2BeOZkMfBHtiMOdUAHrKFWxT6dMOuEvMkGOqUBpc6ADV7FuQhax3TUL8uH4zwox90lkYZksHP0t%2BDC%2BzI4ExeuNzolj7jSkMv8%2BoapYSiXbUmti9OuB81dDWbS59w7aJgO0f8By0acKL8fdegIxHdzQbr1GoF7ERhqgPY23XKkPU3UHhQaOnZ1UxaP4e2%2B3WS6meNti9O0y2MAt30%2BJ8AADTweJFUJ%2Fxv4wro7RR0qTzHoAlOJzgHMPCHq8dmm8uOu&X-Amz-Signature=32839550d5c45abe29a17390ad1c3f6ac305f0318521e0a4c4773d7e48b7235b)

Arquitectura simple de aplicación no crítica con ALB, instancias EC2 y base de datos en EC2.

### Flujo de Migración
![Flujo de Migración](https://stack-sense-bgr-reports.s3.us-east-1.amazonaws.com/diagrams/eba/eba_migration_flow.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIASSLOFJESQ4CXORPN%2F20251202%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20251202T151806Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLWVhc3QtMSJGMEQCIHP21iWjCbS47KlE%2B0hchpxjdosSkIPPz2n1TNS0lkTcAiBYJ8cF1ubsqvJlj%2Bt%2FHw7ag3CLGAuRzZV580NkilymmyqgAwgYEAAaDDE3Njg2MTU2MzE3MyIMj35euxSTDV01odYVKv0CPZ9Uq0HMWxO31EzAhCUPeVBpcSj2fdbFNTY93Uj%2FCGy%2FJWum7duKFVAFLxIDxZ%2BfQdiQ5D1z6FTnxYo%2ByY7BV2yDOMHtSndN70TcLjLLNAqBn6f4KjFwUQqOJLDyNVHXYLzi7Vn6DYdnUJa456vi%2BZzz5YfxiiRkakhphtBx7aM0bs5TwaxUMcO5NUcZdzB4VqesgMa7jV2wEXAU8ThrmW8vlnpipvPq8QfNci%2FfEtnwFcgy%2BIqjCTxksgEYISOTl7P3a9NiWv9XSKkS7IKl7hbdoYg4lIQ7pPzrhgx0DP8cNc8Jr4rtCZgBoDJxlvoeiNBLXCZGq%2B7z6ulRWQcW9wUQl65%2Bn%2Fa8Mebp0NGN6HtcA8tiIGBsfMs4BYKAl9CTtpfctrGSId%2BdzKytq5bosj6TZAVRQRLZWBQbDmGh59eQiaTwfizc%2FcVqaS55hcs4DguYPiaMKP%2BNqJz8F6YZ0Ffnkgv%2B%2FMgQkyT%2BeOZkMfBHtiMOdUAHrKFWxT6dMOuEvMkGOqUBpc6ADV7FuQhax3TUL8uH4zwox90lkYZksHP0t%2BDC%2BzI4ExeuNzolj7jSkMv8%2BoapYSiXbUmti9OuB81dDWbS59w7aJgO0f8By0acKL8fdegIxHdzQbr1GoF7ERhqgPY23XKkPU3UHhQaOnZ1UxaP4e2%2B3WS6meNti9O0y2MAt30%2BJ8AADTweJFUJ%2Fxv4wro7RR0qTzHoAlOJzgHMPCHq8dmm8uOu&X-Amz-Signature=24ada34a37e9a5a2778699d2cbe60f7ce52415e0c22959cce0fce8d8c50bfd02)

Flujo de migración en 2 fases: Apps no críticas (semanas 3-4) y apps críticas (semanas 5-8) usando AWS Application Migration Service.

---

---

## 🔍 Justificación de Ediciones SQL Server

### Análisis Basado en Cloudamize

Del análisis de los 122 servidores monitoreados por Cloudamize:
- **15 servidores** usan SQL Server **Enterprise Edition**
- **18 servidores** usan SQL Server **Standard Edition**
- **2 servidores** usan SQL Server **Express Edition**

### Decisiones por Aplicación

#### Portal Guía BGR y Portal Adm BGR → SQL Server Web
**Razón**: 
- Aplicaciones web estándar sin requerimientos enterprise
- No identificados servidores SQL específicos en Cloudamize
- SQL Server Web Edition suficiente para workloads web

**Features incluidas**:
- Hasta 16 cores
- Hasta 64 GB RAM
- Backups automáticos
- Encryption at rest

---

#### Backoffice Banca Digital → SQL Server Standard
**Razón**:
- Aplicación crítica de banca requiere alta disponibilidad
- RDS Multi-AZ proporciona HA sin necesidad de Always On
- Servidores identificados en Cloudamize no requieren features Enterprise

**Features incluidas**:
- Multi-AZ para alta disponibilidad
- Backups automáticos con point-in-time recovery
- Read replicas para escalabilidad de lectura
- Encryption at rest y in transit
- Hasta 128 cores y 4 TB RAM

**Features Enterprise NO requeridas**:
- Always On Availability Groups (RDS Multi-AZ lo reemplaza)
- Particionamiento de tablas (volumen de datos manejable)
- Compresión avanzada (no crítico para esta app)

---

#### Api Portal → SQL Server Enterprise
**Razón**:
- **15 servidores** en Cloudamize usan Enterprise Edition
- API crítica con requerimientos de HA avanzada
- Identificados servidores ECBRPRQ48, ECBRPRQ52, ecbrprq74 con Enterprise

**Features Enterprise requeridas**:
- **Always On Availability Groups**: HA sin downtime para API crítica
- **Compresión de datos**: Optimización de storage y performance
- **Particionamiento de tablas**: Manejo eficiente de grandes volúmenes
- **Replicación transaccional**: Sincronización en tiempo real
- **Online index operations**: Mantenimiento sin downtime

**Justificación de costo**:
- API es el componente más crítico de la infraestructura
- Downtime de API impacta múltiples aplicaciones
- Features Enterprise justificadas por criticidad del negocio

---

## 📐 Arquitectura Detallada por Aplicación

### 1. Seq (Logging) - $250/mes
**Componentes**:
- 2x t3.medium EC2 (app servers)
- 1x t3.medium EC2 (database)
- 200 GB EBS gp3
- Security Group

**Arquitectura**:
```
Internet → ALB → EC2 (Seq App) → EC2 (Seq DB)
```

---

### 2. Sonar Qube - $200/mes
**Componentes**:
- 2x t3.medium EC2 (SonarQube)
- 1x t3.medium EC2 (PostgreSQL)
- 150 GB EBS gp3
- Security Group

**Arquitectura**:
```
Developers → ALB → EC2 (SonarQube) → EC2 (PostgreSQL)
```

---

### 3. Saras - $280/mes
**Componentes**:
- 3x t3.medium EC2 (app servers)
- 1x t3.medium EC2 (database)
- 200 GB EBS gp3
- Security Group

**Arquitectura**:
```
Users → ALB → EC2 (Saras App) → EC2 (DB)
```

---

### 4. Backoffice Sistemas - $350/mes
**Componentes**:
- 3x t3.medium EC2 (web/app)
- 2x t3.medium EC2 (services)
- 250 GB EBS gp3
- Security Group

**Arquitectura**:
```
Internal Users → ALB → EC2 (Web) → EC2 (Services)
```

---

### 5. Portal Guía BGR - $452/mes
**Componentes**:
- 2x t3.large EC2 (web servers)
- 1x t3.medium EC2 (app server)
- 1x db.t3.medium RDS (SQL Server Web)
- 300 GB EBS gp3
- ALB + Auto Scaling

**Arquitectura**:
```
Internet → ALB → EC2 (Web) → EC2 (App) → RDS (SQL Server Web)
                    ↓
                CloudWatch
```

---

### 6. Portal Adm BGR - $452/mes
**Componentes**:
- 2x t3.large EC2 (web servers)
- 1x t3.medium EC2 (app server)
- 1x db.t3.medium RDS (SQL Server Web)
- 300 GB EBS gp3
- ALB + Auto Scaling

**Arquitectura**:
```
Internal → ALB → EC2 (Web) → EC2 (App) → RDS (SQL Server Web)
                   ↓
               CloudWatch
```

---

### 7. Backoffice Banca Digital - $883/mes
**Componentes**:
- 3x t3.large EC2 (web servers)
- 2x t3.large EC2 (app servers)
- 1x db.m5.large RDS Multi-AZ (SQL Server Standard)
- 400 GB EBS gp3
- ALB + Auto Scaling

**Arquitectura**:
```
Internal → ALB → EC2 (Web) → EC2 (App) → RDS Multi-AZ (SQL Server Standard)
                   ↓              ↓
              CloudWatch    Secrets Manager
```

**Justificación SQL Standard**:
- Aplicación crítica de banca requiere alta disponibilidad
- RDS Multi-AZ proporciona HA sin necesidad de Always On
- Features Standard suficientes: backups automáticos, read replicas, encryption

---

### 8. Api Portal - $1,962/mes
**Componentes**:
- 3x t3.large EC2 (API servers)
- 2x t3.large EC2 (services)
- 1x db.m5.xlarge RDS Multi-AZ (SQL Server Enterprise)
- 350 GB EBS gp3
- ALB + Auto Scaling

**Arquitectura**:
```
Apps/Services → ALB → EC2 (API) → EC2 (Services) → RDS Multi-AZ (SQL Server Enterprise)
                        ↓              ↓
                   CloudWatch    Secrets Manager
```

**Justificación SQL Enterprise**:
- API crítica con requerimientos de alta disponibilidad avanzada
- Requiere Always On Availability Groups para HA sin downtime
- Compresión de datos para optimizar storage y performance
- Particionamiento de tablas para manejo de grandes volúmenes
- Replicación transaccional para sincronización en tiempo real

---

## 👥 Equipos Necesarios

### 1. Equipo Core (Tiempo Completo)

#### AWS Solutions Architect (1)
**Responsabilidades**:
- Diseño de arquitectura AWS
- Definición de servicios y sizing
- Revisión de seguridad y compliance
- Optimización de costos

**Duración**: 10 semanas

---

#### Cloud Migration Engineer (2)
**Responsabilidades**:
- Migración de servidores (Lift & Shift)
- Configuración de EC2 y RDS
- Implementación de networking
- Testing y validación

**Duración**: 8 semanas

---

#### DevOps Engineer (1)
**Responsabilidades**:
- Automatización con IaC (Terraform/CDK)
- CI/CD pipelines
- Configuración de monitoring
- Gestión de secretos

**Duración**: 8 semanas

---

### 2. Equipo de Soporte (Tiempo Parcial)

#### Database Administrator (1)
**Responsabilidades**:
- Migración de bases de datos a RDS
- Configuración de backups
- Optimización de queries
- Validación de performance

**Duración**: 4 semanas (50%)

---

#### Security Engineer (1)
**Responsabilidades**:
- Configuración de Security Groups
- IAM roles y policies
- Secrets Manager setup
- Security assessment

**Duración**: 3 semanas (50%)

---

#### Application Owners (8)
**Responsabilidades**:
- Validación funcional
- Testing de aplicaciones
- Documentación de cambios
- Aprobación de go-live

**Duración**: 2 semanas cada uno (25%)

---

### 3. Equipo de Gestión

#### Project Manager (1)
**Responsabilidades**:
- Coordinación de equipos
- Seguimiento de cronograma
- Gestión de riesgos
- Comunicación con stakeholders

**Duración**: 10 semanas (50%)

---

#### Technical Lead (1)
**Responsabilidades**:
- Liderazgo técnico
- Resolución de blockers
- Code reviews
- Mentoring del equipo

**Duración**: 10 semanas

---

## 📅 Cronograma EBA (10 Semanas)

### Fase 1: Preparación (Semanas 1-2)

**Semana 1**:
- [ ] Kick-off del proyecto
- [ ] Setup de cuentas AWS
- [ ] Diseño de arquitectura detallada
- [ ] Definición de naming conventions
- [ ] Creación de VPC y subnets

**Semana 2**:
- [ ] Configuración de IAM roles
- [ ] Setup de CloudWatch
- [ ] Preparación de runbooks
- [ ] Instalación de herramientas (AWS CLI, Terraform)
- [ ] Training del equipo

---

### Fase 2: Migración Apps No Críticas (Semanas 3-4)

**Semana 3**:
- [ ] Migración Seq (5 VMs)
- [ ] Migración Sonar Qube (3 VMs)
- [ ] Testing funcional
- [ ] Documentación

**Semana 4**:
- [ ] Migración Saras (4 VMs)
- [ ] Migración Backoffice Sistemas (5 VMs)
- [ ] Testing funcional
- [ ] Ajustes y optimización

---

### Fase 3: Migración Apps Críticas (Semanas 5-8)

**Semana 5-6**:
- [ ] Migración Portal Guía BGR (4 VMs + RDS)
- [ ] Migración Portal Adm BGR (4 VMs + RDS)
- [ ] Testing exhaustivo
- [ ] Performance tuning

**Semana 7-8**:
- [ ] Migración Backoffice Banca Digital (6 VMs + RDS)
- [ ] Migración Api Portal (5 VMs + RDS)
- [ ] Testing de integración
- [ ] Security assessment

---

### Fase 4: Estabilización (Semanas 9-10)

**Semana 9**:
- [ ] Monitoreo y ajustes
- [ ] Optimización de costos
- [ ] Documentación final
- [ ] Training a operaciones

**Semana 10**:
- [ ] Validación final con stakeholders
- [ ] Handover a operaciones
- [ ] Retrospectiva del proyecto
- [ ] Planificación de siguientes waves

---

## 🛠️ Herramientas y Tecnologías

### Migración
- **AWS Application Migration Service (MGN)**: Replicación de servidores
- **AWS Database Migration Service (DMS)**: Migración de DBs a RDS
- **CloudEndure**: Backup alternativo

### Infrastructure as Code
- **Terraform**: Provisión de infraestructura
- **AWS CDK**: Alternativa para componentes complejos

### CI/CD
- **AWS CodePipeline**: Pipelines de despliegue
- **AWS CodeBuild**: Build de aplicaciones
- **GitHub Actions**: Alternativa

### Monitoring
- **CloudWatch**: Métricas y logs
- **CloudWatch Dashboards**: Visualización
- **SNS**: Alertas

### Security
- **AWS Secrets Manager**: Gestión de credenciales
- **AWS Systems Manager**: Gestión de instancias
- **Security Hub**: Compliance

---

## 📊 KPIs y Métricas de Éxito

### Técnicos
| KPI | Objetivo | Medición |
|-----|----------|----------|
| Disponibilidad | >99.5% | CloudWatch |
| Latencia | <500ms | CloudWatch |
| Error rate | <1% | Application logs |
| Tiempo de migración | <10 semanas | Cronograma |

### Financieros
| KPI | Objetivo | Medición |
|-----|----------|----------|
| Costo mensual | <$5,000 | AWS Cost Explorer |
| Variación presupuesto | ±10% | Billing dashboard |
| Costo por aplicación | Según plan | Tag-based costing |

### Operacionales
| KPI | Objetivo | Medición |
|-----|----------|----------|
| Tiempo de despliegue | <30 min | Pipeline metrics |
| MTTR | <2 horas | Incident logs |
| Satisfacción equipo | >8/10 | Encuestas |

---

## ⚠️ Riesgos y Mitigaciones

### Riesgo 1: Exceder presupuesto de $5K
**Probabilidad**: Media  
**Impacto**: Alto  
**Mitigación**:
- Monitoreo diario de costos
- Alertas en $4,500
- Rightsizing agresivo
- Apagar instancias no productivas

### Riesgo 2: Downtime en apps críticas
**Probabilidad**: Media  
**Impacto**: Alto  
**Mitigación**:
- Migración en ventanas de mantenimiento
- Rollback plan documentado
- Testing exhaustivo pre-producción
- Soporte 24/7 durante go-live

### Riesgo 3: Performance degradado
**Probabilidad**: Baja  
**Impacto**: Medio  
**Mitigación**:
- Sizing basado en datos Cloudamize
- Testing de carga pre-producción
- Auto Scaling configurado
- Monitoreo proactivo

### Riesgo 4: Resistencia del equipo
**Probabilidad**: Media  
**Impacto**: Medio  
**Mitigación**:
- Training previo
- Documentación clara
- Soporte continuo
- Quick wins tempranos

---

## 📋 Entregables

### Documentación
- [ ] Arquitectura detallada (diagramas)
- [ ] Runbooks de migración
- [ ] Runbooks operativos
- [ ] Guías de troubleshooting
- [ ] Documentación de APIs

### Código
- [ ] Terraform modules
- [ ] Scripts de automatización
- [ ] CI/CD pipelines
- [ ] Monitoring dashboards

### Reportes
- [ ] Reporte semanal de progreso
- [ ] Análisis de costos
- [ ] Métricas de performance
- [ ] Lecciones aprendidas

---

## ✅ Criterios de Éxito

1. ✅ **8 aplicaciones** migradas y en producción
2. ✅ **Costo mensual** <$5,000 USD
3. ✅ **Disponibilidad** >99.5%
4. ✅ **Tiempo de migración** <10 semanas
5. ✅ **Cero incidentes** críticos post-migración
6. ✅ **Equipo capacitado** en AWS
7. ✅ **Documentación completa**
8. ✅ **Stakeholders satisfechos**

---

## 🚀 Próximos Pasos

### Inmediatos (Esta semana)
1. Aprobar plan EBA
2. Asignar equipo
3. Provisionar cuentas AWS
4. Kick-off meeting

### Corto plazo (Próximas 2 semanas)
1. Diseño detallado de arquitectura
2. Setup de ambiente AWS
3. Preparación de herramientas
4. Training del equipo

### Mediano plazo (Semanas 3-10)
1. Ejecución de migraciones
2. Testing y validación
3. Estabilización
4. Handover

---

**Aprobaciones requeridas**:
- [ ] Sponsor ejecutivo
- [ ] Gerente de IT
- [ ] Gerente de Seguridad
- [ ] Gerente Financiero

**Fecha límite aprobación**: 2025-12-09
