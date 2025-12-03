# Saras

**Criticidad**: Media  
**Tipo**: Aplicación Empresarial  
**Stack**: .NET/IIS  
**Base de Datos**: SQL Server

---

## 📊 Recursos Actuales

| Métrica | Valor |
|---------|-------|
| VMs | 2 |
| vCPUs | 12 |
| RAM | 18.0 GB |

### Servidores Identificados

| VM | vCPUs | RAM (GB) | OS | Estado |
|-------|-------|----------|-----|--------|
| ecbrprw83 | 8 | 10.0 | Microsoft Windows Server 2019  | poweredOn |
| ecbrtsw98 | 4 | 8.0 | Microsoft Windows Server 2019  | poweredOn |


---

## 🛠️ Stack Tecnológico

**Tecnologías detectadas:**
- SQL Server
- .NET
- Redis

**Puertos identificados:** 84, 92, 95, 8043


---

## 🏗️ Arquitectura AWS Propuesta

### Componentes Recomendados

**Compute:**
- EC2 instances (2+ para HA)
- Considerar: ECS si es containerizable

**Database:**
- RDS SQL Server (Multi-AZ para HA)
- Automated backups (7-35 días)
- Read replicas si es necesario

**Storage:**
- EBS gp3 para discos de aplicación
- S3 para archivos estáticos y backups
- EFS si requiere file sharing entre instancias

**Networking:**
- VPC con subnets públicas y privadas
- NAT Gateway para salida a internet
- VPC Endpoints para servicios AWS
- Route 53 para DNS

**Security:**
- Security Groups (least privilege)
- WAF en ALB (si es web pública)
- Secrets Manager para credenciales
- IAM roles para EC2
- KMS para encriptación

**Monitoring:**
- CloudWatch Logs y Metrics
- CloudWatch Alarms
- X-Ray para tracing (APIs)
- SNS para notificaciones


---

## 📐 Diagrama de Arquitectura

![Arquitectura AWS](../diagrams/arch_saras.png)

**Componentes principales:**
- Compute: EC2 / Auto Scaling
- Database: RDS Multi-AZ
- Load Balancing: ALB/NLB
- Storage: EBS / S3 / EFS
- Security: Security Groups, Secrets Manager
- Monitoring: CloudWatch, SNS

---

## 🎯 Estrategia de Migración

### Fase 1: Preparación
- [ ] Documentar dependencias con otras aplicaciones
- [ ] Identificar datos sensibles y requisitos de compliance
- [ ] Definir ventana de mantenimiento
- [ ] Preparar plan de rollback

### Fase 2: Infraestructura AWS
- [ ] Crear VPC y subnets
- [ ] Configurar Security Groups
- [ ] Provisionar RDS (si aplica)
- [ ] Configurar ALB/NLB

### Fase 3: Migración
- [ ] Migrar base de datos (DMS si es necesario)
- [ ] Migrar servidores de aplicación (MGN)
- [ ] Configurar Auto Scaling
- [ ] Pruebas funcionales

### Fase 4: Cutover
- [ ] Actualizar DNS
- [ ] Monitoreo intensivo 24-48h
- [ ] Validación con usuarios
- [ ] Desmantelar on-premise

---

## 📋 Dependencias

**Aplicaciones relacionadas:**
- *Pendiente de identificar*

**Servicios externos:**
- *Pendiente de identificar*

**Integraciones:**

**URLs identificadas:**
- https://MSAPIS-TEST.BGR.COM:8043
- https://MSAPIS.BGR.COM:8043
- https://ecbrprncapi.bgr.com:8043
- https://ecbrtsncapi.bgr.com:8043


---

## ⚠️ Riesgos y Consideraciones

- **Downtime**: Planificar ventana de mantenimiento
- **Datos**: Validar estrategia de migración de BD
- **Performance**: Realizar pruebas de carga en AWS
- **Costos**: Monitorear durante primeros 30 días

---

## 💰 Estimación de Costos (Preliminar)

*Pendiente de cálculo detallado en Fase 3*

**Componentes principales:**
- Compute (EC2): $XXX/mes
- Database (RDS): $XXX/mes
- Storage (EBS/S3): $XXX/mes
- Networking: $XXX/mes
- **Total estimado**: $XXX/mes

---

**Última actualización**: 2025-12-01  
**Estado**: En análisis
