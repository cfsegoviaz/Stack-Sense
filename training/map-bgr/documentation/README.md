# Documentation - Documentación Técnica

Documentación técnica del proyecto MAP-BGR.

---

## 📁 Contenido

### 📂 eba-plans/
**Planes de Early Business Adoption (EBA)**

Planes para llevar aplicaciones a producción rápidamente:
- `EBA_README.md`: Introducción a EBA
- `EBA_PLAN.md`: Plan EBA general
- `EBA_PLAN_BABELFISH.md`: Plan con Aurora Babelfish
- `EBA_PLAN_CONTAINERS.md`: Plan con contenedores

### 📂 sql-analysis/
**Análisis de SQL Server**
- `SQL_SERVER_ANALYSIS.md`: Análisis detallado de instancias SQL Server

---

## 🎯 Planes EBA

### EBA General
**Objetivo**: 8 aplicaciones en producción, $5,000/mes budget

**Aplicaciones**:
1. Seq (Logging)
2. Sonar Qube
3. Saras
4. Backoffice Sistemas
5. Portal Guía BGR
6. Portal Adm BGR
7. Backoffice Banca Digital
8. Api Portal

### EBA con Babelfish
**Objetivo**: Migrar SQL Server a Aurora PostgreSQL con Babelfish

**Beneficios**:
- 50% reducción de costos en BD
- Sin cambios de código
- Compatibilidad SQL Server (puerto 1433)

### EBA con Contenedores
**Objetivo**: Modernizar aplicaciones a contenedores

**Beneficios**:
- Arquitectura cloud-native
- Auto-scaling
- Reducción de costos

---

## 📊 Análisis SQL Server

### Instancias Identificadas
- Análisis de versiones
- Análisis de tamaño
- Recomendaciones de migración
- Opciones: RDS SQL Server vs Aurora Babelfish

---

## 🔍 Uso

### Leer Plan EBA
```bash
cat eba-plans/EBA_PLAN.md
```

### Ver Plan con Babelfish
```bash
cat eba-plans/EBA_PLAN_BABELFISH.md
```

### Revisar Análisis SQL
```bash
cat sql-analysis/SQL_SERVER_ANALYSIS.md
```

---

**Última actualización**: 2025-12-05
