# Configuración de Kiro CLI

Este directorio contiene instrucciones personalizadas para Kiro CLI.

## Archivo de Instrucciones

**`instructions.md`** - Reglas y guías que Kiro CLI debe seguir automáticamente

### Cómo Funciona

Kiro CLI lee automáticamente este archivo cuando trabajas en este proyecto y aplica las reglas definidas, incluyendo:

- ❌ NO usar separadores HR (`---`) en documentos
- ✅ Seguir estructura de STYLE_GUIDE.md
- ✅ Generar diagramas con MCP
- ✅ Verificar checklist antes de entregar

### Activación

Las instrucciones se activan automáticamente cuando:
1. Estás en el directorio del proyecto
2. Kiro CLI detecta el archivo `.kiro/instructions.md`
3. Inicias una conversación o tarea

### Actualización

Para modificar las reglas:
```bash
# Editar instrucciones
vim .kiro/instructions.md

# Las instrucciones se aplican en la próxima conversación
```

### Verificación

Para verificar que las instrucciones están activas:
```bash
# Kiro CLI mostrará las instrucciones personalizadas al inicio
kiro-cli chat
```

## Referencias

- **Guía de Estilo**: `training/map-bgr/modernization-proposals/templates/STYLE_GUIDE.md`
- **Documentación Kiro**: https://docs.aws.amazon.com/amazonq/
