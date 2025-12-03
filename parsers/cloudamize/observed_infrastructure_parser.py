#!/usr/bin/env python3
"""
Cloudamize Observed Infrastructure Parser
Extrae datos del archivo Observed-Infrastructure.xlsx del OLA de Cloudamize
"""
import sys
import csv
from pathlib import Path
from zipfile import ZipFile
from xml.etree import ElementTree as ET


class CloudamizeObservedInfraParser:
    def __init__(self, xlsx_path: str):
        self.xlsx_path = Path(xlsx_path)
        self.sheets = {}
        
    def parse(self):
        """Parse Excel file y extrae todas las pestañas"""
        with ZipFile(self.xlsx_path) as zf:
            # Leer workbook.xml para obtener nombres de sheets
            wb_xml = zf.read('xl/workbook.xml')
            wb_root = ET.fromstring(wb_xml)
            
            # Namespace de Excel
            ns = {'main': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
            
            # Obtener nombres de sheets
            sheet_names = []
            for sheet in wb_root.findall('.//main:sheet', ns):
                sheet_names.append(sheet.get('name'))
            
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
                    sheet_data = self._parse_sheet(sheet_xml, shared_strings, ns)
                    self.sheets[sheet_name] = sheet_data
                except Exception as e:
                    print(f"Error procesando {sheet_name}: {e}", file=sys.stderr)
        
        return self.sheets
    
    def _parse_sheet(self, xml_data, shared_strings, ns):
        """Parse una hoja individual"""
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
            
            if any(row_data):  # Solo agregar filas no vacías
                rows.append(row_data)
        
        return rows
    
    def export_to_csv(self, output_dir: str):
        """Exporta cada sheet a un archivo CSV"""
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        exported = []
        for sheet_name, data in self.sheets.items():
            if not data:
                continue
            
            # Sanitizar nombre de archivo
            safe_name = sheet_name.replace(' ', '_').replace('/', '_')
            csv_path = output_path / f"{safe_name}.csv"
            
            with open(csv_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerows(data)
            
            exported.append(str(csv_path))
            print(f"✓ Exportado: {csv_path} ({len(data)} filas)")
        
        return exported


def main():
    if len(sys.argv) < 2:
        print("Uso: python3 observed_infrastructure_parser.py <archivo.xlsx> [output_dir]")
        sys.exit(1)
    
    xlsx_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else f"{Path(xlsx_file).stem}_csv"
    
    print(f"Parseando: {xlsx_file}")
    parser = CloudamizeObservedInfraParser(xlsx_file)
    sheets = parser.parse()
    
    print(f"\nPestañas encontradas: {len(sheets)}")
    for name in sheets.keys():
        print(f"  - {name}")
    
    print(f"\nExportando a CSV en: {output_dir}")
    exported = parser.export_to_csv(output_dir)
    
    print(f"\n✓ Completado: {len(exported)} archivos CSV generados")


if __name__ == '__main__':
    main()
