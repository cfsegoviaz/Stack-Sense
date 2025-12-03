#!/usr/bin/env python3
"""
Generador de recomendaciones EC2 y estimación de costos AWS
"""
import pandas as pd
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
REPORTS_DIR = BASE_DIR / "reports"

# Precios EC2 us-east-1 (On-Demand, Linux/Windows)
EC2_PRICING = {
    # General Purpose - T3
    't3.nano': {'vcpu': 2, 'memory': 0.5, 'price_linux': 0.0052, 'price_windows': 0.0146},
    't3.micro': {'vcpu': 2, 'memory': 1, 'price_linux': 0.0104, 'price_windows': 0.0198},
    't3.small': {'vcpu': 2, 'memory': 2, 'price_linux': 0.0208, 'price_windows': 0.0302},
    't3.medium': {'vcpu': 2, 'memory': 4, 'price_linux': 0.0416, 'price_windows': 0.051},
    't3.large': {'vcpu': 2, 'memory': 8, 'price_linux': 0.0832, 'price_windows': 0.1664},
    't3.xlarge': {'vcpu': 4, 'memory': 16, 'price_linux': 0.1664, 'price_windows': 0.3328},
    't3.2xlarge': {'vcpu': 8, 'memory': 32, 'price_linux': 0.3328, 'price_windows': 0.6656},
    
    # General Purpose - M5
    'm5.large': {'vcpu': 2, 'memory': 8, 'price_linux': 0.096, 'price_windows': 0.192},
    'm5.xlarge': {'vcpu': 4, 'memory': 16, 'price_linux': 0.192, 'price_windows': 0.384},
    'm5.2xlarge': {'vcpu': 8, 'memory': 32, 'price_linux': 0.384, 'price_windows': 0.768},
    'm5.4xlarge': {'vcpu': 16, 'memory': 64, 'price_linux': 0.768, 'price_windows': 1.536},
    'm5.8xlarge': {'vcpu': 32, 'memory': 128, 'price_linux': 1.536, 'price_windows': 3.072},
    
    # Compute Optimized - C5
    'c5.large': {'vcpu': 2, 'memory': 4, 'price_linux': 0.085, 'price_windows': 0.177},
    'c5.xlarge': {'vcpu': 4, 'memory': 8, 'price_linux': 0.17, 'price_windows': 0.354},
    'c5.2xlarge': {'vcpu': 8, 'memory': 16, 'price_linux': 0.34, 'price_windows': 0.708},
    'c5.4xlarge': {'vcpu': 16, 'memory': 32, 'price_linux': 0.68, 'price_windows': 1.416},
    
    # Memory Optimized - R5
    'r5.large': {'vcpu': 2, 'memory': 16, 'price_linux': 0.126, 'price_windows': 0.252},
    'r5.xlarge': {'vcpu': 4, 'memory': 32, 'price_linux': 0.252, 'price_windows': 0.504},
    'r5.2xlarge': {'vcpu': 8, 'memory': 64, 'price_linux': 0.504, 'price_windows': 1.008},
    'r5.4xlarge': {'vcpu': 16, 'memory': 128, 'price_linux': 1.008, 'price_windows': 2.016},
}

# Precios EBS (por GB-mes)
EBS_PRICING = {
    'gp3': 0.08,
    'gp2': 0.10,
    'io2': 0.125,
    'st1': 0.045,
}

def recommend_instance_type(vcpu, memory_gb, os):
    """Recomendar tipo de instancia EC2 óptimo"""
    
    # Determinar si es Windows
    is_windows = 'windows' in str(os).lower()
    price_key = 'price_windows' if is_windows else 'price_linux'
    
    # Calcular ratio CPU/Memory
    cpu_memory_ratio = vcpu / memory_gb if memory_gb > 0 else 0
    
    # Seleccionar familia según ratio
    if cpu_memory_ratio > 0.5:  # CPU intensive
        family = 'c5'
    elif cpu_memory_ratio < 0.25:  # Memory intensive
        family = 'r5'
    elif vcpu <= 8 and memory_gb <= 32:  # Burstable
        family = 't3'
    else:  # General purpose
        family = 'm5'
    
    # Filtrar instancias de la familia
    candidates = {k: v for k, v in EC2_PRICING.items() 
                  if k.startswith(family) and v['vcpu'] >= vcpu and v['memory'] >= memory_gb}
    
    if not candidates:
        # Fallback a m5
        candidates = {k: v for k, v in EC2_PRICING.items() 
                      if k.startswith('m5') and v['vcpu'] >= vcpu and v['memory'] >= memory_gb}
    
    if not candidates:
        # Última opción: la más grande
        return 'm5.8xlarge', EC2_PRICING['m5.8xlarge'][price_key]
    
    # Seleccionar la más pequeña que cumpla
    best = min(candidates.items(), key=lambda x: (x[1]['vcpu'], x[1]['memory']))
    
    return best[0], best[1][price_key]

def calculate_storage_cost(storage_gb):
    """Calcular costo de almacenamiento EBS"""
    # Usar gp3 por defecto
    return storage_gb * EBS_PRICING['gp3']

def analyze_and_recommend():
    """Analizar todas las VMs y generar recomendaciones"""
    
    print("🔍 Analizando VMs y generando recomendaciones EC2...")
    print("=" * 70)
    
    # Cargar inventario
    df = pd.read_csv(REPORTS_DIR / "01_inventario_vms_produccion.csv")
    
    # Cargar datos de disco
    df_disk = pd.read_csv(BASE_DIR / "RVTools_export_all_250709_064325_DCP_csv" / "vDisk.csv")
    
    # Calcular storage por VM
    storage_by_vm = df_disk.groupby('VM')['Capacity MiB'].sum() / 1024  # GB
    
    recommendations = []
    
    for _, vm in df.iterrows():
        vm_name = vm['nombre']
        vcpu = int(vm['vcpus'])
        memory_gb = float(vm['memory_gb'])
        os = vm['os']
        powerstate = vm['powerstate']
        
        # Storage
        storage_gb = storage_by_vm.get(vm_name, 50)  # Default 50GB
        
        # Recomendar instancia
        instance_type, hourly_cost = recommend_instance_type(vcpu, memory_gb, os)
        
        # Calcular costos
        monthly_compute = hourly_cost * 730  # 730 horas/mes
        monthly_storage = calculate_storage_cost(storage_gb)
        monthly_total = monthly_compute + monthly_storage
        
        # Calcular ahorro con Reserved Instance (1 año)
        ri_discount = 0.40  # 40% descuento
        monthly_ri = monthly_total * (1 - ri_discount)
        
        recommendations.append({
            'vm_name': vm_name,
            'current_vcpu': vcpu,
            'current_memory_gb': memory_gb,
            'current_storage_gb': round(storage_gb, 2),
            'os': str(os),
            'powerstate': powerstate,
            'recommended_instance': instance_type,
            'instance_vcpu': EC2_PRICING[instance_type]['vcpu'],
            'instance_memory_gb': EC2_PRICING[instance_type]['memory'],
            'monthly_compute_usd': round(monthly_compute, 2),
            'monthly_storage_usd': round(monthly_storage, 2),
            'monthly_total_usd': round(monthly_total, 2),
            'monthly_ri_usd': round(monthly_ri, 2),
            'annual_total_usd': round(monthly_total * 12, 2),
            'annual_ri_usd': round(monthly_ri * 12, 2)
        })
    
    return recommendations

def generate_summary(recommendations):
    """Generar resumen de costos"""
    
    df = pd.DataFrame(recommendations)
    
    # Solo VMs encendidas
    df_on = df[df['powerstate'] == 'poweredOn']
    
    summary = {
        'total_vms': len(df),
        'vms_on': len(df_on),
        'vms_off': len(df) - len(df_on),
        
        'total_vcpus': int(df['current_vcpu'].sum()),
        'total_memory_gb': round(df['current_memory_gb'].sum(), 2),
        'total_storage_gb': round(df['current_storage_gb'].sum(), 2),
        
        'monthly_cost_on_demand': round(df_on['monthly_total_usd'].sum(), 2),
        'monthly_cost_ri': round(df_on['monthly_ri_usd'].sum(), 2),
        'monthly_savings_ri': round(df_on['monthly_total_usd'].sum() - df_on['monthly_ri_usd'].sum(), 2),
        
        'annual_cost_on_demand': round(df_on['monthly_total_usd'].sum() * 12, 2),
        'annual_cost_ri': round(df_on['monthly_ri_usd'].sum() * 12, 2),
        'annual_savings_ri': round((df_on['monthly_total_usd'].sum() - df_on['monthly_ri_usd'].sum()) * 12, 2),
        
        'by_instance_type': df_on.groupby('recommended_instance').agg({
            'vm_name': 'count',
            'monthly_total_usd': 'sum'
        }).to_dict(),
        
        'by_os': df_on.groupby('os').agg({
            'vm_name': 'count',
            'monthly_total_usd': 'sum'
        }).to_dict()
    }
    
    return summary

def main():
    print("🚀 Generando recomendaciones EC2 y estimación de costos...")
    print("=" * 70)
    
    # Generar recomendaciones
    recommendations = analyze_and_recommend()
    
    # Generar resumen
    summary = generate_summary(recommendations)
    
    # Guardar CSV
    df = pd.DataFrame(recommendations)
    csv_file = REPORTS_DIR / "04_recomendaciones_ec2.csv"
    df.to_csv(csv_file, index=False)
    print(f"\n✅ CSV generado: {csv_file}")
    
    # Guardar JSON
    json_file = REPORTS_DIR / "04_estimacion_costos.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump({
            'summary': summary,
            'recommendations': recommendations
        }, f, indent=2, ensure_ascii=False)
    print(f"✅ JSON generado: {json_file}")
    
    # Mostrar resumen
    print("\n" + "=" * 70)
    print("💰 RESUMEN DE COSTOS AWS")
    print("=" * 70)
    
    print(f"\n📊 Inventario:")
    print(f"   Total VMs: {summary['total_vms']}")
    print(f"   VMs Encendidas: {summary['vms_on']}")
    print(f"   VMs Apagadas: {summary['vms_off']}")
    
    print(f"\n💻 Recursos:")
    print(f"   Total vCPUs: {summary['total_vcpus']}")
    print(f"   Total RAM: {summary['total_memory_gb']:.0f} GB")
    print(f"   Total Storage: {summary['total_storage_gb']:.0f} GB")
    
    print(f"\n💰 Costos Mensuales (VMs encendidas):")
    print(f"   On-Demand: ${summary['monthly_cost_on_demand']:,.2f}")
    print(f"   Reserved Instances (1yr): ${summary['monthly_cost_ri']:,.2f}")
    print(f"   Ahorro mensual: ${summary['monthly_savings_ri']:,.2f} (40%)")
    
    print(f"\n💰 Costos Anuales:")
    print(f"   On-Demand: ${summary['annual_cost_on_demand']:,.2f}")
    print(f"   Reserved Instances: ${summary['annual_cost_ri']:,.2f}")
    print(f"   Ahorro anual: ${summary['annual_savings_ri']:,.2f}")
    
    print(f"\n📊 Top 5 Tipos de Instancia:")
    instance_counts = df[df['powerstate'] == 'poweredOn']['recommended_instance'].value_counts().head(5)
    for inst, count in instance_counts.items():
        print(f"   {inst}: {count} VMs")
    
    print("\n" + "=" * 70)

if __name__ == '__main__':
    main()
