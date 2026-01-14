# Garantías/SISGAR - Plan de Modernización
## Sistema de Gestión de Garantías

**Fecha**: 2026-01-07  
**Aplicación**: Garantías/SISGAR  
**Estrategia Recomendada**: Retain (Iniciativa Riesgo 2027)  
**Timeline**: 4 semanas (migración básica)

---

## 🎯 Información de la Aplicación

### Descripción
Sistema de gestión de garantías crediticias. Parte de la iniciativa estratégica **Riesgo 2027** que contempla modernización integral del área de riesgos.

### Situación Actual

| Atributo | Valor |
|----------|-------|
| **Servidor** | sisgar-srv |
| **IP** | 172.20.1.60 |
| **vCPUs** | 4 |
| **RAM** | 16 GB |
| **Storage** | 200 GB |
| **OS** | Windows Server 2016 |
| **Criticidad** | Alta |
| **Usuarios** | ~100 |

### Stack Tecnológico
- **Frontend**: ASP.NET Web Forms
- **Backend**: .NET Framework 4.5
- **Database**: SQL Server 2016
- **Área**: Riesgo Crediticio

### ⚠️ Hallazgos Clave
- **Iniciativa Riesgo 2027**: Sistema incluido en roadmap estratégico
- **Dependencia de área Riesgos**: Decisiones de modernización centralizadas
- **SQL Server 2016**: Versión con soporte hasta 2026
- **Criticidad alta**: Gestión de garantías es proceso crítico
- **Recomendación**: Retain hasta definición de Riesgo 2027

---

## 🏗️ Opciones de Arquitectura

### Opción 1: Retain - Iniciativa Riesgo 2027 (RECOMENDADA)

![Arquitectura EC2 Retain](./diagrams/generated-diagrams/garantias_ec2.png)

| Servicio | Configuración | Costo/mes |
|----------|---------------|-----------|
| EC2 m5.large | Windows Server | $150 |
| RDS SQL Server Standard | db.m5.large | $500 |
| EBS gp3 | 200 GB | $20 |
| CloudWatch | Logs y métricas | $10 |
| AWS Backup | Diario | $20 |
| **TOTAL** | | **$800/mes** |

**Ahorro**: 20% vs costo actual ($1,000/mes)

#### 💡 Tips y Recomendaciones IA

**Cuándo elegir:**
- Iniciativa Riesgo 2027 confirmada
- Sin recursos para modernización paralela
- Evitar duplicación de esfuerzo
- Alineamiento estratégico requerido

**Consideraciones:**
- Coordinar con equipo Riesgo 2027
- Documentar requerimientos actuales
- Participar en definición de nuevo sistema
- Mantener sistema estable hasta migración

**Recomendaciones:**
- Migrar a AWS como Lift & Shift
- Usar Reserved Instances para ahorro
- Documentar integraciones
- Preparar datos para migración futura

**Ideal para:**
- Aplicaciones con iniciativas planificadas
- Evitar inversión que será reemplazada
- Alineamiento con estrategia corporativa

#### 📋 Esfuerzo Escala24x7

| Tarea | Horas | Equipo |
|-------|-------|--------|
| VPC/Redes | 4 | Infra |
| EC2 Instance | 2 | Infra |
| RDS SQL Server | 2 | Infra |
| EBS Storage | 2 | Infra |
| MGN Configuration | 2 | Infra |
| MGN Instance | 1 | Infra |
| MGN Tests | 1 | Infra |
| AWS Backup Configuration | 4 | Infra |
| CloudWatch Dashboard | 8 | Infra |
| Testing y validación | 8 | QA |
| Knowledge transfer | 6 | Infra |
| **TOTAL** | **40** | |

**Costo implementación**: 40 horas × $150/hora = **$6,000 USD**

---

### Opción 2: ECS + Aurora (Modernización Independiente)

![Arquitectura ECS Aurora](./diagrams/generated-diagrams/garantias_ecs.png)

| Servicio | Configuración | Costo/mes |
|----------|---------------|-----------|
| ECS Fargate | .NET Core (2 tasks) | $150 |
| Aurora PostgreSQL | db.r5.large | $180 |
| Application Load Balancer | HTTPS | $25 |
| CloudWatch | Logs y métricas | $15 |
| **TOTAL** | | **$400/mes** |

**Ahorro**: 60% vs costo actual

#### 💡 Tips y Recomendaciones IA

**Cuándo elegir:**
- Iniciativa Riesgo 2027 cancelada
- Modernización urgente requerida
- Recursos disponibles para desarrollo

**Consideraciones:**
- Puede duplicar esfuerzo con Riesgo 2027
- Requiere refactorización a .NET Core
- Migración SQL Server → PostgreSQL
- Validar con área de Riesgos

**Recomendaciones:**
- Solo si Riesgo 2027 no procede
- Coordinar con stakeholders
- Evaluar ROI vs esperar iniciativa

**Ideal para:**
- Modernización independiente
- Si iniciativa 2027 se cancela

#### 📋 Esfuerzo Escala24x7

| Tarea | Horas | Equipo |
|-------|-------|--------|
| VPC/Redes | 4 | Infra |
| Fargate Cluster | 2 | Infra |
| Fargate Service (2 tasks) | 8 | Infra |
| ALB | 2 | Infra |
| Aurora PostgreSQL | 2 | Infra |
| DMS replication instance | 4 | Data |
| DMS replication task | 4 | Data |
| Application pipeline (ECS) | 4 | Infra |
| Desarrollo .NET Core | 80 | Delivery |
| CloudWatch Dashboard | 8 | Infra |
| Testing y validación | 32 | QA |
| Knowledge transfer | 10 | Infra |
| **TOTAL** | **160** | |

**Costo implementación**: 160 horas × $150/hora = **$24,000 USD**

---

## 📊 Comparativa

| Criterio | Retain (Riesgo 2027) | ECS + Aurora |
|----------|----------------------|--------------|
| **Costo/mes** | $800 | $400 |
| **Ahorro** | 20% | 60% |
| **Inversión inicial** | $6,000 | $24,000 |
| **Timeline** | 4 semanas | 10 semanas |
| **Riesgo duplicación** | ❌ No | ✅ Sí |
| **Alineado estrategia** | ✅ Sí | ❌ No |

---

## 🔄 Plan de Migración Retain

### Fase 1: Preparación (Semana 1)
- Documentar configuración actual
- Identificar integraciones
- Planificar ventana de migración
- Preparar ambiente AWS

### Fase 2: Migración (Semanas 2-3)
- Crear EC2 Windows Server
- Configurar RDS SQL Server
- Migrar aplicación
- Migrar base de datos

### Fase 3: Validación (Semana 4)
- Testing funcional
- Validar integraciones
- Configurar backups
- Go-live

---

## 🔗 Dependencias con Riesgo 2027

| Aspecto | Consideración |
|---------|---------------|
| **Timeline** | Esperar definición Q2 2027 |
| **Alcance** | Garantías incluido en scope |
| **Datos** | Preparar para migración |
| **Integraciones** | Documentar para nuevo sistema |
| **Usuarios** | Participar en requerimientos |

---

## ✅ Recomendación Final

**Retain - Iniciativa Riesgo 2027** por:
1. **Alineamiento estratégico** - sistema incluido en roadmap
2. **Evitar duplicación** - no invertir en lo que será reemplazado
3. **Migración básica** - solo Lift & Shift a AWS
4. **Bajo riesgo** - mantener estabilidad actual
5. **Participación en Riesgo 2027** - influir en nuevo sistema

**Acción inmediata**: Coordinar con equipo Riesgo 2027 para:
- Confirmar inclusión de Garantías/SISGAR
- Participar en definición de requerimientos
- Documentar funcionalidad actual
- Preparar datos para migración

---

**Última actualización**: 2026-01-07
