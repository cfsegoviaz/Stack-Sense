# Brightmail - Plan de Modernización
## Antispam Symantec para Notificaciones BGR

**Fecha**: 2026-01-07  
**Aplicación**: Brightmail  
**Estrategia Recomendada**: Amazon SES (Replace)  
**Timeline**: 3 semanas

---

## 🎯 Información de la Aplicación

### Descripción
Sistema antispam Symantec Brightmail SMG para filtrado de correos y notificaciones del banco. Instalado en servidor CentOS 7 Linux.

### Situación Actual

| Atributo | Valor |
|----------|-------|
| **Servidor** | notificaciones.bgr.com.ec |
| **IP** | 172.20.115.32 |
| **vCPUs** | 4 |
| **RAM** | 8 GB |
| **Storage** | 100 GB |
| **OS** | CentOS 7 Linux |
| **Versión** | Brightmail SMG 10.9.1 |
| **Criticidad** | Media |

### ⚠️ Hallazgos Clave
- **CentOS 7 EOL**: Sistema operativo llegó a fin de vida en junio 2024
- **Licencias Symantec**: Costo recurrente de licenciamiento
- **Uso principal**: Notificaciones transaccionales (no email corporativo)
- **Volumen**: ~500K emails/mes
- **Candidato ideal para Amazon SES**: Servicio managed sin licencias

---

## 🏗️ Opciones de Arquitectura

### Opción 1: Amazon SES Nativo (RECOMENDADA)

![Arquitectura SES](./diagrams/generated-diagrams/brightmail_ses.png)

| Servicio | Configuración | Costo/mes |
|----------|---------------|-----------|
| Amazon SES | Email sending | $50 |
| Lambda | Filtrado custom | $10 |
| SNS | Notificaciones bounce/complaint | $10 |
| S3 | Logs y archivos | $10 |
| CloudWatch | Métricas y alertas | $10 |
| **TOTAL** | | **$100/mes** |

**Ahorro**: 75% vs costo actual ($400/mes)

#### 💡 Tips y Recomendaciones IA

**Cuándo elegir:**
- Notificaciones transaccionales
- Alto volumen de emails
- Eliminar licencias Symantec
- Escalabilidad automática requerida

**Consideraciones:**
- Configurar DKIM, SPF y DMARC para deliverability
- Warmup de IP para nuevos dominios
- Monitorear bounce rates (< 5%)
- Configurar complaint feedback loops

**Recomendaciones:**
- Empezar con volumen bajo e incrementar gradualmente
- Usar dedicated IPs para volumen alto
- Implementar Lambda para filtrado custom si necesario
- Configurar SNS para notificaciones de bounces

**Ideal para:**
- Notificaciones transaccionales bancarias
- Confirmaciones de operaciones
- Alertas de seguridad
- OTPs y códigos de verificación

#### 📋 Esfuerzo Escala24x7

| Tarea | Horas | Equipo |
|-------|-------|--------|
| SES Configuration | 4 | Infra |
| Lambda Function (filtrado) | 8 | Infra |
| SNS Configuration | 4 | Infra |
| S3 Bucket | 2 | Infra |
| CloudWatch Dashboard | 8 | Infra |
| Route 53 (DKIM/SPF) | 2 | Infra |
| Testing y validación | 8 | Infra |
| Knowledge transfer | 4 | Infra |
| **TOTAL** | **40** | |

**Costo implementación**: 40 horas × $150/hora = **$6,000 USD**

---

### Opción 2: EC2 Linux Lift & Shift

![Arquitectura EC2](./diagrams/generated-diagrams/brightmail_ec2.png)

| Servicio | Configuración | Costo/mes |
|----------|---------------|-----------|
| EC2 t3.large | Amazon Linux 2 | $80 |
| Symantec License | Brightmail SMG | $150 |
| EBS gp3 | 100 GB | $10 |
| CloudWatch | Logs y métricas | $10 |
| **TOTAL** | | **$300/mes** |

**Ahorro**: 25% vs costo actual

#### 💡 Tips y Recomendaciones IA

**Cuándo elegir:**
- Timeline muy agresivo
- Paso intermedio antes de SES
- Requisitos de compliance específicos

**Consideraciones:**
- CentOS 7 EOL - migrar a Amazon Linux 2
- Mantiene costo de licencias Symantec
- Requiere mantenimiento de servidor
- Planificar migración a SES

**Recomendaciones:**
- Solo como paso intermedio
- Migrar OS a Amazon Linux 2
- Documentar configuración para SES
- Planificar migración en 6 meses

**Ideal para:**
- Migraciones urgentes con deadline
- Organizaciones con restricciones de cambio

#### 📋 Esfuerzo Escala24x7

| Tarea | Horas | Equipo |
|-------|-------|--------|
| EC2 Instance | 2 | Infra |
| EBS Storage | 2 | Infra |
| CloudWatch Logs | 4 | Infra |
| MGN Configuration | 2 | Infra |
| MGN Migration | 1 | Infra |
| MGN Tests | 1 | Infra |
| Testing y validación | 8 | Infra |
| Knowledge transfer | 4 | Infra |
| **TOTAL** | **24** | |

**Costo implementación**: 24 horas × $150/hora = **$3,600 USD**

---

### Opción 3: Amazon WorkMail

![Arquitectura WorkMail](./diagrams/generated-diagrams/brightmail_ses.png)

| Servicio | Configuración | Costo/mes |
|----------|---------------|-----------|
| Amazon WorkMail | Enterprise | $150 |
| S3 | Archivos adjuntos | $20 |
| CloudWatch | Logs | $10 |
| **TOTAL** | | **$200/mes** |

**Ahorro**: 50% vs costo actual

#### 💡 Tips y Recomendaciones IA

**Cuándo elegir:**
- Se requiere email corporativo completo
- No solo notificaciones transaccionales
- Calendarios y contactos incluidos

**Consideraciones:**
- Mayor costo que SES
- Incluye antispam y antivirus
- Integración con Active Directory
- Solo si se necesita email completo

**Recomendaciones:**
- Evaluar si solo se necesitan notificaciones
- Usar SES si solo son transaccionales
- WorkMail para email corporativo completo

**Ideal para:**
- Email corporativo managed
- Organizaciones sin Exchange/O365

#### 📋 Esfuerzo Escala24x7

| Tarea | Horas | Equipo |
|-------|-------|--------|
| WorkMail Configuration | 8 | Infra |
| S3 Bucket | 2 | Infra |
| Route 53 DNS | 2 | Infra |
| CloudWatch Logs | 4 | Infra |
| Migración usuarios | 8 | Infra |
| Testing y validación | 8 | Infra |
| Knowledge transfer | 8 | Infra |
| **TOTAL** | **40** | |

**Costo implementación**: 40 horas × $150/hora = **$6,000 USD**

---

## 📊 Comparativa

| Criterio | SES Nativo | EC2 Lift & Shift | WorkMail |
|----------|------------|------------------|----------|
| **Costo/mes** | $100 | $300 | $200 |
| **Ahorro** | 75% | 25% | 50% |
| **Licencias** | ❌ No | ✅ Symantec | ❌ No |
| **Managed** | ✅ Sí | ❌ No | ✅ Sí |
| **Escalabilidad** | Automática | Manual | Automática |
| **Complejidad** | Baja | Media | Baja |
| **Timeline** | 3 semanas | 2 semanas | 3 semanas |

---

## 🔄 Plan de Migración SES

### Fase 1: Preparación (Semana 1)
- Configurar cuenta SES en producción
- Verificar dominio bgr.com.ec
- Configurar DKIM, SPF, DMARC
- Crear Lambda para filtrado (si necesario)

### Fase 2: Testing (Semana 2)
- Warmup de IP con volumen bajo
- Pruebas con subset de notificaciones
- Validar deliverability
- Configurar monitoreo CloudWatch

### Fase 3: Migración (Semana 3)
- Migrar aplicaciones a usar SES
- Monitorear bounce/complaint rates
- Decomisionar Brightmail
- Documentación final

---

## ✅ Recomendación Final

**Amazon SES Nativo** por:
1. **75% ahorro** ($100/mes vs $400/mes)
2. **Sin licencias Symantec** - elimina costo recurrente
3. **Servicio managed** - sin mantenimiento de servidor
4. **Escalabilidad automática** - crece con demanda
5. **Alta deliverability** - reputación AWS
6. **Integración nativa** - Lambda, SNS, CloudWatch

---

**Última actualización**: 2026-01-07
