# 03. Migration Strategy

**Audiencia:** Project Managers, Arquitectos, Equipo de Migración  
**Propósito:** Estrategias y planes detallados de migración

---

## 📄 Documentos

### 03_PRIMERA_OLA_MIGRACION.md
**Descripción:** Plan detallado de la primera ola de migración  
**Contenido:**
- Aplicaciones: PortalGuiaBGR, Api Portal
- Timeline: Meses 1-3
- Servicios compartidos a implementar
- Pasos de migración detallados
- Validaciones y testing

### 05_ESTRATEGIAS_OPTIMIZACION.md
**Descripción:** Estrategias de optimización de costos  
**Contenido:**
- Oportunidades de ahorro
- Reserved Instances
- Savings Plans
- Right-sizing
- Migración a Aurora PostgreSQL

### 05_estrategia_7rs.csv (56 KB)
**Descripción:** Estrategia 7Rs de AWS por aplicación  
**Formato:** CSV  
**Contenido:**
- Rehost, Replatform, Refactor, etc.
- Recomendación por aplicación
- Justificación técnica

---

## 🎯 Plan de Migración

### Ola 1 (Meses 1-3) - Piloto
**Aplicaciones:**
- PortalGuiaBGR
- Api Portal

**Objetivo:** Validar patrones y establecer servicios compartidos

### Ola 2 (Meses 4-6) - Core
**Aplicaciones:**
- PortalAdministrativoBGR
- Backoffice Sistemas BGR

**Objetivo:** Aplicar patrones validados

### Ola 3 (Meses 7-9) - Modernas
**Aplicaciones:**
- Backoffice Banca Digital (.NET 8)
- Saras (.NET 8)

**Objetivo:** Migración rápida (solo containerización)

### Ola 4 (Meses 10-12) - DevOps
**Aplicaciones:**
- Seq → CloudWatch Logs
- SonarQube → CodeGuru

**Objetivo:** Reemplazar con servicios managed

---

## 💡 Estrategias de Optimización

### Corto Plazo (0-3 meses)
- Reserved Instances (30% ahorro)
- Savings Plans (20% ahorro)
- Right-sizing (10-15% ahorro)

### Mediano Plazo (3-6 meses)
- Migración a Aurora PostgreSQL (60% ahorro en BD)
- Auto-scaling policies

### Largo Plazo (6-12 meses)
- Serverless para apps de bajo tráfico
- S3 Intelligent-Tiering

**Ahorro potencial total:** Hasta 82% vs on-premise
