#!/usr/bin/env python3
"""
Ejemplo: Análisis de Cloudamize Migration Planner - Server Applications
"""
import csv
import sys
from pathlib import Path
from collections import defaultdict


def analyze_migration_planner(csv_file: str):
    """Analiza el CSV de Server Applications"""
    
    csv_path = Path(csv_file)
    
    if not csv_path.exists():
        print(f"❌ Archivo no encontrado: {csv_file}")
        return
    
    print("=" * 70)
    print("ANÁLISIS CLOUDAMIZE - MIGRATION PLANNER")
    print("=" * 70)
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        records = list(reader)
    
    # Análisis general
    print(f"\n📊 RESUMEN GENERAL")
    print("-" * 70)
    print(f"Total Registros: {len(records)}")
    
    # Servidores únicos
    servers = set()
    for rec in records:
        server = rec.get('Server Machine', '')
        if server:
            servers.add(server)
    print(f"Servidores Únicos: {len(servers)}")
    
    # Análisis por Wave
    print(f"\n🌊 ANÁLISIS POR WAVE")
    print("-" * 70)
    waves = defaultdict(lambda: {'servers': set(), 'processes': 0})
    
    for rec in records:
        wave = rec.get('Wave', 'Unknown')
        server = rec.get('Server Machine', '')
        
        waves[wave]['servers'].add(server)
        waves[wave]['processes'] += 1
    
    for wave in sorted(waves.keys()):
        data = waves[wave]
        print(f"{wave:20} | Servers: {len(data['servers']):3} | Processes: {data['processes']:4}")
    
    # Análisis por Migration Strategy
    print(f"\n🎯 ESTRATEGIAS DE MIGRACIÓN (7R's)")
    print("-" * 70)
    strategies = defaultdict(lambda: {'servers': set(), 'processes': 0})
    
    for rec in records:
        strategy = rec.get('Migration Strategy', 'Unknown')
        server = rec.get('Server Machine', '')
        
        strategies[strategy]['servers'].add(server)
        strategies[strategy]['processes'] += 1
    
    for strategy in sorted(strategies.keys(), key=lambda x: len(strategies[x]['servers']), reverse=True):
        data = strategies[strategy]
        print(f"{strategy:20} | Servers: {len(data['servers']):3} | Processes: {data['processes']:4}")
    
    # Análisis por Business Application
    print(f"\n💼 APLICACIONES DE NEGOCIO")
    print("-" * 70)
    apps = defaultdict(lambda: {'servers': set(), 'processes': 0})
    
    for rec in records:
        app = rec.get('Business Application', '-')
        server = rec.get('Server Machine', '')
        
        if app and app != '-':
            apps[app]['servers'].add(server)
            apps[app]['processes'] += 1
    
    if apps:
        print(f"Total Aplicaciones: {len(apps)}")
        print(f"\nTop 10 Aplicaciones:")
        for app in sorted(apps.keys(), key=lambda x: len(apps[x]['servers']), reverse=True)[:10]:
            data = apps[app]
            print(f"  {app[:50]:50} | Servers: {len(data['servers']):3}")
    else:
        print("No se encontraron aplicaciones de negocio mapeadas")
    
    # Análisis por Server Asset
    print(f"\n🏷️  TIPOS DE ASSET")
    print("-" * 70)
    assets = defaultdict(lambda: {'servers': set(), 'processes': 0})
    
    for rec in records:
        asset = rec.get('Server Asset', 'Unknown')
        server = rec.get('Server Machine', '')
        
        assets[asset]['servers'].add(server)
        assets[asset]['processes'] += 1
    
    for asset in sorted(assets.keys(), key=lambda x: len(assets[x]['servers']), reverse=True):
        data = assets[asset]
        print(f"{asset:30} | Servers: {len(data['servers']):3} | Processes: {data['processes']:4}")
    
    # Top procesos
    print(f"\n⚙️  TOP 10 PROCESOS MÁS COMUNES")
    print("-" * 70)
    processes = defaultdict(int)
    
    for rec in records:
        process = rec.get('Server Process', '')
        if process:
            processes[process] += 1
    
    for process, count in sorted(processes.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"{process[:50]:50} | {count:4} instancias")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python analyze_migration_planner.py <Server_Applications.csv>")
        print("\nEjemplo:")
        print("  python analyze_migration_planner.py data/MigrationPlanner_csv/Server_Applications.csv")
        sys.exit(1)
    
    csv_file = sys.argv[1]
    analyze_migration_planner(csv_file)
