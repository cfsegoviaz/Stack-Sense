#!/bin/bash
# analyze_app.sh - Helper para analizar aplicaciones del portafolio BGR
# Uso: ./analyze_app.sh <app-slug> o ./analyze_app.sh --next

set -e

PROPOSALS_DIR="$(dirname "$0")/../modernization-proposals"
CHECKLIST="$PROPOSALS_DIR/ANALYSIS_CHECKLIST.md"

# Función para mostrar siguiente app pendiente
show_next() {
    echo "📋 Próximas aplicaciones pendientes (Prioridad 1):"
    echo ""
    grep -A 20 "Prioridad 1" "$CHECKLIST" | grep "⬜" | head -5
    echo ""
    echo "Usa: ./analyze_app.sh <app-slug>"
}

# Función para preparar análisis
prepare_analysis() {
    local APP_SLUG=$1
    local APP_DIR="$PROPOSALS_DIR/$APP_SLUG"
    
    # Crear estructura
    mkdir -p "$APP_DIR/diagrams"
    
    echo "✅ Directorio creado: $APP_DIR"
    echo ""
    echo "📝 Ejecuta en Kiro CLI:"
    echo ""
    echo "Analiza la aplicación \"$APP_SLUG\" del portafolio MAP-BGR siguiendo el template en training/map-bgr/modernization-proposals/templates/ANALYSIS_PROMPT.md"
    echo ""
}

# Main
if [ "$1" == "--next" ] || [ -z "$1" ]; then
    show_next
elif [ "$1" == "--help" ]; then
    echo "Uso: ./analyze_app.sh <app-slug> | --next | --help"
else
    prepare_analysis "$1"
fi
