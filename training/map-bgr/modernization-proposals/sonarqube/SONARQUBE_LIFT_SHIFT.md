# SonarQube - Lift & Shift a AWS
## Migración de Herramienta DevOps Crítica

**Fecha**: 2025-12-04  
**Aplicación**: SonarQube  
**Tipo**: Code Quality & Security Analysis  
**Estrategia**: Lift & Shift con optimizaciones  
**Timeline**: 2 semanas

---

## 🎯 Contexto

### ¿Qué es SonarQube?
SonarQube es una plataforma de análisis de código que:
- Detecta bugs y vulnerabilidades
- Mide code quality y technical debt
- Integra con CI/CD pipelines
- Soporta 25+ lenguajes de programación

### Situación Actual
- **3 VMs** sobredimensionadas (42 vCPUs, 144GB RAM)
- **SQL Server** como base de datos
- **Uso**: Análisis de código para todos los proyectos
- **Criticidad**: Media-Alta (herramienta DevOps core)

---

## 🏗️ Arquitectura AWS Propuesta

![Arquitectura SonarQube](./generated-diagrams/sonarqube_lift_shift.png)

### Componentes

#### Compute
- **EC2 Instance**: t3.xlarge (4 vCPU, 16GB RAM)
- **OS**: Amazon Linux 2 o Ubuntu 22.04
- **SonarQube**: Community o Enterprise Edition

#### Database
- **RDS PostgreSQL**: db.t3.large (2 vCPU, 8GB RAM)
- **Multi-AZ**: Alta disponibilidad
- **Automated Backups**: 7 días retention

#### Storage
- **EFS**: Shared storage para plugins y datos
- **S3**: Backups y archivos de análisis
- **EBS gp3**: 100GB para OS y aplicación

#### Networking
- **ALB**: HTTPS con SSL/TLS
- **Private Subnets**: EC2 y RDS sin IP pública
- **NAT Gateway**: Salida a internet para updates

#### Monitoring
- **CloudWatch**: Logs y métricas
- **SNS**: Alertas por email/Slack

---

## 💡 Optimizaciones vs On-Premise

### Cambio de Base de Datos
**De**: SQL Server  
**A**: PostgreSQL (recomendado por SonarQube)

**Razones**:
- ✅ **Costo**: PostgreSQL es gratis vs licencias SQL Server
- ✅ **Performance**: Mejor para SonarQube
- ✅ **Soporte**: Recomendación oficial de SonarSource
- ✅ **Compatibilidad**: 100% soportado

### Cambio de OS
**De**: Windows Server  
**A**: Linux (Amazon Linux 2 o Ubuntu)

**Razones**:
- ✅ **Costo**: Sin licencias Windows
- ✅ **Performance**: Menor overhead
- ✅ **Recursos**: Menos RAM/CPU requerido
- ✅ **Actualizaciones**: Más rápidas y simples

---

## 🚀 Plan de Migración (2 Semanas)

### Semana 1: Preparación e Infraestructura

#### Día 1-2: Setup AWS
```bash
# Crear VPC
aws ec2 create-vpc --cidr-block 10.1.0.0/16

# Crear subnets
aws ec2 create-subnet --vpc-id vpc-xxx --cidr-block 10.1.1.0/24  # Public
aws ec2 create-subnet --vpc-id vpc-xxx --cidr-block 10.1.10.0/24 # Private App
aws ec2 create-subnet --vpc-id vpc-xxx --cidr-block 10.1.20.0/24 # Private DB

# Crear RDS PostgreSQL
aws rds create-db-instance \
  --db-instance-identifier sonarqube-db \
  --db-instance-class db.t3.large \
  --engine postgres \
  --engine-version 15.4 \
  --master-username sonarqube \
  --master-user-password [SECURE_PASSWORD] \
  --allocated-storage 100 \
  --storage-type gp3 \
  --multi-az \
  --backup-retention-period 7
```

#### Día 3: Preparar EC2 y EFS
```bash
# Crear EFS
aws efs create-file-system \
  --performance-mode generalPurpose \
  --throughput-mode bursting \
  --encrypted

# Lanzar EC2 con Amazon Linux 2
aws ec2 run-instances \
  --image-id ami-0c55b159cbfafe1f0 \
  --instance-type t3.xlarge \
  --key-name sonarqube-key \
  --security-group-ids sg-xxx \
  --subnet-id subnet-xxx \
  --iam-instance-profile Name=SonarQubeRole
```

#### Día 4: Instalar SonarQube
```bash
# Conectar a EC2
ssh -i sonarqube-key.pem ec2-user@[EC2_IP]

# Instalar Java 17
sudo yum install -y java-17-amazon-corretto

# Descargar SonarQube
wget https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-10.3.0.82913.zip
unzip sonarqube-10.3.0.82913.zip
sudo mv sonarqube-10.3.0.82913 /opt/sonarqube

# Configurar usuario
sudo useradd sonar
sudo chown -R sonar:sonar /opt/sonarqube

# Montar EFS
sudo mkdir /mnt/efs
sudo mount -t nfs4 [EFS_DNS]:/ /mnt/efs
```

#### Día 5: Configurar SonarQube
```properties
# /opt/sonarqube/conf/sonar.properties

# Database
sonar.jdbc.username=sonarqube
sonar.jdbc.password=[RDS_PASSWORD]
sonar.jdbc.url=jdbc:postgresql://[RDS_ENDPOINT]:5432/sonarqube

# Web Server
sonar.web.host=0.0.0.0
sonar.web.port=9000
sonar.web.context=/

# Elasticsearch
sonar.search.javaOpts=-Xmx2G -Xms2G

# Paths
sonar.path.data=/mnt/efs/data
sonar.path.temp=/mnt/efs/temp
```

**Entregables Semana 1**:
- ✅ Infraestructura AWS lista
- ✅ SonarQube instalado y configurado
- ✅ Conectado a RDS PostgreSQL

---

### Semana 2: Migración y Go-Live

#### Día 1-2: Migración de Datos
```bash
# Backup de SQL Server on-premise
# Opción 1: Usar SonarQube backup/restore
cd /opt/sonarqube
./bin/linux-x86-64/sonar.sh stop

# Exportar datos desde SQL Server
# Usar herramienta de migración de SonarQube

# Importar a PostgreSQL
psql -h [RDS_ENDPOINT] -U sonarqube -d sonarqube < backup.sql

# Iniciar SonarQube
./bin/linux-x86-64/sonar.sh start
```

#### Día 3: Configurar ALB
```bash
# Crear ALB
aws elbv2 create-load-balancer \
  --name sonarqube-alb \
  --subnets subnet-xxx subnet-yyy \
  --security-groups sg-xxx

# Crear Target Group
aws elbv2 create-target-group \
  --name sonarqube-tg \
  --protocol HTTP \
  --port 9000 \
  --vpc-id vpc-xxx \
  --health-check-path /api/system/status

# Registrar EC2
aws elbv2 register-targets \
  --target-group-arn arn:aws:elasticloadbalancing:... \
  --targets Id=i-xxx
```

#### Día 4: Testing
- [ ] Validar acceso via ALB
- [ ] Testing de análisis de código
- [ ] Validar integración con CI/CD
- [ ] Performance testing
- [ ] Validar plugins instalados

#### Día 5: Go-Live
- [ ] Actualizar DNS a ALB
- [ ] Comunicar a desarrolladores
- [ ] Monitoreo intensivo
- [ ] Validación con usuarios
- [ ] Documentación

**Entregables Semana 2**:
- ✅ SonarQube en producción
- ✅ Datos migrados
- ✅ Integración CI/CD funcionando

---

## 💰 Estimación de Costos

### Compute
| Componente | Especificación | Cantidad | Costo/hora | Horas/mes | Subtotal |
|------------|----------------|----------|------------|-----------|----------|
| EC2 | t3.xlarge (4 vCPU, 16GB) | 1 | $0.1664 | 730 | $121 |
| **Total Compute** | | | | | **$121** |

### Database
| Componente | Especificación | Costo/mes |
|------------|----------------|-----------|
| RDS PostgreSQL | db.t3.large Multi-AZ | $146 |
| Storage (100GB) | gp3 | $12 |
| **Total Database** | | **$158** |

### Storage
| Componente | Costo/mes |
|------------|-----------|
| EFS (50GB) | $15 |
| S3 Backups (20GB) | $0.50 |
| EBS gp3 (100GB) | $8 |
| **Total Storage** | **$23.50** |

### Networking
| Componente | Costo/mes |
|------------|-----------|
| ALB | $23 |
| NAT Gateway | $33 |
| Data Transfer | $5 |
| **Total Networking** | **$61** |

### Monitoring
| Componente | Costo/mes |
|------------|-----------|
| CloudWatch | $3 |
| SNS | $0.50 |
| **Total Monitoring** | **$3.50** |

### TOTAL MENSUAL

| Categoría | Costo |
|-----------|-------|
| Compute | $121 |
| Database | $158 |
| Storage | $23.50 |
| Networking | $61 |
| Monitoring | $3.50 |
| **Subtotal** | **$367** |
| Contingencia (10%) | $37 |
| **TOTAL** | **$404/mes** |

**Comparativa**:
- **Actual**: ~$1,500/mes (3 VMs + SQL Server)
- **AWS**: $404/mes
- **Ahorro**: $1,096/mes (73%)

---

## 🔧 Configuración Detallada

### SonarQube System Service

```bash
# /etc/systemd/system/sonarqube.service
[Unit]
Description=SonarQube service
After=syslog.target network.target

[Service]
Type=forking
ExecStart=/opt/sonarqube/bin/linux-x86-64/sonar.sh start
ExecStop=/opt/sonarqube/bin/linux-x86-64/sonar.sh stop
User=sonar
Group=sonar
Restart=always
LimitNOFILE=65536
LimitNPROC=4096

[Install]
WantedBy=multi-user.target

# Habilitar servicio
sudo systemctl enable sonarqube
sudo systemctl start sonarqube
```

### Security Groups

#### ALB Security Group
```yaml
Inbound:
  - Port 443 (HTTPS): 0.0.0.0/0
  - Port 80 (HTTP): 0.0.0.0/0 (redirect to 443)

Outbound:
  - Port 9000: EC2 Security Group
```

#### EC2 Security Group
```yaml
Inbound:
  - Port 9000: ALB Security Group
  - Port 22 (SSH): 10.1.0.0/16 (management)
  - Port 2049 (NFS): EFS Security Group

Outbound:
  - Port 5432: RDS Security Group
  - Port 443: 0.0.0.0/0 (updates, plugins)
  - Port 2049: EFS Security Group
```

#### RDS Security Group
```yaml
Inbound:
  - Port 5432: EC2 Security Group

Outbound:
  - None required
```

### CloudWatch Alarms

```yaml
Alarms:
  - EC2 CPU > 80% por 5 min
  - RDS CPU > 80% por 5 min
  - RDS Storage < 20%
  - ALB 5xx errors > 10
  - ALB Unhealthy targets > 0
  - EFS Throughput > 80%
```

---

## 🔄 Integración con CI/CD

### Azure DevOps Integration

```yaml
# azure-pipelines.yml
trigger:
  - main

pool:
  vmImage: 'ubuntu-latest'

steps:
  - task: SonarQubePrepare@5
    inputs:
      SonarQube: 'SonarQube-AWS'
      scannerMode: 'CLI'
      configMode: 'manual'
      cliProjectKey: 'my-project'
      cliProjectName: 'My Project'
      cliSources: '.'

  - task: Maven@3
    inputs:
      goals: 'clean verify'

  - task: SonarQubeAnalyze@5

  - task: SonarQubePublish@5
    inputs:
      pollingTimeoutSec: '300'
```

### GitHub Actions Integration

```yaml
# .github/workflows/sonarqube.yml
name: SonarQube Analysis

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  sonarqube:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
        with:
          fetch-depth: 0

      - name: SonarQube Scan
        uses: sonarsource/sonarqube-scan-action@master
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
          SONAR_HOST_URL: https://sonarqube.bgr.com
```

---

## 📊 Monitoreo y Métricas

### CloudWatch Dashboards

```yaml
Widgets:
  - SonarQube Response Time
  - Analysis Queue Length
  - Database Connections
  - CPU Utilization (EC2 & RDS)
  - Memory Usage
  - Disk I/O
  - Network Throughput
```

### SonarQube Metrics

```yaml
Key Metrics:
  - Lines of Code Analyzed
  - Code Coverage %
  - Technical Debt Ratio
  - Bugs Detected
  - Vulnerabilities Found
  - Code Smells
  - Duplications %
```

---

## 🔒 Seguridad y Compliance

### SSL/TLS Configuration

```bash
# Solicitar certificado ACM
aws acm request-certificate \
  --domain-name sonarqube.bgr.com \
  --validation-method DNS

# Configurar HTTPS en ALB
aws elbv2 create-listener \
  --load-balancer-arn arn:aws:elasticloadbalancing:... \
  --protocol HTTPS \
  --port 443 \
  --certificates CertificateArn=arn:aws:acm:... \
  --default-actions Type=forward,TargetGroupArn=arn:aws:elasticloadbalancing:...
```

### Authentication

```properties
# LDAP/Active Directory Integration
sonar.security.realm=LDAP
ldap.url=ldap://ldap.bgr.com:389
ldap.bindDn=cn=sonar,ou=users,dc=bgr,dc=com
ldap.bindPassword=[LDAP_PASSWORD]
ldap.user.baseDn=ou=users,dc=bgr,dc=com
ldap.user.request=(&(objectClass=user)(sAMAccountName={login}))
```

### Backup Strategy

```bash
# Script de backup diario
#!/bin/bash
# /opt/scripts/sonarqube-backup.sh

DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR=/mnt/efs/backups

# Backup PostgreSQL
pg_dump -h [RDS_ENDPOINT] -U sonarqube sonarqube | gzip > $BACKUP_DIR/db_$DATE.sql.gz

# Backup configuración
tar -czf $BACKUP_DIR/conf_$DATE.tar.gz /opt/sonarqube/conf

# Sync a S3
aws s3 sync $BACKUP_DIR s3://sonarqube-backups-bgr/

# Limpiar backups antiguos (>30 días)
find $BACKUP_DIR -name "*.gz" -mtime +30 -delete

# Cron job
# 0 2 * * * /opt/scripts/sonarqube-backup.sh
```

---

## 🎯 Optimizaciones Post-Migración

### Performance Tuning

```properties
# sonar.properties - Optimizaciones

# Elasticsearch
sonar.search.javaOpts=-Xmx4G -Xms4G -XX:MaxDirectMemorySize=2G

# Web Server
sonar.web.javaOpts=-Xmx2G -Xms2G

# Compute Engine
sonar.ce.javaOpts=-Xmx2G -Xms2G

# Workers
sonar.ce.workerCount=2
```

### Database Optimization

```sql
-- Índices adicionales para performance
CREATE INDEX idx_projects_uuid ON projects(uuid);
CREATE INDEX idx_issues_component ON issues(component_uuid);
CREATE INDEX idx_snapshots_project ON snapshots(project_uuid);

-- Vacuum y analyze regular
VACUUM ANALYZE;
```

### Caching

```properties
# Redis para cache (opcional)
sonar.cache.type=redis
sonar.cache.redis.host=[ELASTICACHE_ENDPOINT]
sonar.cache.redis.port=6379
```

---

## 📋 Checklist de Migración

### Pre-Migración
- [ ] Backup completo de SonarQube actual
- [ ] Exportar configuración y plugins
- [ ] Documentar integraciones CI/CD
- [ ] Listar usuarios y permisos
- [ ] Identificar proyectos críticos

### Infraestructura AWS
- [ ] VPC y subnets creados
- [ ] RDS PostgreSQL provisionado
- [ ] EC2 instance lanzado
- [ ] EFS montado
- [ ] ALB configurado
- [ ] Security Groups configurados
- [ ] SSL certificate instalado

### Instalación
- [ ] Java 17 instalado
- [ ] SonarQube instalado
- [ ] Conectado a RDS
- [ ] Plugins instalados
- [ ] Configuración migrada

### Testing
- [ ] Análisis de código funciona
- [ ] Integración CI/CD validada
- [ ] Performance aceptable
- [ ] Usuarios pueden acceder
- [ ] Backups funcionando

### Go-Live
- [ ] DNS actualizado
- [ ] Comunicación a equipos
- [ ] Monitoreo activo
- [ ] Documentación completa

---

## ⚠️ Riesgos y Mitigaciones

### Riesgo 1: Pérdida de Datos Históricos
**Probabilidad**: Baja  
**Impacto**: Alto  
**Mitigación**:
- Backup completo antes de migración
- Testing exhaustivo de migración en ambiente dev
- Validación de integridad de datos post-migración
- Mantener on-premise 2 semanas como fallback

### Riesgo 2: Incompatibilidad de Plugins
**Probabilidad**: Media  
**Impacto**: Medio  
**Mitigación**:
- Listar todos los plugins actuales
- Verificar compatibilidad con versión nueva
- Testing de plugins en ambiente dev
- Plan B: versión anterior de SonarQube

### Riesgo 3: Performance Degradado
**Probabilidad**: Baja  
**Impacto**: Medio  
**Mitigación**:
- Sizing adecuado (t3.xlarge)
- PostgreSQL optimizado
- Monitoreo proactivo
- Auto-scaling si necesario

---

## ✅ Criterios de Éxito

1. ✅ **SonarQube funcionando** en AWS
2. ✅ **Datos históricos migrados** completamente
3. ✅ **Integración CI/CD** funcionando
4. ✅ **Performance** igual o mejor
5. ✅ **Costo** <$500/mes
6. ✅ **Disponibilidad** >99.5%
7. ✅ **Backups automáticos** configurados

---

## 🎯 Próximos Pasos

### Inmediatos
1. [ ] Aprobar plan de migración
2. [ ] Asignar equipo técnico
3. [ ] Crear ambiente AWS
4. [ ] Iniciar setup de infraestructura

### Semana 1
1. [ ] Completar infraestructura AWS
2. [ ] Instalar y configurar SonarQube
3. [ ] Testing inicial

### Semana 2
1. [ ] Migrar datos
2. [ ] Configurar integraciones
3. [ ] Go-live
4. [ ] Documentación

---

**Última actualización**: 2025-12-04  
**Versión**: 1.0  
**Estado**: Listo para implementación  
**Timeline**: 2 semanas
