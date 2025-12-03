"""
Ejemplo: Análisis de export RVTools y generación de recomendaciones AWS
"""
import sys
sys.path.append('..')

from parsers.rvtools.parser import RVToolsParser
from analysis.aws_recommender import AWSRecommender
import json


def analyze_rvtools_export(file_path: str):
    """Analiza un export de RVTools y genera recomendaciones"""
    
    print("📊 Analizando export de RVTools...")
    parser = RVToolsParser(file_path)
    data = parser.parse()
    
    print("\n✅ Datos cargados")
    print(f"   Sheets encontrados: {list(data.keys())}")
    
    # Obtener resumen de VMs
    vms = parser.get_vm_summary()
    print(f"\n🖥️  Total de VMs: {len(vms)}")
    
    # Calcular totales
    totals = parser.get_total_resources()
    print("\n📈 Recursos totales:")
    print(f"   CPUs: {totals['total_cpus']}")
    print(f"   Memoria: {totals['total_memory_gb']:.2f} GB")
    print(f"   Storage: {totals['total_storage_gb']:.2f} GB")
    
    # Generar recomendaciones AWS
    print("\n🔍 Generando recomendaciones AWS...")
    recommender = AWSRecommender()
    recommendations = recommender.analyze_vm_list(vms)
    
    # Guardar reporte
    report = {
        'summary': totals,
        'vms_analyzed': len(vms),
        'recommendations': recommendations
    }
    
    output_file = '../reports/migration_recommendations.json'
    with open(output_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n✅ Reporte generado: {output_file}")
    
    # Mostrar primeras 3 recomendaciones
    print("\n📋 Primeras recomendaciones:")
    for rec in recommendations[:3]:
        print(f"\n   VM: {rec['vm_name']}")
        print(f"   → Instancia: {rec['aws_recommendation']['instance']['recommended_type']}")
        print(f"   → Storage: {rec['aws_recommendation']['storage']['type']}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python analyze_rvtools.py <ruta_archivo_rvtools.xlsx>")
        sys.exit(1)
    
    analyze_rvtools_export(sys.argv[1])
