#!/usr/bin/env python3
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from datetime import datetime
import os

base_path = "/Users/christian/Projects/escala/stack-sense/training/map-bgr"
output_pdf = f"{base_path}/reports/BGR_Migration_Strategy.pdf"
diagrams_path = f"{base_path}/diagrams"

doc = SimpleDocTemplate(output_pdf, pagesize=letter, rightMargin=0.75*inch, leftMargin=0.75*inch, topMargin=1*inch, bottomMargin=0.75*inch)
styles = getSampleStyleSheet()

# Custom styles
title_style = ParagraphStyle('Title', parent=styles['Heading1'], fontSize=24, textColor=colors.HexColor('#1a1a1a'), spaceAfter=30, alignment=TA_CENTER, fontName='Helvetica-Bold')
h1_style = ParagraphStyle('H1', parent=styles['Heading1'], fontSize=16, textColor=colors.HexColor('#0066cc'), spaceAfter=12, spaceBefore=16, fontName='Helvetica-Bold')
h2_style = ParagraphStyle('H2', parent=styles['Heading2'], fontSize=13, textColor=colors.HexColor('#0066cc'), spaceAfter=10, spaceBefore=10, fontName='Helvetica-Bold')
normal = ParagraphStyle('Normal', parent=styles['Normal'], fontSize=10, spaceAfter=6)
bullet = ParagraphStyle('Bullet', parent=styles['Normal'], fontSize=10, leftIndent=20, spaceAfter=4)

story = []

# COVER PAGE
story.append(Spacer(1, 2*inch))
story.append(Paragraph("BGR Applications", title_style))
story.append(Paragraph("Estrategia de Migración a AWS", title_style))
story.append(Spacer(1, 0.5*inch))
story.append(Paragraph("Lift & Shift vs Modernización", h1_style))
story.append(Spacer(1, 1*inch))
story.append(Paragraph(f"<b>Fecha:</b> 1 de diciembre, 2025", normal))
story.append(Paragraph("<b>Total de Aplicaciones:</b> 6", normal))
story.append(Paragraph("<b>Duración:</b> 12 meses", normal))
story.append(Paragraph("<b>Ahorro Estimado:</b> 49.7% ($31,720/año)", normal))
story.append(PageBreak())

# SECTION 1: RESUMEN EJECUTIVO
story.append(Paragraph("1. Resumen Ejecutivo", h1_style))
story.append(Paragraph("Este documento presenta dos estrategias de migración para las 6 aplicaciones BGR hacia AWS:", normal))
story.append(Spacer(1, 0.1*inch))

exec_data = [
    ["Métrica", "On-Premise", "Lift & Shift", "Modernización"],
    ["Costo Mensual", "$5,320", "$3,990", "$2,677"],
    ["Ahorro", "-", "25%", "49.7%"],
    ["Tiempo Migración", "-", "3-4 meses", "9-12 meses"],
    ["Escalabilidad", "Manual", "Limitada", "Auto-scaling"],
    ["Disponibilidad", "99%", "99.9%", "99.99%"],
]
exec_table = Table(exec_data, colWidths=[1.8*inch, 1.3*inch, 1.3*inch, 1.3*inch])
exec_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0066cc')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 10),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
]))
story.append(exec_table)
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("<b>Recomendación:</b> Estrategia de Modernización para maximizar beneficios a largo plazo.", normal))
story.append(PageBreak())

# SECTION 2: INFRAESTRUCTURA ACTUAL
story.append(Paragraph("2. Infraestructura Actual (On-Premise)", h1_style))
story.append(Paragraph("<b>Servidor Principal: ECBRTSW21</b>", h2_style))

server_data = [
    ["Componente", "Especificación"],
    ["Nombre", "ECBRTSW21"],
    ["Sistema Operativo", "Windows Server 2016 Standard"],
    ["vCPU", "4"],
    ["RAM", "8 GB"],
    ["Storage", "300 GB (2x 150GB disks)"],
    ["Aplicaciones", "6 aplicaciones compartidas"],
]
server_table = Table(server_data, colWidths=[2*inch, 4*inch])
server_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0066cc')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
]))
story.append(server_table)
story.append(Spacer(1, 0.2*inch))

story.append(Paragraph("<b>Aplicaciones Hospedadas:</b>", h2_style))
apps_data = [
    ["#", "Aplicación", "Stack", "Estado"],
    ["1", "PortalGuiaBGR", ".NET Framework 4.7.1", "Obsoleto"],
    ["2", "Api Portal", ".NET Framework 4.7.1", "Obsoleto"],
    ["3", "PortalAdministrativoBGR", ".NET Framework 4.7.1", "Obsoleto"],
    ["4", "Backoffice Sistemas BGR", ".NET Framework 4.7.1", "Obsoleto"],
    ["5", "Backoffice Banca Digital", ".NET Core 8", "Moderno"],
    ["6", "Saras", ".NET Core 8", "Moderno"],
]
apps_table = Table(apps_data, colWidths=[0.4*inch, 2.2*inch, 2*inch, 1.2*inch])
apps_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0066cc')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BACKGROUND', (0, 1), (0, 4), colors.HexColor('#ffcccc')),
    ('BACKGROUND', (0, 5), (0, 6), colors.HexColor('#ccffcc')),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
]))
story.append(apps_table)
story.append(PageBreak())

# SECTION 3: MIGRATION FLOW
story.append(Paragraph("3. Flujo de Migración: Origen → Destino", h1_style))
story.append(Paragraph("El siguiente diagrama muestra el mapeo de servidores on-premise hacia la infraestructura AWS:", normal))
story.append(Spacer(1, 0.2*inch))

if os.path.exists(f"{diagrams_path}/migration_flow.png"):
    img = Image(f"{diagrams_path}/migration_flow.png", width=6.5*inch, height=4*inch)
    story.append(img)
story.append(PageBreak())

# SECTION 4: LIFT & SHIFT
story.append(Paragraph("4. Estrategia 1: Lift & Shift", h1_style))
story.append(Paragraph("<b>Descripción:</b> Migración directa de VMs a EC2 con cambios mínimos.", normal))
story.append(Spacer(1, 0.1*inch))

story.append(Paragraph("<b>Ventajas:</b>", h2_style))
story.append(Paragraph("• Migración rápida (3-4 meses)", bullet))
story.append(Paragraph("• Riesgo bajo - sin cambios de código", bullet))
story.append(Paragraph("• Familiaridad con Windows Server", bullet))
story.append(Paragraph("• Herramientas AWS MGN automatizan proceso", bullet))
story.append(Spacer(1, 0.1*inch))

story.append(Paragraph("<b>Desventajas:</b>", h2_style))
story.append(Paragraph("• Costos de licencias Windows + SQL Server", bullet))
story.append(Paragraph("• No aprovecha servicios managed de AWS", bullet))
story.append(Paragraph("• Escalabilidad limitada", bullet))
story.append(Paragraph("• Deuda técnica persiste (.NET 4.7.1)", bullet))
story.append(Spacer(1, 0.2*inch))

lift_cost_data = [
    ["Componente", "Configuración", "Costo/Mes"],
    ["EC2 Windows", "2x t3.large", "$240"],
    ["RDS SQL Server", "db.m5.large Standard", "$400"],
    ["EBS Storage", "500 GB gp3", "$50"],
    ["Load Balancer", "ALB", "$25"],
    ["Backup", "AWS Backup", "$30"],
    ["<b>Total por App</b>", "", "<b>$665</b>"],
    ["<b>Total 6 Apps</b>", "", "<b>$3,990</b>"],
]
lift_table = Table(lift_cost_data, colWidths=[2*inch, 2.5*inch, 1.3*inch])
lift_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#ff9900')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BACKGROUND', (0, -2), (-1, -1), colors.HexColor('#ffffcc')),
    ('FONTNAME', (0, -2), (-1, -1), 'Helvetica-Bold'),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
]))
story.append(lift_table)
story.append(Spacer(1, 0.1*inch))
story.append(Paragraph("<b>Ahorro vs On-Premise:</b> 25% ($1,330/mes)", normal))
story.append(PageBreak())

# Continue with more sections...
print("Building PDF...")
doc.build(story)
print(f"✅ PDF generated: {output_pdf}")
