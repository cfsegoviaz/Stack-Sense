# Getting Started - Propuestas de Modernización

## 🎯 Bienvenido

Este directorio contiene todas las propuestas de modernización para el proyecto MAP-BGR. Aquí encontrarás planes detallados, arquitecturas, costos y timelines para cada aplicación.

---

## 📚 Documentos Principales

### 1. [README.md](./README.md)
**Qué contiene**: Resumen ejecutivo del programa completo
- Tabla de todas las aplicaciones
- Estrategias de modernización
- Costos consolidados
- Roadmap de implementación

**Cuándo leerlo**: Primera vez que accedes al directorio

---

### 2. [INDEX.md](./INDEX.md)
**Qué contiene**: Índice visual y navegación rápida
- Estructura del directorio
- Acceso rápido por estrategia
- Búsqueda por tecnología/costo/timeline

**Cuándo leerlo**: Para encontrar información específica rápidamente

---

### 3. Carpetas de Aplicaciones
Cada aplicación tiene su propia carpeta con:
- **README.md**: Resumen ejecutivo de la aplicación
- **PLAN.md**: Plan completo de migración/modernización
- **diagrams/**: Diagramas de arquitectura

---

## 🚀 Flujo de Trabajo Recomendado

### Para Revisar una Aplicación

```
1. Leer README.md de la aplicación
   ↓
2. Ver diagrama de arquitectura
   ↓
3. Leer plan completo (PLAN.md)
   ↓
4. Validar costos y timeline
   ↓
5. Aprobar o solicitar cambios
```

### Para Agregar Nueva Aplicación

```
1. Crear directorio
   ↓
2. Copiar template apropiado
   ↓
3. Personalizar con información específica
   ↓
4. Generar diagramas
   ↓
5. Crear README de la aplicación
   ↓
6. Actualizar README.md principal
   ↓
7. Actualizar INDEX.md
```

---

## 📖 Ejemplos de Uso

### Ejemplo 1: Quiero ver todas las aplicaciones
```bash
# Leer README.md principal
cat README.md

# Ver tabla de aplicaciones
# Sección: "Resumen de Aplicaciones"
```

### Ejemplo 2: Quiero ver detalles de SARAS
```bash
# Ir a carpeta de SARAS
cd saras/

# Leer resumen ejecutivo
cat README.md

# Ver diagrama
open diagrams/saras_modernization_complete.png

# Leer plan completo
cat SARAS_MODERNIZATION_PLAN.md
```

### Ejemplo 3: Quiero agregar nueva aplicación
```bash
# Crear estructura
mkdir nueva-app
mkdir nueva-app/diagrams

# Copiar template
cp templates/lift-and-shift-template.md nueva-app/PLAN.md

# Editar plan
vim nueva-app/PLAN.md

# Crear README
vim nueva-app/README.md

# Actualizar índices
vim README.md
vim INDEX.md
```

---

## 🎨 Convenciones de Nombres

### Archivos
- **README.md**: Resumen ejecutivo (en cada carpeta)
- **[APP]_[STRATEGY].md**: Plan completo
  - Ejemplos: `SARAS_MODERNIZATION_PLAN.md`, `SONARQUBE_LIFT_SHIFT.md`

### Carpetas
- **Minúsculas con guiones**: `api-portal`, `backoffice-sistemas`
- **Sin espacios**: Usar guiones en lugar de espacios
- **Descriptivo**: Nombre claro de la aplicación

### Diagramas
- **[app]_[tipo].png**: Nombre descriptivo
  - Ejemplos: `saras_modernization_complete.png`, `sonarqube_lift_shift.png`

---

## 📊 Estructura de Documentos

### README.md de Aplicación
```markdown
# [Aplicación] - [Estrategia]

**Estrategia**: [Tipo]
**Timeline**: [X] semanas
**Costo AWS**: $[X]/mes
**Ahorro**: [X]%

## Documentos
- Link al plan completo

## Resumen Ejecutivo
- Transformación
- Beneficios
- Fases

## Arquitectura
- Diagrama
- Componentes

## Costos
- Tabla de costos

## Estado
- Checklist
```

### Plan Completo
```markdown
# [Aplicación] - Plan Completo

## Contexto
## Arquitectura
## Plan de Migración (detallado)
## Costos (detallado)
## Configuración Técnica
## Riesgos y Mitigaciones
## Criterios de Éxito
## Próximos Pasos
```

---

## 🔍 Búsqueda Rápida

### Por Estrategia
```bash
# Modernización
ls -d */  | grep -E "(saras)"

# Static Site
ls -d */  | grep -E "(api-portal)"

# Lift & Shift
ls -d */  | grep -E "(backoffice|sonarqube)"
```

### Por Costo
```bash
# Bajo costo (<$100/mes)
grep -r "TOTAL.*\$[0-9]\{1,2\}\..*mes" */README.md

# Medio costo ($100-$500/mes)
grep -r "TOTAL.*\$[1-4][0-9]\{2\}.*mes" */README.md

# Alto costo (>$500/mes)
grep -r "TOTAL.*\$[5-9][0-9]\{2\}.*mes" */README.md
```

---

## 🛠️ Herramientas Útiles

### Generar Diagrama
```python
# Usar generate_diagram tool de Kiro CLI
# Ver ejemplos en carpetas existentes
```

### Calcular Costos
```bash
# Usar AWS Pricing Calculator
# https://calculator.aws

# O usar AWS CLI
aws pricing get-products --service-code AmazonEC2 ...
```

### Validar Markdown
```bash
# Instalar markdownlint
npm install -g markdownlint-cli

# Validar archivo
markdownlint README.md
```

---

## 📞 Soporte

### Preguntas Frecuentes

**P: ¿Dónde está el resumen de todas las aplicaciones?**  
R: En [README.md](./README.md) principal

**P: ¿Cómo encuentro una aplicación específica?**  
R: Usa [INDEX.md](./INDEX.md) para navegación rápida

**P: ¿Qué template uso para nueva aplicación?**  
R: Depende de la estrategia:
- Lift & Shift: `templates/lift-and-shift-template.md`
- Containerización: `templates/containerization-template.md` (pendiente)
- Static Site: `templates/static-site-template.md` (pendiente)

**P: ¿Cómo actualizo los costos?**  
R: Edita el archivo PLAN.md de la aplicación y actualiza la tabla de costos

**P: ¿Dónde guardo los diagramas?**  
R: En la carpeta `diagrams/` dentro de cada aplicación

---

## ✅ Checklist de Calidad

Antes de considerar una propuesta completa, verifica:

- [ ] README.md de la aplicación creado
- [ ] Plan completo (PLAN.md) documentado
- [ ] Diagrama de arquitectura generado
- [ ] Costos calculados y validados
- [ ] Timeline definido
- [ ] Riesgos identificados
- [ ] Criterios de éxito definidos
- [ ] README.md principal actualizado
- [ ] INDEX.md actualizado

---

## 🎯 Próximos Pasos

1. **Leer** [README.md](./README.md) para contexto general
2. **Explorar** carpetas de aplicaciones existentes
3. **Revisar** templates disponibles
4. **Agregar** nuevas aplicaciones según necesidad

---

**Última actualización**: 2025-12-05  
**Versión**: 1.0  
**Mantenedor**: Equipo de Migración MAP-BGR
