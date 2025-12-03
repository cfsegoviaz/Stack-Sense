# EBA - Early Business Adoption
## Proyecto MAP-BGR

**Objetivo**: Migrar 8 aplicaciones a AWS con presupuesto de $5,000/mes  
**Duración**: 8-10 semanas  
**Estado**: 📋 Planificación

---

## 📁 Documentos del EBA

### Plan Principal
- **[EBA_PLAN.md](EBA_PLAN.md)** - Plan completo de EBA
  - Aplicaciones seleccionadas
  - Arquitectura detallada
  - Cronograma de 10 semanas
  - Equipos necesarios
  - Riesgos y mitigaciones

### Calculadora de Costos
- **[EBA_COST_CALCULATOR.csv](EBA_COST_CALCULATOR.csv)** - Desglose detallado
  - Costo por servicio AWS
  - Costo por aplicación
  - Total: $2,944/mes (41% bajo presupuesto)

### Diagramas de Arquitectura
- **[diagrams/eba_general_architecture.png](diagrams/eba_general_architecture.png)** - Arquitectura general
- **[diagrams/eba_network_architecture.png](diagrams/eba_network_architecture.png)** - Arquitectura de red
- **[diagrams/eba_api_portal_detailed.png](diagrams/eba_api_portal_detailed.png)** - App crítica
- **[diagrams/eba_sonarqube_detailed.png](diagrams/eba_sonarqube_detailed.png)** - App no crítica
- **[diagrams/eba_migration_flow.png](diagrams/eba_migration_flow.png)** - Flujo de migración

---

## 🎯 Resumen Ejecutivo

### Alcance
- **8 aplicaciones** (36 VMs)
- **4 apps críticas** con RDS Multi-AZ
- **4 apps no críticas** con Lift & Shift simple

### Presupuesto
| Concepto | Monto |
|----------|-------|
| Costo mensual | $4,587 |
| Presupuesto | $5,000 |
| Margen | $413 (8%) |

### Cronograma
| Fase | Duración | Aplicaciones |
|------|----------|--------------|
| Preparación | 2 semanas | Setup AWS |
| Apps No Críticas | 2 semanas | Seq, SonarQube, Saras, BO Sistemas |
| Apps Críticas | 4 semanas | Portal Guía, Portal Adm, BO Banca, Api Portal |
| Estabilización | 2 semanas | Testing y handover |

---

## 🏗️ Arquitectura

### Componentes Principales
- **36 EC2 instances** (t3.medium y t3.large)
- **4 RDS instances** (SQL Server)
- **2 ALB** (público e interno)
- **1 NAT Gateway**
- **CloudWatch** para monitoring
- **Secrets Manager** para credenciales

### Estrategia
- **Mínima modernización**: Lift & Shift prioritario
- **Servicios managed**: Solo RDS para bases de datos
- **Alta disponibilidad**: Multi-AZ para apps críticas
- **Optimización de costos**: Instancias rightsized

---

## 👥 Equipo Requerido

### Core Team (Tiempo Completo)
- 1 AWS Solutions Architect (10 semanas)
- 2 Cloud Migration Engineers (8 semanas)
- 1 DevOps Engineer (8 semanas)
- 1 Technical Lead (10 semanas)

### Support Team (Tiempo Parcial)
- 1 Database Administrator (4 semanas, 50%)
- 1 Security Engineer (3 semanas, 50%)
- 8 Application Owners (2 semanas cada uno, 25%)
- 1 Project Manager (10 semanas, 50%)

---

## 📊 Aplicaciones

| # | Aplicación | VMs | Criticidad | SQL Edition | Costo/mes |
|---|------------|-----|------------|-------------|-----------|
| 1 | Seq | 5 | Baja | - | $250 |
| 2 | SonarQube | 3 | Media | - | $200 |
| 3 | Saras | 4 | Media | - | $280 |
| 4 | Backoffice Sistemas | 5 | Media | - | $350 |
| 5 | Portal Guía BGR | 4 | Alta | Web | $452 |
| 6 | Portal Adm BGR | 4 | Alta | Web | $452 |
| 7 | Backoffice Banca | 6 | Alta | **Standard** | $883 |
| 8 | Api Portal | 5 | Alta | **Enterprise** | $1,962 |

**Nota**: Ediciones SQL Server basadas en análisis de Cloudamize (15 servidores con Enterprise identificados)

---

## 🚀 Próximos Pasos

### Esta Semana
1. [ ] Revisar y aprobar plan EBA
2. [ ] Asignar equipo
3. [ ] Provisionar cuentas AWS
4. [ ] Kick-off meeting

### Próximas 2 Semanas
1. [ ] Diseño detallado de arquitectura
2. [ ] Setup de ambiente AWS
3. [ ] Preparación de herramientas
4. [ ] Training del equipo

### Semanas 3-10
1. [ ] Ejecución de migraciones
2. [ ] Testing y validación
3. [ ] Estabilización
4. [ ] Handover a operaciones

---

## 📋 Checklist de Aprobaciones

- [ ] Sponsor ejecutivo
- [ ] Gerente de IT
- [ ] Gerente de Seguridad
- [ ] Gerente Financiero
- [ ] Application Owners (8)

**Fecha límite**: 2025-12-09

---

## 📞 Contactos

**Project Manager**: TBD  
**Technical Lead**: TBD  
**AWS Solutions Architect**: TBD

---

**Última actualización**: 2025-12-02
