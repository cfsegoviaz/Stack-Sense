#!/usr/bin/env python3
"""
Ejemplo: Análisis de datos de Cloudamize Observed Infrastructure
"""
import csv
import sys
from pathlib import Path
from collections import defaultdict


def analyze_cloudamize(csv_dir: str):
    """Analiza los CSVs generados de Cloudamize"""
    
    csv_path = Path(csv_dir)
    
    if not csv_path.exists():
        print(f"❌ Directorio no encontrado: {csv_dir}")
        return
    
    print("=" * 60)
    print("ANÁLISIS CLOUDAMIZE - OBSERVED INFRASTRUCTURE")
    print("=" * 60)
    
    # Analizar Compute
    compute_file = csv_path / "Compute.csv"
    if compute_file.exists():
        analyze_compute(compute_file)
    
    # Analizar Storage
    storage_file = csv_path / "Storage.csv"
    if storage_file.exists():
        analyze_storage(storage_file)
    
    # Analizar Network
    network_file = csv_path / "Network.csv"
    if network_file.exists():
        analyze_network(network_file)


def analyze_compute(file_path):
    """Analiza datos de Compute"""
    print("\n📊 COMPUTE ANALYSIS")
    print("-" * 60)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # Skip first header row
        headers = next(reader)  # Real headers
        
        servers = []
        for row in reader:
            servers.append(dict(zip(headers, row)))
        
        total_vcpu = 0
        total_memory = 0
        cpu_utils = []
        os_count = defaultdict(int)
        
        for server in servers:
            try:
                vcpu = int(server.get('Observed vCPU', '0') or '0')
                memory = float(server.get('Observed Memory Provisioned (GB)', '0') or '0')
                cpu_util = float(server.get('Current CPU Utilization (%)', '0') or '0')
                os = server.get('OS', 'Unknown')
                
                total_vcpu += vcpu
                total_memory += memory
                cpu_utils.append(cpu_util)
                os_count[os] += 1
            except (ValueError, TypeError):
                continue
        
        print(f"Total Servers: {len(servers)}")
        print(f"Total vCPUs: {total_vcpu}")
        print(f"Total Memory: {total_memory:.2f} GB")
        
        if cpu_utils:
            avg_cpu = sum(cpu_utils) / len(cpu_utils)
            print(f"Avg CPU Utilization: {avg_cpu:.2f}%")
        
        print("\nOS Distribution:")
        for os, count in sorted(os_count.items(), key=lambda x: x[1], reverse=True)[:5]:
            print(f"  {os}: {count}")


def analyze_storage(file_path):
    """Analiza datos de Storage"""
    print("\n💾 STORAGE ANALYSIS")
    print("-" * 60)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # Skip first header row
        headers = next(reader)  # Real headers
        
        disks = []
        for row in reader:
            disks.append(dict(zip(headers, row)))
        
        total_capacity = 0
        total_used = 0
        total_iops = 0
        
        for disk in disks:
            try:
                capacity = float(disk.get('Observed Disk Capacity (GB)', '0') or '0')
                used = float(disk.get('Observed Disk Occupancy (GB)', '0') or '0')
                iops = float(disk.get('Peak IOPS', '0') or '0')
                
                total_capacity += capacity
                total_used += used
                total_iops += iops
            except (ValueError, TypeError):
                continue
        
        print(f"Total Disks: {len(disks)}")
        print(f"Total Capacity: {total_capacity:.2f} GB")
        usage_pct = (total_used/total_capacity*100) if total_capacity > 0 else 0
        print(f"Total Used: {total_used:.2f} GB ({usage_pct:.1f}%)")
        print(f"Total Peak IOPS: {total_iops:.0f}")


def analyze_network(file_path):
    """Analiza datos de Network"""
    print("\n🌐 NETWORK ANALYSIS")
    print("-" * 60)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # Skip first header row
        headers = next(reader)  # Real headers
        
        interfaces = []
        for row in reader:
            interfaces.append(dict(zip(headers, row)))
        
        total_outbound = 0
        total_inbound = 0
        
        for iface in interfaces:
            try:
                outbound = float(iface.get('GB/month leaving server', '0') or '0')
                inbound = float(iface.get('GB/month from other Servers/Devices', '0') or '0')
                
                total_outbound += outbound
                total_inbound += inbound
            except (ValueError, TypeError):
                continue
        
        print(f"Total Interfaces: {len(interfaces)}")
        print(f"Total Outbound: {total_outbound:.2f} GB/month")
        print(f"Total Inbound: {total_inbound:.2f} GB/month")
        print(f"Total Traffic: {total_outbound + total_inbound:.2f} GB/month")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python analyze_cloudamize.py <directorio_csv>")
        print("\nEjemplo:")
        print("  python analyze_cloudamize.py data/Observed-Infrastructure_csv/")
        sys.exit(1)
    
    csv_dir = sys.argv[1]
    analyze_cloudamize(csv_dir)
