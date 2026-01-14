# Ventana Marco - Plan de Modernización
## Aplicación Java Legacy sin Código Fuente

**Fecha**: 2026-01-07  
**Aplicación**: Ventana Marco  
**Estrategia Recomendada**: Refactor (ECS + Angular)  
**Timeline**: 16 semanas

---

## 🎯 Información de la Aplicación

### Descripción
Aplicación Java legacy con interfaz Swing. **Sin código fuente disponible** - requiere reingeniería completa para modernización.

### Situación Actual

| Atributo | Valor |
|----------|-------|
| **Servidor** | ventana-marco-srv |
| **IP** | 172.20.1.50 |
| **vCPUs** | 4 |
| **RAM** | 8 GB |
| **Storage** | 100 GB |
| **OS** | Windows Server 2012 |
| **Criticidad** | Media |
| **Usuarios** | ~50 |

### Stack Tecnológico
- **Frontend**: Java Swing (desktop)
- **Backend**: Java 6
- **Database**: SQL Server 2008
- **Código Fuente**: ❌ NO DISPONIBLE

### ⚠️ Hallazgos Clave
- **Sin código fuente**: Imposible modificar o mantener
- **Java 6 obsoleto**: Versión sin soporte desde 2013
- **Windows Server 2012**: Sistema operativo obsoleto
- **SQL Server 2008**: Base de datos sin soporte
- **Java Swing**: Tecnología desktop obsoleta
- **Riesgo de seguridad**: Stack completo sin parches

---

## 🏗️ Opciones de Arquitectura

### Opción 1: ECS + Angular Reengineering (RECOMENDADA)

![Arquitectura ECS Angular](./diagrams/generated-diagrams/ventana_marco_ecs.png)

| Servicio | Configuración | Costo/mes |
|----------|---------------|-----------|
| ECS Fargate | .NET Core API (2 tasks) | $100 |
| Aurora PostgreSQL | db.t3.medium | $80 |
| CloudFront | Angular SPA | $20 |
| S3 | Static hosting | $10 |
| Application Load Balancer | HTTPS | $25 |
| CloudWatch | Logs y métricas | $15 |
| **TOTAL** | | **$250/mes** |

**Ahorro**: 58% vs costo actual ($600/mes)

#### 💡 Tips y Recomendaciones IA

**Cuándo elegir:**
- Aplicación crítica para el negocio
- Sin código fuente disponible
- Modernización completa requerida
- Presupuesto para reingeniería

**Consideraciones:**
- Requiere análisis funcional exhaustivo
- Documentar comportamiento actual
- Testing con usuarios finales
- Migración de datos SQL Server → PostgreSQL

**Recomendaciones:**
- Análisis funcional antes de desarrollo
- Desarrollo iterativo con feedback
- UAT con usuarios clave
- Plan de capacitación

**Ideal para:**
- Aplicaciones legacy sin código
- Modernización completa
- Tecnología web moderna

#### 📋 Esfuerzo Escala24x7

| Tarea | Horas | Equipo |
|-------|-------|--------|
| VPC/Redes | 4 | Infra |
| Fargate Cluster | 2 | Infra |
| Fargate Service (2 tasks) | 8 | Infra |
| ALB | 2 | Infra |
| Aurora PostgreSQL | 2 | Infra |
| CloudFront Distribution | 2 | Infra |
| S3 Bucket (static) | 2 | Infra |
| DMS replication instance | 4 | Data |
| DMS replication task | 4 | Data |
| Application pipeline (ECS) | 4 | Infra |
| Análisis funcional | 80 | Delivery |
| Desarrollo backend .NET Core | 160 | Delivery |
| Desarrollo frontend Angular | 120 | Delivery |
| CloudWatch Dashboard | 8 | Infra |
| Testing y UAT | 40 | QA |
| Knowledge transfer | 24 | Infra |
| **TOTAL** | **466** | |

**Costo implementación**: 466 horas × $150/hora = **$69,900 USD**

#### Esfuerzo de Implementación

| Fase | Horas | Costo |
|------|-------|-------|
| Análisis funcional | 80 | $12,000 |
| Desarrollo backend | 160 | $24,000 |
| Desarrollo frontend | 120 | $18,000 |
| Testing y UAT | 40 | $6,000 |
| **TOTAL** | **400** | **$60,000** |

---

### Opción 2: Retire - Evaluar Necesidad

| Servicio | Configuración | Costo/mes |
|----------|---------------|-----------|
| N/A | Decomisionar | $0 |
| **TOTAL** | | **$0/mes** |

**Ahorro**: 100%

#### 💡 Tips y Recomendaciones IA

**Cuándo elegir:**
- Funcionalidad duplicada en otras apps
- Bajo uso actual
- Sin usuarios activos
- Costo de reingeniería no justificado

**Consideraciones:**
- Análisis de impacto obligatorio
- Comunicación a usuarios
- Plan de transición
- Documentar decisión

**Recomendaciones:**
- Validar uso real con métricas
- Entrevistar usuarios
- Identificar alternativas existentes
- Documentar funcionalidad para futuro

**Ideal para:**
- Aplicaciones obsoletas sin uso
- Funcionalidad absorbida por otras apps

#### 📋 Esfuerzo Escala24x7

| Tarea | Horas | Equipo |
|-------|-------|--------|
| Análisis de impacto | 16 | Delivery |
| Documentación funcional | 8 | Delivery |
| Comunicación stakeholders | 8 | PM |
| Plan de transición | 4 | PM |
| Decomisionamiento | 4 | Infra |
| **TOTAL** | **40** | |

**Costo implementación**: 40 horas × $150/hora = **$6,000 USD**

---

## 📊 Comparativa

| Criterio | ECS + Angular | Retire |
|----------|---------------|--------|
| **Costo/mes** | $250 | $0 |
| **Ahorro mensual** | 58% | 100% |
| **Inversión inicial** | $60,000 | $6,000 |
| **Timeline** | 16 semanas | 4 semanas |
| **Riesgo** | Medio | Medio |
| **Funcionalidad** | Modernizada | Perdida |

---

## 🔄 Plan de Reingeniería

### Fase 1: Análisis Funcional (Semanas 1-4)
- Documentar todas las funcionalidades
- Entrevistar usuarios clave
- Mapear flujos de trabajo
- Identificar integraciones
- Definir requerimientos

### Fase 2: Diseño (Semanas 5-6)
- Arquitectura de solución
- Diseño de base de datos
- Mockups de interfaz
- Plan de migración de datos
- Validación con stakeholders

### Fase 3: Desarrollo Backend (Semanas 7-10)
- API REST en .NET Core
- Migración de lógica de negocio
- Integración con Aurora PostgreSQL
- Unit tests

### Fase 4: Desarrollo Frontend (Semanas 11-14)
- Angular SPA
- Componentes UI
- Integración con API
- Responsive design

### Fase 5: Testing y Go-Live (Semanas 15-16)
- Testing integral
- UAT con usuarios
- Capacitación
- Go-live con soporte

---

## ⚠️ Riesgos y Mitigaciones

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| Funcionalidad no documentada | Alta | Alto | Análisis exhaustivo con usuarios |
| Resistencia al cambio | Media | Medio | Capacitación y comunicación |
| Datos inconsistentes | Media | Alto | Validación y limpieza previa |
| Integraciones desconocidas | Media | Alto | Discovery técnico completo |

---

## ✅ Recomendación Final

**ECS + Angular Reengineering** por:
1. **Aplicación sin código fuente** - no hay otra opción de modernización
2. **Stack completamente obsoleto** - Java 6, Windows 2012, SQL 2008
3. **Riesgo de seguridad** - sin parches disponibles
4. **58% ahorro mensual** después de inversión inicial
5. **Tecnología moderna** - mantenible a largo plazo
6. **ROI en 2.5 años** - $60K inversión / $350 ahorro mensual

**Alternativa**: Si el análisis de uso revela bajo valor de negocio, considerar **Retire**.

---

**Última actualización**: 2026-01-07
