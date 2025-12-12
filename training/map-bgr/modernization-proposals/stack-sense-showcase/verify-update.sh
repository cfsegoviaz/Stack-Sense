#!/bin/bash

# Script de verificación de actualización del showcase
# Verifica que Backoffice Sistemas esté correctamente integrado

echo "🔍 Verificando actualización del Stack Sense Showcase..."
echo ""

# Colores
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Contadores
PASSED=0
FAILED=0

# Función para verificar archivo
check_file() {
    if [ -f "$1" ]; then
        echo -e "${GREEN}✓${NC} $2"
        ((PASSED++))
    else
        echo -e "${RED}✗${NC} $2"
        ((FAILED++))
    fi
}

# Función para verificar contenido
check_content() {
    if grep -q "$2" "$1" 2>/dev/null; then
        echo -e "${GREEN}✓${NC} $3"
        ((PASSED++))
    else
        echo -e "${RED}✗${NC} $3"
        ((FAILED++))
    fi
}

echo "📁 Verificando archivos..."
echo ""

# Verificar diagrama
check_file "public/diagrams/backoffice_sistemas_hybrid_architecture.png" "Diagrama de Backoffice Sistemas"

# Verificar documentos
check_file "APPLICATIONS.md" "Documento APPLICATIONS.md"
check_file "RESUMEN_ACTUALIZADO.md" "Documento RESUMEN_ACTUALIZADO.md"
check_file "src/App.tsx" "Archivo App.tsx"

echo ""
echo "📝 Verificando contenido..."
echo ""

# Verificar contenido en App.tsx
check_content "src/App.tsx" "Backoffice Sistemas" "App.tsx contiene 'Backoffice Sistemas'"
check_content "src/App.tsx" "Direct Connect" "App.tsx menciona Direct Connect"
check_content "src/App.tsx" "t3.xlarge" "App.tsx especifica tipo de instancia"
check_content "src/App.tsx" "685" "App.tsx incluye número de usuarios"

# Verificar contenido en APPLICATIONS.md
check_content "APPLICATIONS.md" "Backoffice Sistemas" "APPLICATIONS.md contiene 'Backoffice Sistemas'"
check_content "APPLICATIONS.md" "37%" "APPLICATIONS.md incluye porcentaje de ahorro"
check_content "APPLICATIONS.md" "Direct Connect" "APPLICATIONS.md menciona Direct Connect"
check_content "APPLICATIONS.md" "\$279/mes" "APPLICATIONS.md incluye ahorro mensual"

# Verificar totales actualizados
check_content "APPLICATIONS.md" "5,179" "APPLICATIONS.md tiene totales actualizados"

echo ""
echo "📊 Resumen de verificación:"
echo ""
echo -e "  ${GREEN}Pasadas:${NC} $PASSED"
echo -e "  ${RED}Fallidas:${NC} $FAILED"
echo ""

if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}✓ Todas las verificaciones pasaron correctamente!${NC}"
    echo ""
    echo "🚀 El showcase está listo para usar."
    echo ""
    echo "Para iniciar el showcase:"
    echo "  cd stack-sense-showcase"
    echo "  npm install"
    echo "  npm run dev"
    exit 0
else
    echo -e "${RED}✗ Algunas verificaciones fallaron.${NC}"
    echo ""
    echo "Por favor revisa los archivos marcados con ✗"
    exit 1
fi
