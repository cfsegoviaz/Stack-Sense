#!/usr/bin/env python3
"""
Análisis completo del inventario de producción MAP-BGR
"""
import pandas as pd
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
CSV_DIR = BASE_DIR / "RVTools_export_all_250709_064325_DCP_csv"
REPORTS_DIR = BASE_DIR / "reports"
REPORTS_DIR.mkdir(exist_ok=True)

def analyze_vms():
    """Análisis detallado de VMs"""
    df = pd.read_csv(CSV_DIR / "vInfo.csv")
    
    analysis = {
        "total_vms": len(df),
        "vms_encendidas": len(df[df['Powerstate'] == 'poweredOn']),
        "vms_apagadas": len(df[df['Powerstate'] == 'poweredOff']),
        "vms_suspendidas": len(df[df['Powerstate'] == 'suspended']),
        "templates": len(df[df['Template'] == True]),
        
        "recursos": {
            "total_vcpus": int(df['# CPU'].sum()),
            "total_memory_gb": round(df['Memory'].sum() / 1024, 2),
            "avg_vcpus_per_vm": round(df['# CPU'].mean(), 2),
            "avg_memory_gb_per_vm": round(df['Memory'].mean() / 1024, 2),
            "max_vcpus": int(df['# CPU'].max()),
            "max_memory_gb": round(df['Memory'].max() / 1024, 2)
        },
        
        "sistemas_operativos": df['OS according to the VMware Tools'].value_counts().to_dict(),
        
        "vms_por_cluster": df['Cluster'].value_counts().to_dict() if 'Cluster' in df.columns else {},
        
        "vms_criticas": {
            "con_snapshots": len(df[df['Consolidation Needed'] == True]),
            "sin_vmware_tools": len(df[df['Guest state'] != 'running'])
        }
    }
    
    # Lista detallada de VMs
    vms_list = []
    for _, row in df.iterrows():
        vms_list.append({
            "nombre": row['VM'],
            "powerstate": row['Powerstate'],
            "vcpus": int(row['# CPU']),
            "memory_gb": round(row['Memory'] / 1024, 2),
            "os": row['OS according to the VMware Tools'],
            "ip": row.get('Primary IP Address', ''),
            "dns": row.get('DNS Name', ''),
            "cluster": row.get('Cluster', ''),
            "host": row.get('Host', '')
        })
    
    return analysis, vms_list

def analyze_storage():
    """Análisis de almacenamiento"""
    df_disk = pd.read_csv(CSV_DIR / "vDisk.csv")
    df_partition = pd.read_csv(CSV_DIR / "vPartition.csv")
    
    analysis = {
        "total_discos": len(df_disk),
        "total_particiones": len(df_partition),
        "capacidad_total_gb": round(df_disk['Capacity MiB'].sum() / 1024, 2),
        "espacio_usado_gb": round(df_partition['Consumed MiB'].sum() / 1024, 2) if 'Consumed MiB' in df_partition.columns else 0,
        "tipos_disco": df_disk['Disk Mode'].value_counts().to_dict() if 'Disk Mode' in df_disk.columns else {}
    }
    
    return analysis

def analyze_network():
    """Análisis de red"""
    df_net = pd.read_csv(CSV_DIR / "vNetwork.csv")
    
    analysis = {
        "total_interfaces": len(df_net),
        "vms_con_red": df_net['VM'].nunique(),
        "redes": df_net['Network'].value_counts().to_dict() if 'Network' in df_net.columns else {}
    }
    
    return analysis

def analyze_hosts():
    """Análisis de hosts ESXi"""
    df_host = pd.read_csv(CSV_DIR / "vHost.csv")
    
    analysis = {
        "total_hosts": len(df_host),
        "hosts_info": []
    }
    
    for _, row in df_host.iterrows():
        analysis["hosts_info"].append({
            "nombre": row.get('Host', ''),
            "cluster": row.get('Cluster', ''),
            "cpu_model": row.get('CPU Model', ''),
            "cpu_cores": row.get('# CPU', 0),
            "memory_gb": round(row.get('Memory', 0) / 1024, 2) if 'Memory' in row else 0,
            "esxi_version": row.get('ESX Version', '')
        })
    
    return analysis

def analyze_datastores():
    """Análisis de datastores"""
    df_ds = pd.read_csv(CSV_DIR / "vDatastore.csv")
    
    analysis = {
        "total_datastores": len(df_ds),
        "capacidad_total_tb": round(df_ds['Capacity MiB'].sum() / 1024 / 1024, 2),
        "espacio_libre_tb": round(df_ds['Free MiB'].sum() / 1024 / 1024, 2),
        "uso_porcentaje": round((1 - df_ds['Free MiB'].sum() / df_ds['Capacity MiB'].sum()) * 100, 2),
        "datastores": []
    }
    
    for _, row in df_ds.iterrows():
        analysis["datastores"].append({
            "nombre": row.get('Name', ''),
            "tipo": row.get('Type', ''),
            "capacidad_gb": round(row.get('Capacity MiB', 0) / 1024, 2),
            "libre_gb": round(row.get('Free MiB', 0) / 1024, 2),
            "uso_pct": round((1 - row.get('Free MiB', 0) / row.get('Capacity MiB', 1)) * 100, 2)
        })
    
    return analysis

def identify_legacy_systems(vms_list):
    """Identificar sistemas legacy que requieren atención"""
    legacy = {
        "windows_2003": [],
        "windows_2008": [],
        "sistemas_antiguos": []
    }
    
    for vm in vms_list:
        os = str(vm['os']).lower() if vm['os'] else ''
        if '2003' in os:
            legacy["windows_2003"].append(vm['nombre'])
        elif '2008' in os:
            legacy["windows_2008"].append(vm['nombre'])
    
    return legacy

def main():
    print("🔍 Analizando inventario de producción MAP-BGR...")
    print("=" * 60)
    
    # Análisis de VMs
    print("\n📊 Analizando VMs...")
    vm_analysis, vms_list = analyze_vms()
    
    # Análisis de almacenamiento
    print("💾 Analizando almacenamiento...")
    storage_analysis = analyze_storage()
    
    # Análisis de red
    print("🌐 Analizando red...")
    network_analysis = analyze_network()
    
    # Análisis de hosts
    print("🖥️  Analizando hosts ESXi...")
    hosts_analysis = analyze_hosts()
    
    # Análisis de datastores
    print("📦 Analizando datastores...")
    datastores_analysis = analyze_datastores()
    
    # Identificar sistemas legacy
    print("⚠️  Identificando sistemas legacy...")
    legacy_systems = identify_legacy_systems(vms_list)
    
    # Consolidar reporte
    report = {
        "proyecto": "MAP-BGR",
        "ambiente": "Producción",
        "fecha_analisis": "2025-12-01",
        "fuente": "RVTools_export_all_250709_064325_DCP.xlsm",
        
        "resumen_ejecutivo": {
            "total_vms": vm_analysis["total_vms"],
            "total_vcpus": vm_analysis["recursos"]["total_vcpus"],
            "total_memory_gb": vm_analysis["recursos"]["total_memory_gb"],
            "total_storage_gb": storage_analysis["capacidad_total_gb"],
            "total_hosts": hosts_analysis["total_hosts"],
            "total_datastores": datastores_analysis["total_datastores"]
        },
        
        "vms": vm_analysis,
        "almacenamiento": storage_analysis,
        "red": network_analysis,
        "hosts": hosts_analysis,
        "datastores": datastores_analysis,
        "sistemas_legacy": legacy_systems,
        "vms_detalle": vms_list
    }
    
    # Guardar reporte JSON
    output_file = REPORTS_DIR / "01_inventario_produccion.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Reporte generado: {output_file}")
    
    # Guardar CSV de VMs
    df_vms = pd.DataFrame(vms_list)
    csv_file = REPORTS_DIR / "01_inventario_vms_produccion.csv"
    df_vms.to_csv(csv_file, index=False)
    print(f"✅ CSV generado: {csv_file}")
    
    # Mostrar resumen
    print("\n" + "=" * 60)
    print("📈 RESUMEN EJECUTIVO")
    print("=" * 60)
    print(f"\n🖥️  VMs: {vm_analysis['total_vms']} ({vm_analysis['vms_encendidas']} encendidas)")
    print(f"💻 vCPUs: {vm_analysis['recursos']['total_vcpus']}")
    print(f"💾 RAM: {vm_analysis['recursos']['total_memory_gb']} GB")
    print(f"📦 Storage: {storage_analysis['capacidad_total_gb']} GB")
    print(f"🏢 Hosts: {hosts_analysis['total_hosts']}")
    print(f"💿 Datastores: {datastores_analysis['total_datastores']}")
    
    print(f"\n⚠️  SISTEMAS LEGACY:")
    print(f"   Windows 2003: {len(legacy_systems['windows_2003'])} VMs")
    print(f"   Windows 2008: {len(legacy_systems['windows_2008'])} VMs")
    
    print("\n" + "=" * 60)

if __name__ == '__main__':
    main()
