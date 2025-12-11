# Changelog - Stack Sense Showcase

## [1.1.0] - 2025-12-11

### ✨ Agregado
- **Diagramas de Arquitectura**: Integración de diagramas visuales para cada aplicación
  - Api Portal: `app_apiportal.png`
  - SARAS: `app_saras.png`
  - SonarQube: `arch_sonarqube.png`
  - Backoffice Sistemas: `app_backoffice_sistemas.png`
  - Seq: `arch_seq_cloudwatch.png`
  - Arquitectura General: `bgr_aws_architecture.png`
  - Flujo de Migración: `migration_flow.png`

- **Script de Sincronización**: `sync-diagrams.sh` para actualizar diagramas desde el proyecto principal
- **Documentación Mejorada**:
  - `APPLICATIONS.md`: Índice completo de aplicaciones y diagramas
  - `CHANGELOG.md`: Historial de cambios
  - README actualizado con instrucciones detalladas

### 🔧 Modificado
- `src/App.tsx`: Agregada propiedad `diagram` a cada aplicación
- Componente de visualización: Nueva sección para mostrar diagramas de arquitectura
- README: Instrucciones de despliegue y actualización de diagramas

### 📁 Estructura
```
stack-sense-showcase/
├── public/
│   └── diagrams/          # ✨ NUEVO
│       ├── app_apiportal.png
│       ├── app_saras.png
│       ├── arch_sonarqube.png
│       ├── app_backoffice_sistemas.png
│       ├── arch_seq_cloudwatch.png
│       ├── arch_seq_ec2.png
│       ├── bgr_aws_architecture.png
│       └── migration_flow.png
├── src/
│   ├── App.tsx            # 🔧 MODIFICADO
│   ├── main.tsx
│   └── index.css
├── sync-diagrams.sh       # ✨ NUEVO
├── APPLICATIONS.md        # ✨ NUEVO
├── CHANGELOG.md           # ✨ NUEVO
└── README.md              # 🔧 MODIFICADO
```

---

## [1.0.0] - 2025-12-11

### ✨ Inicial
- Dashboard interactivo con 5 aplicaciones
- Análisis de costos y ahorros
- Comparación de arquitecturas (actual vs objetivo)
- Insights del arquitecto
- Diseño responsive con Tailwind CSS
