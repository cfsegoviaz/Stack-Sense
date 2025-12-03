#!/usr/bin/env python3
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib.enums import TA_CENTER

base_path = "/Users/christian/Projects/escala/stack-sense/training/map-bgr"
output_pdf = f"{base_path}/reports/BGR_Migration_Strategy_Complete.pdf"
diagrams_path = f"{base_path}/diagrams"

doc = SimpleDocTemplate(output_pdf, pagesize=letter, rightMargin=0.75*inch, leftMargin=0.75*inch, topMargin=1*inch, bottomMargin=0.75*inch)

# Styles
title_style = ParagraphStyle('Title', fontSize=24, textColor=colors.HexColor('#1a1a1a'), spaceAfter=30, alignment=TA_CENTER, fontName='Helvetica-Bold')
h1_style = ParagraphStyle('H1', fontSize=16, textColor=colors.HexColor('#0066cc'), spaceAfter=12, spaceBefore=16, fontName='Helvetica-Bold')
h2_style = ParagraphStyle('H2', fontSize=13, textColor=colors.HexColor('#0066cc'), spaceAfter=10, spaceBefore=10, fontName='Helvetica-Bold')
normal = ParagraphStyle('Normal', fontSize=10, spaceAfter=6)
bullet = ParagraphStyle('Bullet', fontSize=10, leftIndent=20, spaceAfter=4)

story = []

# COVER
story.append(Spacer(1, 2*inch))
story.append(Paragraph("BGR Applications", title_style))
story.append(Paragraph("Estrategia de Migración a AWS", title_style))
story.append(Spacer(1, 0.5*inch))
story.append(Paragraph("Lift & Shift vs Modernización", h1_style))
story.append(Spacer(1, 1*inch))
story.append(Paragraph("<b>Fecha:</b> 1 de diciembre, 2025", normal))
story.append(Paragraph("<b>Aplicaciones:</b> 6", normal))
story.append(Paragraph("<b>Duración:</b> 12 meses", normal))
story.append(Paragraph("<b>Ahorro:</b> 49.7% ($31,720/año)", normal))
story.append(PageBreak())

# EXECUTIVE SUMMARY
story.append(Paragraph("Resumen Ejecutivo", h1_style))
story.append(Paragraph("Comparativa de estrategias de migración:", normal))
story.append(Spacer(1, 0.1*inch))

exec_data = [
    ["Métrica", "On-Premise", "Lift & Shift", "Modernización"],
    ["Costo Mensual", "$5,320", "$3,990", "$2,677"],
    ["Ahorro Anual", "-", "$15,960", "$31,720"],
    ["Tiempo", "-", "3-4 meses", "9-12 meses"],
    ["Escalabilidad", "Manual", "Limitada", "Auto-scaling"],
    ["Disponibilidad", "99%", "99.9%", "99.99%"],
    ["Deuda Técnica", "Alta", "Alta", "Eliminada"],
]
exec_table = Table(exec_data, colWidths=[1.8*inch, 1.3*inch, 1.3*inch, 1.3*inch])
exec_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0066cc')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
]))
story.append(exec_table)
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("<b>✅ Recomendación:</b> Estrategia de Modernización", normal))
story.append(PageBreak())

# INFRASTRUCTURE
story.append(Paragraph("Infraestructura Actual", h1_style))
story.append(Paragraph("<b>Servidor: ECBRTSW21</b>", h2_style))

server_data = [
    ["vCPU", "4"], ["RAM", "8 GB"], ["Storage", "300 GB"],
    ["OS", "Windows Server 2016"], ["Apps", "6 aplicaciones"],
]
server_table = Table(server_data, colWidths=[2*inch, 4*inch])
server_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#0066cc')),
    ('TEXTCOLOR', (0, 0), (0, -1), colors.whitesmoke),
    ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
]))
story.append(server_table)
story.append(Spacer(1, 0.2*inch))

apps_data = [
    ["Aplicación", "Stack", "Estado"],
    ["PortalGuiaBGR", ".NET 4.7.1", "⚠️ Obsoleto"],
    ["Api Portal", ".NET 4.7.1", "⚠️ Obsoleto"],
    ["PortalAdministrativoBGR", ".NET 4.7.1", "⚠️ Obsoleto"],
    ["Backoffice Sistemas", ".NET 4.7.1", "⚠️ Obsoleto"],
    ["Backoffice Banca", ".NET Core 8", "✅ Moderno"],
    ["Saras", ".NET Core 8", "✅ Moderno"],
]
apps_table = Table(apps_data, colWidths=[2.5*inch, 2*inch, 1.3*inch])
apps_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0066cc')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
]))
story.append(apps_table)
story.append(PageBreak())

# MIGRATION FLOW
story.append(Paragraph("Flujo de Migración", h1_style))
if os.path.exists(f"{diagrams_path}/migration_flow.png"):
    story.append(Image(f"{diagrams_path}/migration_flow.png", width=6.5*inch, height=4*inch))
story.append(PageBreak())

# LIFT & SHIFT
story.append(Paragraph("Estrategia 1: Lift & Shift", h1_style))
story.append(Paragraph("Migración directa de VMs a EC2 sin cambios de código.", normal))
story.append(Spacer(1, 0.1*inch))
story.append(Paragraph("<b>✅ Ventajas:</b>", h2_style))
story.append(Paragraph("• Rápido (3-4 meses)", bullet))
story.append(Paragraph("• Bajo riesgo", bullet))
story.append(Paragraph("• Sin cambios de código", bullet))
story.append(Spacer(1, 0.1*inch))
story.append(Paragraph("<b>❌ Desventajas:</b>", h2_style))
story.append(Paragraph("• Licencias Windows/SQL Server", bullet))
story.append(Paragraph("• Deuda técnica persiste", bullet))
story.append(Paragraph("• Escalabilidad limitada", bullet))
story.append(Spacer(1, 0.2*inch))

lift_data = [
    ["Componente", "Costo/Mes"],
    ["EC2 Windows (t3.large)", "$240"],
    ["RDS SQL Server", "$400"],
    ["Storage + Backup", "$80"],
    ["Load Balancer", "$25"],
    ["<b>Total/App</b>", "<b>$665</b>"],
    ["<b>Total 6 Apps</b>", "<b>$3,990</b>"],
]
lift_table = Table(lift_data, colWidths=[3.5*inch, 2.3*inch])
lift_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#ff9900')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTNAME', (0, -2), (-1, -1), 'Helvetica-Bold'),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
]))
story.append(lift_table)
story.append(PageBreak())

# MODERNIZATION
story.append(Paragraph("Estrategia 2: Modernización", h1_style))
story.append(Paragraph("Migración a contenedores con .NET 8 en ECS Fargate.", normal))
story.append(Spacer(1, 0.1*inch))
story.append(Paragraph("<b>✅ Ventajas:</b>", h2_style))
story.append(Paragraph("• 49.7% ahorro de costos", bullet))
story.append(Paragraph("• Auto-scaling automático", bullet))
story.append(Paragraph("• 99.99% disponibilidad", bullet))
story.append(Paragraph("• Elimina deuda técnica", bullet))
story.append(Paragraph("• Sin licencias Windows", bullet))
story.append(Spacer(1, 0.1*inch))
story.append(Paragraph("<b>⚠️ Consideraciones:</b>", h2_style))
story.append(Paragraph("• Requiere modernización de código", bullet))
story.append(Paragraph("• Mayor tiempo (9-12 meses)", bullet))
story.append(Paragraph("• Capacitación del equipo", bullet))
story.append(Spacer(1, 0.2*inch))

mod_data = [
    ["Componente", "Costo/Mes"],
    ["ECS Fargate", "$216"],
    ["RDS SQL Server", "$175"],
    ["Load Balancer", "$8"],
    ["Shared Services", "$8"],
    ["<b>Total/App</b>", "<b>$407</b>"],
    ["<b>Total 6 Apps</b>", "<b>$2,677</b>"],
]
mod_table = Table(mod_data, colWidths=[3.5*inch, 2.3*inch])
mod_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#00cc66')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTNAME', (0, -2), (-1, -1), 'Helvetica-Bold'),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
]))
story.append(mod_table)
story.append(PageBreak())

# INDIVIDUAL ARCHITECTURES
apps = [
    ("PortalGuiaBGR", "app_portalguiabgr.png", "3 tasks, 2v/4GB", "$407"),
    ("Api Portal", "app_apiportal.png", "5 tasks, 2v/4GB", "$552"),
    ("PortalAdministrativoBGR", "app_portaladministrativo.png", "2 tasks, 1v/2GB", "$263"),
    ("Backoffice Sistemas", "app_backoffice_sistemas.png", "3 tasks, 2v/4GB", "$407"),
    ("Backoffice Banca", "app_backoffice_banca.png", "3 tasks, 2v/4GB", "$559"),
    ("Saras", "app_saras.png", "2 tasks, 2v/4GB", "$487"),
]

for app_name, diagram, config, cost in apps:
    story.append(Paragraph(f"Arquitectura: {app_name}", h1_style))
    story.append(Paragraph(f"<b>Configuración:</b> {config}", normal))
    story.append(Paragraph(f"<b>Costo mensual:</b> {cost}", normal))
    story.append(Spacer(1, 0.1*inch))
    if os.path.exists(f"{diagrams_path}/{diagram}"):
        story.append(Image(f"{diagrams_path}/{diagram}", width=6.5*inch, height=3.5*inch))
    story.append(PageBreak())

# COST SUMMARY
story.append(Paragraph("Resumen de Costos", h1_style))
cost_data = [
    ["Aplicación", "Lift & Shift", "Modernización", "Ahorro"],
    ["PortalGuiaBGR", "$665", "$407", "$258 (39%)"],
    ["Api Portal", "$665", "$552", "$113 (17%)"],
    ["PortalAdministrativoBGR", "$665", "$263", "$402 (60%)"],
    ["Backoffice Sistemas", "$665", "$407", "$258 (39%)"],
    ["Backoffice Banca", "$665", "$559", "$106 (16%)"],
    ["Saras", "$665", "$487", "$178 (27%)"],
    ["<b>TOTAL</b>", "<b>$3,990</b>", "<b>$2,677</b>", "<b>$1,313</b>"],
]
cost_table = Table(cost_data, colWidths=[2*inch, 1.3*inch, 1.3*inch, 1.3*inch])
cost_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0066cc')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
    ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#ccffcc')),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
]))
story.append(cost_table)
story.append(PageBreak())

# TIMELINE
story.append(Paragraph("Plan de Implementación", h1_style))
timeline_data = [
    ["Fase", "Duración", "Actividades"],
    ["Mes 0", "1 mes", "Setup AWS, VPC, IAM"],
    ["Ola 1", "3 meses", "PortalGuiaBGR, Api Portal"],
    ["Ola 2", "3 meses", "PortalAdm, Backoffice Sistemas"],
    ["Ola 3", "3 meses", "Backoffice Banca, Saras"],
    ["Cierre", "2 meses", "Optimización, Decommission"],
]
timeline_table = Table(timeline_data, colWidths=[1.5*inch, 1.5*inch, 3*inch])
timeline_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0066cc')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
]))
story.append(timeline_table)

print("Building complete PDF...")
doc.build(story)
print(f"✅ Complete PDF generated: {output_pdf}")
