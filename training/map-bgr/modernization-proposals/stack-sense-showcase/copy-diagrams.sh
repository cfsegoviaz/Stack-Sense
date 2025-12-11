#!/bin/bash

# Script para copiar diagramas desde generated-diagrams a public/diagrams

SHOWCASE_DIR="training/map-bgr/modernization-proposals/stack-sense-showcase"
SOURCE_DIR="generated-diagrams"

# Crear carpeta de destino
mkdir -p "$SHOWCASE_DIR/public/diagrams"

echo "Copiando diagramas..."

# Copiar diagramas existentes
if [ -f "$SOURCE_DIR/api_portal_architecture" ]; then
  cp "$SOURCE_DIR/api_portal_architecture" "$SHOWCASE_DIR/public/diagrams/app_apiportal.png"
  echo "✓ Api Portal copiado"
fi

if [ -f "$SOURCE_DIR/saras_architecture" ]; then
  cp "$SOURCE_DIR/saras_architecture" "$SHOWCASE_DIR/public/diagrams/app_saras.png"
  echo "✓ SARAS copiado"
fi

if [ -f "$SOURCE_DIR/sonarqube_architecture" ]; then
  cp "$SOURCE_DIR/sonarqube_architecture" "$SHOWCASE_DIR/public/diagrams/arch_sonarqube.png"
  echo "✓ SonarQube copiado"
fi

if [ -f "$SOURCE_DIR/portal_guia_architecture" ]; then
  cp "$SOURCE_DIR/portal_guia_architecture" "$SHOWCASE_DIR/public/diagrams/app_backoffice_sistemas.png"
  echo "✓ Backoffice copiado"
fi

echo ""
echo "Diagramas faltantes (necesitas generarlos o agregarlos manualmente):"
echo "  - arch_seq_cloudwatch.png"
echo "  - arch_seq_ec2.png"
echo ""
echo "Coloca estos archivos en: $SHOWCASE_DIR/public/diagrams/"
