#!/usr/bin/env python3
"""
Analizador de Infraestructura BGR
Analiza datos de RVTools para entender la infraestructura de servidores
"""

import pandas as pd
import json
from pathlib import Path
from collections import Counter
import re

def analyze_rvtools_data(file_path):
    """Analiza el archivo RVTools de BGR"""
    
    print(f"Analizando archivo RVTools: {file_path}")
    
    try:
        # Leer las diferentes hojas del archivo Excel
        excel_file = pd.ExcelFile(file_path)
        print(f"Hojas disponibles: {excel_file.sheet_names}")
        
        # Leer hoja vInfo (información de VMs)
        if 'vInfo' in excel_file.sheet_names:
            vinfo_df = pd.read_excel(file_path, sheet_name='vInfo')
            print(f"VMs encontradas en vInfo: {len(vinfo_df)}")
        else:
            print("Hoja vInfo no encontrada")
            return None
            
        # Leer hoja vHost (información de hosts ESXi)
        vhost_df = None
        if 'vHost' in excel_file.sheet_names:
            vhost_df = pd.read_excel(file_path, sheet_name='vHost')
            print(f"Hosts ESXi encontrados: {len(vhost_df)}")
        
        # Análisis de VMs
        vm_analysis = analyze_vms(vinfo_df)
        
        # Análisis de Hosts
        host_analysis = analyze_hosts(vhost_df) if vhost_df is not None else {}
        
        # Generar reporte
        report = generate_infrastructure_report(vm_analysis, host_analysis)
        
        return {
            'vm_analysis': vm_analysis,
            'host_analysis': host_analysis,
            'report': report
        }
        
    except Exception as e:
        print(f"Error analizando archivo: {e}")
        return None

def analyze_vms(df):
    """Analiza las máquinas virtuales"""
    
    analysis = {}
    
    # Total de VMs
    total_vms = len(df)
    analysis['total_vms'] = total_vms
    
    # Análisis por Sistema Operativo
    if 'OS' in df.columns:
        os_counts = df['OS'].value_counts()
        analysis['os_distribution'] = os_counts.to_dict()
        
        # Clasificar Windows vs Linux
        windows_count = 0
        linux_count = 0
        other_count = 0
        
        for os_name, count in os_counts.items():
            if pd.isna(os_name):
                other_count += count
            elif 'windows' in str(os_name).lower() or 'microsoft' in str(os_name).lower():
                windows_count += count
            elif any(linux_dist in str(os_name).lower() for linux_dist in ['linux', 'ubuntu', 'centos', 'redhat', 'suse', 'debian']):
                linux_count += count
            else:
                other_count += count
        
        analysis['os_summary'] = {
            'windows': windows_count,
            'linux': linux_count,
            'other': other_count
        }
    
    # Análisis por Estado de Power
    if 'Powerstate' in df.columns:
        power_states = df['Powerstate'].value_counts()
        analysis['power_states'] = power_states.to_dict()
    
    # Análisis de recursos (CPU, RAM)
    if 'CPUs' in df.columns:
        analysis['cpu_stats'] = {
            'total_vcpus': df['CPUs'].sum(),
            'avg_vcpus_per_vm': df['CPUs'].mean(),
            'max_vcpus': df['CPUs'].max(),
            'min_vcpus': df['CPUs'].min()
        }
    
    if 'Memory' in df.columns:
        # Convertir memoria a GB si está en MB
        memory_gb = df['Memory'] / 1024 if df['Memory'].max() > 1000 else df['Memory']
        analysis['memory_stats'] = {
            'total_memory_gb': memory_gb.sum(),
            'avg_memory_per_vm_gb': memory_gb.mean(),
            'max_memory_gb': memory_gb.max(),
            'min_memory_gb': memory_gb.min()
        }
    
    # Análisis por Host ESXi
    if 'Host' in df.columns:
        host_distribution = df['Host'].value_counts()
        analysis['vms_per_host'] = host_distribution.to_dict()
        analysis['total_hosts'] = len(host_distribution)
    
    # Análisis por Cluster
    if 'Cluster' in df.columns:
        cluster_distribution = df['Cluster'].value_counts()
        analysis['vms_per_cluster'] = cluster_distribution.to_dict()
    
    # Análisis de nombres de VM (patrones BGR)
    if 'VM' in df.columns:
        vm_names = df['VM'].tolist()
        bgr_patterns = analyze_vm_naming_patterns(vm_names)
        analysis['naming_patterns'] = bgr_patterns
    
    return analysis

def analyze_hosts(df):
    """Analiza los hosts ESXi"""
    
    if df is None or df.empty:
        return {}
    
    analysis = {}
    
    # Total de hosts
    analysis['total_hosts'] = len(df)
    
    # Análisis de versiones ESXi
    if 'ESX Version' in df.columns:
        esxi_versions = df['ESX Version'].value_counts()
        analysis['esxi_versions'] = esxi_versions.to_dict()
    
    # Análisis de CPU físicas
    if 'CPU Model' in df.columns:
        cpu_models = df['CPU Model'].value_counts()
        analysis['cpu_models'] = cpu_models.to_dict()
    
    if '# CPU' in df.columns:
        analysis['cpu_stats'] = {
            'total_physical_cpus': df['# CPU'].sum(),
            'avg_cpus_per_host': df['# CPU'].mean()
        }
    
    # Análisis de memoria física
    if 'Memory' in df.columns:
        memory_gb = df['Memory'] / 1024 / 1024 / 1024  # Convertir a GB
        analysis['memory_stats'] = {
            'total_physical_memory_gb': memory_gb.sum(),
            'avg_memory_per_host_gb': memory_gb.mean()
        }
    
    return analysis

def analyze_vm_naming_patterns(vm_names):
    """Analiza patrones de nombres de VMs BGR"""
    
    patterns = {
        'ecb_servers': 0,  # Servidores que empiezan con ECB
        'production': 0,   # Servidores de producción (PR)
        'test': 0,         # Servidores de test (TS)
        'development': 0,  # Servidores de desarrollo (DV)
        'windows_servers': 0,  # Servidores Windows (W)
        'linux_servers': 0,   # Servidores Linux (L)
        'database_servers': 0, # Servidores de BD
        'web_servers': 0,     # Servidores Web
        'app_servers': 0      # Servidores de aplicación
    }
    
    for vm_name in vm_names:
        if pd.isna(vm_name):
            continue
            
        vm_name = str(vm_name).upper()
        
        # Patrón ECB (Banco BGR)
        if vm_name.startswith('ECB'):
            patterns['ecb_servers'] += 1
            
            # Identificar ambiente
            if 'PR' in vm_name:
                patterns['production'] += 1
            elif 'TS' in vm_name:
                patterns['test'] += 1
            elif 'DV' in vm_name:
                patterns['development'] += 1
            
            # Identificar tipo de servidor
            if 'W' in vm_name and not 'WEB' in vm_name:
                patterns['windows_servers'] += 1
            elif 'L' in vm_name:
                patterns['linux_servers'] += 1
            
            # Identificar función
            if any(db_pattern in vm_name for db_pattern in ['SQL', 'DB', 'BD', 'CL']):
                patterns['database_servers'] += 1
            elif any(web_pattern in vm_name for web_pattern in ['WEB', 'IIS', 'W']):
                patterns['web_servers'] += 1
            elif any(app_pattern in vm_name for app_pattern in ['APP', 'AP']):
                patterns['app_servers'] += 1
    
    return patterns

def generate_infrastructure_report(vm_analysis, host_analysis):
    """Genera reporte de infraestructura"""
    
    report = []
    report.append("=" * 80)
    report.append("ANÁLISIS DE INFRAESTRUCTURA BGR")
    report.append("Basado en datos de RVTools")
    report.append("=" * 80)
    report.append("")
    
    # Resumen ejecutivo
    report.append("## RESUMEN EJECUTIVO")
    report.append(f"- Total de VMs: {vm_analysis.get('total_vms', 0):,}")
    report.append(f"- Total de Hosts ESXi: {host_analysis.get('total_hosts', vm_analysis.get('total_hosts', 0))}")
    
    if 'os_summary' in vm_analysis:
        os_summary = vm_analysis['os_summary']
        report.append(f"- VMs Windows: {os_summary.get('windows', 0):,}")
        report.append(f"- VMs Linux: {os_summary.get('linux', 0):,}")
        report.append(f"- Otros SO: {os_summary.get('other', 0):,}")
    
    if 'cpu_stats' in vm_analysis:
        cpu_stats = vm_analysis['cpu_stats']
        report.append(f"- Total vCPUs: {cpu_stats.get('total_vcpus', 0):,}")
    
    if 'memory_stats' in vm_analysis:
        memory_stats = vm_analysis['memory_stats']
        report.append(f"- Total RAM: {memory_stats.get('total_memory_gb', 0):.1f} GB")
    
    report.append("")
    
    # Distribución por Sistema Operativo
    if 'os_distribution' in vm_analysis:
        report.append("## DISTRIBUCIÓN POR SISTEMA OPERATIVO")
        os_dist = vm_analysis['os_distribution']
        for os_name, count in sorted(os_dist.items(), key=lambda x: x[1], reverse=True)[:10]:
            if not pd.isna(os_name):
                report.append(f"- {os_name}: {count:,} VMs")
        report.append("")
    
    # Estados de las VMs
    if 'power_states' in vm_analysis:
        report.append("## ESTADOS DE LAS VMs")
        power_states = vm_analysis['power_states']
        for state, count in power_states.items():
            report.append(f"- {state}: {count:,} VMs")
        report.append("")
    
    # Distribución por Host
    if 'vms_per_host' in vm_analysis:
        report.append("## TOP 10 HOSTS CON MÁS VMs")
        vms_per_host = vm_analysis['vms_per_host']
        for host, count in list(vms_per_host.items())[:10]:
            report.append(f"- {host}: {count:,} VMs")
        report.append("")
    
    # Patrones de nombres BGR
    if 'naming_patterns' in vm_analysis:
        report.append("## ANÁLISIS DE SERVIDORES BGR")
        patterns = vm_analysis['naming_patterns']
        report.append(f"- Servidores ECB (BGR): {patterns.get('ecb_servers', 0):,}")
        report.append(f"- Producción: {patterns.get('production', 0):,}")
        report.append(f"- Test: {patterns.get('test', 0):,}")
        report.append(f"- Desarrollo: {patterns.get('development', 0):,}")
        report.append(f"- Servidores Windows: {patterns.get('windows_servers', 0):,}")
        report.append(f"- Servidores Linux: {patterns.get('linux_servers', 0):,}")
        report.append(f"- Servidores BD: {patterns.get('database_servers', 0):,}")
        report.append(f"- Servidores Web: {patterns.get('web_servers', 0):,}")
        report.append(f"- Servidores App: {patterns.get('app_servers', 0):,}")
        report.append("")
    
    # Información de Hosts ESXi
    if host_analysis:
        report.append("## INFRAESTRUCTURA VMWARE")
        if 'esxi_versions' in host_analysis:
            report.append("### Versiones ESXi:")
            for version, count in host_analysis['esxi_versions'].items():
                report.append(f"- {version}: {count} hosts")
        
        if 'cpu_stats' in host_analysis:
            cpu_stats = host_analysis['cpu_stats']
            report.append(f"### CPU Física:")
            report.append(f"- Total CPUs físicas: {cpu_stats.get('total_physical_cpus', 0)}")
            report.append(f"- Promedio por host: {cpu_stats.get('avg_cpus_per_host', 0):.1f}")
        
        if 'memory_stats' in host_analysis:
            memory_stats = host_analysis['memory_stats']
            report.append(f"### Memoria Física:")
            report.append(f"- Total RAM física: {memory_stats.get('total_physical_memory_gb', 0):.1f} GB")
            report.append(f"- Promedio por host: {memory_stats.get('avg_memory_per_host_gb', 0):.1f} GB")
        report.append("")
    
    # Recomendaciones
    report.append("## RECOMENDACIONES PARA MIGRACIÓN AWS")
    
    total_vms = vm_analysis.get('total_vms', 0)
    if total_vms > 300:
        report.append("- Infraestructura GRANDE: Considerar migración por fases")
        report.append("- Implementar AWS Migration Hub para tracking")
        report.append("- Usar AWS Application Migration Service (MGN)")
    elif total_vms > 100:
        report.append("- Infraestructura MEDIANA: Migración por aplicaciones")
        report.append("- Considerar modernización de aplicaciones críticas")
    else:
        report.append("- Infraestructura PEQUEÑA: Migración directa factible")
    
    if 'os_summary' in vm_analysis:
        os_summary = vm_analysis['os_summary']
        windows_pct = (os_summary.get('windows', 0) / total_vms) * 100 if total_vms > 0 else 0
        linux_pct = (os_summary.get('linux', 0) / total_vms) * 100 if total_vms > 0 else 0
        
        report.append(f"- Windows ({windows_pct:.1f}%): Usar EC2 Windows, considerar modernización")
        report.append(f"- Linux ({linux_pct:.1f}%): Candidatos para contenedores/serverless")
    
    report.append("- Evaluar licenciamiento Microsoft en AWS")
    report.append("- Implementar AWS Backup para protección de datos")
    report.append("- Considerar Reserved Instances para ahorro de costos")
    
    return "\n".join(report)

def main():
    """Función principal"""
    
    # Archivo RVTools de BGR
    rvtools_file = Path("training/map-bgr/RVTools_export_all_250709_064325_DCP.xlsm")
    
    if not rvtools_file.exists():
        print(f"Archivo no encontrado: {rvtools_file}")
        return
    
    # Analizar datos
    results = analyze_rvtools_data(rvtools_file)
    
    if results:
        # Guardar reporte
        output_path = Path("reports/bgr_infrastructure_analysis.txt")
        output_path.parent.mkdir(exist_ok=True)
        output_path.write_text(results['report'], encoding='utf-8')
        
        # Guardar JSON con datos detallados
        json_path = Path("reports/bgr_infrastructure_analysis.json")
        json_data = {
            'vm_analysis': results['vm_analysis'],
            'host_analysis': results['host_analysis']
        }
        json_path.write_text(json.dumps(json_data, indent=2, ensure_ascii=False), encoding='utf-8')
        
        print(f"\n✅ Análisis completado")
        print(f"📄 Reporte: {output_path}")
        print(f"📊 JSON: {json_path}")
        print(f"\n{results['report']}")
    else:
        print("❌ Error en el análisis")

if __name__ == "__main__":
    main()