# Plan de Migración - Backoffice Sistemas BGR

**Aplicación**: Backoffice Sistemas BGR  
**Estrategia**: Lift & Shift con Arquitectura Híbrida  
**Timeline**: 3 semanas  
**Fecha**: 2025-12-12

---

## 🚀 Plan de Migración Detallado

### Semana 1: Preparación e Infraestructura AWS

#### Día 1-2: Setup Conectividad Híbrida

**Actividades**:
- [ ] Solicitar Direct Connect (1 Gbps) - Lead time: 2-4 semanas
- [ ] Configurar Customer Gateway on-premise
- [ ] Crear Virtual Private Gateway en AWS
- [ ] Establecer VPN Site-to-Site (backup temporal)
- [ ] Configurar BGP routing
- [ ] Probar conectividad on-premise ↔ AWS
- [ ] Validar latencia < 10ms
- [ ] Configurar VPC Flow Logs

**Responsables**: Equipo de Networking BGR + AWS Solutions Architect

**Entregables**:
- ✅ Conectividad híbrida establecida
- ✅ Latencia validada < 10ms
- ✅ Redundancia configurada (VPN backup)

#### Día 3-4: Infraestructura AWS Base

**Actividades**:
- [ ] Crear VPC (10.100.0.0/16)
- [ ] Crear subnets (public y private en 2 AZs)
- [ ] Configurar Internet Gateway
- [ ] Configurar NAT Gateways (2 para HA)
- [ ] Configurar Route Tables
- [ ] Crear Security Groups (ALB, EC2, Management)
- [ ] Configurar Network ACLs
- [ ] Crear Application Load Balancer
- [ ] Configurar Target Groups
- [ ] Configurar Health Checks

**Responsables**: Equipo de Infraestructura BGR + AWS

**Entregables**:
- ✅ VPC y networking configurado
- ✅ Load Balancer operativo
- ✅ Security Groups creados

#### Día 5: Preparar Compute y Storage

**Actividades**:
- [ ] Lanzar 2 EC2 instances (t3.xlarge)
- [ ] Instalar Windows Server 2016 Standard
- [ ] Configurar EBS volumes (200 GB gp3)
- [ ] Instalar IIS Web Server
- [ ] Instalar .NET Framework 4.7.1
- [ ] Configurar Windows Firewall
- [ ] Instalar CloudWatch Agent
- [ ] Instalar SSM Agent
- [ ] Instalar CodeDeploy Agent
- [ ] Crear S3 buckets (artifacts, backups, logs)

**Responsables**: Equipo de Sistemas BGR

**Entregables**:
- ✅ EC2 instances listas
- ✅ Software base instalado
- ✅ Storage configurado

**Checkpoint Semana 1**:
- ✅ Infraestructura AWS completa
- ✅ Conectividad híbrida operativa
- ✅ Servidores preparados

---

### Semana 2: Configuración de Aplicación y Testing

#### Día 1-2: Despliegue de Aplicación

**Actividades**:
- [ ] Copiar código fuente desde on-premise
- [ ] Configurar IIS Sites y Application Pools
- [ ] Actualizar connection strings (SQL Server on-premise)
- [ ] Configurar LDAP connection (Active Directory)
- [ ] Configurar integración con microservicio notificador
- [ ] Configurar archivo ConfiguracionesServicioWeb.config
- [ ] Instalar plugins (ajaxToolkit, Bootstrap)
- [ ] Configurar SSL certificates en ALB
- [ ] Registrar instances en Target Group
- [ ] Validar health checks

**Responsables**: Equipo de Desarrollo BGR + TCS

**Entregables**:
- ✅ Aplicación desplegada en AWS
- ✅ Configuraciones actualizadas
- ✅ Health checks pasando

#### Día 3: Configuración CI/CD

**Actividades Azure DevOps**:
- [ ] Crear Service Connection a AWS (OIDC)
- [ ] Configurar IAM Role para Azure DevOps
- [ ] Crear Azure Pipeline (build + deploy)
- [ ] Configurar Azure Repos
- [ ] Crear appspec.yml para CodeDeploy
- [ ] Crear scripts de deployment (PowerShell)
- [ ] Configurar CodeDeploy Application
- [ ] Crear Deployment Group (Production)
- [ ] Probar deployment manual
- [ ] Validar rollback automático

**Responsables**: Equipo DevOps BGR

**Entregables**:
- ✅ Pipeline CI/CD configurado
- ✅ Deployment automatizado
- ✅ Rollback validado

#### Día 4: Testing Funcional

**Actividades**:
- [ ] Testing de autenticación (LDAP)
- [ ] Testing de conexión a base de datos
- [ ] Testing de funcionalidades core:
  - [ ] Gestión de Personas
  - [ ] Gestión de Departamentos/Empleados
  - [ ] Gestión de Proveedores
  - [ ] Gestión de Extensiones Telefónicas
- [ ] Testing de integración con notificador
- [ ] Testing de logs de auditoría
- [ ] Validar performance (latencia < 2s)
- [ ] Testing de carga (100 usuarios concurrentes)

**Responsables**: Equipo QA BGR

**Entregables**:
- ✅ Testing funcional completo
- ✅ Performance validado
- ✅ Bugs documentados y resueltos

#### Día 5: Configuración de Monitoreo

**Actividades**:
- [ ] Configurar CloudWatch Dashboards
- [ ] Crear CloudWatch Alarms:
  - [ ] EC2 CPU > 80% por 5 min
  - [ ] EC2 Memory > 80% por 5 min
  - [ ] ALB 5xx errors > 10
  - [ ] ALB Unhealthy targets > 0
  - [ ] Direct Connect down
  - [ ] VPN tunnel down
- [ ] Configurar SNS topics (email + SMS)
- [ ] Configurar CloudWatch Logs
- [ ] Configurar VPC Flow Logs
- [ ] Crear runbook de operaciones
- [ ] Documentar procedimientos de troubleshooting

**Responsables**: Equipo de Operaciones BGR

**Entregables**:
- ✅ Monitoreo completo configurado
- ✅ Alertas operativas
- ✅ Runbook documentado

**Checkpoint Semana 2**:
- ✅ Aplicación funcionando en AWS
- ✅ CI/CD operativo
- ✅ Testing completo
- ✅ Monitoreo activo

---

### Semana 3: Go-Live y Estabilización

#### Día 1: Preparación Go-Live

**Actividades**:
- [ ] Backup completo de producción on-premise
- [ ] Validar plan de rollback
- [ ] Comunicar ventana de mantenimiento a usuarios
- [ ] Preparar equipo de soporte (24/7)
- [ ] Validar checklist de go-live
- [ ] Freeze de cambios en código
- [ ] Sincronización final de datos
- [ ] Validación de conectividad híbrida

**Responsables**: Equipo completo BGR

**Entregables**:
- ✅ Backup completo
- ✅ Plan de rollback validado
- ✅ Equipo preparado

#### Día 2: Cutover (Sábado - Ventana de Mantenimiento)

**Timeline del Cutover**:

```
00:00 - Inicio ventana de mantenimiento
00:15 - Detener aplicación on-premise
00:30 - Backup final de base de datos
01:00 - Actualizar DNS (Route 53)
01:15 - Validar propagación DNS
01:30 - Activar tráfico en ALB
02:00 - Testing smoke con usuarios piloto
03:00 - Monitoreo intensivo
04:00 - Validación completa
05:00 - Go/No-Go decision
06:00 - Comunicar éxito o rollback
```

**Actividades**:
- [ ] Detener aplicación on-premise
- [ ] Actualizar DNS a ALB de AWS
- [ ] Validar propagación DNS (nslookup)
- [ ] Activar tráfico en AWS
- [ ] Testing con usuarios piloto (10 usuarios)
- [ ] Validar logs de aplicación
- [ ] Validar métricas de CloudWatch
- [ ] Validar conectividad a base de datos
- [ ] Validar autenticación LDAP
- [ ] Monitoreo intensivo (2 horas)

**Responsables**: Equipo completo BGR + AWS Support

**Criterios Go/No-Go**:
- ✅ DNS propagado correctamente
- ✅ Health checks pasando
- ✅ Usuarios piloto validando OK
- ✅ Latencia < 2s
- ✅ Sin errores críticos en logs
- ✅ Conectividad híbrida estable

**Plan de Rollback** (si No-Go):
1. Revertir DNS a on-premise (5 min)
2. Reactivar aplicación on-premise (10 min)
3. Validar funcionamiento (15 min)
4. Comunicar a usuarios (inmediato)
5. Análisis post-mortem (siguiente día)

#### Día 3-4: Monitoreo Post-Deploy

**Actividades**:
- [ ] Monitoreo 24/7 (turnos de 8 horas)
- [ ] Validar métricas cada hora:
  - [ ] CPU, RAM, Disk, Network
  - [ ] ALB requests, latency, errors
  - [ ] Conectividad híbrida
  - [ ] Logs de aplicación
- [ ] Recolectar feedback de usuarios
- [ ] Documentar incidentes
- [ ] Ajustes de performance (si necesario)
- [ ] Optimización de queries (si necesario)
- [ ] Ajustes de configuración (si necesario)

**Responsables**: Equipo de Operaciones BGR (turnos)

**Entregables**:
- ✅ Aplicación estable en producción
- ✅ Usuarios satisfechos
- ✅ Incidentes documentados

#### Día 5: Documentación y Handover

**Actividades**:
- [ ] Actualizar documentación de arquitectura
- [ ] Documentar configuraciones AWS
- [ ] Crear runbook de operaciones
- [ ] Documentar procedimientos de troubleshooting
- [ ] Crear guía de deployment
- [ ] Documentar lecciones aprendidas
- [ ] Training a equipo de soporte
- [ ] Training a equipo de operaciones
- [ ] Retrospectiva del proyecto
- [ ] Celebración del equipo 🎉

**Responsables**: Arquitecto + Líderes de equipo

**Entregables**:
- ✅ Documentación completa
- ✅ Equipo capacitado
- ✅ Lecciones aprendidas documentadas

**Checkpoint Semana 3**:
- ✅ Aplicación en producción AWS
- ✅ Usuarios operando normalmente
- ✅ Monitoreo estable
- ✅ Documentación completa
- ✅ Equipo capacitado

---

## 📋 Checklist Completo de Migración

### Pre-Migración
- [ ] Auditoría de aplicación actual
- [ ] Documentar dependencias
- [ ] Backup completo on-premise
- [ ] Plan de rollback documentado
- [ ] Comunicación a stakeholders
- [ ] Aprobación de ventana de mantenimiento
- [ ] Equipo de soporte preparado

### Infraestructura AWS
- [ ] VPC creado (10.100.0.0/16)
- [ ] Subnets configuradas (2 AZs)
- [ ] Security Groups creados
- [ ] Load Balancer configurado
- [ ] EC2 instances lanzadas (2x t3.xlarge)
- [ ] Conectividad híbrida establecida
- [ ] Direct Connect operativo
- [ ] VPN backup configurado

### Aplicación
- [ ] Software instalado (IIS, .NET 4.7.1)
- [ ] Aplicación desplegada
- [ ] Configuraciones actualizadas
- [ ] Connection strings configurados
- [ ] LDAP integrado
- [ ] Microservicio notificador integrado
- [ ] SSL certificates configurados
- [ ] Health checks pasando

### CI/CD
- [ ] Azure DevOps Service Connection
- [ ] IAM Roles configurados
- [ ] Azure Pipeline creado
- [ ] CodeDeploy configurado
- [ ] appspec.yml creado
- [ ] Scripts de deployment
- [ ] Deployment manual validado
- [ ] Rollback automático validado

### Testing
- [ ] Testing funcional completo
- [ ] Testing de autenticación
- [ ] Testing de base de datos
- [ ] Testing de integración
- [ ] Testing de performance
- [ ] Testing de carga
- [ ] Testing de seguridad
- [ ] UAT con usuarios

### Monitoreo
- [ ] CloudWatch Dashboards
- [ ] CloudWatch Alarms
- [ ] SNS topics configurados
- [ ] CloudWatch Logs
- [ ] VPC Flow Logs
- [ ] Runbook de operaciones
- [ ] Procedimientos de troubleshooting

### Go-Live
- [ ] DNS actualizado
- [ ] Tráfico en AWS
- [ ] Usuarios validando
- [ ] Monitoreo intensivo
- [ ] Sin errores críticos
- [ ] Performance OK
- [ ] Comunicación de éxito

### Post-Deploy
- [ ] Documentación actualizada
- [ ] Training completado
- [ ] Lecciones aprendidas
- [ ] Retrospectiva
- [ ] Celebración 🎉

---

## ⚠️ Riesgos y Mitigaciones

### Riesgo 1: Latencia en Conectividad Híbrida
**Probabilidad**: MEDIA  
**Impacto**: ALTO  
**Descripción**: Latencia > 10ms entre AWS y base de datos on-premise puede afectar performance de la aplicación.

**Mitigación**:
- Usar Direct Connect (1 Gbps) en lugar de VPN
- Implementar connection pooling agresivo
- Configurar timeouts apropiados (30s)
- Implementar retry logic con exponential backoff
- Monitorear latencia en tiempo real
- Tener plan de rollback listo

### Riesgo 2: Falla en Autenticación LDAP
**Probabilidad**: BAJA  
**Impacto**: CRÍTICO  
**Descripción**: Problemas de conectividad con Active Directory on-premise pueden impedir login de usuarios.

**Mitigación**:
- Validar conectividad LDAP en testing exhaustivo
- Configurar timeouts apropiados
- Implementar circuit breaker
- Tener credenciales de emergencia
- Monitorear conexiones LDAP
- Plan de rollback inmediato

### Riesgo 3: Incompatibilidad de .NET Framework 4.7.1
**Probabilidad**: BAJA  
**Impacto**: ALTO  
**Descripción**: .NET Framework 4.7.1 es obsoleto y puede tener problemas en Windows Server 2016.

**Mitigación**:
- Testing exhaustivo en ambiente de desarrollo
- Validar todas las funcionalidades
- Tener ambiente de rollback listo
- Considerar upgrade a .NET Framework 4.8 (post-migración)
- Documentar workarounds

### Riesgo 4: Falla en Direct Connect
**Probabilidad**: BAJA  
**Impacto**: CRÍTICO  
**Descripción**: Falla en Direct Connect puede dejar aplicación sin acceso a base de datos.

**Mitigación**:
- Configurar VPN Site-to-Site como backup
- Failover automático a VPN
- Monitorear estado de Direct Connect
- Alertas inmediatas de falla
- SLA de AWS Direct Connect (99.95%)
- Plan de contingencia documentado

### Riesgo 5: Problemas en Cutover
**Probabilidad**: MEDIA  
**Impacto**: ALTO  
**Descripción**: Problemas durante el cutover pueden extender ventana de mantenimiento.

**Mitigación**:
- Ensayar cutover en ambiente de test
- Documentar cada paso del cutover
- Tener equipo completo disponible
- Ventana de mantenimiento amplia (6 horas)
- Plan de rollback detallado (< 30 min)
- Comunicación constante con stakeholders

### Riesgo 6: Resistencia al Cambio de Usuarios
**Probabilidad**: MEDIA  
**Impacto**: MEDIO  
**Descripción**: Usuarios pueden resistirse al cambio o reportar problemas menores como críticos.

**Mitigación**:
- Comunicación temprana y frecuente
- Training a usuarios clave
- Usuarios piloto en testing
- Soporte 24/7 primera semana
- FAQ documentado
- Canal de comunicación directo

---

## ✅ Criterios de Éxito

1. ✅ **Aplicación funcionando** en AWS sin errores críticos
2. ✅ **Performance** igual o mejor que on-premise (latencia < 2s)
3. ✅ **Disponibilidad** > 99.9% (SLA)
4. ✅ **Conectividad híbrida** estable (latencia < 10ms)
5. ✅ **Zero data loss** durante migración
6. ✅ **Usuarios satisfechos** (> 90% feedback positivo)
7. ✅ **CI/CD operativo** con deployments automatizados
8. ✅ **Monitoreo completo** con alertas configuradas
9. ✅ **Documentación completa** y equipo capacitado
10. ✅ **Costo** dentro del presupuesto ($450/mes)

---

## 🎯 Próximos Pasos Inmediatos

1. [ ] **Aprobar plan de migración** - Stakeholders BGR
2. [ ] **Solicitar Direct Connect** - Equipo de Networking (lead time 2-4 semanas)
3. [ ] **Asignar equipo técnico** - Gerencia BGR
4. [ ] **Crear ambiente AWS** - Equipo de Infraestructura
5. [ ] **Configurar Azure DevOps** - Equipo DevOps
6. [ ] **Iniciar testing** - Equipo QA
7. [ ] **Programar ventana de mantenimiento** - Gerencia BGR

---

**Última actualización**: 2025-12-12  
**Versión**: 1.0  
**Estado**: DRAFT - Pendiente de aprobación
