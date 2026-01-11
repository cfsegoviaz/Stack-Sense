# API Portal Terraform Infrastructure

## Arquitectura

Esta configuración de Terraform despliega una arquitectura completa de API Portal en AWS:

- **VPC** con subnets públicas y privadas
- **API Gateway** como punto de entrada
- **Lambda** para lógica de negocio
- **RDS PostgreSQL** para base de datos
- **CloudFront** para CDN y caché
- **Security Groups** e **IAM roles** apropiados

## Uso

1. **Inicializar Terraform:**
```bash
cd terraform/api-portal
terraform init
```

2. **Crear archivo de variables:**
```bash
cp terraform.tfvars.example terraform.tfvars
# Editar terraform.tfvars con tus valores
```

3. **Planificar el despliegue:**
```bash
terraform plan
```

4. **Aplicar la infraestructura:**
```bash
terraform apply
```

## Variables requeridas

Crear `terraform.tfvars`:
```hcl
aws_region   = "us-east-1"
project_name = "mi-api-portal"
environment  = "dev"
db_password  = "tu-password-seguro"
```

## Outputs

- `api_gateway_url`: URL del API Gateway
- `cloudfront_domain`: Dominio de CloudFront
- `lambda_function_name`: Nombre de la función Lambda

## Limpieza

```bash
terraform destroy
```
