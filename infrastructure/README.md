# API Portal - Infrastructure as Code

Infraestructura como código para la modernización del API Portal BGR usando AWS CDK.

## 📋 Información de la Aplicación

- **Nombre**: API Portal BGR
- **Descripción**: Portal estático de APIs que define entrada y salida de peticiones
- **Stack Actual**: ASP.NET C# (.NET Framework 4.7.1) + SQL Server 2016
- **Arquitectura Objetivo**: Contenedores en AWS ECS Fargate + RDS SQL Server
- **Responsable**: Erik Palma (erik.palma@bgr.com.ec)

## 🏗️ Arquitectura AWS

### Componentes Principales

1. **VPC Multi-AZ**
   - Subnets públicas, privadas y de base de datos
   - NAT Gateway para conectividad saliente
   - Security Groups con principio de menor privilegio

2. **ECS Fargate**
   - Contenedores sin servidor
   - Auto Scaling basado en CPU y memoria
   - Health checks y logging integrado

3. **Application Load Balancer**
   - Terminación SSL/TLS
   - Redirección HTTP a HTTPS
   - Distribución de tráfico

4. **RDS SQL Server**
   - SQL Server Express Edition
   - Multi-AZ para producción
   - Backups automáticos
   - Encriptación en reposo

5. **CloudFront CDN**
   - Distribución global de contenido
   - Cache optimizado
   - Integración con S3 para assets estáticos

6. **S3**
   - Almacenamiento de assets estáticos
   - Versionado habilitado
   - Encriptación S3-managed

## 🚀 Despliegue

### Prerrequisitos

```bash
# Instalar dependencias
npm install

# Configurar credenciales AWS
aws configure

# Bootstrap CDK (solo primera vez)
npm run bootstrap
```

### Comandos de Despliegue

```bash
# Desarrollo
npm run deploy:dev

# Producción
npm run deploy:prod

# Ver diferencias antes del despliegue
npm run diff:dev
npm run diff:prod

# Generar templates CloudFormation
npm run synth
```

### Variables de Entorno

```bash
# Requeridas
export CDK_DEFAULT_ACCOUNT=123456789012
export CDK_DEFAULT_REGION=us-east-1

# Opcionales para producción
export DOMAIN_NAME=api-portal.bgr.com.ec
export CERTIFICATE_ARN=arn:aws:acm:us-east-1:123456789012:certificate/xxx
```

## 🔧 Configuración por Ambiente

### Desarrollo
- **Instancias**: 1 ECS task, RDS t3.medium
- **Multi-AZ**: Deshabilitado
- **Auto Scaling**: 1-3 tasks
- **Retención logs**: 30 días

### Producción
- **Instancias**: 2+ ECS tasks, RDS con Multi-AZ
- **Auto Scaling**: 2-10 tasks
- **Deletion Protection**: Habilitado
- **Dominio personalizado**: api-portal.bgr.com.ec

## 💰 Estimación de Costos (us-east-1)

### Desarrollo (~$180/mes)
- ECS Fargate: ~$35/mes (1 task, 1 vCPU, 2GB RAM)
- RDS SQL Server Express: ~$25/mes (t3.medium)
- ALB: ~$22/mes
- NAT Gateway: ~$45/mes
- CloudFront: ~$1/mes (bajo tráfico)
- S3: ~$5/mes
- Otros (logs, secrets): ~$10/mes

### Producción (~$450/mes)
- ECS Fargate: ~$140/mes (2-4 tasks promedio)
- RDS SQL Server Express Multi-AZ: ~$180/mes
- ALB: ~$22/mes
- NAT Gateway: ~$45/mes
- CloudFront: ~$15/mes (tráfico medio)
- S3: ~$15/mes
- Otros (logs, secrets, backups): ~$25/mes

## 🔒 Seguridad

- **Encriptación**: En tránsito (TLS 1.2+) y en reposo
- **Network**: VPC aislada, Security Groups restrictivos
- **Secrets**: AWS Secrets Manager para credenciales DB
- **Access**: IAM roles con permisos mínimos
- **Monitoring**: CloudWatch logs y métricas

## 📊 Monitoreo

### Métricas Clave
- CPU y memoria utilization (ECS)
- Response time y error rate (ALB)
- Database connections y performance (RDS)
- Cache hit ratio (CloudFront)

### Alarmas Configuradas
- High CPU utilization (>80%)
- High memory utilization (>85%)
- Database connection errors
- Application errors (5xx responses)

## 🔄 Estrategia de Migración

### Fase 1: Preparación
1. Modernizar aplicación a .NET 6/8
2. Containerizar aplicación
3. Migrar base de datos a RDS

### Fase 2: Despliegue
1. Desplegar infraestructura en desarrollo
2. Pruebas de funcionalidad y performance
3. Despliegue en producción con blue/green

### Fase 3: Optimización
1. Ajustar auto scaling basado en métricas reales
2. Optimizar cache de CloudFront
3. Implementar CI/CD pipeline

## 🛠️ Comandos Útiles

```bash
# Ver recursos desplegados
aws cloudformation describe-stacks --stack-name ApiPortalDevStack

# Conectar a base de datos
aws rds describe-db-instances --db-instance-identifier api-portal-dev

# Ver logs de aplicación
aws logs tail /aws/ecs/api-portal-dev --follow

# Escalar manualmente
aws ecs update-service --cluster api-portal-dev --service api-portal-dev --desired-count 3
```

## 📚 Referencias

- [AWS CDK Documentation](https://docs.aws.amazon.com/cdk/)
- [ECS Fargate Best Practices](https://docs.aws.amazon.com/AmazonECS/latest/bestpracticesguide/)
- [RDS SQL Server Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html)
- [CloudFront Performance](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ConfiguringCaching.html)

## 🆘 Troubleshooting

### Problemas Comunes

1. **ECS Task no inicia**
   ```bash
   aws ecs describe-services --cluster api-portal-dev --services api-portal-dev
   aws logs tail /aws/ecs/api-portal-dev --follow
   ```

2. **Base de datos no conecta**
   ```bash
   aws rds describe-db-instances
   # Verificar Security Groups y subnets
   ```

3. **ALB health check falla**
   ```bash
   aws elbv2 describe-target-health --target-group-arn <arn>
   ```

4. **CloudFront cache issues**
   ```bash
   aws cloudfront create-invalidation --distribution-id <id> --paths "/*"
   ```