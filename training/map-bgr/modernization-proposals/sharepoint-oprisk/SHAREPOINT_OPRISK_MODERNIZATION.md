# SharePoint OpRisk - Plan de Modernización
## SharePoint para Reportes de Riesgo Operacional

**Fecha**: 2026-01-07  
**Aplicación**: SharePoint OpRisk  
**Estrategia Recomendada**: S3 + QuickSight (Replatform)  
**Timeline**: 6 semanas

---

## 🎯 Información de la Aplicación

### Descripción
SharePoint Server 2013 utilizado para almacenamiento y visualización de reportes de riesgo operacional. Servidor legacy con Windows Server 2012.

### Situación Actual

| Atributo | Valor |
|----------|-------|
| **Servidor** | sharepoint-oprisk-srv |
| **IP** | 172.20.1.70 |
| **vCPUs** | 4 |
| **RAM** | 16 GB |
| **Storage** | 200 GB |
| **OS** | Windows Server 2012 |
| **Criticidad** | Media |
| **Usuarios** | ~30 |

### Stack Tecnológico
- **Frontend**: SharePoint 2013
- **Backend**: SharePoint Server
- **Database**: SQL Server 2012
- **Área**: Riesgo Operacional

### ⚠️ Hallazgos Clave
- **SharePoint 2013 EOL**: Sin soporte extendido desde 2023
- **Windows Server 2012 EOL**: Sistema operativo obsoleto
- **SQL Server 2012 EOL**: Base de datos sin soporte
- **Uso principal**: Reportes y dashboards (no colaboración)
- **Licenciamiento costoso**: SharePoint + SQL Server + Windows
- **Candidato ideal para QuickSight**: Reportería moderna sin licencias

---

## 🏗️ Opciones de Arquitectura

### Opción 1: S3 + QuickSight (RECOMENDADA)

![Arquitectura S3 QuickSight](./diagrams/generated-diagrams/sharepoint_oprisk_s3.png)

| Servicio | Configuración | Costo/mes |
|----------|---------------|-----------|
| S3 | Documentos y datos (~200 GB) | $20 |
| QuickSight | Enterprise (~10 usuarios) | $80 |
| Athena | Queries (~20 GB/mes) | $20 |
| Glue | ETL (~10 DPU-horas) | $20 |
| CloudWatch | Logs y métricas | $10 |
| **TOTAL** | | **$150/mes** |

**Ahorro**: 70% vs costo actual ($500/mes)

#### 💡 Tips y Recomendaciones IA

**Cuándo elegir:**
- Uso principal es reportería
- No se requiere colaboración SharePoint
- Dashboards interactivos deseados
- Eliminar licencias Microsoft

**Consideraciones:**
- Migrar documentos a S3
- Recrear reportes en QuickSight
- Capacitar usuarios en nueva herramienta
- Athena para queries ad-hoc

**Recomendaciones:**
- POC con reportes principales
- Migración por fases
- Capacitación antes de go-live
- Mantener SharePoint en paralelo inicialmente

**Ideal para:**
- Reportería y dashboards
- Análisis de datos
- Visualizaciones interactivas

#### 📋 Esfuerzo Escala24x7

| Tarea | Horas | Equipo |
|-------|-------|--------|
| S3 Bucket | 2 | Infra |
| Data Lake catalog (Athena/Glue) | 8 | Data |
| Data Lake ingestion (S3) | 4 | Data |
| Data Lake transform (Glue) | 8 | Data |
| Quicksight data source | 4 | Data |
| Quicksight dataset | 4 | Data |
| Quicksight dashboards (5) | 20 | Data |
| Quicksight user config | 5 | Data |
| CloudWatch Logs | 4 | Infra |
| Migración documentos | 8 | Infra |
| Testing y validación | 8 | QA |
| Knowledge transfer | 5 | Data |
| **TOTAL** | **80** | |

**Costo implementación**: 80 horas × $150/hora = **$12,000 USD**

---

### Opción 2: SharePoint Online

| Servicio | Configuración | Costo/mes |
|----------|---------------|-----------|
| SharePoint Online | Plan 1 (~30 usuarios) | $250 |
| Site-to-Site VPN | Conexión segura | $50 |
| **TOTAL** | | **$300/mes** |

**Ahorro**: 40% vs costo actual

#### 💡 Tips y Recomendaciones IA

**Cuándo elegir:**
- Se requiere colaboración SharePoint
- Usuarios familiarizados con SharePoint
- Integración con Microsoft 365

**Consideraciones:**
- Mayor costo que S3 + QuickSight
- Dependencia de Microsoft
- Migración de contenido requerida
- Licenciamiento por usuario

**Recomendaciones:**
- Solo si colaboración es crítica
- Evaluar si solo se necesitan reportes
- Considerar Microsoft 365 completo

**Ideal para:**
- Colaboración documental
- Integración Microsoft 365

#### 📋 Esfuerzo Escala24x7

| Tarea | Horas | Equipo |
|-------|-------|--------|
| VPN Site-to-Site | 16 | Infra |
| SharePoint Online config | 8 | Infra |
| Migración contenido | 16 | Infra |
| Configuración usuarios | 8 | Infra |
| Testing y validación | 8 | QA |
| Knowledge transfer | 4 | Infra |
| **TOTAL** | **60** | |

**Costo implementación**: 60 horas × $150/hora = **$9,000 USD**

---

## 📊 Comparativa

| Criterio | S3 + QuickSight | SharePoint Online |
|----------|-----------------|-------------------|
| **Costo/mes** | $150 | $300 |
| **Ahorro** | 70% | 40% |
| **Licencias Microsoft** | ❌ No | ✅ Sí |
| **Dashboards interactivos** | ✅ Sí | Limitado |
| **Colaboración** | Limitada | ✅ Sí |
| **Queries ad-hoc** | ✅ Athena | ❌ No |
| **Timeline** | 6 semanas | 4 semanas |

---

## 🔄 Plan de Migración S3 + QuickSight

### Fase 1: Análisis y Diseño (Semana 1)
- Inventario de documentos y reportes
- Identificar reportes críticos
- Diseñar estructura S3
- Planificar dashboards QuickSight

### Fase 2: Configuración (Semana 2)
- Crear buckets S3
- Configurar Glue crawlers
- Crear catálogo Athena
- Configurar QuickSight

### Fase 3: Migración de Datos (Semanas 3-4)
- Migrar documentos a S3
- Extraer datos de SQL Server
- Cargar datos en S3/Athena
- Validar integridad

### Fase 4: Dashboards (Semana 5)
- Recrear reportes en QuickSight
- Configurar datasets
- Crear visualizaciones
- Validar con usuarios

### Fase 5: Go-Live (Semana 6)
- Capacitación usuarios
- Go-live
- Soporte post-migración
- Decomisionar SharePoint

---

## 📊 Reportes a Migrar

| Reporte | Frecuencia | Complejidad | Prioridad |
|---------|------------|-------------|-----------|
| Dashboard OpRisk | Diario | Alta | 1 |
| Indicadores KRI | Semanal | Media | 2 |
| Eventos de Riesgo | Mensual | Media | 3 |
| Reportes SBS | Trimestral | Alta | 4 |

---

## ✅ Recomendación Final

**S3 + QuickSight** por:
1. **70% ahorro** ($150/mes vs $500/mes)
2. **Sin licencias Microsoft** - elimina SharePoint, SQL Server, Windows
3. **Dashboards modernos** - QuickSight interactivo
4. **Queries ad-hoc** - Athena para análisis
5. **Escalabilidad** - S3 ilimitado
6. **Stack obsoleto** - SharePoint 2013, SQL 2012, Windows 2012 sin soporte

**Nota**: Si se requiere colaboración documental, considerar SharePoint Online como alternativa.

---

**Última actualización**: 2026-01-07
