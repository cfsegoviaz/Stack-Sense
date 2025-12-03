#!/bin/bash
# Helper script para proyecto MAP-BGR

PROJECT_DIR="/Users/christian/Projects/escala/stack-sense/training/map-bgr"
CSV_DIR="$PROJECT_DIR/RVTools_export_all_250709_064325_DCP_csv"

echo "🚀 MAP-BGR Helper"
echo "=================="
echo ""

case "$1" in
  "status")
    echo "📊 Estado del Proyecto:"
    echo ""
    echo "Archivos CSV: $(ls -1 $CSV_DIR/*.csv 2>/dev/null | wc -l)"
    echo "Reportes: $(ls -1 $PROJECT_DIR/reports/*.{json,csv,xlsx,md} 2>/dev/null | wc -l)"
    echo "Diagramas: $(ls -1 $PROJECT_DIR/diagrams/*.{png,svg} 2>/dev/null | wc -l)"
    echo "Docs: $(ls -1 $PROJECT_DIR/docs/*.{md,pdf} 2>/dev/null | wc -l)"
    echo ""
    ;;
    
  "summary")
    echo "📈 Resumen Rápido de Producción:"
    cd /Users/christian/Projects/escala/stack-sense
    source venv/bin/activate 2>/dev/null
    python3 << 'EOF'
import pandas as pd
df = pd.read_csv('training/map-bgr/RVTools_export_all_250709_064325_DCP_csv/vInfo.csv')
print(f"VMs: {len(df)} | vCPUs: {df['# CPU'].sum()} | RAM: {df['Memory'].sum()/1024:.0f} GB")
print(f"Encendidas: {len(df[df['Powerstate']=='poweredOn'])} | Apagadas: {len(df[df['Powerstate']=='poweredOff'])}")
EOF
    ;;
    
  "progress")
    cat $PROJECT_DIR/PROGRESS.md
    ;;
    
  "plan")
    cat $PROJECT_DIR/PLAN_MIGRACION.md
    ;;
    
  *)
    echo "Comandos disponibles:"
    echo "  ./helper.sh status    - Estado de archivos generados"
    echo "  ./helper.sh summary   - Resumen rápido de VMs"
    echo "  ./helper.sh progress  - Ver progreso del proyecto"
    echo "  ./helper.sh plan      - Ver plan de migración"
    echo ""
    ;;
esac
