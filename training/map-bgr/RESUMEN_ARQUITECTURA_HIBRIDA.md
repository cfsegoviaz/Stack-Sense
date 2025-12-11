# Resumen Ejecutivo - Arquitectura Híbrida BGR

**Fecha**: 2025-12-04  
**Decisión**: Bases de datos permanecen on-premise

---

## 🎯 Cambio Arquitectónico

### Decisión del Cliente
BGR ha manifestado que **las bases de datos deberán continuar on-premise** por temas de dependencias existentes.

### Impacto
- ✅ Aplicaciones migran a AWS (EC2, ALB, S3, ElastiCache)
- ❌ Bases de datos permanecen on-premise (SQL Server, PostgreSQL)
- ✅ Conectividad híbrida: Direct Connect + VPN

---

## 📊 Comparativa de Costos

### Antes (Todo en AWS con RDS)
| Aplicación | Costo Mensual |
|------------|---------------|
| Saras | $625 |
| SonarQube | $1,225 |
| API Portal | $2,830 |
| Portal Guía | $2,830 |
| **TOTAL** | **$7,510/mes** |

### Ahora (Híbrido - BD On-Premise)
| Aplicación | Costo Mensual | Ahorro |
|------------|---------------|--------|
| Saras | $296 | -$329 |
| SonarQube | $511 | -$714 |
| API Portal | $1,387 | -$1,443 |
| Portal Guía | $1,386 | -$1,444 |
| **TOTAL** | **$3,580/mes** | **-$3,930/mes** |

### Balance
- **Ahorro mensual**: $3,930/mes (52% reducción)
- **Ahorro anual**: $47,160/año
- **Con Reserved Instances**: $3,196/mes (ahorro adicional de $384/mes)

---

## 🏗️ Arquitectura Híbrida

### Componentes en AWS
✅ EC2 Auto Scaling Groups (Multi-AZ)  
✅ Application Load Balancers  
✅ ElastiCache Redis (API Portal, Portal Guía)  
✅ CloudFront + WAF (aplicaciones críticas)  
✅ S3 + EFS para storage  
✅ CodeDeploy para CI/CD  
✅ CloudWatch + X-Ray para monitoring  

### Componentes On-Premise
✅ SQL Server (Saras, API Portal, Portal Guía)  
✅ PostgreSQL (SonarQube)  
✅ Infraestructura de BD existente  

### Conectividad Híbrida
✅ **AWS Direct Connect 1 Gbps** (primario)  
  - Latencia: < 10ms  
  - Ancho de banda dedicado  
  - SLA 99.95%  
  - Costo: $228/mes + $0.02/GB  

✅ **VPN Site-to-Site** (backup)  
  - 2 túneles IPSec  
  - Failover automático  
  - Costo: $73/mes  

✅ **Virtual Private Gateway** en VPC  
✅ **Customer Gateway** on-premise  

**Costo total conectividad**: $401/mes (compartido entre 4 aplicaciones)

---

## 📈 Desglose de Costos por Aplicación

### 1. Saras ($296/mes)
- EC2: $120
- Networking: $45
- Storage: $10
- Híbrido: $75
- Otros: $46

### 2. SonarQube ($511/mes)
- EC2: $300
- Networking: $45
- Storage: $45 (EFS + S3)
- Híbrido: $75
- Otros: $46

### 3. API Portal ($1,387/mes)
- EC2: $180
- Networking: $425 (CloudFront, API GW, WAF)
- Cache: $150
- Storage: $45
- Híbrido: $75
- Otros: $87

### 4. Portal Guía ($1,386/mes)
- EC2: $180
- Networking: $400 (CloudFront, WAF)
- Cache: $200
- Storage: $45
- Híbrido: $76
- Otros: $82

---

## ✅ Beneficios de la Arquitectura Híbrida

### Financieros
- ✅ **52% reducción** en costos AWS
- ✅ **$47,160/año** de ahorro
- ✅ No requiere migración de BD
- ✅ No requiere re-licenciamiento SQL Server

### Técnicos
- ✅ Mantiene dependencias existentes
- ✅ No requiere refactoring de aplicaciones
- ✅ Latencia < 10ms con Direct Connect
- ✅ Alta disponibilidad (Direct Connect + VPN)
- ✅ Escalabilidad en compute (AWS)

### Operacionales
- ✅ Equipo de BD mantiene control
- ✅ Procesos de backup existentes
- ✅ Compliance on-premise preservado
- ✅ Migración por fases más simple

---

## ⚠️ Consideraciones y Riesgos

### Latencia
- **Direct Connect**: < 10ms ✅
- **VPN**: 20-50ms ⚠️
- **Crítico**: Queries frecuentes a BD

### Dependencia de Conectividad
- **Riesgo**: Si falla Direct Connect y VPN
- **Mitigación**: Redundancia automática
- **SLA**: 99.95% (Direct Connect)

### Ancho de Banda
- **1 Gbps**: Suficiente para 4 apps
- **Monitoreo**: Alertas > 70% utilización
- **Escalamiento**: Upgrade a 10 Gbps si necesario

### Performance
- **Connection Pooling**: Obligatorio
- **Caching Agresivo**: ElastiCache crítico
- **Query Optimization**: Reducir round-trips

---

## 📋 Plan de Implementación

### Fase 1: Conectividad (Semanas 1-4)
- [ ] Solicitar Direct Connect (lead time: 2-4 semanas)
- [ ] Configurar Customer Gateway on-premise
- [ ] Crear Virtual Private Gateway en AWS
- [ ] Establecer VPN Site-to-Site (backup)
- [ ] Probar conectividad y latencia
- [ ] Configurar monitoring

### Fase 2: Infraestructura AWS (Semanas 3-5)
- [ ] Crear VPC y subnets
- [ ] Configurar Security Groups
- [ ] Provisionar ALBs
- [ ] Configurar Auto Scaling Groups
- [ ] Setup S3, EFS, ElastiCache
- [ ] Configurar CodeDeploy

### Fase 3: Migración Piloto (Semanas 6-10)
- [ ] Migrar Saras (aplicación simple)
- [ ] Migrar SonarQube (herramienta interna)
- [ ] Validar performance con BD on-premise
- [ ] Ajustar connection pooling
- [ ] Optimizar queries

### Fase 4: Migración Producción (Semanas 11-16)
- [ ] Migrar API Portal
- [ ] Migrar Portal Guía BGR
- [ ] Monitoreo intensivo 24/7
- [ ] Validación con usuarios
- [ ] Desmantelar VMs on-premise

---

## 🎯 Métricas de Éxito

### Performance
- ✅ Latencia DB < 10ms (p95)
- ✅ Response time < 500ms (p95)
- ✅ Availability > 99.9%

### Costos
- ✅ Costo mensual < $3,600
- ✅ Ahorro > $3,900/mes vs RDS
- ✅ ROI < 6 meses

### Operacional
- ✅ Zero downtime en migración
- ✅ Deployments < 15 minutos
- ✅ Rollback < 5 minutos

---

## 📁 Documentos Relacionados

1. **REGLAS_PROYECTO_BGR.md** - Reglas de arquitectura y deployment
2. **AUTO_SCALING_CONFIG.md** - Configuración detallada de ASG
3. **CALCULADORA_COSTOS_HIBRIDA.md** - Desglose completo de costos
4. **ARQUITECTURAS_AWS.md** - Arquitecturas detalladas por aplicación
5. **diagrams/** - Diagramas de arquitectura actualizados

---

## 🚀 Próximos Pasos Inmediatos

1. ✅ Arquitecturas híbridas definidas
2. ✅ Diagramas actualizados
3. ✅ Calculadora de costos actualizada
4. ⏳ **Aprobar arquitectura híbrida con BGR**
5. ⏳ **Solicitar Direct Connect (urgente - 2-4 semanas lead time)**
6. ⏳ Configurar VPN Site-to-Site
7. ⏳ Provisionar infraestructura AWS
8. ⏳ Iniciar migración piloto

---

**Última actualización**: 2025-12-04  
**Estado**: Arquitectura híbrida definida y documentada  
**Decisión**: Bases de datos permanecen on-premise
