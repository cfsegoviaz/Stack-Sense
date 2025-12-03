#!/usr/bin/env python3
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from datetime import datetime
import os

# Paths
base_path = "/Users/christian/Projects/escala/stack-sense/training/map-bgr"
output_pdf = f"{base_path}/reports/BGR_Migration_Strategy.pdf"
diagrams_path = f"{base_path}/diagrams"

# Create PDF
doc = SimpleDocTemplate(output_pdf, pagesize=letter,
                        rightMargin=0.75*inch, leftMargin=0.75*inch,
                        topMargin=1*inch, bottomMargin=0.75*inch)

# Styles
styles = getSampleStyleSheet()
title_style = ParagraphStyle('CustomTitle', parent=styles['Heading1'], fontSize=24, textColor=colors.HexColor('#1a1a1a'), spaceAfter=30, alignment=TA_CENTER)
heading1_style = ParagraphStyle('CustomHeading1', parent=styles['Heading1'], fontSize=18, textColor=colors.HexColor('#0066cc'), spaceAfter=12, spaceBefore=12)
heading2_style = ParagraphStyle('CustomHeading2', parent=styles['Heading2'], fontSize=14, textColor=colors.HexColor('#0066cc'), spaceAfter=10, spaceBefore=10)
normal_style = ParagraphStyle('CustomNormal', parent=styles['Normal'], fontSize=10, alignment=TA_JUSTIFY, spaceAfter=6)
bullet_style = ParagraphStyle('CustomBullet', parent=styles['Normal'], fontSize=10, leftIndent=20, spaceAfter=6)

story = []

# Cover Page
story.append(Spacer(1, 2*inch))
story.append(Paragraph("BGR Applications", title_style))
story.append(Paragraph("Estrategia de Migración a AWS", title_style))
story.append(Spacer(1, 0.5*inch))
story.append(Paragraph("Lift & Shift vs Modernización", heading1_style))
story.append(Spacer(1, 1*inch))
story.append(Paragraph(f"Fecha: {datetime.now().strftime('%d de diciembre, 2025')}", normal_style))
story.append(Paragraph("Total de Aplicaciones: 6", normal_style))
story.append(Paragraph("Duración: 12 meses", normal_style))
story.append(PageBreak())

# Table of Contents
story.append(Paragraph("Tabla de Contenidos", heading1_style))
story.append(Spacer(1, 0.2*inch))
toc_data = [
    ["1.", "Resumen Ejecutivo", "3"],
    ["2.", "Infraestructura Actual (On-Premise)", "4"],
    ["3.", "Flujo de Migración: Origen → Destino", "5"],
    ["4.", "Estrategia 1: Lift & Shift", "6"],
    ["5.", "Estrategia 2: Modernización con Contenedores", "8"],
    ["6.", "Comparativa de Estrategias", "10"],
    ["7.", "Arquitecturas Objetivo por Aplicación", "11"],
    ["8.", "Costos y ROI", "17"],
    ["9.", "Plan de Implementación", "18"],
]
toc_table = Table(toc_data, colWidths=[0.5*inch, 5*inch, 1*inch])
toc_table.setStyle(TableStyle([
    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 0), (-1, -1), 10),
    ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
    ('ALIGN', (2, 0), (2, -1), 'RIGHT'),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
]))
story.append(toc_table)
story.append(PageBreak())

print("✅ PDF structure created - generating content...")

# Build PDF
doc.build(story)
print(f"✅ PDF generated: {output_pdf}")
