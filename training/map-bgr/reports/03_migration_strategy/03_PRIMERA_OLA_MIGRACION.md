# Primera Ola de Migración - MAP-BGR

**Fecha**: 2025-12-01  
**Objetivo**: Migrar aplicaciones piloto a AWS  
**Duración estimada**: 4-6 semanas

---

## 🎯 Estrategia de Primera Ola

### Criterios de Selección

**Aplicaciones seleccionadas para Ola 1:**
1. ✅ **Criticidad Media** (menor riesgo)
2. ✅ **Arquitectura simple** (fácil de migrar)
3. ✅ **Pocas dependencias** (menor complejidad)
4. ✅ **Buen candidato para aprendizaje** (validar proceso)

---

## 📱 Aplicaciones Seleccionadas

### 1. Sonar Qube (Herramienta DevOps) - PILOTO
**Criticidad**: Media  
**VMs**: 5 servidores  
**Recursos**: 42 vCPUs, 144 GB RAM

**Razones para selección:**
- ✅ No es crítica para negocio (herramienta interna)
- ✅ Arquitectura estándar (App + DB)
- ✅ Comunidad activa y documentación
- ✅ Fácil rollback si hay problemas

**Servidores identificados:**
- ecbrprq45 (16 vCPUs, 24 GB)
- ecbrprq64 (16 vCPUs, 18 GB)
- ecbrprq69 (12 vCPUs, 120 GB) - Base de datos
- Y otros 2 servidores

### 2. Saras (Aplicación Empresarial)
**Criticidad**: Media  
**VMs**: 2 servidores  
**Recursos**: 12 vCPUs, 18 GB RAM

**Razones para selección:**
- ✅ Aplicación pequeña (2 VMs)
- ✅ Criticidad media
- ✅ Buena para validar proceso

**Servidores identificados:**
- 2 servidores a confirmar

### 3. Seq (Logging/Observabilidad)
**Criticidad**: Media  
**VMs**: 5 servidores  
**Recursos**: 42 vCPUs, 144 GB RAM

**Razones para selección:**
- ✅ Herramienta de soporte (no crítica)
- ✅ Puede mejorar observabilidad en AWS
- ✅ Fácil de reemplazar si falla

---

## 📊 Resumen de Primera Ola

| Métrica | Valor |
|---------|-------|
| **Aplicaciones** | 3 |
| **VMs Totales** | 12 |
| **vCPUs Totales** | 96 |
| **RAM Total** | 306 GB |
| **% del Total** | ~3% de VMs, ~5% de recursos |

---

## 🏗️ Arquitecturas de Referencia

### Diagrama General - Primera Ola

![Primera Ola General](https://stack-sense.s3.us-east-1.amazonaws.com/map-bgr/diagrams/primera_ola_general.png)

---

### Arquitectura 1: Sonar Qube

![Arquitectura SonarQube](https://stack-sense.s3.us-east-1.amazonaws.com/map-bgr/diagrams/arch_sonarqube.png)

**Componentes AWS:**
- **Compute**: 
  - EC2 t3.xlarge (4 vCPU, 16 GB) x2 en Auto Scaling
  - Application Load Balancer
- **Database**: 
  - RDS PostgreSQL db.r5.2xlarge (8 vCPU, 64 GB) Multi-AZ
- **Storage**: 
  - EBS gp3 500 GB para app
  - RDS storage 500 GB
- **Networking**: 
  - VPC con 3 subnets (1 pública, 2 privadas)
  - NAT Gateway
- **Security**: 
  - Security Groups restrictivos
  - Secrets Manager para credenciales
- **Backup**: 
  - RDS automated backups (7 días)
  - AWS Backup para EBS

**Estimación de costos mensual**: ~$1,200 USD

---

### Arquitectura 2: Saras (Aplicación Simple)

![Arquitectura Saras](https://stack-sense.s3.us-east-1.amazonaws.com/map-bgr/diagrams/arch_saras.png)

**Componentes AWS:**
- **Compute**: 
  - EC2 t3.large (2 vCPU, 8 GB) x2
- **Database**: 
  - RDS SQL Server db.t3.medium (2 vCPU, 4 GB) Multi-AZ
- **Storage**: 
  - EBS gp3 100 GB
- **Networking**: 
  - VPC con 2 subnets privadas
- **Security**: 
  - Security Groups
  - Secrets Manager

**Estimación de costos mensual**: ~$600 USD

---

### Arquitectura 3: Seq (Logging)

#### Opción Recomendada: CloudWatch

![Arquitectura Seq CloudWatch](https://stack-sense.s3.us-east-1.amazonaws.com/map-bgr/diagrams/arch_seq_cloudwatch.png)

**Componentes AWS:**
- **Opción 2 - Refactor** (Recomendado):
  - CloudWatch Logs
  - CloudWatch Insights
  - S3 para almacenamiento largo plazo

**Estimación de costos mensual**: ~$300 USD (ahorro 60%)

---

#### Opción Alternativa: EC2

![Arquitectura Seq EC2](https://stack-sense.s3.us-east-1.amazonaws.com/map-bgr/diagrams/arch_seq_ec2.png)

**Componentes AWS:**
- **Opción 1 - Rehost**: 
  - EC2 t3.xlarge x2
  - EBS gp3 1 TB
  - NLB
- **Opción 2 - Refactor** (Recomendado):
  - CloudWatch Logs
  - CloudWatch Insights
  - S3 para almacenamiento largo plazo

**Estimación de costos mensual**: 
- Opción 1: ~$800 USD
- Opción 2: ~$300 USD (ahorro 60%)

---

## 📋 Plan de Ejecución Detallado

### Semana 1-2: Preparación

#### Infraestructura Base AWS
- [ ] Crear cuenta AWS (si no existe)
- [ ] Configurar AWS Organizations
- [ ] Implementar Landing Zone
- [ ] Crear VPC de producción (10.0.0.0/16)
- [ ] Configurar subnets (públicas y privadas)
- [ ] Configurar NAT Gateway
- [ ] Configurar VPN/Direct Connect a on-premise
- [ ] Implementar Security Groups base
- [ ] Configurar IAM roles y políticas
- [ ] Configurar CloudWatch y SNS

#### Preparación de Aplicaciones
- [ ] **Sonar Qube**:
  - [ ] Documentar configuración actual
  - [ ] Identificar plugins y extensiones
  - [ ] Backup completo de BD
  - [ ] Documentar integraciones (CI/CD)
  
- [ ] **Saras**:
  - [ ] Documentar configuración
  - [ ] Backup de BD
  - [ ] Identificar usuarios y permisos
  
- [ ] **Seq**:
  - [ ] Documentar fuentes de logs
  - [ ] Evaluar migración a CloudWatch
  - [ ] Backup de configuración

### Semana 3-4: Migración

#### Sonar Qube (Días 1-5)
- [ ] **Día 1**: Provisionar infraestructura AWS
  - [ ] Crear RDS PostgreSQL
  - [ ] Crear EC2 instances
  - [ ] Configurar ALB
  - [ ] Configurar Security Groups
  
- [ ] **Día 2-3**: Migrar base de datos
  - [ ] Usar AWS DMS para migración inicial
  - [ ] Validar integridad de datos
  - [ ] Configurar replicación continua
  
- [ ] **Día 4**: Migrar aplicación
  - [ ] Instalar SonarQube en EC2
  - [ ] Configurar conexión a RDS
  - [ ] Migrar plugins y configuración
  
- [ ] **Día 5**: Pruebas y validación
  - [ ] Pruebas funcionales
  - [ ] Validar integraciones CI/CD
  - [ ] Pruebas de performance

#### Saras (Días 6-8)
- [ ] **Día 6**: Provisionar infraestructura
  - [ ] Crear RDS SQL Server
  - [ ] Crear EC2 instances
  
- [ ] **Día 7**: Migrar BD y app
  - [ ] Migrar base de datos
  - [ ] Instalar aplicación
  
- [ ] **Día 8**: Pruebas
  - [ ] Validación funcional
  - [ ] Pruebas de usuarios

#### Seq (Días 9-10)
- [ ] **Día 9**: Implementar solución
  - [ ] Opción 1: Migrar Seq a EC2
  - [ ] Opción 2: Configurar CloudWatch (recomendado)
  
- [ ] **Día 10**: Configurar fuentes
  - [ ] Redirigir logs a nueva solución
  - [ ] Validar recepción de logs

### Semana 5: Cutover y Estabilización

#### Cutover (Fin de semana)
- [ ] **Sonar Qube**:
  - [ ] Sincronización final de BD
  - [ ] Actualizar DNS/URLs
  - [ ] Redirigir tráfico a AWS
  - [ ] Monitoreo intensivo 24h
  
- [ ] **Saras**:
  - [ ] Sincronización final
  - [ ] Cutover de aplicación
  - [ ] Validación con usuarios
  
- [ ] **Seq**:
  - [ ] Redirigir todos los logs
  - [ ] Validar recepción

#### Estabilización (Semana completa)
- [ ] Monitoreo 24/7
- [ ] Ajustes de performance
- [ ] Optimización de costos
- [ ] Documentación de lecciones aprendidas

### Semana 6: Cierre y Documentación

- [ ] Validación final con stakeholders
- [ ] Documentar configuración final
- [ ] Actualizar runbooks
- [ ] Desmantelar servidores on-premise
- [ ] Reporte de lecciones aprendidas
- [ ] Planificar Ola 2

---

## 🎯 Dependencias Identificadas

### Sonar Qube
**Dependencias externas:**
- Integración con Jenkins/GitLab CI
- Conexión a repositorios Git
- LDAP/Active Directory para autenticación

**Mitigación:**
- Mantener conectividad híbrida (VPN)
- Configurar VPC Peering si es necesario
- Documentar endpoints y puertos

### Saras
**Dependencias externas:**
- Conexión a sistemas core banking (posible)
- Integración con Active Directory

**Mitigación:**
- Validar conectividad antes de cutover
- Mantener VPN activa

### Seq
**Dependencias externas:**
- Recibe logs de múltiples aplicaciones

**Mitigación:**
- Actualizar configuración de aplicaciones gradualmente
- Mantener Seq on-premise en paralelo 1 semana

---

## ⚠️ Riesgos y Mitigaciones

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| Latencia en conectividad híbrida | Media | Alto | Implementar Direct Connect antes de migración |
| Pérdida de datos en migración BD | Baja | Alto | Backups completos, validación de integridad, rollback plan |
| Incompatibilidad de versiones | Media | Medio | Validar versiones en ambiente de prueba |
| Downtime extendido | Baja | Alto | Ventana de mantenimiento amplia, rollback automatizado |
| Costos mayores a estimado | Media | Medio | Monitoreo de costos diario, alertas configuradas |
| Dependencias no documentadas | Alta | Alto | Discovery exhaustivo, pruebas en paralelo |

---

## 💰 Estimación de Costos Primera Ola

### Costos Mensuales Recurrentes

| Aplicación | Compute | Database | Storage | Networking | Total/mes |
|------------|---------|----------|---------|------------|-----------|
| Sonar Qube | $300 | $600 | $100 | $200 | $1,200 |
| Saras | $200 | $250 | $50 | $100 | $600 |
| Seq (Opción 1) | $300 | - | $300 | $200 | $800 |
| Seq (Opción 2) | - | - | $200 | $100 | $300 |
| **Total** | | | | | **$2,600 - $2,900** |

### Costos One-Time

- Migración (DMS, MGN): $500
- Consultoría/Soporte: $5,000
- Capacitación equipo: $2,000
- **Total One-Time**: $7,500

### Comparación vs On-Premise

**Estimación on-premise (3 apps, 12 VMs):**
- Hardware amortizado: $1,500/mes
- Licencias: $800/mes
- Energía y cooling: $400/mes
- Personal (parcial): $2,000/mes
- **Total on-premise**: ~$4,700/mes

**Ahorro potencial**: 
- Sin optimización: -$1,800/mes (38% más caro)
- Con optimización (RIs, rightsizing): $2,100/mes → **Ahorro de $2,600/mes (55%)**

---

## 📊 KPIs de Éxito

### Técnicos
- [ ] Uptime > 99.5% post-migración
- [ ] Latencia < 100ms (p95)
- [ ] 0 pérdida de datos
- [ ] Tiempo de migración < 6 semanas

### Negocio
- [ ] 0 incidentes críticos
- [ ] Satisfacción usuarios > 85%
- [ ] Costos dentro de presupuesto (+/- 10%)
- [ ] Documentación completa al 100%

### Aprendizaje
- [ ] Runbooks actualizados
- [ ] Equipo capacitado en AWS
- [ ] Lecciones aprendidas documentadas
- [ ] Proceso optimizado para Ola 2

---

## 📅 Cronograma Visual

```
Semana 1-2: Preparación
████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░

Semana 3-4: Migración
░░░░░░░░░░░░████████████░░░░░░░░░░░░░░░░

Semana 5: Cutover
░░░░░░░░░░░░░░░░░░░░░░░░████████░░░░░░░░

Semana 6: Cierre
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████
```

---

## 🎓 Lecciones para Ola 2

**Aplicar aprendizajes de Ola 1 para:**
- Aplicaciones críticas (Portales BGR)
- Mayor cantidad de VMs
- Arquitecturas más complejas
- Menor tiempo de migración

---

**Última actualización**: 2025-12-01  
**Estado**: Planificación  
**Aprobación requerida**: Pendiente
