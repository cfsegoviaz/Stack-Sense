# Diagramas de Arquitectura AWS - MAP-BGR

Diagramas profesionales generados con `diagrams.py` para visualizar las arquitecturas propuestas.

---

## 🎯 Diagrama General

### Primera Ola de Migración

![Primera Ola General](primera_ola_general.png)

**Descripción**: Vista general de la primera ola de migración (Ola 0 - Piloto) con 3 aplicaciones y 12 VMs.

---

## 📱 Portales Web

### PortalAdmBGR

![PortalAdmBGR](arch_portaladmbgr.png)

**Componentes**: Route 53, CloudFront, WAF, ALB, EC2 Auto Scaling, RDS Multi-AZ, S3  
**Criticidad**: Alta  
**VMs**: 6 | **vCPUs**: 48 | **RAM**: 156 GB

---

### PortalGuiaBGR

![PortalGuiaBGR](arch_portalguiabgr.png)

**Componentes**: Route 53, CloudFront, WAF, ALB, EC2 Auto Scaling, RDS Multi-AZ, S3  
**Criticidad**: Alta  
**VMs**: 5 | **vCPUs**: 42 | **RAM**: 144 GB

---

### Api Portal

![Api Portal](arch_api_portal.png)

**Componentes**: Route 53, CloudFront, WAF, ALB, EC2 Auto Scaling, RDS Multi-AZ, S3  
**Criticidad**: Alta  
**VMs**: 5 | **vCPUs**: 42 | **RAM**: 144 GB

---

## 🏢 Aplicaciones Backoffice

### Backoffice Banca Digital

![Backoffice Banca Digital](arch_backoffice_banca_digital.png)

**Componentes**: Internal ALB, EC2, RDS Multi-AZ, EFS, VPN/Direct Connect  
**Criticidad**: Alta  
**VMs**: 3 | **vCPUs**: 10 | **RAM**: 20 GB

---

### Backoffice Sistemas

![Backoffice Sistemas](arch_backoffice_sistemas.png)

**Componentes**: Internal ALB, EC2, RDS Multi-AZ, EFS, VPN/Direct Connect  
**Criticidad**: Media  
**VMs**: 5 | **vCPUs**: 42 | **RAM**: 144 GB

---

## 🔧 Herramientas DevOps

### SonarQube

![SonarQube](arch_sonarqube.png)

**Componentes**: ALB, EC2 Auto Scaling, RDS PostgreSQL Multi-AZ, EBS  
**Criticidad**: Media  
**VMs**: 5 | **vCPUs**: 42 | **RAM**: 144 GB  
**Estimación**: $1,200/mes

**✅ Seleccionada para Ola 0 (Piloto)**

---

## 📊 Logging y Observabilidad

### Seq - Opción CloudWatch (Recomendada)

![Seq CloudWatch](arch_seq_cloudwatch.png)

**Componentes**: CloudWatch Logs, CloudWatch Insights, S3  
**Criticidad**: Media  
**VMs**: 5 | **vCPUs**: 42 | **RAM**: 144 GB  
**Estimación**: $300/mes  
**Ahorro**: 60% vs EC2

**✅ Seleccionada para Ola 0 (Piloto) - Opción CloudWatch**

---

### Seq - Opción EC2 (Alternativa)

![Seq EC2](arch_seq_ec2.png)

**Componentes**: NLB, EC2, EBS  
**Estimación**: $800/mes

---

## 📦 Aplicaciones Empresariales

### Saras

![Saras](arch_saras.png)

**Componentes**: EC2, RDS SQL Server Multi-AZ, EBS, VPN  
**Criticidad**: Media  
**VMs**: 2 | **vCPUs**: 12 | **RAM**: 18 GB  
**Estimación**: $600/mes

**✅ Seleccionada para Ola 0 (Piloto)**

---

## 📋 Resumen de Diagramas

| Diagrama | Archivo | Aplicación | Ola |
|----------|---------|------------|-----|
| Primera Ola General | `primera_ola_general.png` | - | Ola 0 |
| PortalAdmBGR | `arch_portaladmbgr.png` | Portal Web | Ola 3 |
| PortalGuiaBGR | `arch_portalguiabgr.png` | Portal Web | Ola 2 |
| Api Portal | `arch_api_portal.png` | API/Portal | Ola 2 |
| Backoffice Banca | `arch_backoffice_banca_digital.png` | Backoffice | Ola 1 |
| Backoffice Sistemas | `arch_backoffice_sistemas.png` | Backoffice | Ola 1 |
| SonarQube | `arch_sonarqube.png` | DevOps | **Ola 0** ✅ |
| Seq CloudWatch | `arch_seq_cloudwatch.png` | Logging | **Ola 0** ✅ |
| Seq EC2 | `arch_seq_ec2.png` | Logging | Alternativa |
| Saras | `arch_saras.png` | Empresarial | **Ola 0** ✅ |

---

## 🛠️ Generación de Diagramas

Los diagramas fueron generados usando `diagrams.py`:

```bash
python scripts/generate_diagrams.py
```

**Herramientas utilizadas:**
- Python 3.x
- diagrams library
- Graphviz

---

## 📐 Convenciones

**Colores y símbolos:**
- 🟦 Azul: Servicios AWS
- 🟩 Verde: Componentes on-premise
- ➡️ Flechas sólidas: Flujo de datos normal
- ⤏ Flechas punteadas: Migración/Sincronización

**Clusters:**
- AWS Cloud: Servicios en AWS
- VPC: Virtual Private Cloud
- Subnets: Públicas y privadas
- On-Premise: Infraestructura actual

---

**Última actualización**: 2025-12-01  
**Total diagramas**: 10  
**Generado por**: scripts/generate_diagrams.py
