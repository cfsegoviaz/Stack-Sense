# Seq - Propuesta de Modernización y Migración a AWS
## Servidor de Logs Centralizado

**Fecha**: 2025-12-11  
**Aplicación**: Seq  
**Tipo**: Log Management Platform  
**Estrategia**: Modernización con servicios AWS nativos  
**Timeline**: 3-4 semanas


## 🎯 Contexto

### ¿Qué es Seq?
Seq es una plataforma autohosteable que funciona como servidor de logs centralizado:
- Recolección y almacenamiento de logs estructurados
- Búsqueda y análisis en tiempo real
- Dashboards y visualizaciones
- Alertas y notificaciones
- API para integración con aplicaciones

### Situación Actual

#### Servidores Identificados

**Producción:**
- **ECBRPRW44** (172.20.1.111)
  - 4 vCPUs, 20 GB RAM
  - Windows Server 2016
  - Uso CPU: 21.47% | RAM: 10.28 GB
  
- **ECBRPRW45** (172.20.1.112)
  - 8 vCPUs, 20 GB RAM
  - Windows Server 2016
  - Uso CPU: 21.47% | RAM: 14.81 GB

- **ECBRPRCL13** (172.20.167.59) - Base de Datos
  - 24 vCPUs, 80 GB RAM
  - Windows Server 2016
  - SQL Server 2016 Enterprise Edition
  - Uso CPU: 50.99% | RAM: 85.90 GB

**Testing:**
- **ECBRTSCC01**
- **ECBRTSW21**

#### Stack Tecnológico Actual
- **Frontend/Backend**: ASP.NET C# (.NET Framework 4.7.1) - **OBSOLETO**
- **Base de Datos**: SQL Server 2016 Enterprise
- **Sistema Operativo**: Windows Server 2016
- **Plugins**: ajaxToolkit v3.5, Bootstrap

#### Características de la Aplicación
- **Usuarios**: 685 colaboradores del BGR
- **Propósito**: Guía telefónica y directorio del BGR
- **Criticidad**: Media (servicio interno)
- **Dependencias**:
  - Base de datos: PORTAL_ADMINISTRATIVO_BGR
  - Microservicio: BGRCELULAR (Notificador)
  - Identidades: Active Directory
  - Configuración: Tcs.ServicioConfiguracionBGR.WS


## 🏗️ Arquitectura Actual (AS-IS)

![Arquitectura Actual](./diagrams/generated-diagrams/seq_current_architecture.png)

### Componentes On-Premise

### Problemas Identificados
1. ❌ **Tecnología Obsoleta**: .NET Framework 4.7.1 (EOL)
2. ❌ **Sobredimensionamiento**: Servidor DB con 24 vCPUs para uso del 50%
3. ❌ **Costos de Licenciamiento**: SQL Server Enterprise + Windows Server
4. ❌ **Falta de Escalabilidad**: Arquitectura monolítica
5. ❌ **Sin DevOps**: No hay CI/CD, automatización ni monitoreo proactivo
6. ❌ **Dependencias Legacy**: Active Directory on-premise


## 💡 Arquitectura Propuesta (TO-BE)

### Opción 1: Modernización Completa (RECOMENDADA)

#### Reemplazo con Servicios AWS Nativos
En lugar de migrar Seq tal cual, modernizar con servicios AWS especializados:

**Para Logs de Aplicaciones:**
- **Amazon CloudWatch Logs**: Recolección y almacenamiento
- **CloudWatch Logs Insights**: Búsqueda y análisis
- **CloudWatch Dashboards**: Visualización
- **CloudWatch Alarms + SNS**: Alertas

**Para Logs Estructurados Avanzados:**
- **Amazon OpenSearch Service**: Búsqueda y análisis avanzado
- **OpenSearch Dashboards**: Visualización tipo Kibana
- **Lambda**: Procesamiento y transformación de logs
- **S3**: Almacenamiento a largo plazo (archival)

#### Arquitectura Modernizada
![Arquitectura AWS Modernizada](./diagrams/generated-diagrams/seq_aws_modernized.png)

#### Componentes AWS

**Ingesta de Logs:**
- **CloudWatch Logs Agent**: En cada servidor/contenedor
- **Kinesis Data Firehose**: Para alto volumen (opcional)
- **Lambda**: Transformación y enriquecimiento

**Almacenamiento y Análisis:**
- **CloudWatch Logs**: Retención 30-90 días
- **OpenSearch Service**: 
  - Cluster: 2 nodos t3.medium.search
  - Storage: 100 GB EBS gp3
  - Multi-AZ para HA
- **S3 Glacier**: Archival >90 días

**Visualización:**
- **CloudWatch Dashboards**: Métricas operacionales
- **OpenSearch Dashboards**: Análisis detallado
- **QuickSight**: Reportes ejecutivos (opcional)

**Alertas:**
- **CloudWatch Alarms**: Umbrales y anomalías
- **SNS**: Notificaciones email/Slack
- **EventBridge**: Automatización de respuestas

**Seguridad:**
- **IAM**: Control de acceso granular
- **VPC**: Aislamiento de red
- **KMS**: Encriptación de logs
- **CloudTrail**: Auditoría de accesos


### Opción 2: Lift & Shift (No Recomendada)

Si se requiere mantener Seq por razones específicas:

#### Componentes
- **EC2**: t3.medium (2 vCPU, 4 GB RAM) - Linux
- **RDS PostgreSQL**: db.t3.medium (2 vCPU, 4 GB RAM)
- **EFS**: Storage compartido para logs
- **ALB**: Load balancing con HTTPS
- **S3**: Backups

**Razones para NO recomendar:**
- Seq es una solución on-premise que duplica funcionalidad AWS nativa
- Costos de licenciamiento y mantenimiento
- Menor integración con ecosistema AWS
- Requiere gestión de infraestructura


## 📊 Análisis de Costos

![Comparación de Arquitecturas](./diagrams/generated-diagrams/seq_comparison.png)

### Opción 1: Modernización con Servicios AWS (RECOMENDADA)

#### CloudWatch Logs
- **Ingesta**: 10 GB/día × $0.50/GB = $150/mes
- **Storage**: 300 GB × $0.03/GB = $9/mes
- **Insights Queries**: 100 GB escaneados × $0.005/GB = $0.50/mes
- **Subtotal CloudWatch**: **$159.50/mes**

#### OpenSearch Service (para análisis avanzado)
- **Instancias**: 2 × t3.medium.search × $0.073/hora = $105/mes
- **Storage**: 100 GB × $0.135/GB = $13.50/mes
- **Subtotal OpenSearch**: **$118.50/mes**

#### S3 Archival
- **Glacier Deep Archive**: 500 GB × $0.00099/GB = $0.50/mes

#### Total Mensual Opción 1: **~$278/mes** (~$3,336/año)

#### 📋 Esfuerzo Escala24x7 - Opción 1 (Modernización AWS)

| Tarea | Horas | Equipo |
|-------|-------|--------|
| CloudWatch Logs setup | 4 | Infra |
| OpenSearch Cluster | 6 | Infra |
| Kinesis Data Firehose | 4 | Infra |
| Lambda Functions | 16 | Infra |
| S3 Bucket (archival) | 2 | Infra |
| CloudWatch Dashboard | 8 | Infra |
| CloudWatch Alarms | 8 | Infra |
| SNS Topics | 4 | Infra |
| Migración datos | 16 | Infra |
| Testing y validación | 16 | QA |
| Knowledge transfer | 16 | Infra |
| **TOTAL** | **100** | |

**Costo implementación**: 100 horas × $150/hora = **$15,000 USD**

### Opción 2: Lift & Shift Seq

#### Compute
- **EC2 t3.medium**: $0.0416/hora × 730 horas = $30/mes
- **EBS gp3**: 50 GB × $0.08/GB = $4/mes

#### Database
- **RDS PostgreSQL db.t3.medium**: $0.068/hora × 730 = $50/mes
- **Storage**: 50 GB × $0.115/GB = $5.75/mes
- **Backup**: 50 GB × $0.095/GB = $4.75/mes

#### Networking
- **ALB**: $16.20/mes + $0.008/LCU-hora = ~$25/mes
- **Data Transfer**: 100 GB × $0.09/GB = $9/mes

#### Total Mensual Opción 2: **~$129/mes** (~$1,548/año)

#### 📋 Esfuerzo Escala24x7 - Opción 2 (Lift & Shift)

| Tarea | Horas | Equipo |
|-------|-------|--------|
| VPC/Redes | 4 | Infra |
| EC2 Instance | 2 | Infra |
| RDS PostgreSQL | 2 | Infra |
| EFS Storage | 4 | Infra |
| ALB | 2 | Infra |
| S3 Bucket | 2 | Infra |
| MGN Configuration | 2 | Infra |
| MGN Instance | 1 | Infra |
| MGN Tests | 1 | Infra |
| CloudWatch Logs | 4 | Infra |
| Testing y validación | 8 | QA |
| Knowledge transfer | 4 | Infra |
| **TOTAL** | **36** | |

**Costo implementación**: 36 horas × $150/hora = **$5,400 USD**

### Comparación con On-Premise Actual

**Costos Actuales Estimados:**
- SQL Server Enterprise: ~$14,000/año (licencia)
- Windows Server: ~$1,000/año × 3 servidores = $3,000/año
- Hardware (depreciación): ~$5,000/año
- **Total On-Premise**: **~$22,000/año**

**Ahorro con Opción 1**: $22,000 - $3,336 = **$18,664/año (85% ahorro)**  
**Ahorro con Opción 2**: $22,000 - $1,548 = **$20,452/año (93% ahorro)**


## 🚀 Plan de Migración

![Timeline de Migración](./diagrams/generated-diagrams/seq_migration_flow.png)

### Opción 1: Modernización (4 semanas)

#### Semana 1: Diseño y Preparación
**Días 1-2: Análisis de Logs Actuales**
- Identificar tipos de logs y volúmenes
- Mapear aplicaciones que envían logs a Seq
- Definir retención y políticas de archival
- Diseñar estructura de log groups

**Días 3-5: Setup Infraestructura AWS**
```bash
# Crear log groups
aws logs create-log-group --log-group-name /bgr/applications/portal-guia
aws logs create-log-group --log-group-name /bgr/applications/backoffice
aws logs create-log-group --log-group-name /bgr/applications/api-portal

# Configurar retención
aws logs put-retention-policy \
  --log-group-name /bgr/applications/portal-guia \
  --retention-in-days 30

# Crear OpenSearch domain
aws opensearch create-domain \
  --domain-name bgr-logs \
  --engine-version OpenSearch_2.11 \
  --cluster-config InstanceType=t3.medium.search,InstanceCount=2 \
  --ebs-options EBSEnabled=true,VolumeType=gp3,VolumeSize=100
```

#### Semana 2: Migración de Logs
**Días 1-3: Configurar Agentes**
- Instalar CloudWatch Agent en servidores
- Configurar envío de logs a CloudWatch
- Implementar Lambda para transformación
- Setup Kinesis Firehose para OpenSearch

**Días 4-5: Validación Paralela**
- Ejecutar Seq y CloudWatch en paralelo
- Comparar logs y métricas
- Ajustar configuraciones

#### Semana 3: Dashboards y Alertas
**Días 1-3: Crear Visualizaciones**
- Migrar dashboards de Seq a CloudWatch/OpenSearch
- Configurar métricas personalizadas
- Crear queries de Insights

**Días 4-5: Configurar Alertas**
```bash
# Crear alarma de errores
aws cloudwatch put-metric-alarm \
  --alarm-name bgr-high-error-rate \
  --alarm-description "Alerta cuando hay muchos errores" \
  --metric-name ErrorCount \
  --namespace BGR/Applications \
  --statistic Sum \
  --period 300 \
  --threshold 100 \
  --comparison-operator GreaterThanThreshold \
  --evaluation-periods 2

# Crear SNS topic para notificaciones
aws sns create-topic --name bgr-log-alerts
aws sns subscribe \
  --topic-arn arn:aws:sns:us-east-1:ACCOUNT:bgr-log-alerts \
  --protocol email \
  --notification-endpoint ops@bgr.com.ec
```

#### Semana 4: Cutover y Optimización
**Días 1-2: Migración Final**
- Actualizar todas las aplicaciones para usar CloudWatch
- Desactivar envío a Seq
- Monitorear estabilidad

**Días 3-5: Optimización**
- Ajustar retención según uso real
- Optimizar queries de Insights
- Configurar archival a S3
- Documentación y capacitación


## 📋 Checklist de Migración

### Pre-Migración
- [ ] Inventario completo de aplicaciones que usan Seq
- [ ] Análisis de volumen de logs (GB/día)
- [ ] Identificación de dashboards críticos
- [ ] Mapeo de alertas existentes
- [ ] Definición de políticas de retención
- [ ] Aprobación de presupuesto AWS

### Durante Migración
- [ ] Crear log groups en CloudWatch
- [ ] Configurar OpenSearch domain
- [ ] Instalar CloudWatch Agent en servidores
- [ ] Configurar Lambda para transformación
- [ ] Migrar dashboards
- [ ] Configurar alertas y SNS
- [ ] Pruebas de búsqueda y análisis
- [ ] Validación de volúmenes y costos

### Post-Migración
- [ ] Monitoreo de estabilidad (1 semana)
- [ ] Ajuste de configuraciones
- [ ] Capacitación a equipos
- [ ] Documentación actualizada
- [ ] Descomisionar Seq on-premise
- [ ] Revisión de costos reales vs estimados


## 🎓 Capacitación Requerida

### Para Desarrolladores
- **CloudWatch Logs SDK**: Integración en aplicaciones
- **Structured Logging**: Best practices
- **Log Levels**: Uso correcto de INFO, WARN, ERROR

### Para Operaciones
- **CloudWatch Logs Insights**: Sintaxis de queries
- **OpenSearch Dashboards**: Creación de visualizaciones
- **CloudWatch Alarms**: Configuración de alertas
- **S3 Lifecycle**: Gestión de archival

### Para Arquitectos
- **Log Aggregation Patterns**: Diseño de soluciones
- **Cost Optimization**: Estrategias de retención
- **Security Best Practices**: Encriptación y acceso


## ⚠️ Riesgos y Mitigaciones

### Riesgos Técnicos

**1. Pérdida de Logs Durante Migración**
- **Probabilidad**: Media
- **Impacto**: Alto
- **Mitigación**: 
  - Ejecutar Seq y CloudWatch en paralelo
  - Validar volúmenes diariamente
  - Mantener Seq activo 2 semanas post-migración

**2. Queries Complejas No Soportadas**
- **Probabilidad**: Media
- **Impacto**: Medio
- **Mitigación**:
  - Mapear queries críticas antes de migrar
  - Usar OpenSearch para queries avanzadas
  - Documentar alternativas

**3. Costos Mayores a lo Estimado**
- **Probabilidad**: Media
- **Impacto**: Medio
- **Mitigación**:
  - Monitorear costos diariamente
  - Configurar AWS Budgets con alertas
  - Ajustar retención según necesidad real

### Riesgos de Negocio

**4. Resistencia al Cambio**
- **Probabilidad**: Alta
- **Impacto**: Medio
- **Mitigación**:
  - Capacitación temprana
  - Documentación clara
  - Soporte dedicado primeras semanas

**5. Dependencias No Identificadas**
- **Probabilidad**: Media
- **Impacto**: Alto
- **Mitigación**:
  - Análisis exhaustivo de integraciones
  - Pruebas en ambiente de testing
  - Plan de rollback


## 📈 Beneficios de la Modernización

### Técnicos
✅ **Escalabilidad Automática**: CloudWatch escala según demanda  
✅ **Alta Disponibilidad**: Multi-AZ nativo  
✅ **Integración Nativa**: Con todo el ecosistema AWS  
✅ **Búsqueda Avanzada**: OpenSearch con ML  
✅ **Sin Mantenimiento**: Servicios managed  

### Operacionales
✅ **Reducción de Complejidad**: Menos servidores que gestionar  
✅ **Monitoreo Unificado**: Todo en CloudWatch  
✅ **Alertas Inteligentes**: Detección de anomalías  
✅ **Archival Automático**: Lifecycle policies  

### Financieros
✅ **85% Ahorro**: vs on-premise actual  
✅ **Sin Licencias**: No SQL Server ni Windows  
✅ **Pay-as-you-go**: Solo pagas lo que usas  
✅ **Costos Predecibles**: Fácil de presupuestar  


## 🔐 Consideraciones de Seguridad

### Encriptación
- **En Tránsito**: TLS 1.2+ para todos los logs
- **En Reposo**: KMS para CloudWatch y OpenSearch
- **Archival**: S3 con SSE-KMS

### Control de Acceso
- **IAM Roles**: Acceso granular por aplicación
- **Resource Policies**: Restricción de log groups
- **VPC Endpoints**: Tráfico privado a CloudWatch
- **MFA**: Para acceso a OpenSearch Dashboards

### Auditoría
- **CloudTrail**: Registro de todos los accesos
- **Config**: Compliance de configuraciones
- **GuardDuty**: Detección de amenazas

### Compliance
- **Retención**: Según políticas corporativas
- **Segregación**: Log groups por criticidad
- **Backup**: Automático con S3 versioning


## 📚 Documentación y Recursos

### AWS Services
- [CloudWatch Logs Documentation](https://docs.aws.amazon.com/cloudwatch/logs/)
- [OpenSearch Service Guide](https://docs.aws.amazon.com/opensearch-service/)
- [CloudWatch Logs Insights Query Syntax](https://docs.aws.amazon.com/cloudwatch/logs/insights/)

### Best Practices
- [Logging Best Practices](https://docs.aws.amazon.com/prescriptive-guidance/latest/logging-monitoring-for-application-owners/)
- [Cost Optimization for Logs](https://aws.amazon.com/blogs/mt/cost-optimization-for-amazon-cloudwatch-logs/)

### Capacitación
- [AWS CloudWatch Workshop](https://catalog.workshops.aws/observability/)
- [OpenSearch Fundamentals](https://opensearch.org/docs/latest/)


## 🎯 Recomendación Final

**Opción Recomendada**: **Modernización Completa (Opción 1)**

### Razones:
1. ✅ **85% de ahorro** vs on-premise
2. ✅ **Integración nativa** con ecosistema AWS
3. ✅ **Escalabilidad automática** sin gestión
4. ✅ **Servicios managed** sin mantenimiento
5. ✅ **Búsqueda avanzada** con OpenSearch
6. ✅ **Alertas inteligentes** con ML

### Timeline: 4 semanas
### Inversión Inicial: ~$5,000 (setup y capacitación)
### Costo Mensual: ~$278/mes
### ROI: Positivo en 3 meses


## 📞 Próximos Pasos

1. **Aprobación de Propuesta**: Presentar a stakeholders
2. **Asignación de Recursos**: Equipo de migración
3. **Kick-off Meeting**: Alinear expectativas
4. **Inicio de Semana 1**: Análisis y diseño
5. **Go-Live**: Semana 4


**Documento preparado por**: Equipo de Arquitectura AWS  
**Fecha**: 11 de Diciembre, 2025  
**Versión**: 1.0
