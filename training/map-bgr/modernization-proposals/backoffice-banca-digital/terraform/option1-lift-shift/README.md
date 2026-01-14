# Opción 1: Lift & Shift - Terraform

## Arquitectura
- 2x EC2 t3.xlarge (Windows Server 2016)
- Application Load Balancer
- EBS gp3 (200 GB)
- VPN Gateway (conectividad híbrida)

## Costo Estimado: $547.91/mes

## Despliegue

```bash
# Inicializar
terraform init

# Planificar
terraform plan

# Aplicar
terraform apply
```

## Variables Principales

| Variable | Default | Descripción |
|----------|---------|-------------|
| aws_region | us-east-1 | Región AWS |
| environment | prod | Ambiente |
| vpc_cidr | 10.100.0.0/16 | CIDR del VPC |
| onprem_cidr | 172.20.0.0/16 | CIDR on-premise |

## Post-Despliegue

1. Configurar Customer Gateway para VPN
2. Instalar aplicación .NET Core 8 en EC2
3. Configurar IIS
4. Actualizar connection strings
