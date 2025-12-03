#!/usr/bin/env python3
"""
Convierte archivo RVTools (XLSM/XLSX) a múltiples archivos CSV
"""
import pandas as pd
import sys
from pathlib import Path


def convert_rvtools_to_csv(input_file: str, output_dir: str = None):
    """Convierte cada sheet de RVTools a un archivo CSV separado"""
    
    input_path = Path(input_file)
    
    if not input_path.exists():
        print(f"❌ Archivo no encontrado: {input_file}")
        return
    
    # Directorio de salida
    if output_dir is None:
        output_dir = input_path.parent / f"{input_path.stem}_csv"
    else:
        output_dir = Path(output_dir)
    
    output_dir.mkdir(exist_ok=True)
    
    print(f"📂 Leyendo: {input_path.name}")
    
    try:
        xl_file = pd.ExcelFile(input_file, engine='openpyxl')
        sheets = xl_file.sheet_names
        
        print(f"📊 Sheets encontrados: {len(sheets)}")
        
        for sheet in sheets:
            print(f"   → Procesando: {sheet}...", end=" ")
            
            df = pd.read_excel(xl_file, sheet_name=sheet)
            
            # Limpiar nombre del sheet para archivo
            safe_name = sheet.replace(' ', '_').replace('/', '_')
            output_file = output_dir / f"{safe_name}.csv"
            
            df.to_csv(output_file, index=False, encoding='utf-8')
            print(f"✅ ({len(df)} filas)")
        
        print(f"\n✅ Conversión completa: {output_dir}")
        print(f"📁 {len(sheets)} archivos CSV generados")
        
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python rvtools_to_csv.py <archivo_rvtools.xlsm> [directorio_salida]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None
    
    convert_rvtools_to_csv(input_file, output_dir)
