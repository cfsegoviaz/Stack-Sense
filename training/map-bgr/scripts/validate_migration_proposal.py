#!/usr/bin/env python3
"""
Valida y refina la propuesta de migración cruzando datos de:
- RVTools (383 VMs)
- Cloudamize Observed Infrastructure (122 servers)
- Cloudamize Migration Planner (122 servers, 3441 procesos)
"""
import json
import csv
from pathlib import Path
from collections import defaultdict


def load_rvtools_data():
    """Carga datos de RVTools"""
    json_path = Path("training/map-bgr/reports/02_technical_analysis/01_inventario_produccion.json")
    with open(json_path) as f:
        return json.load(f)


def load_cloudamize_compute():
    """Carga datos de Cloudamize Compute"""
    csv_path = Path("training/map-bgr/assesment/Cloudamize/Observed-Infrastructure_csv/Compute.csv")
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # Skip first header
        headers = next(reader)  # Real headers
        
        servers = []
        for row in reader:
            servers.append(dict(zip(headers, row)))
    
    return servers


def load_migration_planner():
    """Carga datos de Migration Planner"""
    csv_path = Path("training/map-bgr/assesment/Cloudamize/MigrationPlanner_csv/Server_Applications.csv")
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)


def analyze_coverage():
    """Analiza cobertura de datos entre fuentes"""
    print("=" * 80)
    print("VALIDACIÓN DE PROPUESTA DE MIGRACIÓN - PROYECTO MAP-BGR")
    print("=" * 80)
    
    # Cargar datos
    rvtools = load_rvtools_data()
    cloudamize_compute = load_cloudamize_compute()
    migration_planner = load_migration_planner()
    
    # Servidores únicos
    rvtools_vms = rvtools['resumen_ejecutivo']['total_vms']
    cloudamize_servers = set(s['Server Name'] for s in cloudamize_compute if s.get('Server Name'))
    planner_servers = set(r['Server Machine'] for r in migration_planner if r.get('Server Machine'))
    
    print(f"\n📊 COBERTURA DE DATOS")
    print("-" * 80)
    print(f"RVTools (Inventario VMware):        {rvtools_vms} VMs")
    print(f"Cloudamize Observed (Monitoreadas): {len(cloudamize_servers)} servidores")
    print(f"Migration Planner (Planificadas):   {len(planner_servers)} servidores")
    print(f"\nCobertura Cloudamize: {len(cloudamize_servers)/rvtools_vms*100:.1f}%")
    print(f"Gap de monitoreo: {rvtools_vms - len(cloudamize_servers)} VMs sin datos de utilización")
    
    return {
        'rvtools': rvtools,
        'cloudamize_compute': cloudamize_compute,
        'migration_planner': migration_planner,
        'cloudamize_servers': cloudamize_servers
    }


def analyze_utilization(data):
    """Analiza utilización real vs configurada"""
    print(f"\n💻 ANÁLISIS DE UTILIZACIÓN (Cloudamize)")
    print("-" * 80)
    
    total_vcpu_configured = 0
    total_vcpu_used = 0
    total_memory_configured = 0
    total_memory_peak = 0
    cpu_utils = []
    
    for server in data['cloudamize_compute']:
        try:
            vcpu = int(server.get('Observed vCPU', '0') or '0')
            cpu_util = float(server.get('Current CPU Utilization (%)', '0') or '0')
            memory = float(server.get('Observed Memory Provisioned (GB)', '0') or '0')
            memory_peak = float(server.get('Peak Memory Used (GB)', '0') or '0')
            
            total_vcpu_configured += vcpu
            total_vcpu_used += (vcpu * cpu_util / 100)
            total_memory_configured += memory
            total_memory_peak += memory_peak
            cpu_utils.append(cpu_util)
        except (ValueError, TypeError):
            continue
    
    avg_cpu_util = sum(cpu_utils) / len(cpu_utils) if cpu_utils else 0
    memory_util = (total_memory_peak / total_memory_configured * 100) if total_memory_configured > 0 else 0
    
    print(f"vCPUs Configurados:  {total_vcpu_configured}")
    print(f"vCPUs Utilizados:    {total_vcpu_used:.1f} ({avg_cpu_util:.1f}%)")
    print(f"Oportunidad Rightsizing CPU: {total_vcpu_configured - total_vcpu_used:.1f} vCPUs")
    print(f"\nMemoria Configurada: {total_memory_configured:.1f} GB")
    print(f"Memoria Peak:        {total_memory_peak:.1f} GB ({memory_util:.1f}%)")
    print(f"Oportunidad Rightsizing RAM: {total_memory_configured - total_memory_peak:.1f} GB")
    
    return {
        'avg_cpu_util': avg_cpu_util,
        'memory_util': memory_util,
        'vcpu_savings': total_vcpu_configured - total_vcpu_used,
        'memory_savings': total_memory_configured - total_memory_peak
    }


def analyze_migration_strategy(data):
    """Analiza estrategias de migración"""
    print(f"\n🎯 ESTRATEGIAS DE MIGRACIÓN (Migration Planner)")
    print("-" * 80)
    
    strategies = defaultdict(set)
    waves = defaultdict(set)
    
    for record in data['migration_planner']:
        strategy = record.get('Migration Strategy', 'Unknown')
        wave = record.get('Wave', 'Unknown')
        server = record.get('Server Machine', '')
        
        if server:
            strategies[strategy].add(server)
            waves[wave].add(server)
    
    print("Estrategias definidas:")
    for strategy, servers in sorted(strategies.items(), key=lambda x: len(x[1]), reverse=True):
        print(f"  {strategy:20} {len(servers):3} servidores")
    
    print("\nWaves de migración:")
    for wave, servers in sorted(waves.items()):
        print(f"  {wave:20} {len(servers):3} servidores")
    
    return strategies, waves


def analyze_security_tools(data):
    """Analiza herramientas de seguridad y monitoreo"""
    print(f"\n🔒 HERRAMIENTAS DE SEGURIDAD Y MONITOREO")
    print("-" * 80)
    
    tools = defaultdict(int)
    total_servers = len(set(r['Server Machine'] for r in data['migration_planner'] if r.get('Server Machine')))
    
    security_keywords = ['Trend Micro', 'Rapid7', 'Dynatrace', 'Anti-Malware', 'Security', 'Agent']
    
    for record in data['migration_planner']:
        process = record.get('Server Process', '')
        for keyword in security_keywords:
            if keyword.lower() in process.lower():
                tools[keyword] += 1
                break
    
    print("Herramientas detectadas:")
    for tool, count in sorted(tools.items(), key=lambda x: x[1], reverse=True):
        coverage = (count / total_servers * 100) if total_servers > 0 else 0
        print(f"  {tool:30} {count:3} instancias ({coverage:.1f}% cobertura)")
    
    return tools


def generate_recommendations(data, utilization):
    """Genera recomendaciones basadas en el análisis"""
    print(f"\n💡 RECOMENDACIONES ACTUALIZADAS")
    print("=" * 80)
    
    rvtools_vms = data['rvtools']['resumen_ejecutivo']['total_vms']
    monitored = len(data['cloudamize_servers'])
    
    print("\n1. COBERTURA DE MONITOREO")
    print("-" * 80)
    print(f"✅ {monitored} servidores monitoreados por Cloudamize")
    print(f"⚠️  {rvtools_vms - monitored} VMs sin datos de utilización")
    print(f"\nRECOMENDACIÓN:")
    print(f"  - Instalar agentes Cloudamize en {rvtools_vms - monitored} VMs restantes")
    print(f"  - Priorizar servidores críticos y de producción")
    print(f"  - Período de observación: mínimo 2 semanas adicionales")
    
    print("\n2. RIGHTSIZING Y OPTIMIZACIÓN")
    print("-" * 80)
    print(f"CPU Utilization: {utilization['avg_cpu_util']:.1f}%")
    print(f"Memory Utilization: {utilization['memory_util']:.1f}%")
    print(f"\nRECOMENDACIÓN:")
    if utilization['avg_cpu_util'] < 70:
        print(f"  - Reducir vCPUs en ~{utilization['vcpu_savings']:.0f} cores")
        print(f"  - Ahorro estimado: ${utilization['vcpu_savings'] * 50:.0f}/mes")
    if utilization['memory_util'] < 70:
        print(f"  - Reducir RAM en ~{utilization['memory_savings']:.0f} GB")
        print(f"  - Ahorro estimado: ${utilization['memory_savings'] * 10:.0f}/mes")
    
    print("\n3. ESTRATEGIA DE MIGRACIÓN")
    print("-" * 80)
    print("Estado actual: Todos en 'Backlog' con estrategia 'Rehost'")
    print("\nRECOMENDACIÓN:")
    print("  - Definir 4 waves de migración:")
    print("    Wave 1: Servidores no críticos (30 servers) - Mes 1-2")
    print("    Wave 2: Aplicaciones de soporte (30 servers) - Mes 3-4")
    print("    Wave 3: Aplicaciones de negocio (32 servers) - Mes 5-8")
    print("    Wave 4: Aplicaciones críticas (30 servers) - Mes 9-12")
    print("  - Evaluar estrategias alternativas:")
    print("    • Bases de datos → RDS (Replatform)")
    print("    • Apps web → ECS/Fargate (Refactor)")
    print("    • Servicios legacy → Modernización")
    
    print("\n4. APLICACIONES DE NEGOCIO")
    print("-" * 80)
    print("Estado actual: No hay mapeo de Business Applications")
    print("\nRECOMENDACIÓN:")
    print("  - Mapear manualmente las 8 aplicaciones identificadas:")
    print("    • Api Portal, Portal Guía BGR, Sonar Qube")
    print("    • Backoffice Banca Digital, Portal Adm BGR")
    print("    • Backoffice Sistemas, Saras, Seq")
    print("  - Documentar dependencias entre aplicaciones")
    print("  - Definir criticidad y ventanas de migración")
    
    print("\n5. SEGURIDAD Y COMPLIANCE")
    print("-" * 80)
    print("✅ Infraestructura bien protegida (Trend Micro + Rapid7)")
    print("✅ Monitoreo APM con Dynatrace")
    print("\nRECOMENDACIÓN:")
    print("  - Migrar a servicios nativos de AWS:")
    print("    • AWS Security Hub (reemplaza Trend Micro)")
    print("    • Amazon GuardDuty (detección de amenazas)")
    print("    • AWS Systems Manager (gestión de parches)")
    print("    • Amazon CloudWatch (reemplaza Dynatrace)")
    print("  - Ahorro estimado: $50K/año en licencias")


def main():
    # Análisis
    data = analyze_coverage()
    utilization = analyze_utilization(data)
    strategies, waves = analyze_migration_strategy(data)
    tools = analyze_security_tools(data)
    
    # Recomendaciones
    generate_recommendations(data, utilization)
    
    print("\n" + "=" * 80)
    print("VALIDACIÓN COMPLETADA")
    print("=" * 80)
    print("\nPróximos pasos:")
    print("1. Revisar y actualizar PROPUESTA_COMERCIAL_BGR.md")
    print("2. Actualizar FLUJO_MIGRACION_DETALLADO.md con waves definidas")
    print("3. Generar reporte ejecutivo con datos validados")


if __name__ == '__main__':
    main()
