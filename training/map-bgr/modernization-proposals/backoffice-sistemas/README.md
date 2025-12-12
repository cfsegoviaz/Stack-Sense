# Backoffice Sistemas BGR - Modernization Proposal

**Aplicación**: Backoffice Sistemas BGR  
**Estrategia**: Lift & Shift con Arquitectura Híbrida  
**Estado**: DRAFT - Pendiente de aprobación  
**Fecha**: 2025-12-12  
**Responsable**: Erik Palma (erik.palma@bgr.com.ec)

---

## 📋 Resumen Ejecutivo

Propuesta de migración de la aplicación **Backoffice Sistemas BGR** a AWS utilizando una estrategia de **Lift & Shift** con **arquitectura híbrida**. La aplicación se migrará a AWS mientras la base de datos permanece on-premise, cumpliendo con las reglas del proyecto BGR.

### Métricas Clave

| Métrica | Valor |
|---------|-------|
| **Timeline** | 3 semanas |
| **Costo Mensual** | $548.35 (inicial) → $621.19 (optimizado) |
| **Ahorro vs On-Premise** | 37% ($279/mes) |
| **Usuarios Impactados** | 685 colaboradores BGR |
| **Disponibilidad Target** | 99.9% |
| **Criticidad** | ALTA |

---

## 📁 Documentos del Proyecto

### 1. [BACKOFFICE_SISTEMAS_MODERNIZATION.md](./BACKOFFICE_SISTEMAS_MODERNIZATION.md)
Documento principal con:
- Información detallada de la aplicación
- Arquitectura AWS propuesta
- **Diagrama de arquitectura híbrida** (generado con AWS Diagrams)
- Componentes y configuraciones
- Integración CI/CD con Azure DevOps

**Diagrama**: [backoffice_sistemas_hybrid_architecture.png](./diagrams/backoffice_sistemas_hybrid_architecture.png)

### 2. [PLAN_MIGRACION.md](./PLAN_MIGRACION.md)
Plan detallado de migración con:
- Timeline de 3 semanas
- Actividades día a día
- Checklist completo
- Riesgos y mitigaciones
- Criterios de éxito
- Plan de rollback

### 3. [ESTIMACION_COSTOS.md](./ESTIMACION_COSTOS.md)
Análisis financiero completo con:
- Desglose detallado de costos
- Comparativa On-Premise vs AWS
- Optimizaciones recomendadas
- Proyección a 3 años
- ROI y ahorros

### 4. [ARQUITECTURA_DETALLADA.md](./ARQUITECTURA_DETALLADA.md)
Documentación técnica detallada con:
- Explicación completa del diagrama de arquitectura
- Especificaciones de cada componente AWS
- Configuraciones de conectividad híbrida
- Flujos de datos detallados
- Security Groups e IAM Roles
- SLAs y alta disponibilidad

---

## 🎯 Información de la Aplicación

### Descripción
Aplicación parametrizadora para diversos sistemas del banco BGR. Permite la gestión centralizada de configuraciones y parámetros para múltiples aplicaciones del ecosistema bancario.

### Infraestructura Actual

**Servidores de Aplicación**:
- ECBRPRW44: 4 vCPU, 20 GB RAM, Windows Server 2016
- ECBRPRW45: 8 vCPU, 20 GB RAM, Windows Server 2016

**Base de Datos** (On-Premise):
- ECBRPRCL13: 24 vCPU, 80 GB RAM, SQL Server 2016 Enterprise

**Stack Tecnológico**:
- Frontend: ASP.NET C# (.NET Framework 4.7.1)
- Backend: C# (.NET Framework 4.7.1)
- Base de Datos: SQL Server 2016 Enterprise (On-Premise)

### Dependencias Críticas
- Base de datos: PORTAL_ADMINISTRATIVO_BGR (compartida)
- Microservicio: BGRCELULAR (Notificador)
- Identidades: Active Directory (LDAP)
- Configuración: Tcs.ServicioConfiguracionBGR.WS

---

## 🏗️ Arquitectura Propuesta

### Modelo: Arquitectura Híbrida

**Componentes en AWS**:
- 2x EC2 t3.xlarge (4 vCPU, 16 GB RAM)
- Application Load Balancer (ALB)
- VPC con subnets públicas y privadas (2 AZs)
- Direct Connect (1 Gbps) + VPN backup
- CloudWatch monitoring
- S3 para artifacts y backups

**Componentes On-Premise**:
- SQL Server 2016 Enterprise (ECBRPRCL13)
- Active Directory (LDAP)
- Microservicio Notificador

### Conectividad Híbrida

```
AWS VPC ←→ Direct Connect (1 Gbps) ←→ On-Premise Datacenter
         ←→ VPN Site-to-Site (backup) ←→
```

**Latencia Target**: < 10ms  
**Ancho de Banda**: 1 Gbps  
**Redundancia**: Direct Connect + VPN backup

---

## 💰 Costos Estimados

### Costo Mensual (Optimizado)

| Categoría | Costo |
|-----------|-------|
| Compute (Reserved) | $146.00 |
| Networking | $372.73 |
| Storage | $38.55 |
| Monitoring | $5.80 |
| CI/CD | $1.64 |
| **Total** | **$564.72** |
| Contingencia (10%) | $56.47 |
| **TOTAL MENSUAL** | **$621.19** |

### Comparativa vs On-Premise

| Modelo | Costo Mensual | Ahorro |
|--------|---------------|--------|
| On-Premise | $760.00 | - |
| AWS (Optimizado) | $480.99 | $279.01 (37%) |

### Proyección a 3 Años

| Año | Costo Anual | Optimizaciones |
|-----|-------------|----------------|
| Año 1 | $5,196.00 | Reserved Instances |
| Año 2 | $3,624.00 | Auto Scaling |
| Año 3 | $1,800.00 | Serverless |
| **Total** | **$10,620.00** | **Ahorro: $3,208** |

---

## 🚀 Timeline de Migración

### Semana 1: Infraestructura
- Días 1-2: Conectividad híbrida (Direct Connect + VPN)
- Días 3-4: Infraestructura AWS (VPC, ALB, Security Groups)
- Día 5: Compute y Storage (EC2, EBS, S3)

### Semana 2: Aplicación y Testing
- Días 1-2: Despliegue de aplicación
- Día 3: Configuración CI/CD (Azure DevOps + CodeDeploy)
- Día 4: Testing funcional
- Día 5: Configuración de monitoreo

### Semana 3: Go-Live
- Día 1: Preparación go-live
- Día 2: Cutover (Sábado - ventana de mantenimiento)
- Días 3-4: Monitoreo post-deploy
- Día 5: Documentación y handover

---

## ⚠️ Riesgos Principales

### 1. Latencia en Conectividad Híbrida
**Impacto**: ALTO  
**Mitigación**: Direct Connect (1 Gbps), connection pooling, monitoreo en tiempo real

### 2. Falla en Autenticación LDAP
**Impacto**: CRÍTICO  
**Mitigación**: Testing exhaustivo, circuit breaker, plan de rollback

### 3. Falla en Direct Connect
**Impacto**: CRÍTICO  
**Mitigación**: VPN Site-to-Site como backup, failover automático

### 4. Problemas en Cutover
**Impacto**: ALTO  
**Mitigación**: Ensayo previo, plan de rollback < 30 min, equipo completo disponible

---

## ✅ Criterios de Éxito

1. ✅ Aplicación funcionando en AWS sin errores críticos
2. ✅ Performance igual o mejor (latencia < 2s)
3. ✅ Disponibilidad > 99.9%
4. ✅ Conectividad híbrida estable (latencia < 10ms)
5. ✅ Zero data loss durante migración
6. ✅ Usuarios satisfechos (> 90% feedback positivo)
7. ✅ CI/CD operativo
8. ✅ Monitoreo completo
9. ✅ Documentación completa
10. ✅ Costo dentro del presupuesto

---

## 🔧 Integración CI/CD

### Azure DevOps + AWS CodeDeploy

**Flujo de Deployment**:
```
Developer Push → Azure Repos
       ↓
Azure Pipeline (Build + Test)
       ↓
Package Artifacts (ZIP)
       ↓
Upload to S3
       ↓
Trigger CodeDeploy
       ↓
Blue/Green Deployment
       ↓
Health Checks
       ↓
Complete or Rollback
```

**Componentes**:
- Azure DevOps Service Connection (OIDC)
- AWS CodeDeploy Application
- S3 Bucket para artifacts
- IAM Roles (Azure DevOps, EC2, CodeDeploy)
- CloudWatch Logs

---

## 📊 Optimizaciones Recomendadas

### Corto Plazo (0-3 meses)
- Usar 1 NAT Gateway (ahorro $32.85/mes)
- Reducir retención de logs (ahorro $1.50/mes)
- Consolidar dashboards (ahorro $3.00/mes)

### Mediano Plazo (3-6 meses)
- Comprar Reserved Instances (ahorro $97/mes)
- Implementar Auto Scaling (ahorro $50-100/mes)
- Optimizar Data Transfer (ahorro $10-20/mes)

### Largo Plazo (6-12 meses)
- Migrar a .NET Core + Linux (ahorro $100-150/mes)
- Evaluar Serverless (ahorro $200-300/mes)
- Migrar BD a AWS (ahorro $100-200/mes)

---

## 📞 Contactos

### Responsable del Proyecto
**Erik Palma**  
Jefe de Arquitectura BGR  
Email: erik.palma@bgr.com.ec

### Soporte
**BGR/TCS**  
Soporte y mantenimiento de la aplicación

---

## 📝 Notas Importantes

### Reglas del Proyecto BGR

1. **CI/CD**: Despliegue obligatorio por Azure DevOps
2. **Base de Datos**: Permanece on-premise por dependencias
3. **Conectividad**: Direct Connect + VPN backup requerido
4. **Seguridad**: Tráfico encriptado, Secrets Manager
5. **Monitoreo**: CloudWatch + SNS alertas

### Consideraciones Técnicas

- **.NET Framework 4.7.1**: Obsoleto, considerar upgrade post-migración
- **Windows Server 2016**: Soporte hasta 2027
- **SQL Server 2016**: Soporte hasta 2026
- **Latencia**: Crítica para performance (< 10ms)
- **Connection Pooling**: Esencial para BD on-premise

---

## 🎯 Próximos Pasos

1. [ ] **Aprobar propuesta** - Stakeholders BGR
2. [ ] **Solicitar Direct Connect** - Networking (2-4 semanas lead time)
3. [ ] **Asignar equipo** - Gerencia BGR
4. [ ] **Crear ambiente AWS** - Infraestructura
5. [ ] **Configurar Azure DevOps** - DevOps
6. [ ] **Iniciar testing** - QA
7. [ ] **Programar ventana de mantenimiento** - Gerencia

---

## 📚 Referencias

- [AWS Direct Connect Documentation](https://docs.aws.amazon.com/directconnect/)
- [AWS VPN Site-to-Site Documentation](https://docs.aws.amazon.com/vpn/)
- [AWS CodeDeploy Documentation](https://docs.aws.amazon.com/codedeploy/)
- [Azure DevOps AWS Integration](https://docs.microsoft.com/azure/devops/pipelines/ecosystems/aws)
- [REGLAS_PROYECTO_BGR.md](../../REGLAS_PROYECTO_BGR.md)

---

**Última actualización**: 2025-12-12  
**Versión**: 1.0  
**Estado**: DRAFT - Pendiente de aprobación  
**Próxima revisión**: 2025-12-19
