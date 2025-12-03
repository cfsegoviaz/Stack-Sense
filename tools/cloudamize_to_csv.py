#!/usr/bin/env python3
"""
Convierte archivos Cloudamize (XLSX) a múltiples archivos CSV
Soporta: Observed-Infrastructure y otros exports de Cloudamize OLA
"""
import sys
from pathlib import Path
from zipfile import ZipFile
from xml.etree import ElementTree as ET
import csv


def parse_xlsx_to_csv(xlsx_path: str, output_dir: str = None):
    """Convierte cada sheet de Excel a un archivo CSV separado"""
    
    input_path = Path(xlsx_path)
    
    if not input_path.exists():
        print(f"❌ Archivo no encontrado: {xlsx_path}")
        return
    
    # Directorio de salida
    if output_dir is None:
        output_dir = input_path.parent / f"{input_path.stem}_csv"
    else:
        output_dir = Path(output_dir)
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"📂 Leyendo: {input_path.name}")
    
    try:
        sheets = {}
        
        with ZipFile(input_path) as zf:
            # Leer workbook.xml para nombres de sheets
            wb_xml = zf.read('xl/workbook.xml')
            wb_root = ET.fromstring(wb_xml)
            ns = {'main': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
            
            sheet_names = [
                sheet.get('name')
                for sheet in wb_root.findall('.//main:sheet', ns)
            ]
            
            # Leer strings compartidos
            try:
                strings_xml = zf.read('xl/sharedStrings.xml')
                strings_root = ET.fromstring(strings_xml)
                shared_strings = [
                    ''.join(t.text or '' for t in si.findall('.//main:t', ns))
                    for si in strings_root.findall('.//main:si', ns)
                ]
            except KeyError:
                shared_strings = []
            
            # Procesar cada sheet
            for idx, sheet_name in enumerate(sheet_names, 1):
                try:
                    sheet_xml = zf.read(f'xl/worksheets/sheet{idx}.xml')
                    sheet_data = _parse_sheet(sheet_xml, shared_strings, ns)
                    sheets[sheet_name] = sheet_data
                except Exception as e:
                    print(f"⚠️  Error procesando {sheet_name}: {e}")
        
        print(f"📊 Sheets encontrados: {len(sheets)}")
        
        # Exportar a CSV
        exported = 0
        for sheet_name, data in sheets.items():
            if not data:
                continue
            
            safe_name = sheet_name.replace(' ', '_').replace('/', '_')
            csv_path = output_dir / f"{safe_name}.csv"
            
            with open(csv_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerows(data)
            
            print(f"   → {sheet_name}: ✅ ({len(data)} filas)")
            exported += 1
        
        print(f"\n✅ Conversión completa: {output_dir}")
        print(f"📁 {exported} archivos CSV generados")
        
    except Exception as e:
        print(f"❌ Error: {e}")


def _parse_sheet(xml_data, shared_strings, ns):
    """Parse una hoja individual de Excel"""
    root = ET.fromstring(xml_data)
    rows = []
    
    for row in root.findall('.//main:row', ns):
        row_data = []
        for cell in row.findall('.//main:c', ns):
            value = ''
            cell_type = cell.get('t')
            v_elem = cell.find('.//main:v', ns)
            
            if v_elem is not None:
                if cell_type == 's':  # String compartido
                    idx = int(v_elem.text)
                    value = shared_strings[idx] if idx < len(shared_strings) else ''
                else:
                    value = v_elem.text or ''
            
            row_data.append(value)
        
        if any(row_data):  # Solo filas no vacías
            rows.append(row_data)
    
    return rows


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python cloudamize_to_csv.py <archivo.xlsx> [directorio_salida]")
        print("\nEjemplos:")
        print("  python cloudamize_to_csv.py Observed-Infrastructure.xlsx")
        print("  python cloudamize_to_csv.py Observed-Infrastructure.xlsx output/")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None
    
    parse_xlsx_to_csv(input_file, output_dir)
