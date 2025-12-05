# Backoffice Sistemas BGR - Lift & Shift a AWS
## Migración Rápida con Conectividad Híbrida

**Fecha**: 2025-12-04  
**Aplicación**: Backoffice Sistemas BGR  
**Estrategia**: Lift & Shift (Rehost)  
**Base de Datos**: Mantener On-Premise (Híbrido)  
**Timeline**: 2-3 semanas

---

## 🎯 Estrategia de Migración

### Lift & Shift (Rehost)
- ✅ **Sin cambios de código**: Aplicación migra tal cual
- ✅ **Sin refactorización**: .NET Framework sin modificar
- ✅ **Migración rápida**: 2-3 semanas vs 3-6 meses modernización
- ✅ **Menor riesgo**: Cambios mínimos
- ✅ **Quick wins**: Beneficios inmediatos de AWS

### Base de Datos On-Premise
- ✅ **Mantener SQL Server on-premise**: Sin migración de datos
- ✅ **Conectividad híbrida**: Site-to-Site VPN
- ✅ **Sin downtime de BD**: Base de datos sigue operando
- ✅ **Migración futura**: Planificada para Fase 2

---

## 🏗️ Arquitectura Híbrida

![Arquitectura Híbrida](./generated-diagrams/backoffice_sistemas_hybrid.png)

### Componentes

#### AWS Cloud
- **Application Load Balancer**: Distribución de tráfico HTTPS
- **EC2 Instances (2x)**: Windows Server 2019, t3.xlarge
- **Site-to-Site VPN**: Conectividad segura a on-premise
- **Virtual Private Gateway**: Gateway VPN en AWS
- **NAT Gateway**: Salida a internet
- **CloudWatch**: Monitoring y logs
- **Systems Manager**: Gestión de instancias

#### On-Premise
- **SQL Server**: Base de datos existente
- **VPN Gateway**: Conexión a AWS
- **Firewall**: Reglas de acceso

#### Networking (CRÍTICO)
- **VPC**: 10.0.0.0/16
- **Public Subnet**: 10.0.1.0/24 (ALB, NAT)
- **Private Subnet**: 10.0.10.0/24 (EC2 instances)
- **VPN Tunnel**: Encriptado IPSec
- **Route Tables**: Rutas a on-premise

---

## 🌐 Networking Detallado (ENFOQUE PRINCIPAL)

### 1. VPC Configuration

```hcl
# VPC Principal
CIDR: 10.0.0.0/16

# Subnets
Public Subnet A:  10.0.1.0/24  (us-east-1a)
Public Subnet B:  10.0.2.0/24  (us-east-1b)
Private Subnet A: 10.0.10.0/24 (us-east-1a)
Private Subnet B: 10.0.11.0/24 (us-east-1b)
```

### 2. Site-to-Site VPN

#### Configuración AWS
```bash
# Virtual Private Gateway
aws ec2 create-vpn-gateway \
  --type ipsec.1 \
  --amazon-side-asn 64512

# Attach to VPC
aws ec2 attach-vpn-gateway \
  --vpn-gateway-id vgw-xxxxx \
  --vpc-id vpc-xxxxx

# Customer Gateway (On-Premise)
aws ec2 create-customer-gateway \
  --type ipsec.1 \
  --public-ip [IP_PUBLICA_ONPREMISE] \
  --bgp-asn 65000

# VPN Connection
aws ec2 create-vpn-connection \
  --type ipsec.1 \
  --customer-gateway-id cgw-xxxxx \
  --vpn-gateway-id vgw-xxxxx
```

#### Parámetros VPN
```yaml
Encryption: AES-256
Authentication: SHA-256
DH Group: 14 (2048-bit)
IKE Version: IKEv2
Perfect Forward Secrecy: Enabled
Dead Peer Detection: Enabled
Tunnel 1: 169.254.10.1/30
Tunnel 2: 169.254.10.5/30
```

### 3. Route Tables

#### Public Subnet Route Table
```
Destination         Target
10.0.0.0/16        local
0.0.0.0/0          igw-xxxxx (Internet Gateway)
```

#### Private Subnet Route Table
```
Destination         Target
10.0.0.0/16        local
192.168.0.0/16     vgw-xxxxx (On-Premise via VPN)
0.0.0.0/0          nat-xxxxx (NAT Gateway)
```

### 4. Security Groups

#### ALB Security Group
```yaml
Inbound:
  - Port 443 (HTTPS): 0.0.0.0/0
  - Port 80 (HTTP): 0.0.0.0/0 (redirect to 443)

Outbound:
  - All traffic: 10.0.0.0/16
```

#### EC2 Security Group
```yaml
Inbound:
  - Port 80: ALB Security Group
  - Port 443: ALB Security Group
  - Port 3389 (RDP): 10.0.0.0/16 (management)
  - Port 1433 (SQL): 192.168.0.0/16 (on-premise)

Outbound:
  - Port 1433: 192.168.0.0/16 (SQL Server on-premise)
  - Port 443: 0.0.0.0/0 (updates, AWS services)
  - Port 80: 0.0.0.0/0 (updates)
```

#### SQL Server On-Premise Firewall
```yaml
Inbound:
  - Port 1433: 10.0.0.0/16 (AWS VPC)
  - Source: VPN Tunnel IPs
```

### 5. DNS Configuration

#### Route 53 Private Hosted Zone
```bash
# Crear hosted zone privada
aws route53 create-hosted-zone \
  --name backoffice.internal \
  --vpc VPCRegion=us-east-1,VPCId=vpc-xxxxx \
  --caller-reference $(date +%s)

# Record para SQL Server on-premise
Name: sqlserver.backoffice.internal
Type: A
Value: 192.168.1.10 (IP on-premise)
```

### 6. Network ACLs (Opcional)

#### Private Subnet NACL
```yaml
Inbound:
  100: Allow TCP 1433 from 192.168.0.0/16
  110: Allow TCP 443 from 10.0.0.0/16
  120: Allow TCP 80 from 10.0.0.0/16
  *: Deny all

Outbound:
  100: Allow TCP 1433 to 192.168.0.0/16
  110: Allow TCP 443 to 0.0.0.0/0
  120: Allow TCP 80 to 0.0.0.0/0
  *: Deny all
```

---

## 🚀 Plan de Migración (2-3 Semanas)

### Semana 1: Preparación y Networking

#### Día 1-2: Setup VPC y Networking
- [ ] Crear VPC (10.0.0.0/16)
- [ ] Crear subnets (public y private)
- [ ] Crear Internet Gateway
- [ ] Crear NAT Gateway
- [ ] Configurar Route Tables
- [ ] Crear Security Groups

#### Día 3-4: Configurar VPN
- [ ] Crear Virtual Private Gateway
- [ ] Crear Customer Gateway
- [ ] Establecer VPN Connection
- [ ] Configurar VPN on-premise
- [ ] Testing de conectividad
- [ ] Validar latencia (<50ms)

#### Día 5: Testing de Conectividad
- [ ] Ping a SQL Server on-premise desde AWS
- [ ] Test de conexión SQL desde EC2 temporal
- [ ] Validar throughput de red
- [ ] Documentar IPs y rutas

**Entregables Semana 1**:
- ✅ VPC configurado
- ✅ VPN funcionando
- ✅ Conectividad a SQL Server validada

---

### Semana 2: Migración de Aplicación

#### Día 1-2: Preparar AMI
- [ ] Crear EC2 temporal con Windows Server 2019
- [ ] Instalar IIS y .NET Framework
- [ ] Configurar aplicación
- [ ] Testing de conexión a SQL on-premise
- [ ] Crear AMI (Amazon Machine Image)

#### Día 3: Configurar ALB y Auto Scaling
- [ ] Crear Application Load Balancer
- [ ] Configurar Target Groups
- [ ] Crear Launch Template con AMI
- [ ] Configurar Auto Scaling Group (min 2, max 4)
- [ ] Configurar health checks

#### Día 4: Migración de Aplicación
- [ ] Lanzar instancias EC2 desde AMI
- [ ] Configurar connection strings a SQL on-premise
- [ ] Validar aplicación funciona
- [ ] Testing funcional completo

#### Día 5: Testing y Ajustes
- [ ] Testing de carga
- [ ] Validar performance
- [ ] Ajustar configuraciones
- [ ] Documentar configuración

**Entregables Semana 2**:
- ✅ Aplicación funcionando en AWS
- ✅ Conectada a SQL on-premise
- ✅ ALB y Auto Scaling configurados

---

### Semana 3: Go-Live y Estabilización

#### Día 1: Preparación Final
- [ ] Backup completo on-premise
- [ ] Validación final en AWS
- [ ] Comunicación a usuarios
- [ ] Plan de rollback listo

#### Día 2: Cutover
- [ ] Actualizar DNS a ALB
- [ ] Monitoreo intensivo
- [ ] Validación de tráfico
- [ ] Testing con usuarios

#### Día 3-4: Monitoreo Post-Deploy
- [ ] Monitoreo 24/7
- [ ] Validación de métricas
- [ ] Ajustes de performance
- [ ] Recolección de feedback

#### Día 5: Documentación y Handover
- [ ] Runbook de operaciones
- [ ] Documentación de arquitectura
- [ ] Training a equipo
- [ ] Retrospectiva

**Entregables Semana 3**:
- ✅ Aplicación en producción
- ✅ Usuarios migrando exitosamente
- ✅ Documentación completa

---

## 💰 Estimación de Costos

### Compute (EC2)
| Componente | Especificación | Cantidad | Costo/hora | Horas/mes | Subtotal |
|------------|----------------|----------|------------|-----------|----------|
| EC2 Instances | t3.xlarge (4 vCPU, 16GB) | 2 | $0.1664 | 730 | $243 |
| **Total Compute** | | | | | **$243** |

### Networking
| Componente | Costo/mes |
|------------|-----------|
| Application Load Balancer | $23 |
| NAT Gateway | $33 |
| Site-to-Site VPN | $36 |
| Data Transfer VPN (100GB) | $9 |
| **Total Networking** | **$101** |

### Storage
| Componente | Costo/mes |
|------------|-----------|
| EBS gp3 (200GB x 2) | $16 |
| S3 Backups (50GB) | $1 |
| **Total Storage** | **$17** |

### Monitoring
| Componente | Costo/mes |
|------------|-----------|
| CloudWatch Logs (5GB) | $3 |
| CloudWatch Alarms | $1 |
| Systems Manager | $0 |
| **Total Monitoring** | **$4** |

### TOTAL MENSUAL

| Categoría | Costo |
|-----------|-------|
| Compute | $243 |
| Networking | $101 |
| Storage | $17 |
| Monitoring | $4 |
| **Subtotal** | **$365** |
| Contingencia (10%) | $37 |
| **TOTAL** | **$402/mes** |

**Nota**: SQL Server on-premise mantiene su costo actual

---

## 🔒 Consideraciones de Seguridad

### VPN Security
- ✅ **Encriptación**: AES-256
- ✅ **Autenticación**: Pre-shared keys
- ✅ **Redundancia**: 2 túneles VPN
- ✅ **Monitoring**: CloudWatch VPN metrics

### Network Security
- ✅ **Security Groups**: Least privilege
- ✅ **NACLs**: Capa adicional de seguridad
- ✅ **Private Subnets**: EC2 sin IP pública
- ✅ **VPN Only**: SQL accesible solo via VPN

### Application Security
- ✅ **SSL/TLS**: HTTPS obligatorio en ALB
- ✅ **WAF** (opcional): Protección contra ataques
- ✅ **Secrets Manager**: Credenciales encriptadas
- ✅ **IAM Roles**: Acceso basado en roles

---

## 📊 Monitoreo y Observabilidad

### CloudWatch Metrics
```yaml
EC2:
  - CPUUtilization
  - NetworkIn/Out
  - DiskReadOps/WriteOps
  - StatusCheckFailed

ALB:
  - TargetResponseTime
  - HTTPCode_Target_4XX_Count
  - HTTPCode_Target_5XX_Count
  - HealthyHostCount

VPN:
  - TunnelState
  - TunnelDataIn/Out
```

### CloudWatch Alarms
```yaml
Critical:
  - EC2 CPU > 80% por 5 min
  - ALB 5xx errors > 10 en 5 min
  - VPN Tunnel Down
  - Unhealthy targets > 0

Warning:
  - EC2 CPU > 60% por 10 min
  - ALB latency > 2s
  - VPN latency > 100ms
```

### Systems Manager
- ✅ **Session Manager**: Acceso SSH/RDP sin bastion
- ✅ **Patch Manager**: Actualizaciones automáticas
- ✅ **Run Command**: Ejecución remota de comandos
- ✅ **Parameter Store**: Configuraciones centralizadas

---

## 🔄 Roadmap de Modernización Futura

### Fase 2: Modernización de Aplicación (6 meses)

#### Amazon Q for .NET Transform
```
Herramienta: Amazon Q Developer Agent for code transformation
Objetivo: Migrar de .NET Framework a .NET 8
Timeline: 2-3 meses
```

**Proceso**:
1. **Assessment con Amazon Q**
   - Análisis automático de código
   - Identificación de incompatibilidades
   - Reporte de esfuerzo de migración

2. **Transformación Automática**
   - Amazon Q transforma código a .NET 8
   - Actualiza dependencias
   - Moderniza patrones de código

3. **Testing y Validación**
   - Testing automatizado
   - Validación funcional
   - Performance testing

4. **Containerización**
   - Crear Dockerfile
   - Migrar a ECS Fargate
   - Implementar CI/CD

**Beneficios**:
- ✅ **80% automatización**: Amazon Q hace el trabajo pesado
- ✅ **Reducción de costos**: Contenedores más económicos
- ✅ **Performance**: .NET 8 es 3x más rápido
- ✅ **Escalabilidad**: Auto-scaling nativo

### Fase 3: Migración de Base de Datos (3 meses)

#### Opción 1: RDS SQL Server
```
Servicio: Amazon RDS for SQL Server
Timeline: 2-3 meses
Costo: ~$300/mes (db.t3.large)
```

**Proceso**:
1. **Assessment con DMS**
   - Schema Conversion Tool
   - Análisis de compatibilidad

2. **Migración con DMS**
   - Full load migration
   - CDC (Change Data Capture)
   - Validación de datos

3. **Cutover**
   - Actualizar connection strings
   - Testing exhaustivo
   - Rollback plan

#### Opción 2: Aurora PostgreSQL + Babelfish
```
Servicio: Aurora PostgreSQL con Babelfish
Timeline: 3-4 meses
Costo: ~$150/mes (db.t3.large)
Ahorro: 50% vs RDS SQL Server
```

**Beneficios**:
- ✅ **Compatibilidad SQL Server**: Puerto 1433 (TDS)
- ✅ **Sin cambios de código**: Connection string compatible
- ✅ **50% más económico**: vs RDS SQL Server
- ✅ **Performance**: Motor PostgreSQL optimizado

---

## 📋 Checklist de Migración

### Pre-Migración
- [ ] Auditoría de aplicación actual
- [ ] Documentar dependencias
- [ ] Identificar connection strings
- [ ] Backup completo
- [ ] Plan de rollback documentado

### Networking
- [ ] VPC creado y configurado
- [ ] Subnets creadas (public y private)
- [ ] Internet Gateway configurado
- [ ] NAT Gateway desplegado
- [ ] Route Tables configuradas
- [ ] Security Groups creados
- [ ] VPN establecido y testeado
- [ ] Conectividad a SQL validada

### Aplicación
- [ ] AMI creado con aplicación
- [ ] ALB configurado
- [ ] Auto Scaling Group creado
- [ ] Health checks configurados
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

### Riesgo 1: Latencia VPN
**Probabilidad**: Media  
**Impacto**: Alto  
**Mitigación**:
- Testing exhaustivo de latencia pre-migración
- Optimizar queries SQL
- Implementar caching en aplicación
- Considerar AWS Direct Connect si latencia >50ms

### Riesgo 2: Ancho de Banda VPN
**Probabilidad**: Media  
**Impacto**: Medio  
**Mitigación**:
- Monitorear throughput de VPN
- Implementar compresión de datos
- Optimizar tamaño de resultsets SQL
- Upgrade a Direct Connect si necesario

### Riesgo 3: Disponibilidad VPN
**Probabilidad**: Baja  
**Impacto**: Alto  
**Mitigación**:
- 2 túneles VPN (redundancia)
- Monitoreo proactivo con alarmas
- Procedimiento de failover documentado
- SLA con proveedor de internet

---

## ✅ Criterios de Éxito

1. ✅ **Aplicación funcionando** en AWS EC2
2. ✅ **Conectividad híbrida** estable (<50ms latencia)
3. ✅ **Costo mensual** ~$400 (sin BD)
4. ✅ **Disponibilidad** >99.5%
5. ✅ **Performance** igual o mejor que on-premise
6. ✅ **Zero data loss** durante migración
7. ✅ **Rollback exitoso** si necesario

---

## 🎯 Próximos Pasos

### Inmediatos (Esta Semana)
1. [ ] Aprobar estrategia Lift & Shift
2. [ ] Asignar equipo de migración
3. [ ] Iniciar setup de VPC
4. [ ] Coordinar configuración VPN on-premise
5. [ ] Kick-off meeting

### Corto Plazo (Mes 1)
1. [ ] Completar migración (3 semanas)
2. [ ] Estabilizar en producción
3. [ ] Documentar lecciones aprendidas
4. [ ] Planificar Fase 2 (modernización)

### Mediano Plazo (Meses 2-6)
1. [ ] Iniciar modernización con Amazon Q
2. [ ] Migrar a .NET 8
3. [ ] Containerizar con ECS
4. [ ] Implementar CI/CD

### Largo Plazo (Meses 7-9)
1. [ ] Migrar base de datos a AWS
2. [ ] Eliminar VPN (todo en AWS)
3. [ ] Optimización continua

---

**Última actualización**: 2025-12-04  
**Versión**: 1.0  
**Estado**: Listo para implementación  
**Estrategia**: Lift & Shift con roadmap de modernización
