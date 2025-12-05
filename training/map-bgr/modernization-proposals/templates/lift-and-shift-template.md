# [NOMBRE_APLICACION] - Lift & Shift a AWS
## Template de Migración Rápida

**Fecha**: [FECHA]  
**Aplicación**: [NOMBRE]  
**Estrategia**: Lift & Shift (Rehost)  
**Timeline**: [X] semanas

---

## 🎯 Información de la Aplicación

### Situación Actual
- **VMs**: [NUMERO]
- **vCPUs**: [TOTAL]
- **RAM**: [TOTAL] GB
- **OS**: [SISTEMA_OPERATIVO]
- **Stack**: [TECNOLOGIAS]
- **Base de Datos**: [TIPO_BD]
- **Criticidad**: [BAJA/MEDIA/ALTA]

### Recursos Actuales
| VM | vCPUs | RAM (GB) | OS | Estado |
|-------|-------|----------|-----|--------|
| [VM1] | [X] | [X] | [OS] | poweredOn |
| [VM2] | [X] | [X] | [OS] | poweredOn |

---

## 🏗️ Arquitectura AWS Propuesta

### Componentes

#### Compute
- **EC2 Instances**: [TIPO] ([X] vCPU, [X]GB RAM)
- **Cantidad**: [X] instancias
- **OS**: [SISTEMA_OPERATIVO]

#### Database
- **Opción 1**: RDS [TIPO_BD]
- **Opción 2**: Mantener on-premise (VPN)
- **Recomendación**: [OPCION_RECOMENDADA]

#### Networking
- **VPC**: [CIDR]
- **Subnets**: Public y Private
- **Load Balancer**: ALB o NLB
- **Conectividad**: [VPN/Direct Connect/Internet]

#### Storage
- **EBS**: [X]GB gp3
- **S3**: Backups
- **EFS**: [SI/NO] - [USO]

#### Monitoring
- **CloudWatch**: Logs y métricas
- **SNS**: Alertas
- **Systems Manager**: Gestión

---

## 🚀 Plan de Migración

### Semana 1: Preparación e Infraestructura

#### Día 1-2: Setup AWS
- [ ] Crear VPC y subnets
- [ ] Configurar Security Groups
- [ ] Crear Internet Gateway / NAT Gateway
- [ ] Configurar Route Tables

#### Día 3-4: Preparar Compute
- [ ] Lanzar EC2 instances
- [ ] Instalar software base
- [ ] Configurar aplicación
- [ ] Testing inicial

#### Día 5: Configurar Networking
- [ ] Crear Load Balancer
- [ ] Configurar Target Groups
- [ ] Configurar Health Checks
- [ ] Testing de conectividad

**Entregables Semana 1**:
- ✅ Infraestructura AWS lista
- ✅ Aplicación instalada
- ✅ Networking configurado

---

### Semana 2: Migración y Testing

#### Día 1-2: Migración de Datos
- [ ] Backup de datos actuales
- [ ] Migración de base de datos (si aplica)
- [ ] Validación de integridad
- [ ] Testing de conectividad

#### Día 3: Configuración Final
- [ ] Configurar Auto Scaling (si aplica)
- [ ] Configurar CloudWatch Alarms
- [ ] Configurar backups automáticos
- [ ] Documentar configuración

#### Día 4: Testing
- [ ] Testing funcional completo
- [ ] Testing de performance
- [ ] Testing de carga
- [ ] Validación de usuarios

#### Día 5: Preparación Go-Live
- [ ] Plan de cutover documentado
- [ ] Plan de rollback listo
- [ ] Comunicación a stakeholders
- [ ] Equipo en standby

**Entregables Semana 2**:
- ✅ Aplicación migrada
- ✅ Testing completo
- ✅ Listo para producción

---

### Semana 3: Go-Live y Estabilización

#### Día 1: Cutover
- [ ] Actualizar DNS
- [ ] Monitoreo intensivo
- [ ] Validación de tráfico
- [ ] Testing con usuarios

#### Día 2-3: Monitoreo Post-Deploy
- [ ] Monitoreo 24/7
- [ ] Validación de métricas
- [ ] Ajustes de performance
- [ ] Recolección de feedback

#### Día 4-5: Documentación y Handover
- [ ] Runbook de operaciones
- [ ] Documentación de arquitectura
- [ ] Training a equipo
- [ ] Retrospectiva

**Entregables Semana 3**:
- ✅ Aplicación en producción
- ✅ Documentación completa
- ✅ Equipo capacitado

---

## 💰 Estimación de Costos

### Compute
| Componente | Especificación | Cantidad | Costo/hora | Horas/mes | Subtotal |
|------------|----------------|----------|------------|-----------|----------|
| EC2 | [TIPO] | [X] | $[X] | 730 | $[X] |
| **Total Compute** | | | | | **$[X]** |

### Database
| Componente | Especificación | Costo/mes |
|------------|----------------|-----------|
| RDS [TIPO] | [INSTANCE_TYPE] | $[X] |
| Storage | [X]GB | $[X] |
| **Total Database** | | **$[X]** |

### Networking
| Componente | Costo/mes |
|------------|-----------|
| Load Balancer | $23 |
| NAT Gateway | $33 |
| Data Transfer | $[X] |
| VPN (si aplica) | $36 |
| **Total Networking** | **$[X]** |

### Storage
| Componente | Costo/mes |
|------------|-----------|
| EBS | $[X] |
| S3 | $[X] |
| EFS (si aplica) | $[X] |
| **Total Storage** | **$[X]** |

### Monitoring
| Componente | Costo/mes |
|------------|-----------|
| CloudWatch | $3 |
| SNS | $0.50 |
| **Total Monitoring** | **$3.50** |

### TOTAL MENSUAL

| Categoría | Costo |
|-----------|-------|
| Compute | $[X] |
| Database | $[X] |
| Networking | $[X] |
| Storage | $[X] |
| Monitoring | $[X] |
| **Subtotal** | **$[X]** |
| Contingencia (10%) | $[X] |
| **TOTAL** | **$[X]/mes** |

---

## 🔧 Configuración Detallada

### VPC Configuration
```
VPC CIDR: [X.X.X.X/16]
Public Subnet A: [X.X.1.0/24]
Public Subnet B: [X.X.2.0/24]
Private Subnet A: [X.X.10.0/24]
Private Subnet B: [X.X.11.0/24]
```

### Security Groups

#### Load Balancer SG
```yaml
Inbound:
  - Port 443: 0.0.0.0/0
  - Port 80: 0.0.0.0/0

Outbound:
  - Port [APP_PORT]: EC2 SG
```

#### EC2 Security Group
```yaml
Inbound:
  - Port [APP_PORT]: ALB SG
  - Port 22/3389: [MANAGEMENT_CIDR]

Outbound:
  - Port 443: 0.0.0.0/0
  - Port [DB_PORT]: RDS SG (si aplica)
```

### CloudWatch Alarms
```yaml
Critical:
  - EC2 CPU > 80% por 5 min
  - ALB 5xx errors > 10
  - Unhealthy targets > 0

Warning:
  - EC2 CPU > 60% por 10 min
  - ALB latency > 2s
```

---

## 📋 Checklist de Migración

### Pre-Migración
- [ ] Auditoría de aplicación actual
- [ ] Documentar dependencias
- [ ] Backup completo
- [ ] Plan de rollback documentado
- [ ] Comunicación a stakeholders

### Infraestructura AWS
- [ ] VPC creado
- [ ] Subnets configuradas
- [ ] Security Groups creados
- [ ] Load Balancer configurado
- [ ] EC2 instances lanzadas
- [ ] Database provisionada (si aplica)

### Aplicación
- [ ] Software instalado
- [ ] Aplicación configurada
- [ ] Datos migrados
- [ ] Testing funcional completo
- [ ] Performance validado

### Go-Live
- [ ] DNS actualizado
- [ ] Monitoreo activo
- [ ] Usuarios validando
- [ ] Documentación completa
- [ ] Training completado

---

## ⚠️ Riesgos y Mitigaciones

### Riesgo 1: [DESCRIPCION]
**Probabilidad**: [BAJA/MEDIA/ALTA]  
**Impacto**: [BAJO/MEDIO/ALTO]  
**Mitigación**:
- [ACCION_1]
- [ACCION_2]
- [ACCION_3]

### Riesgo 2: [DESCRIPCION]
**Probabilidad**: [BAJA/MEDIA/ALTA]  
**Impacto**: [BAJO/MEDIO/ALTO]  
**Mitigación**:
- [ACCION_1]
- [ACCION_2]

---

## ✅ Criterios de Éxito

1. ✅ **Aplicación funcionando** en AWS
2. ✅ **Performance** igual o mejor
3. ✅ **Costo** dentro del presupuesto
4. ✅ **Disponibilidad** >[X]%
5. ✅ **Zero data loss** durante migración
6. ✅ **Usuarios satisfechos**
7. ✅ **Documentación completa**

---

## 🎯 Próximos Pasos

1. [ ] Aprobar plan de migración
2. [ ] Asignar equipo técnico
3. [ ] Crear ambiente AWS
4. [ ] Iniciar implementación

---

**Última actualización**: [FECHA]  
**Versión**: 1.0  
**Estado**: [DRAFT/REVIEW/APPROVED]
