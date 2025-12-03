#!/usr/bin/env python3
"""
Clasificación de VMs por estrategia 7R's y optimización de costos
"""
import pandas as pd
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
REPORTS_DIR = BASE_DIR / "reports"

def classify_vm_strategy(vm):
    """Clasificar VM según estrategia 7R's"""
    
    os = str(vm['os']).lower()
    vcpu = vm['current_vcpu']
    memory_gb = vm['current_memory_gb']
    powerstate = vm['powerstate']
    
    # Retire - VMs apagadas
    if powerstate == 'poweredOff':
        return {
            'strategy': 'Retire',
            'reason': 'VM apagada - evaluar si es necesaria',
            'priority': 'Alta',
            'complexity': 'Baja',
            'cost_optimization': 'Eliminar costo completo'
        }
    
    # Retire - Windows 2003 (EOL crítico)
    if '2003' in os:
        return {
            'strategy': 'Retire',
            'reason': 'Windows 2003 EOL - sin soporte desde 2015',
            'priority': 'Crítica',
            'complexity': 'Alta',
            'cost_optimization': 'Upgrade o containerizar'
        }
    
    # Replatform - Windows 2008 (EOL)
    if '2008' in os:
        return {
            'strategy': 'Replatform',
            'reason': 'Windows 2008 EOL - upgrade a 2019/2022',
            'priority': 'Alta',
            'complexity': 'Media',
            'cost_optimization': 'Upgrade antes de migrar'
        }
    
    # Refactor - VMs pequeñas candidatas a Lambda/Containers
    if vcpu <= 2 and memory_gb <= 4:
        return {
            'strategy': 'Refactor',
            'reason': 'Candidato a Lambda o ECS Fargate',
            'priority': 'Media',
            'complexity': 'Alta',
            'cost_optimization': 'Serverless o containers (40-60% ahorro)'
        }
    
    # Replatform - Bases de datos candidatas a RDS
    if 'sql' in os or 'oracle' in os or 'postgres' in os or 'mysql' in os:
        return {
            'strategy': 'Replatform',
            'reason': 'Candidato a RDS/Aurora',
            'priority': 'Media',
            'complexity': 'Media',
            'cost_optimization': 'RDS managed (reduce ops, auto scaling)'
        }
    
    # Rehost - VMs modernas (2016+)
    if any(year in os for year in ['2016', '2019', '2022']) or 'ubuntu' in os or 'linux' in os:
        return {
            'strategy': 'Rehost',
            'reason': 'Lift & Shift - OS moderno',
            'priority': 'Media',
            'complexity': 'Baja',
            'cost_optimization': 'Reserved Instances (40% ahorro)'
        }
    
    # Rehost - Default
    return {
        'strategy': 'Rehost',
        'reason': 'Lift & Shift estándar',
        'priority': 'Baja',
        'complexity': 'Baja',
        'cost_optimization': 'Reserved Instances'
    }

def optimize_costs(recommendations_df):
    """Generar estrategias de optimización de costos"""
    
    optimizations = []
    
    # 1. VMs apagadas
    vms_off = recommendations_df[recommendations_df['powerstate'] == 'poweredOff']
    if len(vms_off) > 0:
        savings = vms_off['monthly_total_usd'].sum()
        optimizations.append({
            'strategy': 'Eliminar VMs apagadas',
            'vms_affected': len(vms_off),
            'monthly_savings': round(savings, 2),
            'annual_savings': round(savings * 12, 2),
            'implementation': 'Inmediata',
            'risk': 'Bajo',
            'actions': [
                'Validar con owners si son necesarias',
                'Crear snapshots antes de eliminar',
                'Eliminar VMs y recursos asociados'
            ]
        })
    
    # 2. Reserved Instances
    vms_on = recommendations_df[recommendations_df['powerstate'] == 'poweredOn']
    ri_savings = (vms_on['monthly_total_usd'] - vms_on['monthly_ri_usd']).sum()
    optimizations.append({
        'strategy': 'Reserved Instances (1 año)',
        'vms_affected': len(vms_on),
        'monthly_savings': round(ri_savings, 2),
        'annual_savings': round(ri_savings * 12, 2),
        'implementation': '3 meses (después de estabilización)',
        'risk': 'Bajo',
        'actions': [
            'Identificar VMs estables (80% del inventario)',
            'Comprar RIs para instancias más usadas',
            'Monitorear utilización de RIs'
        ]
    })
    
    # 3. Rightsizing - VMs sobredimensionadas
    # Detectar VMs con mucha memoria pero pocos CPUs (posible sobredimensionamiento)
    oversized = vms_on[
        (vms_on['instance_memory_gb'] / vms_on['instance_vcpu'] > 8) & 
        (vms_on['current_memory_gb'] / vms_on['current_vcpu'] < 4)
    ]
    if len(oversized) > 0:
        # Estimar 20% de ahorro en estas VMs
        savings = oversized['monthly_total_usd'].sum() * 0.20
        optimizations.append({
            'strategy': 'Rightsizing - Reducir tamaño',
            'vms_affected': len(oversized),
            'monthly_savings': round(savings, 2),
            'annual_savings': round(savings * 12, 2),
            'implementation': '1-2 meses',
            'risk': 'Medio',
            'actions': [
                'Monitorear uso real de CPU/RAM por 2 semanas',
                'Identificar VMs con <50% utilización',
                'Reducir tamaño de instancia gradualmente'
            ]
        })
    
    # 4. Spot Instances para Dev/Test
    # Estimar 20% de VMs son dev/test
    dev_test_count = int(len(vms_on) * 0.20)
    dev_test_cost = vms_on.nsmallest(dev_test_count, 'monthly_total_usd')['monthly_total_usd'].sum()
    spot_savings = dev_test_cost * 0.70  # 70% ahorro con Spot
    optimizations.append({
        'strategy': 'Spot Instances para Dev/Test',
        'vms_affected': dev_test_count,
        'monthly_savings': round(spot_savings, 2),
        'annual_savings': round(spot_savings * 12, 2),
        'implementation': '2-3 meses',
        'risk': 'Bajo',
        'actions': [
            'Identificar ambientes no productivos',
            'Implementar auto-restart en caso de interrupción',
            'Usar Spot para cargas batch y procesamiento'
        ]
    })
    
    # 5. Auto Scaling
    # Estimar 30% de VMs web pueden usar auto scaling
    web_count = int(len(vms_on) * 0.30)
    web_cost = vms_on.nlargest(web_count, 'monthly_total_usd')['monthly_total_usd'].sum()
    autoscaling_savings = web_cost * 0.25  # 25% ahorro en horas no pico
    optimizations.append({
        'strategy': 'Auto Scaling',
        'vms_affected': web_count,
        'monthly_savings': round(autoscaling_savings, 2),
        'annual_savings': round(autoscaling_savings * 12, 2),
        'implementation': '3-4 meses',
        'risk': 'Medio',
        'actions': [
            'Implementar en aplicaciones web y APIs',
            'Configurar políticas de scaling (CPU, memoria, requests)',
            'Definir min/max instancias por aplicación'
        ]
    })
    
    # 6. Migrar a servicios managed
    # Estimar 10% pueden migrar a RDS, Lambda, etc
    managed_count = int(len(vms_on) * 0.10)
    managed_cost = vms_on.sample(min(managed_count, len(vms_on)))['monthly_total_usd'].sum()
    managed_savings = managed_cost * 0.30  # 30% ahorro operacional
    optimizations.append({
        'strategy': 'Servicios Managed (RDS, Lambda, ECS)',
        'vms_affected': managed_count,
        'monthly_savings': round(managed_savings, 2),
        'annual_savings': round(managed_savings * 12, 2),
        'implementation': '4-6 meses',
        'risk': 'Alto',
        'actions': [
            'Migrar bases de datos a RDS/Aurora',
            'Refactorizar microservicios a Lambda',
            'Containerizar aplicaciones en ECS/EKS'
        ]
    })
    
    return optimizations

def main():
    print("🎯 Clasificando VMs por estrategia 7R's...")
    print("=" * 70)
    
    # Cargar recomendaciones
    df = pd.read_csv(REPORTS_DIR / "04_recomendaciones_ec2.csv")
    
    # Clasificar cada VM
    classifications = []
    for _, vm in df.iterrows():
        strategy = classify_vm_strategy(vm)
        classifications.append({
            'vm_name': vm['vm_name'],
            'strategy': strategy['strategy'],
            'reason': strategy['reason'],
            'priority': strategy['priority'],
            'complexity': strategy['complexity'],
            'cost_optimization': strategy['cost_optimization'],
            'current_monthly_cost': vm['monthly_total_usd'],
            'os': vm['os'],
            'powerstate': vm['powerstate']
        })
    
    df_class = pd.DataFrame(classifications)
    
    # Guardar clasificación
    csv_file = REPORTS_DIR / "05_estrategia_7rs.csv"
    df_class.to_csv(csv_file, index=False)
    print(f"✅ Clasificación guardada: {csv_file}")
    
    # Resumen por estrategia
    print("\n📊 RESUMEN POR ESTRATEGIA 7R's:")
    print("=" * 70)
    
    strategy_summary = df_class.groupby('strategy').agg({
        'vm_name': 'count',
        'current_monthly_cost': 'sum'
    }).round(2)
    
    for strategy, row in strategy_summary.iterrows():
        count = int(row['vm_name'])
        cost = row['current_monthly_cost']
        pct = (count / len(df_class)) * 100
        print(f"\n{strategy}:")
        print(f"   VMs: {count} ({pct:.1f}%)")
        print(f"   Costo mensual: ${cost:,.2f}")
    
    # Generar optimizaciones
    print("\n\n💡 ESTRATEGIAS DE OPTIMIZACIÓN:")
    print("=" * 70)
    
    optimizations = optimize_costs(df)
    
    total_monthly_savings = 0
    total_annual_savings = 0
    
    for i, opt in enumerate(optimizations, 1):
        print(f"\n{i}. {opt['strategy']}")
        print(f"   VMs afectadas: {opt['vms_affected']}")
        print(f"   Ahorro mensual: ${opt['monthly_savings']:,.2f}")
        print(f"   Ahorro anual: ${opt['annual_savings']:,.2f}")
        print(f"   Implementación: {opt['implementation']}")
        print(f"   Riesgo: {opt['risk']}")
        
        total_monthly_savings += opt['monthly_savings']
        total_annual_savings += opt['annual_savings']
    
    print("\n" + "=" * 70)
    print("💰 AHORRO TOTAL POTENCIAL:")
    print(f"   Mensual: ${total_monthly_savings:,.2f}")
    print(f"   Anual: ${total_annual_savings:,.2f}")
    print("=" * 70)
    
    # Guardar optimizaciones
    json_file = REPORTS_DIR / "05_optimizaciones_costos.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump({
            'strategy_summary': strategy_summary.to_dict(),
            'optimizations': optimizations,
            'total_savings': {
                'monthly': round(total_monthly_savings, 2),
                'annual': round(total_annual_savings, 2)
            }
        }, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Optimizaciones guardadas: {json_file}")
    
    # Calcular costo optimizado final
    current_monthly = df[df['powerstate'] == 'poweredOn']['monthly_total_usd'].sum()
    ri_monthly = df[df['powerstate'] == 'poweredOn']['monthly_ri_usd'].sum()
    
    # Ahorro adicional más allá de RIs
    additional_savings = total_monthly_savings - optimizations[1]['monthly_savings']
    optimized_monthly = ri_monthly - additional_savings
    
    print("\n" + "=" * 70)
    print("📊 COMPARACIÓN DE COSTOS:")
    print("=" * 70)
    print(f"Actual (On-Demand):        ${current_monthly:,.2f}/mes")
    print(f"Con Reserved Instances:    ${ri_monthly:,.2f}/mes")
    print(f"Totalmente Optimizado:     ${optimized_monthly:,.2f}/mes")
    print(f"\nAhorro vs On-Demand:       ${current_monthly - optimized_monthly:,.2f}/mes ({((current_monthly - optimized_monthly) / current_monthly * 100):.1f}%)")
    print("=" * 70)

if __name__ == '__main__':
    main()
