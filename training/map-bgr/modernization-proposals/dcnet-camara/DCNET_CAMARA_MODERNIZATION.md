# DCNET Cámara - Plan de Modernización
## Sistema de Cámara de Compensación

**Fecha**: 2026-01-07  
**Aplicación**: DCNET Cámara  
**Estrategia Recomendada**: ECS + Textract (Replatform)  
**Timeline**: 12 semanas  
**Iniciativa**: Cámara 2028

---

## 🎯 Información de la Aplicación

### Descripción
Sistema de captura y procesamiento de documentos (papeletas, cheques) para cámara de compensación. Proveedor SOLSOFT. Incluye OCR para digitalización de documentos físicos.

### Situación Actual

| Servidor | IP | vCPUs | RAM | Storage | OS |
|----------|-----|-------|-----|---------|-----|
| ECBRPRKW01 | 172.20.1.140 | 4 | 16 GB | 200 GB | Windows Server 2016 |
| ECBRPRKF01 | 172.20.1.144 | 4 | 16 GB | 200 GB | Windows Server 2016 |
| ECBRPRKC01 | 172.20.115.10 | 4 | 8 GB | 100 GB | Windows Server 2016 |
| ECBRPRKC02 | 172.20.115.11 | 4 | 8 GB | 100 GB | Windows Server 2016 |
| **TOTAL** | | **16** | **48 GB** | **600 GB** | |

### Stack Tecnológico
- **Frontend**: ASP.NET Web, Windows Forms
- **Backend**: .NET Framework 4.7.1
- **Database**: SQL Server 2016 Enterprise
- **Proveedor**: SOLSOFT
- **Funcionalidad**: OCR, Cámara Compensación, Procesamiento Cheques

### ⚠️ Hallazgos Clave
- **Iniciativa Cámara 2028**: Sistema incluido en roadmap de modernización
- **4 servidores**: Infraestructura distribuida para procesamiento
- **SQL Server Enterprise**: Licenciamiento costoso
- **OCR Legacy**: Oportunidad de modernizar con Amazon Textract
- **Integración BCE**: Conexión con Banco Central del Ecuador
- **Criticidad Alta**: Proceso crítico de compensación bancaria

---

## 🏗️ Opciones de Arquitectura

### Opción 1: ECS + Textract + Aurora (RECOMENDADA)

![Arquitectura ECS Textract](./diagrams/generated-diagrams/dcnet_ecs.png)

| Servicio | Configuración | Costo/mes |
|----------|---------------|-----------|
| ECS Fargate | .NET Core (4 tasks HA) | $200 |
| Aurora PostgreSQL | db.r5.large Multi-AZ | $250 |
| Application Load Balancer | HTTPS | $25 |
| Amazon Textract | OCR (~50K páginas/mes) | $150 |
| S3 | Documentos (~500 GB) | $50 |
| AWS DMS | Migración inicial | $50 |
| CloudWatch | Logs y métricas | $25 |
| **TOTAL** | | **$800/mes** |

**Ahorro**: 60% vs costo actual ($2,000/mes)

#### 💡 Tips y Recomendaciones IA

**Cuándo elegir:**
- Modernización completa de cámara
- Iniciativa Cámara 2028
- OCR moderno con IA requerido
- Eliminar licencias SQL Server

**Consideraciones:**
- Validar precisión de Textract con documentos BGR
- POC con cheques y papeletas reales
- Testing exhaustivo antes de producción
- Integración con BCE debe validarse

**Recomendaciones:**
- Empezar con POC de Textract
- Migrar .NET Framework a .NET Core
- Usar Aurora Babelfish si compatibilidad T-SQL crítica
- Implementar por fases (OCR primero, luego app)

**Ideal para:**
- Modernización de OCR con IA
- Procesamiento de documentos bancarios
- Iniciativa Cámara 2028

#### 📋 Esfuerzo Escala24x7

| Tarea | Horas | Equipo |
|-------|-------|--------|
| VPC/Redes | 4 | Infra |
| Fargate Cluster | 2 | Infra |
| Fargate Service (4 tasks) | 16 | Infra |
| ALB | 2 | Infra |
| Aurora PostgreSQL | 2 | Infra |
| DMS replication instance | 4 | Data |
| DMS replication task | 4 | Data |
| S3 Bucket | 2 | Infra |
| Lambda Function (Textract) | 8 | Infra |
| CloudWatch Dashboard | 8 | Infra |
| Application pipeline (ECS) | 4 | Infra |
| Desarrollo .NET Core | 80 | Delivery |
| Testing y validación | 40 | QA |
| Knowledge transfer | 24 | Infra |
| **TOTAL** | **200** | |

**Costo implementación**: 200 horas × $150/hora = **$30,000 USD**

---

### Opción 2: EC2 Lift & Shift

![Arquitectura EC2](./diagrams/generated-diagrams/dcnet_ec2.png)

| Servicio | Configuración | Costo/mes |
|----------|---------------|-----------|
| EC2 m5.large | Windows Server (4 instancias) | $300 |
| RDS SQL Server Enterprise | db.r5.large | $900 |
| Application Load Balancer | HTTPS | $25 |
| S3 | Documentos | $50 |
| EBS gp3 | 600 GB | $60 |
| **TOTAL** | | **$1,500/mes** |

**Ahorro**: 25% vs costo actual

#### 💡 Tips y Recomendaciones IA

**Cuándo elegir:**
- Timeline agresivo
- Paso intermedio antes de Cámara 2028
- Sin recursos para modernización completa

**Consideraciones:**
- Mantiene licencias SQL Server Enterprise (costoso)
- Sin modernización de OCR
- Requiere mantenimiento de Windows
- Planificar modernización posterior

**Recomendaciones:**
- Solo como paso intermedio
- Evaluar Reserved Instances para ahorro
- Documentar para modernización futura
- Planificar Textract en fase 2

**Ideal para:**
- Migraciones urgentes
- Fase inicial antes de Cámara 2028

#### 📋 Esfuerzo Escala24x7

| Tarea | Horas | Equipo |
|-------|-------|--------|
| VPC/Redes | 4 | Infra |
| EC2 Instances (4) | 8 | Infra |
| ALB | 2 | Infra |
| RDS SQL Server | 2 | Infra |
| EBS Storage | 8 | Infra |
| S3 Bucket | 2 | Infra |
| MGN Configuration | 2 | Infra |
| MGN Instances (4) | 4 | Infra |
| MGN Tests | 4 | Infra |
| CloudWatch Dashboard | 8 | Infra |
| Testing y validación | 24 | QA |
| Knowledge transfer | 12 | Infra |
| **TOTAL** | **80** | |

**Costo implementación**: 80 horas × $150/hora = **$12,000 USD**

---

### Opción 3: SaaS Proveedor SOLSOFT

![Arquitectura SaaS](./diagrams/generated-diagrams/dcnet_ecs.png)

| Servicio | Configuración | Costo/mes |
|----------|---------------|-----------|
| SaaS SOLSOFT | DCNET Cloud (si disponible) | $1,000 |
| Site-to-Site VPN | Conexión segura | $50 |
| S3 | Integración | $30 |
| CloudWatch | Monitoreo | $20 |
| **TOTAL** | | **$1,200/mes** |

**Ahorro**: 40% vs costo actual

#### 💡 Tips y Recomendaciones IA

**Cuándo elegir:**
- Proveedor SOLSOFT ofrece versión SaaS
- Sin recursos internos para modernización
- Preferencia por OPEX vs CAPEX

**Consideraciones:**
- Validar disponibilidad con SOLSOFT
- Negociar migración incluida
- Evaluar SLA y soporte
- Dependencia de proveedor

**Recomendaciones:**
- Solicitar demo de versión SaaS
- Comparar funcionalidad vs Textract
- Evaluar costo total 3 años
- Negociar precio por volumen

**Ideal para:**
- Organizaciones que prefieren SaaS
- Sin equipo de desarrollo interno

#### 📋 Esfuerzo Escala24x7

| Tarea | Horas | Equipo |
|-------|-------|--------|
| VPN Site-to-Site | 16 | Infra |
| S3 Bucket (integración) | 2 | Infra |
| CloudWatch Logs | 4 | Infra |
| Coordinación proveedor | 16 | PM |
| Testing integración | 16 | QA |
| Knowledge transfer | 6 | Infra |
| **TOTAL** | **60** | |

**Costo implementación**: 60 horas × $150/hora = **$9,000 USD**

---

## 📊 Comparativa

| Criterio | ECS + Textract | EC2 Lift & Shift | SaaS SOLSOFT |
|----------|----------------|------------------|--------------|
| **Costo/mes** | $800 | $1,500 | $1,200 |
| **Ahorro** | 60% | 25% | 40% |
| **Licencias SQL** | ❌ No | ✅ Enterprise | ❌ No |
| **OCR Moderno** | ✅ Textract IA | ❌ Legacy | Depende |
| **Managed** | ✅ Sí | ❌ No | ✅ Sí |
| **Complejidad** | Alta | Media | Baja |
| **Timeline** | 12 semanas | 6 semanas | 4 semanas |
| **Alineado Cámara 2028** | ✅ Sí | Parcial | Depende |

---

## 🔄 Plan de Migración ECS + Textract

### Fase 1: POC Textract (Semanas 1-3)
- Recopilar muestras de documentos (cheques, papeletas)
- Configurar Textract con documentos BGR
- Validar precisión de OCR
- Comparar con OCR actual

### Fase 2: Desarrollo Backend (Semanas 4-7)
- Migrar .NET Framework a .NET Core
- Containerizar aplicación
- Integrar con Textract API
- Configurar ECS Fargate

### Fase 3: Migración Base de Datos (Semanas 8-9)
- Configurar Aurora PostgreSQL
- Usar AWS SCT para conversión de esquema
- Migrar datos con AWS DMS
- Validar integridad de datos

### Fase 4: Testing y Go-Live (Semanas 10-12)
- Testing integral con operaciones
- Validar integración BCE
- Pruebas de carga
- Go-live con rollback plan

---

## 🔗 Integraciones Críticas

| Sistema | Tipo | Consideración |
|---------|------|---------------|
| BCE (Banco Central) | API/Archivos | Validar conectividad desde AWS |
| Siglo 21 | TCP/IP | Mantener integración existente |
| Core Bancario | Base de datos | Sincronización de datos |

---

## ✅ Recomendación Final

**ECS + Textract + Aurora** por:
1. **60% ahorro** ($800/mes vs $2,000/mes)
2. **OCR con IA** - Amazon Textract superior a OCR legacy
3. **Sin licencias SQL Server** - elimina costo Enterprise
4. **Alineado con Cámara 2028** - modernización completa
5. **Escalabilidad** - ECS Fargate auto-scaling
6. **Alta disponibilidad** - Aurora Multi-AZ

**Nota**: Requiere POC de Textract para validar precisión con documentos bancarios específicos de BGR.

---

**Última actualización**: 2026-01-07
