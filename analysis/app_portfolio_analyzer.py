#!/usr/bin/env python3
"""
Analizador de Portafolio de Aplicaciones BGR
Extrae información técnica de exports HTML y genera análisis de modernización
"""

import re
import json
from pathlib import Path
from html.parser import HTMLParser
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional

@dataclass
class Application:
    name: str
    description: str
    framework: str
    language: str
    version: str
    database: str
    db_version: str
    servers: List[str]
    users: int
    architecture: str
    dependencies: List[str]
    obsolete: bool
    modernization_priority: str
    
class HTMLTableParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_td = False
        self.current_data = []
        self.rows = []
        
    def handle_starttag(self, tag, attrs):
        if tag == 'td':
            self.in_td = True
            
    def handle_endtag(self, tag):
        if tag == 'td':
            self.in_td = False
        elif tag == 'tr' and self.current_data:
            self.rows.append(self.current_data)
            self.current_data = []
            
    def handle_data(self, data):
        if self.in_td:
            self.current_data.append(data.strip())

def extract_value(rows, keyword):
    """Extrae valor de las filas buscando keyword"""
    for row in rows:
        if len(row) >= 2 and keyword.lower() in row[0].lower():
            return row[1] if row[1] else "N/A"
    return "N/A"

def extract_servers(rows):
    """Extrae lista de servidores"""
    servers = []
    for row in rows:
        if len(row) >= 2 and 'servidor' in row[0].lower():
            server_text = row[1]
            servers.extend([s.strip() for s in re.findall(r'ECB[A-Z0-9]+', server_text)])
    return list(set(servers))

def extract_dependencies(rows):
    """Extrae dependencias de otras aplicaciones/servicios"""
    deps = []
    keywords = ['dependencia', 'integra', 'consume', 'servicio']
    for row in rows:
        if len(row) >= 2 and any(k in row[0].lower() for k in keywords):
            deps.append(row[1])
    return [d for d in deps if d and d != "N/A"]

def analyze_html(file_path: Path) -> Application:
    """Analiza un archivo HTML y extrae información de la aplicación"""
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    parser = HTMLTableParser()
    parser.feed(html)
    rows = parser.rows
    
    # Extraer información clave
    name = extract_value(rows, "nombre")
    if name == "N/A":
        name = file_path.stem.replace("G.I-", "").replace("G.I.-", "")
    
    framework = extract_value(rows, "framework")
    language = extract_value(rows, "lenguaje")
    version = extract_value(rows, "versión")
    database = extract_value(rows, "base de datos")
    db_version = extract_value(rows, "versión bd")
    architecture = extract_value(rows, "arquitectura")
    description = extract_value(rows, "descripción")
    
    users_str = extract_value(rows, "usuarios")
    users = int(re.search(r'\d+', users_str).group()) if re.search(r'\d+', users_str) else 0
    
    servers = extract_servers(rows)
    dependencies = extract_dependencies(rows)
    
    # Determinar si es obsoleto
    obsolete = any([
        "4.7" in version or "3.5" in version,
        "2016" in db_version or "2014" in db_version,
        "ajaxtoolkit" in html.lower()
    ])
    
    # Prioridad de modernización
    if obsolete and users > 500:
        priority = "ALTA"
    elif obsolete:
        priority = "MEDIA"
    else:
        priority = "BAJA"
    
    return Application(
        name=name,
        description=description,
        framework=framework,
        language=language,
        version=version,
        database=database,
        db_version=db_version,
        servers=servers,
        users=users,
        architecture=architecture,
        dependencies=dependencies,
        obsolete=obsolete,
        modernization_priority=priority
    )

def generate_report(apps: List[Application]) -> str:
    """Genera reporte de análisis del portafolio"""
    report = []
    report.append("=" * 80)
    report.append("ANÁLISIS DE PORTAFOLIO DE APLICACIONES BGR")
    report.append(f"Fecha: 2025-12-01")
    report.append(f"Total Aplicaciones: {len(apps)}")
    report.append("=" * 80)
    report.append("")
    
    # Resumen ejecutivo
    obsolete_count = sum(1 for app in apps if app.obsolete)
    total_users = sum(app.users for app in apps)
    
    report.append("## RESUMEN EJECUTIVO")
    report.append(f"- Aplicaciones obsoletas: {obsolete_count}/{len(apps)}")
    report.append(f"- Usuarios totales: {total_users:,}")
    report.append(f"- Prioridad ALTA: {sum(1 for a in apps if a.modernization_priority == 'ALTA')}")
    report.append(f"- Prioridad MEDIA: {sum(1 for a in apps if a.modernization_priority == 'MEDIA')}")
    report.append("")
    
    # Detalle por aplicación
    report.append("## DETALLE POR APLICACIÓN")
    report.append("")
    
    for i, app in enumerate(apps, 1):
        report.append(f"### {i}. {app.name}")
        report.append(f"**Prioridad:** {app.modernization_priority}")
        report.append(f"**Stack:** {app.language} {app.framework} {app.version}")
        report.append(f"**Base de Datos:** {app.database} {app.db_version}")
        report.append(f"**Arquitectura:** {app.architecture}")
        report.append(f"**Usuarios:** {app.users:,}")
        report.append(f"**Servidores:** {', '.join(app.servers) if app.servers else 'N/A'}")
        report.append(f"**Obsoleto:** {'SÍ' if app.obsolete else 'NO'}")
        if app.dependencies:
            report.append(f"**Dependencias:** {len(app.dependencies)} identificadas")
        report.append("")
    
    return "\n".join(report)

def main():
    base_path = Path("training/map-bgr")
    html_files = sorted(base_path.glob("G.I*.html"))
    
    print(f"Analizando {len(html_files)} aplicaciones...\n")
    
    apps = []
    for file in html_files:
        print(f"Procesando: {file.name}")
        app = analyze_html(file)
        apps.append(app)
    
    # Generar reporte
    report = generate_report(apps)
    
    # Guardar reporte
    output_path = Path("reports/bgr_app_portfolio_analysis.txt")
    output_path.parent.mkdir(exist_ok=True)
    output_path.write_text(report, encoding='utf-8')
    
    # Guardar JSON
    json_path = Path("reports/bgr_app_portfolio_analysis.json")
    json_data = [asdict(app) for app in apps]
    json_path.write_text(json.dumps(json_data, indent=2, ensure_ascii=False), encoding='utf-8')
    
    print(f"\n✅ Análisis completado")
    print(f"📄 Reporte: {output_path}")
    print(f"📊 JSON: {json_path}")
    print(f"\n{report}")

if __name__ == "__main__":
    main()
