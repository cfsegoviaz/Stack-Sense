# Resumen Ejecutivo - Mapeo de Aplicaciones MAP-BGR

**Fecha**: 2025-12-01  
**Aplicaciones Analizadas**: 8  
**VMs Identificadas**: 36 (9.4% del total)

---

## 📊 Inventario de Aplicaciones

| # | Aplicación | Tipo | Criticidad | VMs | vCPUs | RAM (GB) | Stack |
|---|------------|------|------------|-----|-------|----------|-------|
| 1 | **PortalAdmBGR** | Portal Web | Alta | 6 | 48 | 156 | Unknown |
| 2 | **PortalGuiaBGR** | Portal Web | Alta | 5 | 42 | 144 | Unknown |
| 3 | **Api Portal** | Portal Web | Alta | 5 | 42 | 144 | Unknown |
| 4 | **Backoffice Banca Digital** | Backoffice | Alta | 3 | 10 | 20 | Unknown |
| 5 | **Backoffice Sistemas** | Backoffice | Media | 5 | 42 | 144 | Unknown |
| 6 | **Sonar Qube** | DevOps | Media | 5 | 42 | 144 | Unknown |
| 7 | **Seq** | Logging | Media | 5 | 42 | 144 | Unknown |
| 8 | **Saras** | Empresarial | Media | 2 | 12 | 18 | Unknown |
| | **TOTAL** | | | **36** | **280** | **914** | |

---

## 🎯 Clasificación por Criticidad

### Alta Criticidad (4 aplicaciones)
**Aplicaciones de cara al cliente y operaciones críticas**

- **PortalAdmBGR** - Portal administrativo BGR
- **PortalGuiaBGR** - Portal de guía para clientes
- **Api Portal** - APIs de integración
- **Backoffice Banca Digital** - Operaciones bancarias

**Total**: 19 VMs, 142 vCPUs, 464 GB RAM

**Estrategia**: Migración en Ola 2-3, después de validar proceso con apps no críticas

### Media Criticidad (4 aplicaciones)
**Herramientas de soporte y aplicaciones internas**

- **Backoffice Sistemas** - Gestión de sistemas
- **Sonar Qube** - Análisis de código
- **Seq** - Logging y observabilidad
- **Saras** - Aplicación empresarial

**Total**: 17 VMs, 138 vCPUs, 450 GB RAM

**Estrategia**: Candidatas para Ola 1 (piloto)

---

## 🏗️ Arquitecturas Propuestas por Tipo

### Tipo 1: Portales Web (3 aplicaciones)
**Aplicaciones**: PortalAdmBGR, PortalGuiaBGR, Api Portal

**Arquitectura AWS:**
```
Internet → Route 53 → CloudFront → WAF → ALB → 
EC2 Auto Scaling (Multi-AZ) → RDS Multi-AZ → S3
```

**Componentes clave:**
- Application Load Balancer (ALB)
- EC2 Auto Scaling Group (2-6 instancias)
- RDS Multi-AZ (SQL Server o PostgreSQL)
- CloudFront para CDN
- WAF para seguridad
- S3 para assets estáticos

**Estimación por portal**: $2,500 - $3,500/mes

### Tipo 2: Aplicaciones Backoffice (2 aplicaciones)
**Aplicaciones**: Backoffice Banca Digital, Backoffice Sistemas

**Arquitectura AWS:**
```
VPN/Direct Connect → ALB → EC2 (Multi-AZ) → 
RDS Multi-AZ → EFS (file sharing)
```

**Componentes clave:**
- Application Load Balancer (interno)
- EC2 instances (2-4)
- RDS Multi-AZ
- EFS para archivos compartidos
- VPC Endpoints

**Estimación por app**: $1,500 - $2,000/mes

### Tipo 3: Herramientas DevOps (1 aplicación)
**Aplicación**: Sonar Qube

**Arquitectura AWS:**
```
ALB → EC2 Auto Scaling → RDS PostgreSQL Multi-AZ
```

**Componentes clave:**
- ALB
- EC2 t3.xlarge (2 instancias)
- RDS PostgreSQL
- EBS gp3

**Estimación**: $1,200/mes

### Tipo 4: Logging (1 aplicación)
**Aplicación**: Seq

**Opción A - Rehost:**
```
NLB → EC2 → EBS (1TB)
```
**Estimación**: $800/mes

**Opción B - Refactor (Recomendado):**
```
CloudWatch Logs → CloudWatch Insights → S3 (long-term)
```
**Estimación**: $300/mes (ahorro 60%)

### Tipo 5: Aplicación Simple (1 aplicación)
**Aplicación**: Saras

**Arquitectura AWS:**
```
EC2 (2 instancias) → RDS SQL Server
```

**Componentes clave:**
- EC2 t3.large (2)
- RDS SQL Server t3.medium
- EBS gp3

**Estimación**: $600/mes

---

## 📋 Matriz de Dependencias

### Dependencias Identificadas

| Aplicación | Depende de | Tipo Dependencia |
|------------|------------|------------------|
| PortalAdmBGR | Active Directory | Autenticación |
| PortalGuiaBGR | Api Portal | Integración API |
| Api Portal | Backoffice Sistemas | Datos |
| Backoffice Banca Digital | Core Banking | Integración |
| Sonar Qube | Jenkins/GitLab | CI/CD |
| Seq | Todas las apps | Logs |

**Nota**: Requiere discovery más profundo para mapeo completo

---

## 🎯 Estrategia de Migración por Olas

### Ola 0 - Piloto (Semana 1-6)
**Objetivo**: Validar proceso de migración

- ✅ **Sonar Qube** (5 VMs, 42 vCPUs, 144 GB)
- ✅ **Saras** (2 VMs, 12 vCPUs, 18 GB)
- ✅ **Seq** (5 VMs, 42 vCPUs, 144 GB)

**Total Ola 0**: 12 VMs, 96 vCPUs, 306 GB RAM  
**Riesgo**: Bajo  
**Impacto negocio**: Mínimo

### Ola 1 - Backoffice (Semana 7-12)
**Objetivo**: Migrar aplicaciones internas

- **Backoffice Sistemas** (5 VMs, 42 vCPUs, 144 GB)
- **Backoffice Banca Digital** (3 VMs, 10 vCPUs, 20 GB)

**Total Ola 1**: 8 VMs, 52 vCPUs, 164 GB RAM  
**Riesgo**: Medio  
**Impacto negocio**: Bajo-Medio

### Ola 2 - Portales (Semana 13-20)
**Objetivo**: Migrar aplicaciones de cara al cliente

- **Api Portal** (5 VMs, 42 vCPUs, 144 GB)
- **PortalGuiaBGR** (5 VMs, 42 vCPUs, 144 GB)

**Total Ola 2**: 10 VMs, 84 vCPUs, 288 GB RAM  
**Riesgo**: Alto  
**Impacto negocio**: Alto

### Ola 3 - Portal Crítico (Semana 21-26)
**Objetivo**: Migrar portal administrativo principal

- **PortalAdmBGR** (6 VMs, 48 vCPUs, 156 GB)

**Total Ola 3**: 6 VMs, 48 vCPUs, 156 GB RAM  
**Riesgo**: Alto  
**Impacto negocio**: Crítico

---

## 💰 Estimación de Costos Total

### Por Aplicación (Mensual)

| Aplicación | Estimación Mensual | Anual |
|------------|-------------------|-------|
| PortalAdmBGR | $3,000 | $36,000 |
| PortalGuiaBGR | $2,800 | $33,600 |
| Api Portal | $2,800 | $33,600 |
| Backoffice Banca Digital | $1,500 | $18,000 |
| Backoffice Sistemas | $2,000 | $24,000 |
| Sonar Qube | $1,200 | $14,400 |
| Seq (CloudWatch) | $300 | $3,600 |
| Saras | $600 | $7,200 |
| **TOTAL** | **$14,200** | **$170,400** |

### Con Optimización (Reserved Instances, Savings Plans)

- **Ahorro estimado**: 30-40%
- **Costo optimizado**: $9,900 - $10,500/mes
- **Anual optimizado**: $119,000 - $126,000

---

## 🔍 Hallazgos Clave

### Positivos ✅

1. **Arquitecturas estándar**: Mayoría son apps web tradicionales (fácil migración)
2. **Pocas dependencias complejas**: No se identificaron integraciones muy complejas
3. **Buena distribución**: 50% alta criticidad, 50% media (permite piloto seguro)
4. **Oportunidad de modernización**: Seq puede migrar a CloudWatch (60% ahorro)

### Desafíos ⚠️

1. **Stack desconocido**: No se pudo identificar tecnologías específicas en HTMLs
2. **Dependencias no mapeadas**: Requiere discovery más profundo
3. **Bases de datos**: No se identificaron tipos específicos de BD
4. **Integraciones**: Falta mapear integraciones entre aplicaciones

### Riesgos 🚨

1. **Portales críticos**: 3 portales de alta criticidad requieren planificación cuidadosa
2. **Backoffice Banca**: Posible integración con core banking (complejidad alta)
3. **Active Directory**: Dependencia de AD para autenticación (requiere híbrido)
4. **Datos sensibles**: Aplicaciones bancarias requieren compliance estricto

---

## 📋 Acciones Requeridas

### Inmediatas (Esta semana)

- [ ] Validar stack tecnológico de cada aplicación
- [ ] Identificar tipos de bases de datos
- [ ] Mapear dependencias entre aplicaciones
- [ ] Documentar integraciones con sistemas externos
- [ ] Identificar owners de cada aplicación

### Corto Plazo (Próximas 2 semanas)

- [ ] Realizar discovery técnico detallado
- [ ] Documentar configuraciones actuales
- [ ] Identificar datos sensibles y requisitos compliance
- [ ] Definir ventanas de mantenimiento
- [ ] Preparar plan de comunicación

### Medio Plazo (Próximo mes)

- [ ] Aprobar plan de Ola 0 (piloto)
- [ ] Provisionar infraestructura AWS base
- [ ] Capacitar equipo en AWS
- [ ] Iniciar migración de Ola 0

---

## 📊 Cobertura del Análisis

**VMs Mapeadas**: 36 de 383 (9.4%)  
**vCPUs Mapeados**: 280 de 1,752 (16%)  
**RAM Mapeada**: 914 GB de 5,925 GB (15.4%)

**Nota**: Quedan 347 VMs (90.6%) por mapear a aplicaciones específicas. Se requiere:
1. Análisis de nombres de VMs
2. Entrevistas con equipos técnicos
3. Análisis de tráfico de red
4. Documentación de arquitecturas actuales

---

## 🎯 Recomendaciones

### Prioridad Alta

1. **Completar discovery técnico** de las 8 aplicaciones identificadas
2. **Iniciar Ola 0** con Sonar Qube, Saras y Seq (bajo riesgo)
3. **Mapear VMs restantes** a aplicaciones o identificar huérfanas
4. **Documentar dependencias** críticas antes de migración

### Prioridad Media

5. **Evaluar modernización** de Seq a CloudWatch (ahorro 60%)
6. **Planificar conectividad híbrida** (Direct Connect)
7. **Definir estrategia de datos** (migración, sincronización)
8. **Preparar equipo** con capacitación AWS

### Prioridad Baja

9. **Evaluar containerización** de aplicaciones modernas
10. **Considerar serverless** para APIs y microservicios

---

**Archivos Relacionados:**
- `02_mapa_aplicaciones.json` - Datos completos en JSON
- `docs/APP_*.md` - Documentación detallada por aplicación (8 archivos)
- `03_PRIMERA_OLA_MIGRACION.md` - Plan detallado de Ola 0

**Última actualización**: 2025-12-01  
**Estado**: Completado
