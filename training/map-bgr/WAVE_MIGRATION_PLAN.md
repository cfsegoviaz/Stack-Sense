# Plan de Olas de Migración - BGR

## Resumen Ejecutivo

**Cliente:** Banco General Rumiñahui  
**Total Aplicaciones:** 43  
**Período de Migración:** Enero - Junio 2026 (6 meses)  
**Horas Totales de Implementación:** 3,998 horas (~24 semanas)

### Métricas Consolidadas

| Métrica | Valor |
|---------|-------|
| Costo Mensual Actual | $48,730 |
| Costo Mensual AWS | $24,308 |
| Ahorro Mensual | $24,422 (50%) |
| Ahorro Anual | $293,064 |
| Inversión Implementación | $599,700 (3,998h × $150/h) |
| ROI | ~24 meses |

---

## Wave 1 - Quick Wins
**Enero - Febrero 2026**

### Objetivo
Migrar aplicaciones de baja complejidad para generar victorias tempranas, establecer patrones y ganar confianza del equipo.

### Métricas
- **Aplicaciones:** 13
- **Horas:** 322h (~4 semanas)
- **Costo Actual:** $5,900/mes
- **Costo AWS:** $2,858/mes
- **Ahorro:** 52%

### Aplicaciones

| Aplicación | Horas | Costo AWS | Estrategia |
|------------|-------|-----------|------------|
| Redis | 0h | $0 | Ya migrado |
| API Portal | 8h | $2 | Replatform (S3 + CloudFront) |
| Visor Histórico Cheques | 10h | $4 | Replatform (S3 + CloudFront) |
| Portal Administrativo BGR | 10h | $2 | Replatform (S3 + CloudFront) |
| Portal Guía BGR | 10h | $2 | Replatform (S3 + CloudFront) |
| Acciones y Accionistas | 12h | $8 | Replatform (S3 + CloudFront) |
| RCSA | 24h | $500 | Repurchase (SaaS) |
| Brightmail | 40h | $100 | Replace (Amazon SES) |
| Garantías/SISGAR | 40h | $800 | Retain (hasta Riesgo 2027) |
| BGR Seguridad Central API | 40h | $185 | Replatform (ECS Fargate) |
| Administración Cobranzas SAC | 40h | $800 | Repurchase (SaaS) |
| BGR Acceso Servicios API | 40h | $210 | Replatform (ECS Fargate) |
| Microservicios | 48h | $245 | Replatform (ECS Fargate) |

### Criterios de Éxito
- [ ] 100% de portales estáticos migrados a S3 + CloudFront
- [ ] APIs containerizadas en ECS Fargate
- [ ] Pipelines CI/CD establecidos
- [ ] Runbooks de operación documentados

---

## Wave 2 - Core Applications
**Febrero - Abril 2026**

### Objetivo
Migrar aplicaciones core del negocio que soportan operaciones bancarias críticas, estableciendo patrones de migración de bases de datos SQL Server.

### Métricas
- **Aplicaciones:** 13
- **Horas:** 1,222h (~15 semanas)
- **Costo Actual:** $16,330/mes
- **Costo AWS:** $4,842/mes
- **Ahorro:** 70%

### Aplicaciones

| Aplicación | Horas | Costo AWS | Estrategia |
|------------|-------|-----------|------------|
| Nueva Centralizada | 63h | $268 | Replatform (ECS + Aurora) |
| Estructuras de Control | 67h | $692 | Replatform (ECS + Babelfish) |
| Cuadre Compensación ATMs | 67h | $612 | Replatform (ECS + Aurora) |
| BGR Tu Cuenta | 71h | $617 | Replatform (ECS + Aurora) |
| Calculadora Inmobiliaria | 86h | $54 | Replatform (ECS Fargate) |
| Backoffice Banca Digital | 91h | $296 | Replatform (ECS + Aurora) |
| Librarian | 96h | $12 | Replatform (ECS + S3) |
| SEQ | 100h | $278 | Replatform (OpenSearch) |
| Pruebas Departamentales | 100h | $380 | Replatform (ECS Fargate) |
| BGR Interfaces Siglo | 120h | $485 | Replatform (ECS + SQS) |
| Administrador de Pagos | 120h | $327 | Replatform (ECS + Aurora) |
| BancaOficialCom | 120h | $420 | Replatform (ECS + Aurora) |
| Backoffice Sistemas | 121h | $402 | Replatform (ECS + Aurora) |

### Criterios de Éxito
- [ ] Migración exitosa de SQL Server a Aurora PostgreSQL/Babelfish
- [ ] Zero downtime en aplicaciones críticas
- [ ] Performance igual o mejor que on-premise
- [ ] Backups automatizados y DR configurado

---

## Wave 3 - Providers & Analytics
**Marzo - Mayo 2026**

### Objetivo
Migrar aplicaciones de proveedores externos, sistemas SaaS y plataformas analíticas. Requiere coordinación con vendors.

### Métricas
- **Aplicaciones:** 14
- **Horas:** 1,388h (~17 semanas)
- **Costo Actual:** $23,600/mes
- **Costo AWS:** $14,058/mes
- **Ahorro:** 40%

### Aplicaciones

| Aplicación | Horas | Costo AWS | Estrategia |
|------------|-------|-----------|------------|
| EFlow | 24h | $400 | Repurchase (SaaS nativo) |
| MyABCM | 32h | $600 | Repurchase (SaaS nativo) |
| AURO | 32h | $600 | Repurchase (SaaS nativo) |
| SonarQube | 40h | $404 | Replatform (ECS Fargate) |
| Evolution | 40h | $700 | Repurchase (SaaS nativo) |
| Monitor Plus | 60h | $1,200 | Repurchase (SaaS nativo) |
| SharePoint ITD | 80h | $200 | Replace (S3 + QuickSight) |
| RPA Automation Anywhere | 80h | $2,500 | Repurchase (Cloud nativo) |
| SharePoint OpRisk | 80h | $150 | Replace (S3 + QuickSight) |
| Cubos | 160h | $350 | Replatform (Redshift) |
| Control M | 160h | $5,000 | Repurchase (BMC Cloud) |
| ODS | 200h | $450 | Replatform (Aurora + Glue) |
| DataWarehouse Campañas | 200h | $600 | Replatform (Redshift) |
| SARAS | 200h | $904 | Replatform (ECS + Babelfish) |

### Criterios de Éxito
- [ ] Contratos SaaS actualizados con proveedores
- [ ] Conectividad VPN/DirectConnect con vendors
- [ ] Migración de datos analíticos a Redshift
- [ ] Dashboards recreados en QuickSight

---

## Wave 4 - Complex & Initiatives
**Mayo - Junio 2026**

### Objetivo
Migrar aplicaciones complejas que requieren reingeniería significativa o están alineadas con iniciativas estratégicas futuras (Cámara 2028, Riesgo 2027).

### Métricas
- **Aplicaciones:** 3
- **Horas:** 1,066h (~13 semanas)
- **Costo Actual:** $2,900/mes
- **Costo AWS:** $2,550/mes
- **Ahorro:** 12%

### Aplicaciones

| Aplicación | Horas | Costo AWS | Estrategia | Iniciativa |
|------------|-------|-----------|------------|------------|
| DCNET Cámara | 200h | $800 | Replatform (ECS + Textract) | Cámara 2028 |
| E-Business | 400h | $1,500 | Refactor (Microservicios) | Modernización |
| Ventana Marco | 466h | $250 | Refactor (Angular + ECS) | Sin código fuente |

### Criterios de Éxito
- [ ] Arquitectura de microservicios implementada
- [ ] Código fuente reconstruido donde aplique
- [ ] Integración con iniciativas estratégicas validada
- [ ] Plan de modernización continua definido

---

## Timeline Visual

```
2026
Ene     Feb     Mar     Abr     May     Jun
|-------|-------|-------|-------|-------|-------|
[=== Wave 1 ===]
        [======== Wave 2 ========]
                [======== Wave 3 ========]
                                [=== Wave 4 ===]
```

---

## Dependencias y Riesgos

### Dependencias Críticas
1. **Landing Zone AWS** - Debe estar configurada antes de Wave 1
2. **VPN/DirectConnect** - Requerido para Wave 2 (apps con BD)
3. **Contratos SaaS** - Negociación con vendors para Wave 3
4. **Código fuente** - Reconstrucción para Ventana Marco (Wave 4)

### Riesgos Identificados

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| Latencia BD híbrida | Media | Alto | DirectConnect dedicado |
| Incompatibilidad Babelfish | Baja | Alto | PoC temprano con SCT |
| Resistencia al cambio | Media | Medio | Change management |
| Dependencias no documentadas | Alta | Medio | Discovery con Cloudamize |
| Ventanas de mantenimiento | Alta | Medio | Migraciones en fin de semana |

---

## Equipo Requerido

### Escala24x7
- 1 Arquitecto Cloud (líder técnico)
- 2 Ingenieros DevOps
- 2 Desarrolladores .NET
- 1 DBA (especialista Aurora/Babelfish)
- 1 PM (coordinación)

### BGR (Contraparte)
- Product Owners por aplicación
- Equipo de QA para validación
- DBA para conocimiento de esquemas
- Seguridad para validación de controles

---

## Próximos Pasos

1. **Semana 1-2:** Validación del plan con stakeholders BGR
2. **Semana 3-4:** Configuración de Landing Zone y pipelines base
3. **Semana 5:** Inicio Wave 1 con aplicaciones piloto
4. **Mensual:** Revisión de avance y ajuste de plan

---

*Documento generado por Escala24x7 - Proyecto MAP BGR*  
*Última actualización: Enero 2026*
