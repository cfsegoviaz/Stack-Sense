# Configuración Auto Scaling Groups - BGR

**Fecha**: 2025-12-04  
**Aplicaciones**: Saras, SonarQube, API Portal, Portal Guía BGR

---

## 🎯 Principio de Diseño

**REGLA**: Todas las aplicaciones deben tener **mínimo 2 instancias EC2** distribuidas en Multi-AZ con Auto Scaling Group configurado.

**Razones**:
- Alta disponibilidad (si falla una AZ, la otra sigue funcionando)
- Distribución de carga
- Escalamiento automático según demanda
- Zero-downtime deployments

---

## 1. Saras - Aplicación Empresarial

### Configuración EC2
- **Tipo**: t3.medium (2 vCPU, 4 GB RAM)
- **Mínimo**: 2 instancias
- **Deseado**: 2 instancias
- **Máximo**: 4 instancias

### Auto Scaling Policies

**Scale Out (Aumentar instancias)**
```yaml
MetricName: CPUUtilization
Threshold: 70%
Duration: 5 minutos consecutivos
Action: +1 instancia
Cooldown: 300 segundos
```

**Scale In (Reducir instancias)**
```yaml
MetricName: CPUUtilization
Threshold: 30%
Duration: 10 minutos consecutivos
Action: -1 instancia
Cooldown: 600 segundos
```

**Métricas Adicionales**
```yaml
- Memory Utilization > 75% → +1 instancia
- Request Count > 1000/min → +1 instancia
- Target Tracking: Mantener CPU en 50%
```

### Health Checks
```yaml
Type: ELB
Grace Period: 300 segundos
Interval: 30 segundos
Unhealthy Threshold: 2
Healthy Threshold: 2
```

### Terraform/CloudFormation
```hcl
resource "aws_autoscaling_group" "saras" {
  name                = "bgr-saras-asg"
  min_size            = 2
  max_size            = 4
  desired_capacity    = 2
  health_check_type   = "ELB"
  health_check_grace_period = 300
  
  vpc_zone_identifier = [
    aws_subnet.private_az1.id,
    aws_subnet.private_az2.id
  ]
  
  target_group_arns = [aws_lb_target_group.saras.arn]
  
  launch_template {
    id      = aws_launch_template.saras.id
    version = "$Latest"
  }
  
  tag {
    key                 = "Name"
    value               = "bgr-saras"
    propagate_at_launch = true
  }
}

resource "aws_autoscaling_policy" "saras_scale_out" {
  name                   = "saras-scale-out"
  scaling_adjustment     = 1
  adjustment_type        = "ChangeInCapacity"
  cooldown              = 300
  autoscaling_group_name = aws_autoscaling_group.saras.name
}

resource "aws_autoscaling_policy" "saras_scale_in" {
  name                   = "saras-scale-in"
  scaling_adjustment     = -1
  adjustment_type        = "ChangeInCapacity"
  cooldown              = 600
  autoscaling_group_name = aws_autoscaling_group.saras.name
}

resource "aws_cloudwatch_metric_alarm" "saras_cpu_high" {
  alarm_name          = "saras-cpu-high"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = "2"
  metric_name         = "CPUUtilization"
  namespace           = "AWS/EC2"
  period              = "300"
  statistic           = "Average"
  threshold           = "70"
  alarm_actions       = [aws_autoscaling_policy.saras_scale_out.arn]
  
  dimensions = {
    AutoScalingGroupName = aws_autoscaling_group.saras.name
  }
}

resource "aws_cloudwatch_metric_alarm" "saras_cpu_low" {
  alarm_name          = "saras-cpu-low"
  comparison_operator = "LessThanThreshold"
  evaluation_periods  = "2"
  metric_name         = "CPUUtilization"
  namespace           = "AWS/EC2"
  period              = "600"
  statistic           = "Average"
  threshold           = "30"
  alarm_actions       = [aws_autoscaling_policy.saras_scale_in.arn]
  
  dimensions = {
    AutoScalingGroupName = aws_autoscaling_group.saras.name
  }
}
```

---

## 2. SonarQube - Herramienta DevOps

### Configuración EC2
- **Tipo**: t3.large (2 vCPU, 8 GB RAM)
- **Mínimo**: 2 instancias
- **Deseado**: 2 instancias
- **Máximo**: 4 instancias

### Auto Scaling Policies

**Scale Out**
```yaml
MetricName: CPUUtilization
Threshold: 75%
Duration: 5 minutos consecutivos
Action: +1 instancia
Cooldown: 300 segundos
```

**Scale In**
```yaml
MetricName: CPUUtilization
Threshold: 35%
Duration: 15 minutos consecutivos
Action: -1 instancia
Cooldown: 900 segundos
```

**Métricas Adicionales**
```yaml
- Memory Utilization > 80% → +1 instancia
- Active Analysis Jobs > 5 → +1 instancia
```

### Consideraciones Especiales
- **EFS**: Datos compartidos entre instancias
- **Session Affinity**: Sticky sessions en ALB (1 hora)
- **Warm-up**: 600 segundos para nueva instancia

---

## 3. API Portal - Alta Criticidad

### Configuración EC2
- **Tipo**: t3.medium (2 vCPU, 4 GB RAM)
- **Mínimo**: 2 instancias
- **Deseado**: 3 instancias
- **Máximo**: 8 instancias

### Auto Scaling Policies

**Target Tracking (Recomendado)**
```yaml
TargetValue: 50% CPU
ScaleOut: Cuando CPU > 50% por 3 minutos
ScaleIn: Cuando CPU < 50% por 15 minutos
```

**Step Scaling (Agresivo)**
```yaml
CPU 50-70%: +1 instancia
CPU 70-85%: +2 instancias
CPU > 85%: +3 instancias

CPU < 30%: -1 instancia (después de 15 min)
CPU < 20%: -2 instancias (después de 20 min)
```

**Scheduled Scaling**
```yaml
# Horario laboral (8am-6pm)
Lunes-Viernes 7:45am: Desired = 4
Lunes-Viernes 6:15pm: Desired = 2

# Fin de semana
Sábado-Domingo: Desired = 2
```

**Predictive Scaling**
```yaml
Enabled: true
Mode: ForecastAndScale
SchedulingBuffer: 10 minutos
```

### Métricas Adicionales
```yaml
- Request Count > 2000/min → +1 instancia
- Response Time > 500ms → +1 instancia
- 5xx Errors > 10/min → Alarm (no scale)
- ALB Target Response Time > 1s → +1 instancia
```

### Terraform
```hcl
resource "aws_autoscaling_group" "api_portal" {
  name                = "bgr-api-portal-asg"
  min_size            = 2
  max_size            = 8
  desired_capacity    = 3
  health_check_type   = "ELB"
  health_check_grace_period = 300
  
  vpc_zone_identifier = [
    aws_subnet.private_az1.id,
    aws_subnet.private_az2.id
  ]
  
  target_group_arns = [aws_lb_target_group.api_portal.arn]
  
  launch_template {
    id      = aws_launch_template.api_portal.id
    version = "$Latest"
  }
  
  enabled_metrics = [
    "GroupDesiredCapacity",
    "GroupInServiceInstances",
    "GroupMinSize",
    "GroupMaxSize",
    "GroupTotalInstances"
  ]
  
  tag {
    key                 = "Name"
    value               = "bgr-api-portal"
    propagate_at_launch = true
  }
}

resource "aws_autoscaling_policy" "api_portal_target_tracking" {
  name                   = "api-portal-target-tracking"
  policy_type            = "TargetTrackingScaling"
  autoscaling_group_name = aws_autoscaling_group.api_portal.name
  
  target_tracking_configuration {
    predefined_metric_specification {
      predefined_metric_type = "ASGAverageCPUUtilization"
    }
    target_value = 50.0
  }
}

resource "aws_autoscaling_policy" "api_portal_request_count" {
  name                   = "api-portal-request-count"
  policy_type            = "TargetTrackingScaling"
  autoscaling_group_name = aws_autoscaling_group.api_portal.name
  
  target_tracking_configuration {
    predefined_metric_specification {
      predefined_metric_type = "ALBRequestCountPerTarget"
      resource_label         = "${aws_lb.main.arn_suffix}/${aws_lb_target_group.api_portal.arn_suffix}"
    }
    target_value = 1000.0
  }
}

# Scheduled Scaling - Horario laboral
resource "aws_autoscaling_schedule" "api_portal_morning" {
  scheduled_action_name  = "scale-up-morning"
  min_size              = 2
  max_size              = 8
  desired_capacity      = 4
  recurrence            = "45 7 * * 1-5"
  autoscaling_group_name = aws_autoscaling_group.api_portal.name
}

resource "aws_autoscaling_schedule" "api_portal_evening" {
  scheduled_action_name  = "scale-down-evening"
  min_size              = 2
  max_size              = 8
  desired_capacity      = 2
  recurrence            = "15 18 * * 1-5"
  autoscaling_group_name = aws_autoscaling_group.api_portal.name
}
```

---

## 4. Portal Guía BGR - Alta Criticidad

### Configuración EC2
- **Tipo**: t3.medium (2 vCPU, 4 GB RAM)
- **Mínimo**: 2 instancias
- **Deseado**: 3 instancias
- **Máximo**: 8 instancias

### Auto Scaling Policies

**Idéntico a API Portal** (misma criticidad y patrones de uso)

**Target Tracking**
```yaml
TargetValue: 50% CPU
```

**Step Scaling**
```yaml
CPU 50-70%: +1 instancia
CPU 70-85%: +2 instancias
CPU > 85%: +3 instancias
```

**Scheduled Scaling**
```yaml
Lunes-Viernes 7:45am: Desired = 4
Lunes-Viernes 6:15pm: Desired = 2
Fin de semana: Desired = 2
```

---

## 📊 Comparativa de Configuraciones

| Aplicación | Tipo EC2 | Min | Desired | Max | CPU Target | Costo Base |
|------------|----------|-----|---------|-----|------------|------------|
| **Saras** | t3.medium | 2 | 2 | 4 | 50% | $120/mes |
| **SonarQube** | t3.large | 2 | 2 | 4 | 50% | $300/mes |
| **API Portal** | t3.medium | 2 | 3 | 8 | 50% | $180/mes |
| **Portal Guía** | t3.medium | 2 | 3 | 8 | 50% | $180/mes |

**Nota**: Costos base con instancias "Desired". Puede aumentar con auto-scaling.

---

## 🎯 Mejores Prácticas

### 1. Health Checks
```yaml
ALB Health Check:
  Path: /health
  Interval: 30 segundos
  Timeout: 5 segundos
  Healthy Threshold: 2
  Unhealthy Threshold: 2
  
ASG Health Check:
  Type: ELB
  Grace Period: 300 segundos
```

### 2. Instance Warm-up
```yaml
Default: 300 segundos
SonarQube: 600 segundos (más pesado)
```

### 3. Termination Policies
```yaml
Priority:
  1. OldestInstance
  2. Default (balance across AZs)
```

### 4. Lifecycle Hooks
```yaml
PreTermination:
  - Drain connections (60 segundos)
  - Deregister from service discovery
  - Complete in-flight requests
  
PostLaunch:
  - Wait for health checks
  - Register in service discovery
  - Warm-up cache
```

### 5. Monitoring
```yaml
CloudWatch Metrics:
  - GroupDesiredCapacity
  - GroupInServiceInstances
  - GroupMinSize
  - GroupMaxSize
  - GroupTotalInstances
  
Alarms:
  - Desired != InService (por > 10 min)
  - Scaling activities fallidas
  - Instancias unhealthy
```

---

## 💰 Impacto en Costos

### Antes (1 instancia sin ASG)
```
Saras: 1x t3.large = $60/mes
SonarQube: 1x t3.xlarge = $150/mes
API Portal: 1x t3.large = $60/mes
Portal Guía: 1x t3.large = $60/mes
```

### Después (2+ instancias con ASG)
```
Saras: 2x t3.medium = $120/mes (base)
SonarQube: 2x t3.large = $300/mes (base)
API Portal: 3x t3.medium = $180/mes (base)
Portal Guía: 3x t3.medium = $180/mes (base)
```

### Beneficios
✅ Alta disponibilidad (Multi-AZ)
✅ Escalamiento automático
✅ Zero-downtime deployments
✅ Mejor distribución de carga
✅ Instancias más pequeñas = mejor costo/performance

---

## 🚀 Implementación

### Orden de Despliegue
1. Crear Launch Template
2. Crear Auto Scaling Group
3. Configurar Target Tracking policies
4. Configurar Step Scaling policies (opcional)
5. Configurar Scheduled Scaling
6. Configurar CloudWatch Alarms
7. Probar scaling manualmente
8. Validar health checks
9. Probar deployment con CodeDeploy

### Validación
```bash
# Ver estado del ASG
aws autoscaling describe-auto-scaling-groups \
  --auto-scaling-group-names bgr-api-portal-asg

# Ver actividades de scaling
aws autoscaling describe-scaling-activities \
  --auto-scaling-group-name bgr-api-portal-asg \
  --max-records 20

# Forzar scale out (testing)
aws autoscaling set-desired-capacity \
  --auto-scaling-group-name bgr-api-portal-asg \
  --desired-capacity 4

# Ver métricas
aws cloudwatch get-metric-statistics \
  --namespace AWS/EC2 \
  --metric-name CPUUtilization \
  --dimensions Name=AutoScalingGroupName,Value=bgr-api-portal-asg \
  --start-time 2025-12-04T00:00:00Z \
  --end-time 2025-12-04T23:59:59Z \
  --period 3600 \
  --statistics Average
```

---

**Última actualización**: 2025-12-04  
**Estado**: Configuración definida
