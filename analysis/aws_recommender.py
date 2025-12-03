"""
AWS Recommender - Mapea workloads on-prem a servicios AWS
"""
from typing import Dict, List


class AWSRecommender:
    
    # Mapeo de CPU/RAM a instancias EC2
    INSTANCE_TYPES = [
        {'type': 't3.micro', 'vcpu': 2, 'memory_gb': 1, 'use_case': 'dev/test'},
        {'type': 't3.small', 'vcpu': 2, 'memory_gb': 2, 'use_case': 'low traffic'},
        {'type': 't3.medium', 'vcpu': 2, 'memory_gb': 4, 'use_case': 'general'},
        {'type': 't3.large', 'vcpu': 2, 'memory_gb': 8, 'use_case': 'general'},
        {'type': 't3.xlarge', 'vcpu': 4, 'memory_gb': 16, 'use_case': 'general'},
        {'type': 't3.2xlarge', 'vcpu': 8, 'memory_gb': 32, 'use_case': 'general'},
        {'type': 'm5.large', 'vcpu': 2, 'memory_gb': 8, 'use_case': 'balanced'},
        {'type': 'm5.xlarge', 'vcpu': 4, 'memory_gb': 16, 'use_case': 'balanced'},
        {'type': 'm5.2xlarge', 'vcpu': 8, 'memory_gb': 32, 'use_case': 'balanced'},
        {'type': 'm5.4xlarge', 'vcpu': 16, 'memory_gb': 64, 'use_case': 'balanced'},
        {'type': 'c5.large', 'vcpu': 2, 'memory_gb': 4, 'use_case': 'compute'},
        {'type': 'c5.xlarge', 'vcpu': 4, 'memory_gb': 8, 'use_case': 'compute'},
        {'type': 'r5.large', 'vcpu': 2, 'memory_gb': 16, 'use_case': 'memory'},
        {'type': 'r5.xlarge', 'vcpu': 4, 'memory_gb': 32, 'use_case': 'memory'},
    ]
    
    def recommend_instance(self, vcpu: int, memory_gb: float, workload_type: str = 'general') -> Dict:
        """Recomienda tipo de instancia EC2 basado en specs"""
        
        # Filtrar por tipo de workload
        candidates = [i for i in self.INSTANCE_TYPES 
                     if i['vcpu'] >= vcpu and i['memory_gb'] >= memory_gb]
        
        if not candidates:
            return {'type': 'm5.4xlarge', 'reason': 'Requiere instancia grande'}
        
        # Ordenar por tamaño y retornar la más pequeña que cumpla
        candidates.sort(key=lambda x: (x['vcpu'], x['memory_gb']))
        
        return {
            'recommended_type': candidates[0]['type'],
            'vcpu': candidates[0]['vcpu'],
            'memory_gb': candidates[0]['memory_gb'],
            'use_case': candidates[0]['use_case']
        }
    
    def recommend_storage(self, size_gb: float, iops_required: int = None) -> Dict:
        """Recomienda tipo de almacenamiento EBS"""
        
        if iops_required and iops_required > 16000:
            return {
                'type': 'io2',
                'size_gb': size_gb,
                'reason': 'Alto IOPS requerido'
            }
        elif size_gb > 1000:
            return {
                'type': 'st1',
                'size_gb': size_gb,
                'reason': 'Almacenamiento masivo throughput'
            }
        else:
            return {
                'type': 'gp3',
                'size_gb': size_gb,
                'reason': 'Balance costo/performance'
            }
    
    def analyze_vm_list(self, vms: List[Dict]) -> List[Dict]:
        """Analiza lista de VMs y genera recomendaciones"""
        recommendations = []
        
        for vm in vms:
            vcpu = vm.get('cpus', 2)
            memory_gb = vm.get('memory_mb', 2048) / 1024
            storage_gb = vm.get('provisioned_mb', 50000) / 1024
            
            instance_rec = self.recommend_instance(vcpu, memory_gb)
            storage_rec = self.recommend_storage(storage_gb)
            
            recommendations.append({
                'vm_name': vm.get('name'),
                'current_specs': {
                    'vcpu': vcpu,
                    'memory_gb': memory_gb,
                    'storage_gb': storage_gb
                },
                'aws_recommendation': {
                    'instance': instance_rec,
                    'storage': storage_rec
                }
            })
        
        return recommendations
