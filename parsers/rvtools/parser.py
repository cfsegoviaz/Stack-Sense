"""
RVTools Parser - Extrae información de servidores desde exports de RVTools
"""
import pandas as pd
from typing import Dict, List


class RVToolsParser:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data = {}
    
    def parse(self) -> Dict:
        """Parse RVTools Excel export"""
        xl_file = pd.ExcelFile(self.file_path)
        
        # Sheets principales de RVTools
        sheets = ['vInfo', 'vCPU', 'vMemory', 'vDisk', 'vPartition', 'vNetwork']
        
        for sheet in sheets:
            if sheet in xl_file.sheet_names:
                self.data[sheet] = pd.read_excel(xl_file, sheet_name=sheet)
        
        return self.data
    
    def get_vm_summary(self) -> List[Dict]:
        """Obtiene resumen de VMs con specs principales"""
        if 'vInfo' not in self.data:
            return []
        
        vms = []
        df = self.data['vInfo']
        
        for _, row in df.iterrows():
            vm = {
                'name': row.get('VM'),
                'powerstate': row.get('Powerstate'),
                'cpus': row.get('CPUs'),
                'memory_mb': row.get('Memory'),
                'os': row.get('OS according to the VMware Tools'),
                'provisioned_mb': row.get('Provisioned MB'),
                'in_use_mb': row.get('In Use MB'),
            }
            vms.append(vm)
        
        return vms
    
    def get_total_resources(self) -> Dict:
        """Calcula totales de recursos"""
        vms = self.get_vm_summary()
        
        return {
            'total_vms': len(vms),
            'total_cpus': sum(vm.get('cpus', 0) for vm in vms),
            'total_memory_gb': sum(vm.get('memory_mb', 0) for vm in vms) / 1024,
            'total_storage_gb': sum(vm.get('provisioned_mb', 0) for vm in vms) / 1024,
        }
