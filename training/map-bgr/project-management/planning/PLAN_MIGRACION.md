# Plan de Migración MAP-BGR a AWS

**Cliente**: BGR  
**Fecha Inicio**: 2025-12-01  
**Ambientes**: Desarrollo, QA, Producción  
**VMs Producción**: 383 (base para dimensionamiento)

---

## 🎯 Objetivo

Migrar infraestructura BGR a AWS con estrategia multi-ambiente, minimizando riesgo y asegurando continuidad del negocio.

---

## 📋 FASE 1: DISCOVERY & ASSESSMENT (Semana 1-2)

### 1.1 Análisis de Inventario
- [ ] Analizar 383 VMs de producción (RVTools)
- [ ] Simular inventario de Desarrollo (estimado 30% de prod)
- [ ] Simular inventario de QA (estimado 20% de prod)
- [ ] Identificar VMs críticas vs no críticas
- [ ] Documentar dependencias entre servidores

**Entregables**:
- `reports/01_inventario_completo.json`
- `reports/01_inventario_por_ambiente.csv`

### 1.2 Mapeo de Aplicaciones
- [ ] Analizar documentación HTML de aplicaciones
  - [ ] Api Portal
  - [ ] Portal Guía BGR
  - [ ] Sonar Qube
  - [ ] Backoffice Banca Digital
  - [ ] Portal Adm BGR
  - [ ] Backoffice Sistemas
  - [ ] Saras
  - [ ] Seq
- [ ] Identificar componentes por aplicación (web, app, db, cache)
- [ ] Mapear VMs a aplicaciones
- [ ] Documentar puertos y protocolos
- [ ] Identificar integraciones entre aplicaciones

**Entregables**:
- `reports/02_mapa_aplicaciones.json`
- `diagrams/02_arquitectura_actual.png`

### 1.3 Análisis de Recursos
- [ ] Calcular totales por ambiente (CPU, RAM, Storage)
- [ ] Identificar picos de uso (simular basado en producción)
- [ ] Analizar tipos de almacenamiento requeridos
- [ ] Documentar requisitos de red y ancho de banda
- [ ] Identificar requisitos de backup y DR

**Entregables**:
- `reports/03_analisis_recursos.xlsx`

---

## 📋 FASE 2: ESTRATEGIA & DISEÑO (Semana 3-4)

### 2.1 Estrategia de Migración (7R's)
- [ ] Clasificar VMs por estrategia:
  - [ ] **Rehost** (Lift & Shift): Servidores legacy
  - [ ] **Replatform**: Aplicaciones modernizables
  - [ ] **Refactor**: Aplicaciones cloud-native
  - [ ] **Retire**: Sistemas obsoletos (ej: Windows 2003)
  - [ ] **Retain**: Sistemas que permanecen on-prem
  - [ ] **Repurchase**: Candidatos a SaaS
  - [ ] **Relocate**: VMware Cloud on AWS

**Entregables**:
- `reports/04_estrategia_7rs.csv`

### 2.2 Recomendaciones de Servicios AWS
- [ ] Mapear VMs a instancias EC2 (por ambiente)
- [ ] Identificar candidatos a servicios managed:
  - [ ] RDS (bases de datos)
  - [ ] ECS/EKS (aplicaciones containerizables)
  - [ ] Lambda (microservicios)
  - [ ] ElastiCache (Redis/Memcached)
  - [ ] S3 (almacenamiento de archivos)
- [ ] Recomendar tipos de almacenamiento EBS
- [ ] Diseñar estrategia de networking (VPC, subnets, TGW)
- [ ] Definir estrategia de seguridad (Security Groups, NACLs, WAF)

**Entregables**:
- `reports/05_recomendaciones_aws.json`
- `reports/05_instancias_ec2_por_ambiente.csv`

### 2.3 Arquitectura Target en AWS
- [ ] Diseñar arquitectura multi-cuenta (Dev, QA, Prod)
- [ ] Definir estructura de VPCs y subnets
- [ ] Diseñar conectividad híbrida (Direct Connect / VPN)
- [ ] Arquitectura de alta disponibilidad (Multi-AZ)
- [ ] Estrategia de disaster recovery
- [ ] Diseño de monitoreo y observabilidad

**Entregables**:
- `diagrams/06_arquitectura_target_aws.png`
- `diagrams/06_networking_design.png`
- `reports/06_arquitectura_detallada.md`

### 2.4 Validación Well-Architected
- [ ] Revisar contra pilar de Seguridad
- [ ] Revisar contra pilar de Confiabilidad
- [ ] Revisar contra pilar de Eficiencia de Rendimiento
- [ ] Revisar contra pilar de Optimización de Costos
- [ ] Revisar contra pilar de Excelencia Operacional
- [ ] Revisar contra pilar de Sostenibilidad

**Entregables**:
- `reports/07_well_architected_review.pdf`

---

## 📋 FASE 3: ANÁLISIS DE COSTOS (Semana 5)

### 3.1 Estimación de Costos AWS
- [ ] Calcular costos de compute (EC2, ECS, Lambda)
- [ ] Calcular costos de almacenamiento (EBS, S3, EFS)
- [ ] Calcular costos de red (Data Transfer, NAT Gateway)
- [ ] Calcular costos de bases de datos (RDS)
- [ ] Calcular costos de servicios adicionales
- [ ] Estimar costos por ambiente (Dev, QA, Prod)
- [ ] Calcular costos mensuales y anuales

**Entregables**:
- `reports/08_estimacion_costos_aws.xlsx`
- `reports/08_costos_por_ambiente.csv`

### 3.2 Análisis Comparativo
- [ ] Documentar costos actuales on-premise
- [ ] Comparar TCO on-prem vs AWS (3 años)
- [ ] Identificar oportunidades de ahorro:
  - [ ] Reserved Instances
  - [ ] Savings Plans
  - [ ] Spot Instances
  - [ ] Auto Scaling
- [ ] Calcular ROI de la migración

**Entregables**:
- `reports/09_analisis_tco.xlsx`
- `reports/09_oportunidades_ahorro.md`

---

## 📋 FASE 4: PLAN DE EJECUCIÓN (Semana 6)

### 4.1 Definir Olas de Migración
- [ ] **Ola 0 - Piloto** (Ambiente Dev):
  - [ ] Seleccionar 2-3 aplicaciones no críticas
  - [ ] Validar proceso de migración
  - [ ] Ajustar procedimientos
- [ ] **Ola 1 - QA**:
  - [ ] Migrar ambiente completo de QA
  - [ ] Validar funcionalidad
- [ ] **Ola 2 - Producción Fase 1** (Aplicaciones no críticas):
  - [ ] 30% de aplicaciones
- [ ] **Ola 3 - Producción Fase 2** (Aplicaciones críticas):
  - [ ] 70% restante

**Entregables**:
- `reports/10_olas_migracion.xlsx`
- `reports/10_cronograma_detallado.mpp`

### 4.2 Preparación de Infraestructura Base
- [ ] Crear estructura de cuentas AWS (Organizations)
- [ ] Configurar Landing Zone (Control Tower)
- [ ] Implementar VPCs y networking
- [ ] Configurar conectividad híbrida
- [ ] Implementar IAM y políticas de seguridad
- [ ] Configurar CloudWatch y monitoreo
- [ ] Implementar backup y DR
- [ ] Configurar herramientas de migración (MGN, DMS)

**Entregables**:
- `templates/11_landing_zone_cdk/`
- `templates/11_networking_terraform/`

### 4.3 Runbooks de Migración
- [ ] Procedimiento de migración Rehost (MGN)
- [ ] Procedimiento de migración bases de datos (DMS)
- [ ] Procedimiento de validación post-migración
- [ ] Procedimiento de rollback
- [ ] Matriz de contactos y escalamiento

**Entregables**:
- `docs/12_runbook_migracion.md`
- `docs/12_procedimiento_rollback.md`

---

## 📋 FASE 5: GENERACIÓN DE ENTREGABLES (Semana 7)

### 5.1 Documentación Técnica
- [ ] Documento de arquitectura detallada
- [ ] Diagramas de red y seguridad
- [ ] Matriz de servicios AWS utilizados
- [ ] Guías de operación y mantenimiento
- [ ] Documentación de APIs y integraciones

**Entregables**:
- `docs/arquitectura_tecnica.pdf`
- `docs/guia_operaciones.pdf`

### 5.2 Propuesta Comercial
- [ ] Executive Summary
- [ ] Análisis de situación actual
- [ ] Propuesta de solución AWS
- [ ] Análisis de costos y ROI
- [ ] Plan de implementación
- [ ] Riesgos y mitigaciones
- [ ] Términos y condiciones

**Entregables**:
- `propuesta/propuesta_comercial_bgr.pdf`
- `propuesta/presentacion_ejecutiva.pptx`

### 5.3 Código de Infraestructura
- [ ] Templates CDK para infraestructura base
- [ ] Scripts de automatización
- [ ] Configuraciones de servicios
- [ ] Pipelines CI/CD

**Entregables**:
- `templates/cdk/`
- `templates/terraform/`
- `scripts/automation/`

---

## 📊 MÉTRICAS DE ÉXITO

- [ ] 100% de aplicaciones inventariadas
- [ ] 0 downtime en aplicaciones críticas
- [ ] Reducción de costos operativos > 20%
- [ ] RTO < 4 horas, RPO < 1 hora
- [ ] Cumplimiento de Well-Architected Framework
- [ ] Satisfacción del cliente > 90%

---

## 🚨 RIESGOS Y MITIGACIONES

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| Dependencias no documentadas | Alta | Alto | Discovery exhaustivo, pruebas en Dev/QA |
| Windows Server 2003 (38 VMs) | Alta | Medio | Priorizar upgrade o containerización |
| Downtime en migración | Media | Alto | Migración por fases, rollback plan |
| Sobrecostos AWS | Media | Medio | Monitoreo continuo, rightsizing |
| Falta de skills AWS en equipo | Media | Medio | Capacitación, documentación detallada |

---

## 📅 CRONOGRAMA RESUMIDO

| Fase | Duración | Entregables Clave |
|------|----------|-------------------|
| Discovery & Assessment | 2 semanas | Inventario, Mapeo Apps |
| Estrategia & Diseño | 2 semanas | Arquitectura, Well-Architected |
| Análisis de Costos | 1 semana | TCO, ROI |
| Plan de Ejecución | 1 semana | Olas, Runbooks |
| Generación Entregables | 1 semana | Propuesta, IaC |
| **TOTAL ESTUDIO** | **7 semanas** | Propuesta completa |

---

## 🎯 PRÓXIMOS PASOS INMEDIATOS

1. ✅ Inventario de producción completado
2. ⏭️ Simular inventarios de Dev y QA
3. ⏭️ Analizar documentación de aplicaciones
4. ⏭️ Generar recomendaciones de instancias EC2
5. ⏭️ Calcular costos estimados

---

**Última actualización**: 2025-12-01  
**Responsable**: Equipo Stack Sense
