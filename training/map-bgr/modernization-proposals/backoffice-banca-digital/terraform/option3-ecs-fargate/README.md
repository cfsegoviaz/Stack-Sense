# Opción 3: ECS Fargate - Terraform (Recomendada)

## Arquitectura
- ECS Fargate (2 tasks, 2 vCPU, 4 GB)
- Application Load Balancer
- ECR (Container Registry)
- ElastiCache Redis
- Secrets Manager
- Auto Scaling (2-4 tasks)

## Costo Estimado: $295.80/mes (75% ahorro)

## Despliegue

```bash
# Inicializar
terraform init

# Planificar
terraform plan

# Aplicar
terraform apply

# Build y push de imagen Docker
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com
docker build -t backoffice-banca-digital .
docker tag backoffice-banca-digital:latest ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/backoffice-banca-digital:latest
docker push ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/backoffice-banca-digital:latest
```

## Variables Principales

| Variable | Default | Descripción |
|----------|---------|-------------|
| aws_region | us-east-1 | Región AWS |
| container_image | - | URI de imagen ECR |
| rds_endpoint | db-bancadigitalprod... | RDS existente |

## Dockerfile Ejemplo

```dockerfile
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS base
WORKDIR /app
EXPOSE 80

FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src
COPY . .
RUN dotnet publish -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=build /app/publish .
ENTRYPOINT ["dotnet", "BackofficeBancaDigital.dll"]
```

## Post-Despliegue

1. Actualizar secret en Secrets Manager con connection string real
2. Configurar VPN/Direct Connect
3. Forzar nuevo deployment de ECS
