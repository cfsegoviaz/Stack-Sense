#!/usr/bin/env python3
import re
from pathlib import Path
import json

def clean_text(text):
    """Limpia texto HTML"""
    text = re.sub(r'<br\s*/?>', '\n', text)
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'&quot;', '"', text)
    text = re.sub(r'&amp;', '&', text)
    return text.strip()

def extract_app_data(html_file):
    """Extrae datos de aplicación desde HTML"""
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    data = {'archivo': html_file.name}
    
    # Extraer nombre
    match = re.search(r'<td[^>]*>Nombre APP</td>\s*<td[^>]*>([^<]+)</td>', html)
    if match:
        data['nombre'] = clean_text(match.group(1))
    
    # Extraer descripción
    match = re.search(r'<td[^>]*>Descripción\s*</td>\s*<td[^>]*>([^<]+)</td>', html)
    if match:
        data['descripcion'] = clean_text(match.group(1))
    
    # Buscar la fila con "Productiva"
    prod_match = re.search(
        r'<td[^>]*>Productiva</td>\s*<td[^>]*>([^<]+)</td>\s*<td[^>]*>([^<]+)</td>\s*<td[^>]*>(.*?)</td>',
        html, re.DOTALL
    )
    
    if prod_match:
        data['arquitectura'] = clean_text(prod_match.group(1))
        data['fabricante'] = clean_text(prod_match.group(2))
        data['dependencias'] = clean_text(prod_match.group(3))
    
    # Extraer frontend
    match = re.search(r'<td[^>]*>ASP\.NET C#</td>\s*<td[^>]*>([^<]+)</td>', html)
    if match:
        data['frontend'] = "ASP.NET C#"
        data['frontend_version'] = clean_text(match.group(1))
    
    # Extraer backend
    match = re.search(r'<td[^>]*>C#</td>\s*<td[^>]*>(\.NET Framework[^<]+)</td>', html)
    if match:
        data['backend'] = "C#"
        data['backend_version'] = clean_text(match.group(1))
    
    # Extraer base de datos
    match = re.search(r'<td[^>]*>MICROSOFT SQL SERVER\s*</td>\s*<td[^>]*>([^<]+)</td>', html)
    if match:
        data['database'] = "Microsoft SQL Server"
        data['database_version'] = clean_text(match.group(1))
    
    # Extraer SO
    match = re.search(r'<td[^>]*>WINDOWS SERVER ([^<]+)</td>', html)
    if match:
        data['so_version'] = f"Windows Server {clean_text(match.group(1))}"
    
    # Extraer servidores
    match = re.search(r'<td[^>]*>Producción<br>.*?(ECB[^<]+)</td>', html, re.DOTALL)
    if match:
        servers_text = clean_text(match.group(1))
        data['servidores'] = [s.strip() for s in re.findall(r'ECB\w+', servers_text)]
    
    # Determinar obsolescencia
    if 'backend_version' in data and ('4.7' in data['backend_version'] or '4.5' in data['backend_version']):
        data['backend_obsoleto'] = 'Si'
    
    if 'database_version' in data and '2016' in data['database_version']:
        data['db_obsoleto'] = 'Si (2016 - Soporte extendido hasta 2026)'
    
    return data

def main():
    base_path = Path("training/map-bgr")
    html_files = sorted(base_path.glob("G.I*.html"))
    
    all_apps = []
    
    print("=" * 80)
    print("ANÁLISIS DE APLICACIONES BGR - MODERNIZACIÓN AWS")
    print("=" * 80)
    print()
    
    for html_file in html_files:
        print(f"📄 {html_file.name}")
        data = extract_app_data(html_file)
        all_apps.append(data)
        
        print(f"   Nombre: {data.get('nombre', 'N/A')}")
        print(f"   Stack: {data.get('backend', 'N/A')} {data.get('backend_version', 'N/A')}")
        print(f"   DB: {data.get('database', 'N/A')} {data.get('database_version', 'N/A')}")
        print(f"   Arquitectura: {data.get('arquitectura', 'N/A')}")
        print()
    
    # Guardar JSON
    output_json = Path("reports/bgr_applications.json")
    output_json.parent.mkdir(exist_ok=True)
    output_json.write_text(json.dumps(all_apps, indent=2, ensure_ascii=False))
    
    # Generar reporte markdown
    report = []
    report.append("# Análisis de Aplicaciones BGR para Modernización AWS\n\n")
    report.append(f"**Fecha:** 2025-12-01\n")
    report.append(f"**Total de aplicaciones:** {len(all_apps)}\n\n")
    
    report.append("## 📊 Resumen Ejecutivo\n\n")
    
    dotnet_apps = [a for a in all_apps if '.NET' in a.get('backend_version', '')]
    obsolete_apps = [a for a in all_apps if a.get('backend_obsoleto') == 'Si']
    
    report.append(f"- **Aplicaciones .NET:** {len(dotnet_apps)}/{len(all_apps)}\n")
    report.append(f"- **Stack obsoleto:** {len(obsolete_apps)}/{len(all_apps)}\n")
    report.append(f"- **Arquitectura predominante:** Capas (N-Tier)\n")
    report.append(f"- **Base de datos:** SQL Server 2016 Enterprise\n\n")
    
    report.append("### Recomendación General\n\n")
    report.append("Todas las aplicaciones requieren modernización. Estrategias recomendadas:\n\n")
    report.append("1. **Replatform:** Migrar a .NET 6/8 + contenedores (ECS/EKS)\n")
    report.append("2. **Database:** Migrar a Amazon RDS for SQL Server o Aurora PostgreSQL\n")
    report.append("3. **Infraestructura:** Eliminar dependencia de Windows Server\n")
    report.append("4. **Servicios Managed:** Reemplazar componentes con servicios AWS\n\n")
    
    report.append("---\n\n")
    report.append("## 📋 Detalle por Aplicación\n\n")
    
    for i, app in enumerate(all_apps, 1):
        report.append(f"### {i}. {app.get('nombre', 'Sin nombre')}\n\n")
        
        if app.get('descripcion'):
            report.append(f"**Descripción:** {app.get('descripcion')}\n\n")
        
        report.append("#### Stack Técnico Actual\n\n")
        report.append("| Componente | Tecnología | Versión | Estado |\n")
        report.append("|------------|------------|---------|--------|\n")
        report.append(f"| Frontend | {app.get('frontend', 'N/A')} | {app.get('frontend_version', 'N/A')} | {'⚠️ Obsoleto' if app.get('backend_obsoleto') else '✅'} |\n")
        report.append(f"| Backend | {app.get('backend', 'N/A')} | {app.get('backend_version', 'N/A')} | {'⚠️ Obsoleto' if app.get('backend_obsoleto') else '✅'} |\n")
        report.append(f"| Base de Datos | {app.get('database', 'N/A')} | {app.get('database_version', 'N/A')} | {'⚠️ Soporte extendido' if app.get('db_obsoleto') else '✅'} |\n")
        report.append(f"| SO | {app.get('so_version', 'N/A')} | - | ⚠️ Windows |\n\n")
        
        report.append(f"**Arquitectura:** {app.get('arquitectura', 'N/A')}\n\n")
        
        if app.get('servidores'):
            report.append(f"**Servidores:** {', '.join(app['servidores'][:3])}\n\n")
        
        if app.get('dependencias'):
            report.append("**Dependencias:**\n")
            deps = app['dependencias'].split('\n')
            for dep in deps[:4]:
                if dep.strip():
                    report.append(f"- {dep.strip()}\n")
            report.append("\n")
        
        # Recomendaciones específicas
        report.append("#### 🎯 Estrategia de Modernización Recomendada\n\n")
        
        if '.NET Framework 4' in app.get('backend_version', ''):
            report.append("**Fase 1: Modernización de Código**\n")
            report.append("- Migrar de .NET Framework 4.7.1 a .NET 8\n")
            report.append("- Refactorizar dependencias obsoletas (ajaxToolkit → componentes modernos)\n")
            report.append("- Implementar arquitectura de microservicios si aplica\n\n")
            
            report.append("**Fase 2: Containerización**\n")
            report.append("- Dockerizar aplicación (.NET 8 en Linux containers)\n")
            report.append("- Desplegar en Amazon ECS con Fargate o EKS\n")
            report.append("- Implementar Application Load Balancer\n\n")
            
            report.append("**Fase 3: Base de Datos**\n")
            report.append("- Opción A: Amazon RDS for SQL Server (compatibilidad total)\n")
            report.append("- Opción B: Migrar a Amazon Aurora PostgreSQL (mayor ahorro)\n")
            report.append("- Implementar backups automáticos y Multi-AZ\n\n")
            
            report.append("**Fase 4: Servicios Managed**\n")
            report.append("- Active Directory → AWS Managed Microsoft AD o Amazon Cognito\n")
            report.append("- Configuración centralizada → AWS Systems Manager Parameter Store\n")
            report.append("- Notificaciones → Amazon SNS/SQS\n\n")
        
        report.append("---\n\n")
    
    # Sección de costos estimados
    report.append("## 💰 Estimación de Costos (por aplicación)\n\n")
    report.append("### Opción 1: Lift & Shift (EC2 + RDS SQL Server)\n")
    report.append("- **Compute:** 2x t3.large (Windows) = ~$240/mes\n")
    report.append("- **Database:** RDS SQL Server Standard (db.m5.large) = ~$400/mes\n")
    report.append("- **Load Balancer:** ALB = ~$25/mes\n")
    report.append("- **Total estimado:** ~$665/mes por aplicación\n\n")
    
    report.append("### Opción 2: Modernización (ECS + RDS SQL Server)\n")
    report.append("- **Compute:** ECS Fargate (2 vCPU, 4GB) = ~$60/mes\n")
    report.append("- **Database:** RDS SQL Server Standard (db.m5.large) = ~$400/mes\n")
    report.append("- **Load Balancer:** ALB = ~$25/mes\n")
    report.append("- **Total estimado:** ~$485/mes por aplicación (27% ahorro)\n\n")
    
    report.append("### Opción 3: Modernización Completa (ECS + Aurora PostgreSQL)\n")
    report.append("- **Compute:** ECS Fargate (2 vCPU, 4GB) = ~$60/mes\n")
    report.append("- **Database:** Aurora PostgreSQL (db.r5.large) = ~$180/mes\n")
    report.append("- **Load Balancer:** ALB = ~$25/mes\n")
    report.append("- **Total estimado:** ~$265/mes por aplicación (60% ahorro)\n\n")
    
    report.append(f"**Ahorro anual estimado (8 aplicaciones, Opción 3):** ~$38,400 USD\n\n")
    
    output_md = Path("reports/bgr_applications_modernization.md")
    output_md.write_text(''.join(report))
    
    print(f"\n✅ Análisis completado")
    print(f"📊 JSON: {output_json}")
    print(f"📄 Reporte: {output_md}")
    print(f"\nPróximos pasos:")
    print(f"  1. Revisar el reporte de modernización")
    print(f"  2. Priorizar aplicaciones por impacto de negocio")
    print(f"  3. Crear plan de migración detallado por aplicación")

if __name__ == "__main__":
    main()
