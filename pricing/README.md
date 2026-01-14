# Escala24x7 - Matriz de Esfuerzos de Implementación

## Descripción
Matriz transversal de esfuerzos (horas) para implementación de infraestructura AWS por el equipo de Escala24x7.

## Archivo Principal
- `escala24x7_effort_matrix.json` - Matriz completa en formato JSON

## Uso en Análisis

Al analizar una aplicación, consultar este archivo para calcular:

```
Costo Implementación = Σ(horas por tarea) × tarifa_hora
```

## Categorías Disponibles

| Categoría | Descripción |
|-----------|-------------|
| compute | EC2, ECS, EKS, Lambda, Fargate |
| containers | ECR, Kubernetes |
| database | RDS, Aurora, DynamoDB, ElastiCache |
| storage | S3, EFS, FSx |
| networking | VPC, ALB, NLB, VPN, Direct Connect |
| security | WAF, Secrets Manager, Cognito |
| integration | API Gateway, SNS, SQS, EventBridge |
| monitoring | CloudWatch |
| migration | MGN, DRS, DMS |
| devops | Pipelines CI/CD |
| data_analytics | Glue, Athena, QuickSight |
| ai_ml | Bedrock, SageMaker, Comprehend |

## Ejemplo de Cálculo

**Backoffice Banca Digital - ECS Fargate:**

| Tarea | Horas |
|-------|-------|
| VPC/Redes [Terraform] | 8 |
| Fargate Cluster [Terraform] | 4 |
| Fargate Service [Terraform] | 8 |
| ALB [Terraform] | 4 |
| ECR | 1 |
| Elasticache Cluster [Terraform] | 8 |
| Secrets Manager [Terraform] | 2 |
| VPN [Terraform] | 32 |
| Azure DevOps infrastructure pipeline (Terraform) | 24 |
| **TOTAL** | **91 horas** |

Con tarifa de $150/hora = **$13,650 USD** implementación

## Notas
- Tareas con `[Terraform]` incluyen IaC
- Campo `team` indica equipo especializado requerido
- Horas son estimados base, pueden variar por complejidad
