# Librarian - Plan de Modernización
## Control de Versiones y Seguimiento de Despliegues

**Fecha**: 2026-01-06  
**Aplicación**: Librarian  
**Estrategia Recomendada**: Repurchase (Reemplazo por AWS CodePipeline)  
**Timeline**: 3 semanas

---

## 🎯 Información de la Aplicación

### Descripción
Herramienta de control de versiones y seguimiento de despliegues en ambientes de test y producción. Sistema legacy crítico para el proceso de desarrollo del banco.

### Situación Actual (On-Premise)

| Atributo | Valor |
|----------|-------|
| **Servidores** | ECBRPRW29, ECBRPRW31 |
| **vCPUs Totales** | 4 (2 + 2) |
| **RAM Total** | 7.7 GB (4 + 3.7) |
| **Storage** | ~200 GB |
| **OS** | Windows Server 2003 ⚠️ **OBSOLETO** |
| **Framework** | .NET Framework 1.1 ⚠️ **OBSOLETO** |
| **Base de Datos** | No aplica |
| **Usuarios** | 7 (equipo de desarrollo) |
| **Criticidad** | Media |

### ⚠️ Alertas de Obsolescencia

1. **Windows Server 2003**: Sin soporte desde 2015 (10+ años sin parches de seguridad)
2. **.NET Framework 1.1**: Sin soporte desde 2013 (12+ años obsoleto)
3. **Riesgo de Seguridad**: CRÍTICO - Sistema expuesto a vulnerabilidades conocidas

### Stack Tecnológico Actual

- **Frontend**: ASP.NET Web Forms (.NET 1.1)
- **Backend**: C# .NET Framework 1.1
- **Database**: No aplica (archivos en filesystem)
- **Autenticación**: Active Directory

---

## 🏗️ Opciones de Arquitectura

### Opción 1: Reemplazo por AWS CodePipeline (RECOMENDADA)

![Arquitectura CodePipeline](./diagrams/generated-diagrams/librarian_codepipeline.png)

#### Descripción
Reemplazo completo de Librarian por servicios nativos de AWS para CI/CD. Elimina deuda técnica y moderniza completamente el proceso de despliegues.

#### Componentes
| Servicio | Configuración | Costo/mes |
|----------|---------------|-----------|
| AWS CodeCommit | Repositorio Git ilimitado | $1.00 |
| AWS CodeBuild | 100 min build/mes | $5.00 |
| AWS CodePipeline | 1 pipeline activo | $1.00 |
| AWS CodeDeploy | Despliegues ilimitados | $0.00 |
| Amazon S3 | Artifacts storage | $2.00 |
| CloudWatch | Logs y métricas | $3.00 |
| **TOTAL** | | **$12/mes** |

#### Ventajas
- ✅ Elimina 100% de deuda técnica
- ✅ Servicios managed sin mantenimiento
- ✅ Integración nativa con AWS
- ✅ Escalabilidad ilimitada
- ✅ Seguridad enterprise (IAM, KMS)
- ✅ Costo mínimo ($12/mes)

#### Desventajas
- ❌ Requiere migración de procesos
- ❌ Curva de aprendizaje para equipo
- ❌ Cambio de paradigma (Git vs legacy)

#### 💡 Tips y Recomendaciones IA

**Cuándo elegir esta opción:**
- Equipos que buscan modernizar completamente su proceso de CI/CD
- Organizaciones con estrategia cloud-first
- Cuando se requiere eliminar deuda técnica legacy

**Consideraciones importantes:**
- Requiere migrar histórico de versiones a Git
- Equipo necesita capacitación en Git y CodePipeline
- Integración con Azure DevOps existente es posible

**Recomendaciones de implementación:**
- Empezar con proyecto piloto pequeño
- Documentar procesos actuales antes de migrar
- Configurar branch protection rules

**Ideal para:**
- Equipos DevOps modernos
- Organizaciones que buscan automatización completa

#### 📋 Esfuerzo Escala24x7

| Tarea | Horas | Equipo |
|-------|-------|--------|
| CodeCommit repos | 4 | DevOps |
| CodePipeline | 8 | DevOps |
| CodeBuild projects | 8 | DevOps |
| CodeDeploy | 4 | DevOps |
| S3 Bucket (artifacts) | 2 | Infra |
| DynamoDB Table | 2 | Infra |
| Lambda Functions | 16 | Infra |
| SNS Topics | 4 | Infra |
| CloudWatch Dashboard | 8 | Infra |
| Migración datos | 16 | DevOps |
| Testing y validación | 16 | QA |
| Knowledge transfer | 8 | DevOps |
| **TOTAL** | **96** | |

**Costo implementación**: 96 horas × $150/hora = **$14,400 USD**
- Proyectos con múltiples ambientes (dev/test/prod)

---

### Opción 2: EC2 Lift & Shift Modernizado

![Arquitectura EC2](./diagrams/generated-diagrams/librarian_ec2_modern.png)

#### Descripción
Migración a EC2 con actualización de OS y framework. Mantiene funcionalidad existente pero elimina obsolescencia crítica.

#### Componentes
| Servicio | Configuración | Costo/mes |
|----------|---------------|-----------|
| EC2 t3.small | 2 vCPU, 2 GB RAM - Windows 2019 | $30.66 |
| Application Load Balancer | HTTPS | $22.50 |
| EBS gp3 | 100 GB | $8.00 |
| Amazon S3 | Backups | $2.00 |
| CloudWatch | Logs | $5.00 |
| **TOTAL** | | **$68.16/mes** |

#### Ventajas
- ✅ Migración más simple
- ✅ Mantiene funcionalidad existente
- ✅ Elimina OS obsoleto
- ✅ Menor riesgo de cambio

#### Desventajas
- ❌ Requiere refactoring a .NET 4.8+
- ❌ Mantiene arquitectura legacy
- ❌ Mayor costo que CodePipeline
- ❌ Requiere mantenimiento de servidor

#### 💡 Tips y Recomendaciones IA

**Cuándo elegir esta opción:**
- Migración urgente por riesgo de seguridad
- Equipo sin experiencia en CI/CD moderno
- Cuando se requiere mantener funcionalidad exacta

**Consideraciones importantes:**
- .NET 1.1 NO es compatible con Windows 2019
- Requiere refactoring mínimo a .NET 4.8
- Evaluar esfuerzo de actualización de código

**Recomendaciones de implementación:**
- Usar AWS Application Migration Service (MGN)
- Actualizar .NET Framework antes de migrar
- Configurar backups automáticos en S3

**Ideal para:**
- Migraciones con timeline agresivo
- Equipos que prefieren cambios incrementales

#### 📋 Esfuerzo Escala24x7

| Tarea | Horas | Equipo |
|-------|-------|--------|
| VPC/Redes | 4 | Infra |
| EC2 Instance | 2 | Infra |
| RDS SQL Server | 2 | Infra |
| EBS Storage | 2 | Infra |
| S3 Bucket | 2 | Infra |
| MGN Configuration | 2 | Infra |
| MGN Instance | 1 | Infra |
| MGN Tests | 1 | Infra |
| CloudWatch Logs | 4 | Infra |
| Testing y validación | 8 | QA |
| Knowledge transfer | 4 | Infra |
| **TOTAL** | **32** | |

**Costo implementación**: 32 horas × $150/hora = **$4,800 USD**
- Organizaciones con restricciones de capacitación

---

### Opción 3: Serverless con S3 + Lambda

![Arquitectura Serverless](./diagrams/generated-diagrams/librarian_serverless.png)

#### Descripción
Arquitectura completamente serverless usando Lambda para lógica y S3/DynamoDB para almacenamiento. Máxima modernización con pago por uso.

#### Componentes
| Servicio | Configuración | Costo/mes |
|----------|---------------|-----------|
| API Gateway | REST API | $3.50 |
| AWS Lambda | 2 funciones, 256 MB | $2.00 |
| Amazon S3 | Artifacts versionados | $2.00 |
| DynamoDB | Historial de despliegues | $5.00 |
| Amazon SNS | Notificaciones | $1.00 |
| CloudWatch | Logs | $3.00 |
| **TOTAL** | | **$16.50/mes** |

#### Ventajas
- ✅ Zero server management
- ✅ Pago por uso real
- ✅ Escalabilidad automática
- ✅ Alta disponibilidad nativa

#### Desventajas
- ❌ Requiere desarrollo desde cero
- ❌ Mayor esfuerzo de implementación
- ❌ Cambio completo de arquitectura

#### 💡 Tips y Recomendaciones IA

**Cuándo elegir esta opción:**
- Equipos con experiencia en serverless
- Cuando se busca máxima modernización
- Proyectos con presupuesto para desarrollo

**Consideraciones importantes:**
- Requiere desarrollo completo de nueva aplicación
- Evaluar si funcionalidad justifica el esfuerzo
- Considerar si CodePipeline cubre los requisitos

**Recomendaciones de implementación:**
- Usar SAM o CDK para infraestructura
- Implementar API REST bien documentada
- Configurar versionado en S3

**Ideal para:**
- Organizaciones con estrategia serverless-first
- Equipos que buscan eliminar toda infraestructura

#### 📋 Esfuerzo Escala24x7

| Tarea | Horas | Equipo |
|-------|-------|--------|
| API Gateway | 8 | Infra |
| Lambda Functions | 24 | Infra |
| DynamoDB Tables | 4 | Infra |
| S3 Bucket | 2 | Infra |
| SNS Topics | 4 | Infra |
| Desarrollo Lambdas | 32 | Delivery |
| Application pipeline (SAM) | 4 | Delivery |
| CloudWatch Dashboard | 8 | Infra |
| Testing y validación | 16 | QA |
| Knowledge transfer | 8 | Infra |
| **TOTAL** | **110** | |

**Costo implementación**: 110 horas × $150/hora = **$16,500 USD**
- Proyectos con requisitos personalizados

---

## 📊 Comparativa de Opciones

| Criterio | CodePipeline | EC2 Modernizado | Serverless |
|----------|--------------|-----------------|------------|
| **Costo/mes** | $12 | $68.16 | $16.50 |
| **Ahorro vs actual** | 98% | 86% | 97% |
| **Complejidad** | Media | Baja | Alta |
| **Mantenimiento** | Ninguno | Medio | Bajo |
| **Timeline** | 3 semanas | 2 semanas | 6 semanas |
| **Riesgo** | Bajo | Medio | Medio |
| **Modernización** | Total | Parcial | Total |
| **Recomendado** | ✅ Sí | Solo si urgente | Para custom |

---

## 💰 Estimación de Costos Actual

### Costo On-Premise Estimado
| Componente | Costo/mes |
|------------|-----------|
| 2 VMs Windows Server | $300 |
| Licencias Windows | $100 |
| Mantenimiento/Soporte | $100 |
| **TOTAL ESTIMADO** | **$500/mes** |

### Comparativa de Ahorro
| Opción | Costo AWS | Ahorro Mensual | Ahorro Anual |
|--------|-----------|----------------|--------------|
| CodePipeline | $12 | $488 (98%) | $5,856 |
| EC2 Modernizado | $68 | $432 (86%) | $5,184 |
| Serverless | $16.50 | $483 (97%) | $5,802 |

---

## 🚀 Plan de Implementación (Opción Recomendada)

### Semana 1: Preparación
- [ ] Documentar procesos actuales de Librarian
- [ ] Inventariar proyectos y versiones existentes
- [ ] Configurar AWS CodeCommit
- [ ] Capacitar equipo en Git básico

### Semana 2: Migración
- [ ] Migrar repositorios a CodeCommit
- [ ] Configurar CodePipeline para proyecto piloto
- [ ] Configurar CodeBuild con buildspec.yml
- [ ] Configurar CodeDeploy para ambientes

### Semana 3: Validación y Go-Live
- [ ] Testing de pipeline completo
- [ ] Migrar proyectos restantes
- [ ] Documentación de nuevos procesos
- [ ] Decomisionar servidores legacy

---

## ⚠️ Riesgos y Mitigaciones

### Riesgo 1: Pérdida de Histórico
**Probabilidad**: Media  
**Impacto**: Medio  
**Mitigación**: Exportar y documentar histórico antes de migrar

### Riesgo 2: Resistencia al Cambio
**Probabilidad**: Alta  
**Impacto**: Medio  
**Mitigación**: Capacitación y acompañamiento al equipo

### Riesgo 3: Incompatibilidad de Procesos
**Probabilidad**: Baja  
**Impacto**: Alto  
**Mitigación**: Mapear procesos actuales a CodePipeline

---

## ✅ Recomendación Final

**AWS CodePipeline** es la opción recomendada por:

1. **Elimina 100% de deuda técnica** - No más Windows 2003 ni .NET 1.1
2. **Costo mínimo** - $12/mes vs $500/mes actual (98% ahorro)
3. **Zero mantenimiento** - Servicios fully managed
4. **Modernización completa** - CI/CD enterprise-grade
5. **Seguridad** - Cumple estándares bancarios (IAM, KMS, CloudTrail)

---

**Última actualización**: 2026-01-06  
**Versión**: 1.0  
**Estado**: Listo para implementación
