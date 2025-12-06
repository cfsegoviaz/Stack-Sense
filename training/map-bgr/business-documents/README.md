# Business Documents - Documentos Comerciales y Administrativos

Plantillas y documentos generados para gestión comercial del proyecto MAP-BGR.

---

## 📁 Estructura

```
business-documents/
├── README.md                    # Este archivo
│
├── templates/                   # Plantillas reutilizables
│   ├── sow/                    # Statement of Work templates
│   ├── proposals/              # Propuestas comerciales
│   ├── contracts/              # Contratos y acuerdos
│   └── reports/                # Reportes ejecutivos
│
└── generated/                   # Documentos generados
    ├── sow/                    # SOWs generados
    ├── proposals/              # Propuestas generadas
    ├── contracts/              # Contratos generados
    └── reports/                # Reportes generados
```

---

## 📄 Tipos de Documentos

### 1. Statement of Work (SOW)
**Ubicación**: `templates/sow/` y `generated/sow/`

**Propósito**: Solicitar fondos y definir alcance de trabajo

**Tipos**:
- SOW para AWS EBA (Early Business Adoption)
- SOW para servicios profesionales
- SOW para proyectos específicos

**Plantillas disponibles**:
- `sow-eba-template.md` - Template para solicitud de fondos EBA
- `sow-migration-template.md` - Template para proyectos de migración
- `sow-modernization-template.md` - Template para modernización

---

### 2. Proposals (Propuestas)
**Ubicación**: `templates/proposals/` y `generated/proposals/`

**Propósito**: Propuestas comerciales para clientes

**Tipos**:
- Propuestas técnicas
- Propuestas comerciales
- Propuestas de arquitectura

---

### 3. Contracts (Contratos)
**Ubicación**: `templates/contracts/` y `generated/contracts/`

**Propósito**: Acuerdos y contratos

**Tipos**:
- Contratos de servicios
- Acuerdos de nivel de servicio (SLA)
- Términos y condiciones

---

### 4. Reports (Reportes)
**Ubicación**: `templates/reports/` y `generated/reports/`

**Propósito**: Reportes ejecutivos y de progreso

**Tipos**:
- Reportes ejecutivos
- Reportes de progreso
- Reportes financieros

---

## 🎯 Uso

### Crear Nuevo SOW para EBA

```bash
# 1. Copiar template
cp templates/sow/sow-eba-template.md generated/sow/SOW-EBA-MAP-BGR-2025.md

# 2. Personalizar con información del proyecto
vim generated/sow/SOW-EBA-MAP-BGR-2025.md

# 3. Revisar y aprobar
```

### Crear Nueva Propuesta

```bash
# 1. Copiar template apropiado
cp templates/proposals/proposal-template.md generated/proposals/PROPOSAL-CLIENT-2025.md

# 2. Personalizar
vim generated/proposals/PROPOSAL-CLIENT-2025.md
```

---

## 📋 Convenciones de Nombres

### Templates
- Formato: `[tipo]-[descripcion]-template.md`
- Ejemplos:
  - `sow-eba-template.md`
  - `proposal-migration-template.md`
  - `contract-services-template.md`

### Documentos Generados
- Formato: `[TIPO]-[PROYECTO]-[AÑO]-[VERSION].md`
- Ejemplos:
  - `SOW-EBA-MAP-BGR-2025-v1.md`
  - `PROPOSAL-BGR-MIGRATION-2025-v2.md`
  - `CONTRACT-BGR-SERVICES-2025-FINAL.md`

---

## 🔄 Workflow

### Para SOW de EBA

```
1. Copiar template
   ↓
2. Completar información del proyecto
   - Nombre del proyecto
   - Alcance
   - Timeline
   - Presupuesto
   - Beneficios esperados
   ↓
3. Revisar con equipo técnico
   ↓
4. Revisar con stakeholders
   ↓
5. Enviar a AWS para aprobación
   ↓
6. Archivar versión aprobada
```

---

## 📊 Estado Actual

### Templates Disponibles
- [ ] SOW EBA Template (por agregar)
- [ ] SOW Migration Template
- [ ] Proposal Template
- [ ] Contract Template
- [ ] Executive Report Template

### Documentos Generados
- [ ] SOW EBA MAP-BGR 2025 (por crear)

---

## 🎯 Próximos Pasos

1. [ ] Agregar template SOW EBA
2. [ ] Generar SOW para MAP-BGR
3. [ ] Crear templates adicionales según necesidad
4. [ ] Establecer proceso de aprobación

---

## 📞 Contacto

**Para aprobaciones**:
- SOW: Project Sponsor + AWS Account Manager
- Propuestas: Sales Lead + Technical Lead
- Contratos: Legal + Finance

---

**Última actualización**: 2025-12-05  
**Versión**: 1.0
