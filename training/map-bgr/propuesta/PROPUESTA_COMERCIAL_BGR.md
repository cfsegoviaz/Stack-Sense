# Propuesta de Migración a AWS
## Proyecto MAP-BGR

---

**Presentado a**: BGR  
**Fecha**: 1 de Diciembre, 2025  
**Validez**: 90 días  
**Contacto**: Equipo Stack Sense

---

## 📋 Resumen Ejecutivo

BGR cuenta actualmente con **383 máquinas virtuales** en su infraestructura on-premise, representando una inversión significativa en hardware, licencias y operaciones. Esta propuesta presenta una estrategia integral de migración a Amazon Web Services (AWS) que permitirá a BGR:

### Beneficios Clave

✅ **Reducir costos operativos en 64%** - Ahorro de $2.8M en 3 años  
✅ **Mejorar disponibilidad** - SLA de 99.99% con arquitectura Multi-AZ  
✅ **Aumentar agilidad** - Provisión de recursos en minutos vs semanas  
✅ **Fortalecer seguridad** - Cumplimiento con estándares internacionales  
✅ **Eliminar deuda técnica** - 67 VMs con sistemas operativos EOL  

### Inversión y Retorno

| Concepto | Valor |
|----------|-------|
| **Costo Actual (On-Premise)** | $1,450,000/año |
| **Costo AWS Optimizado** | $522,581/año |
| **Ahorro Anual** | $927,419 (64%) |
| **ROI** | Positivo desde año 1 |
| **Payback Period** | 8 meses |

---

## 🎯 Situación Actual

### Infraestructura On-Premise

**Inventario**:
- 383 máquinas virtuales (350 activas, 33 apagadas)
- 1,752 vCPUs totales
- 5,925 GB de RAM
- 61 TB de almacenamiento
- 14 hosts ESXi
- 33 datastores

**Desafíos Identificados**:

1. **Deuda Técnica Crítica**
   - 46 VMs con Windows Server 2003 (EOL desde 2015)
   - 21 VMs con Windows Server 2008 (EOL desde 2020)
   - Riesgo de seguridad y falta de soporte

2. **Costos Operativos Elevados**
   - Hardware: $400K/año (amortización)
   - Licencias: $350K/año
   - Energía y datacenter: $300K/año
   - Personal IT: $300K/año
   - Mantenimiento: $100K/año

3. **Limitaciones de Escalabilidad**
   - Provisión de recursos: 2-4 semanas
   - Capacidad limitada para picos de demanda
   - Dificultad para implementar DR/HA

4. **Recursos Subutilizados**
   - 33 VMs apagadas (8.6% del inventario)
   - Oportunidad de optimización inmediata

---

## 🚀 Solución Propuesta

### Estrategia de Migración: Enfoque Híbrido por Fases

Proponemos una migración estructurada en **4 olas** durante **12 meses**, utilizando las estrategias de las **7 R's de AWS**:

#### Clasificación de Cargas de Trabajo

| Estrategia | VMs | % | Descripción |
|------------|-----|---|-------------|
| **Rehost** | 261 | 68% | Lift & Shift - Migración directa |
| **Retire** | 77 | 20% | Eliminar o consolidar |
| **Refactor** | 26 | 7% | Modernizar a serverless/containers |
| **Replatform** | 19 | 5% | Upgrade OS o migrar a managed services |

### Arquitectura Target en AWS

#### Componentes Principales

**Compute**:
- EC2 instances con Auto Scaling
- ECS Fargate para aplicaciones containerizadas
- Lambda para microservicios y APIs

**Database**:
- RDS Multi-AZ (SQL Server, PostgreSQL)
- Aurora Serverless para cargas variables
- DynamoDB para datos NoSQL

**Storage**:
- EBS gp3 para discos de aplicación
- S3 para archivos y backups
- EFS para file sharing

**Networking**:
- VPC con arquitectura Multi-AZ
- Application Load Balancer (ALB)
- Direct Connect para conectividad híbrida
- Route 53 para DNS

**Security**:
- AWS WAF para protección web
- Security Groups y NACLs
- Secrets Manager para credenciales
- CloudTrail para auditoría
- GuardDuty para detección de amenazas

**Monitoring**:
- CloudWatch para logs y métricas
- CloudWatch Alarms para alertas
- SNS para notificaciones
- X-Ray para tracing

---

## 📅 Plan de Migración Detallado

### Ola 0: Piloto (Semanas 1-6)

**Objetivo**: Validar proceso de migración con aplicaciones no críticas

**Aplicaciones**:
1. SonarQube (5 VMs) - Herramienta DevOps
2. Saras (2 VMs) - Aplicación empresarial
3. Seq → CloudWatch (5 VMs) - Logging

**Recursos**: 12 VMs, 96 vCPUs, 306 GB RAM  
**Costo mensual**: $2,400 (RI)  
**Duración**: 6 semanas

**Actividades**:
- Semana 1-2: Preparación de infraestructura AWS base
- Semana 3-4: Migración de aplicaciones
- Semana 5: Cutover y validación
- Semana 6: Estabilización y lecciones aprendidas

**Entregables**:
- Infraestructura AWS base configurada
- 3 aplicaciones migradas y operativas
- Runbooks actualizados
- Reporte de lecciones aprendidas

---

### Ola 1: Backoffice (Semanas 7-12)

**Objetivo**: Migrar aplicaciones internas

**Aplicaciones**:
1. Backoffice Sistemas (5 VMs)
2. Backoffice Banca Digital (3 VMs)

**Recursos**: 8 VMs, 52 vCPUs, 164 GB RAM  
**Costo mensual**: $2,100 (RI)  
**Duración**: 6 semanas

**Actividades**:
- Migración de aplicaciones backoffice
- Implementación de conectividad híbrida
- Configuración de accesos internos
- Validación con usuarios

---

### Ola 2: Portales (Semanas 13-20)

**Objetivo**: Migrar aplicaciones de cara al cliente

**Aplicaciones**:
1. Api Portal (5 VMs)
2. PortalGuiaBGR (5 VMs)

**Recursos**: 10 VMs, 84 vCPUs, 288 GB RAM  
**Costo mensual**: $3,600 (RI)  
**Duración**: 8 semanas

**Actividades**:
- Migración de portales web
- Implementación de CloudFront (CDN)
- Configuración de WAF
- Implementación de Auto Scaling
- Pruebas de carga y performance

---

### Ola 3: Portal Crítico (Semanas 21-26)

**Objetivo**: Migrar portal administrativo principal

**Aplicaciones**:
1. PortalAdmBGR (6 VMs)

**Recursos**: 6 VMs, 48 vCPUs, 156 GB RAM  
**Costo mensual**: $2,700 (RI)  
**Duración**: 6 semanas

**Actividades**:
- Migración de portal crítico
- Validación exhaustiva
- Plan de rollback detallado
- Monitoreo 24/7 durante cutover

---

### Ola 4: Resto de Infraestructura (Semanas 27-52)

**Objetivo**: Completar migración de VMs restantes

**Recursos**: 347 VMs  
**Costo mensual**: $65,975 (RI)  
**Duración**: 26 semanas

**Actividades**:
- Migración por grupos funcionales
- Eliminación de 33 VMs apagadas
- Upgrade de 67 VMs con OS EOL
- Optimización continua

---

## 🔄 Proceso de Migración

### Fase 1: Preparación (Semanas 1-2)

#### 1.1 Infraestructura Base AWS

**Actividades**:
- ✅ Crear cuenta AWS y configurar Organizations
- ✅ Implementar AWS Landing Zone con Control Tower
- ✅ Configurar VPC Multi-AZ (10.0.0.0/16)
- ✅ Establecer conectividad híbrida (Direct Connect o VPN)
- ✅ Configurar IAM roles y políticas
- ✅ Implementar CloudWatch y SNS

**Arquitectura de Red**:
```
┌─────────────────────────────────────────────────────────────┐
│                      AWS Cloud (us-east-1)                   │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐ │
│  │                VPC 10.0.0.0/16                         │ │
│  │                                                         │ │
│  │  ┌──────────────────┐        ┌──────────────────┐     │ │
│  │  │  AZ-1a           │        │  AZ-1b           │     │ │
│  │  │                  │        │                  │     │ │
│  │  │  Public Subnet   │        │  Public Subnet   │     │ │
│  │  │  10.0.1.0/24     │        │  10.0.2.0/24     │     │ │
│  │  │  - ALB           │        │  - ALB           │     │ │
│  │  │  - NAT Gateway   │        │  - NAT Gateway   │     │ │
│  │  │                  │        │                  │     │ │
│  │  │  Private Subnet  │        │  Private Subnet  │     │ │
│  │  │  10.0.10.0/24    │        │  10.0.20.0/24    │     │ │
│  │  │  - EC2 Apps      │        │  - EC2 Apps      │     │ │
│  │  │                  │        │                  │     │ │
│  │  │  Private Subnet  │        │  Private Subnet  │     │ │
│  │  │  10.0.30.0/24    │        │  10.0.40.0/24    │     │ │
│  │  │  - RDS           │        │  - RDS           │     │ │
│  │  └──────────────────┘        └──────────────────┘     │ │
│  │                                                         │ │
│  └───────────────────────────────────────────────────────┘ │
│                           │                                 │
│                           │ Direct Connect / VPN            │
└───────────────────────────┼─────────────────────────────────┘
                            │
                    ┌───────▼────────┐
                    │  On-Premise    │
                    │  Datacenter    │
                    └────────────────┘
```

#### 1.2 Herramientas de Migración

**AWS Application Migration Service (MGN)**:
- Replicación continua de servidores
- Migración con downtime mínimo
- Validación antes de cutover

**AWS Database Migration Service (DMS)**:
- Migración de bases de datos
- Replicación continua
- Conversión de esquemas si es necesario

**AWS DataSync**:
- Transferencia de archivos y datos
- Sincronización automática

---

### Fase 2: Migración (Por Ola)

#### 2.1 Preparación de Aplicación

**Semana N**:
- Documentar configuración actual
- Identificar dependencias
- Crear backups completos
- Validar requisitos de red y seguridad
- Preparar plan de rollback

#### 2.2 Replicación

**Semana N+1**:
- Instalar agentes de MGN en servidores origen
- Iniciar replicación continua a AWS
- Validar integridad de datos
- Monitorear progreso de replicación

#### 2.3 Testing

**Semana N+2**:
- Lanzar instancias de prueba en AWS
- Validar funcionalidad de aplicación
- Realizar pruebas de integración
- Ajustar configuraciones según necesidad
- Pruebas de performance

#### 2.4 Cutover

**Fin de Semana (Ventana de Mantenimiento)**:
- Sincronización final de datos
- Detener aplicación en origen
- Activar aplicación en AWS
- Actualizar DNS/rutas
- Validación inmediata

#### 2.5 Estabilización

**Semana N+3**:
- Monitoreo 24/7 durante 72 horas
- Ajustes de performance
- Validación con usuarios
- Documentación de configuración final
- Desmantelar servidores origen (después de 2 semanas)

---

### Fase 3: Optimización (Continua)

#### 3.1 Quick Wins (Mes 1)

**Eliminar VMs Apagadas**:
- Validar con owners
- Crear snapshots
- Eliminar 33 VMs
- **Ahorro**: $51K/año

#### 3.2 Reserved Instances (Mes 3-4)

**Compra de RIs**:
- Analizar patrones de uso (2-4 semanas)
- Comprar RIs para 80% de VMs estables
- Distribución: 70% Standard, 30% Convertible
- **Ahorro**: $614K/año

#### 3.3 Auto Scaling (Mes 4-6)

**Implementación**:
- Configurar en 4 aplicaciones web/API
- Políticas: CPU 60-70%, min 2, max 6-10
- Validar comportamiento
- **Ahorro**: $251K/año

#### 3.4 Servicios Managed (Mes 6-12)

**Modernización**:
- Migrar bases de datos a RDS
- Refactorizar APIs a Lambda
- Containerizar aplicaciones en ECS
- **Ahorro**: $50K/año

---

## 💰 Inversión y Costos

### Costos de Migración (One-Time)

| Concepto | Costo |
|----------|-------|
| **Consultoría y Planificación** | $50,000 |
| **Herramientas de Migración** | $15,000 |
| **Capacitación Equipo** | $20,000 |
| **Soporte durante Migración** | $40,000 |
| **Contingencia (10%)** | $12,500 |
| **TOTAL INVERSIÓN** | **$137,500** |

### Costos Operativos AWS (Mensuales)

| Escenario | Mes 1-2 | Mes 3-6 | Mes 7-12 | Año 2-3 |
|-----------|---------|---------|----------|---------|
| **On-Demand** | $127,958 | $127,958 | $127,958 | $127,958 |
| **Con RIs** | $127,958 | $76,775 | $72,515 | $51,626 |
| **Optimizado** | $123,698 | $72,515 | $51,626 | $43,548 |

### Comparación 3 Años

| Concepto | On-Premise | AWS Optimizado | Ahorro |
|----------|------------|----------------|--------|
| **Año 1** | $1,450,000 | $950,000 | $500,000 |
| **Año 2** | $1,450,000 | $619,512 | $830,488 |
| **Año 3** | $1,450,000 | $522,581 | $927,419 |
| **Inversión Inicial** | - | $137,500 | - |
| **TOTAL 3 AÑOS** | **$4,350,000** | **$2,229,593** | **$2,120,407** |

**ROI**: 1,542% en 3 años  
**Payback Period**: 8 meses

---

## 📊 Análisis de Costos Detallado

### Desglose por Componente (Optimizado)

| Componente | Costo Mensual | Costo Anual |
|------------|---------------|-------------|
| **Compute (EC2)** | $30,000 | $360,000 |
| **Database (RDS)** | $5,300 | $63,600 |
| **Storage (EBS/S3)** | $4,500 | $54,000 |
| **Networking** | $1,200 | $14,400 |
| **Servicios Adicionales** | $2,548 | $30,581 |
| **TOTAL** | **$43,548** | **$522,581** |

### Estrategias de Ahorro Aplicadas

1. **Reserved Instances (1 año)**: -40% ($614K/año)
2. **Eliminar VMs apagadas**: -$51K/año
3. **Spot Instances (dev/test)**: -$47K/año
4. **Auto Scaling**: -$251K/año
5. **Servicios Managed**: -$50K/año

**Ahorro Total**: $1,012,916/año (66% vs On-Demand)

---

## 🎯 Beneficios del Proyecto

### Beneficios Financieros

✅ **Reducción de CAPEX**: Eliminar inversión en hardware  
✅ **Reducción de OPEX**: 64% menos costos operativos  
✅ **Modelo Pay-as-you-go**: Pagar solo por lo que se usa  
✅ **Eliminación de licencias VMware**: $150K/año  

### Beneficios Técnicos

✅ **Alta Disponibilidad**: 99.99% SLA con Multi-AZ  
✅ **Disaster Recovery**: RPO < 1 hora, RTO < 4 horas  
✅ **Escalabilidad**: Auto Scaling automático  
✅ **Performance**: Instancias optimizadas por workload  
✅ **Seguridad**: Cumplimiento con estándares internacionales  

### Beneficios Operacionales

✅ **Agilidad**: Provisión de recursos en minutos  
✅ **Automatización**: IaC con Terraform/CDK  
✅ **Monitoreo**: CloudWatch centralizado  
✅ **Backups**: Automáticos y gestionados  
✅ **Actualizaciones**: Managed services con patching automático  

### Beneficios Estratégicos

✅ **Innovación**: Acceso a 200+ servicios AWS  
✅ **Global**: Expansión a otras regiones en días  
✅ **Modernización**: Eliminar deuda técnica (67 VMs EOL)  
✅ **Competitividad**: Infraestructura de clase mundial  
✅ **Sostenibilidad**: Reducción de huella de carbono  

---

## ⚠️ Gestión de Riesgos

### Riesgos Identificados y Mitigaciones

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| **Downtime durante migración** | Media | Alto | Migración por fases, ventanas de mantenimiento, rollback plan |
| **Dependencias no documentadas** | Alta | Alto | Discovery exhaustivo, pruebas en cada ola |
| **Resistencia al cambio** | Media | Medio | Capacitación, comunicación continua, quick wins |
| **Sobrecostos** | Media | Medio | Monitoreo continuo, alertas de presupuesto, rightsizing |
| **Problemas de performance** | Baja | Alto | Pruebas de carga, sizing adecuado, monitoreo |
| **Pérdida de datos** | Baja | Crítico | Backups completos, validación de integridad, DMS |

### Plan de Contingencia

**Rollback**:
- Mantener servidores origen activos 2 semanas post-migración
- Backups completos antes de cada cutover
- Procedimiento de rollback documentado y probado
- Ventana de rollback: 4 horas

**Soporte**:
- Equipo de soporte 24/7 durante migraciones
- Escalamiento a AWS Support (Enterprise)
- War room durante cutover de aplicaciones críticas

---

## 📋 Entregables del Proyecto

### Documentación

- ✅ Arquitectura detallada de solución AWS
- ✅ Diagramas de red y seguridad (10 diagramas profesionales)
- ✅ Runbooks de migración por aplicación
- ✅ Procedimientos de rollback
- ✅ Guías de operación y mantenimiento
- ✅ Matriz de responsabilidades (RACI)

### Código y Configuración

- ✅ Infraestructura como Código (Terraform/CDK)
- ✅ Scripts de automatización
- ✅ Configuraciones de servicios AWS
- ✅ Pipelines CI/CD

### Reportes

- ✅ Inventario completo de infraestructura
- ✅ Análisis de costos detallado
- ✅ Recomendaciones de optimización
- ✅ Reportes de progreso semanales
- ✅ Reporte final de proyecto

### Capacitación

- ✅ Capacitación en AWS Fundamentals (2 días)
- ✅ Capacitación en servicios específicos (3 días)
- ✅ Sesiones de hands-on labs
- ✅ Documentación de mejores prácticas

---

## 👥 Equipo del Proyecto

### Equipo Stack Sense

- **Arquitecto de Soluciones AWS** (1)
- **Ingeniero de Migración** (2)
- **Especialista en Seguridad** (1)
- **Especialista en Networking** (1)
- **Project Manager** (1)

### Equipo BGR (Requerido)

- **Sponsor Ejecutivo** (1)
- **IT Manager** (1)
- **Administradores de Sistemas** (2-3)
- **DBAs** (1-2)
- **Networking** (1)
- **Security** (1)

---

## 📅 Cronograma Ejecutivo

```
Mes 1-2:  Ola 0 (Piloto)           ████████░░░░░░░░░░░░░░░░
Mes 3:    Ola 1 (Backoffice)       ░░░░░░░░████░░░░░░░░░░░░
Mes 4-5:  Ola 2 (Portales)         ░░░░░░░░░░░░████████░░░░
Mes 6:    Ola 3 (Portal Crítico)   ░░░░░░░░░░░░░░░░░░░░████
Mes 7-12: Ola 4 (Resto)            ░░░░░░░░░░░░░░░░░░░░░░░░████████████
```

**Duración Total**: 12 meses  
**Hitos Clave**: 4 olas completadas  
**Go-Live Final**: Mes 12

---

## 💼 Términos Comerciales

### Modelo de Contratación

**Opción 1: Precio Fijo**
- Inversión total: $137,500
- Incluye todas las actividades descritas
- Garantía de cumplimiento de cronograma

**Opción 2: Time & Materials**
- Tarifa por hora: $150-200/hora según rol
- Estimado: $137,500 (±10%)
- Flexibilidad en alcance

### Forma de Pago

- 30% al inicio del proyecto
- 30% al completar Ola 1
- 30% al completar Ola 3
- 10% al cierre del proyecto

### Garantías

- ✅ Cumplimiento de SLAs definidos
- ✅ Soporte post-migración (3 meses)
- ✅ Corrección de issues sin costo adicional
- ✅ Capacitación incluida

---

## 🎯 Próximos Pasos

### Semana 1-2: Kick-off

1. Firma de contrato
2. Reunión de kick-off
3. Asignación de equipo
4. Acceso a ambientes

### Semana 3-4: Preparación

1. Validación de inventario
2. Configuración de cuenta AWS
3. Implementación de Landing Zone
4. Preparación de herramientas

### Semana 5-6: Inicio Ola 0

1. Migración de SonarQube
2. Migración de Saras
3. Implementación de CloudWatch
4. Validación y estabilización

---

## 📞 Contacto

Para más información o aclaración de dudas:

**Equipo Stack Sense**  
Email: info@stacksense.com  
Teléfono: +1 (XXX) XXX-XXXX  
Web: www.stacksense.com

---

## 📎 Anexos

- **Anexo A**: Inventario Detallado de VMs
- **Anexo B**: Diagramas de Arquitectura (10 diagramas)
- **Anexo C**: Análisis de Costos Detallado
- **Anexo D**: Matriz de Riesgos Completa
- **Anexo E**: Plan de Proyecto Detallado

---

**Validez de la Propuesta**: 90 días desde la fecha de emisión  
**Fecha de Emisión**: 1 de Diciembre, 2025  
**Versión**: 1.0

---

*Esta propuesta es confidencial y está dirigida exclusivamente a BGR. No debe ser compartida con terceros sin autorización previa.*
