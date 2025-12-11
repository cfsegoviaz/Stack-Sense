#!/bin/bash

# Script para sincronizar diagramas desde el proyecto principal
# Uso: ./sync-diagrams.sh

DIAGRAMS_SOURCE="../../diagrams"
DIAGRAMS_DEST="./public/diagrams"

echo "🔄 Sincronizando diagramas..."

# Crear directorio si no existe
mkdir -p "$DIAGRAMS_DEST"

# Copiar diagramas de aplicaciones
cp "../api-portal/diagrams/api_portal_azure_devops_amplify.png" "$DIAGRAMS_DEST/app_apiportal.png"
cp "$DIAGRAMS_SOURCE/app_saras.png" "$DIAGRAMS_DEST/"
cp "$DIAGRAMS_SOURCE/arch_sonarqube.png" "$DIAGRAMS_DEST/"
cp "../backoffice-sistemas/diagrams/backoffice_sistemas_hybrid.png" "$DIAGRAMS_DEST/app_backoffice_sistemas.png"
cp "$DIAGRAMS_SOURCE/arch_seq_cloudwatch.png" "$DIAGRAMS_DEST/"
cp "$DIAGRAMS_SOURCE/arch_seq_ec2.png" "$DIAGRAMS_DEST/"

# Copiar diagramas generales
cp "$DIAGRAMS_SOURCE/bgr_aws_architecture.png" "$DIAGRAMS_DEST/"
cp "$DIAGRAMS_SOURCE/migration_flow.png" "$DIAGRAMS_DEST/"

echo "✅ Diagramas sincronizados exitosamente"
echo ""
echo "📊 Diagramas disponibles:"
ls -lh "$DIAGRAMS_DEST"
