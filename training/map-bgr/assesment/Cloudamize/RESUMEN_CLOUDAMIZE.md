# Resumen Cloudamize - Observed Infrastructure

**Fecha de extracción**: 2025-12-02  
**Archivo fuente**: `Observed-Infrastructure.xlsx`  
**Parser utilizado**: `parsers/cloudamize/observed_infrastructure_parser.py`

---

## 📊 Datos Extraídos

### 1. Compute (122 servidores)
**Archivo**: `Compute.csv`

**Columnas principales**:
- Group Name / Asset
- Server Name / IP Address
- OS / OS Version
- MS SQL Edition / SQL Version
- On Time (%)
- Observed vCPU
- Current CPU Utilization (%)
- Observed Memory Provisioned (GB)
- Peak Memory Used (GB)
- ID (server name + uid)

**Ejemplo**:
```
Server: BGR186Q05
IP: 172.20.1.64
OS: Windows Server 2008 Standard
SQL: SQL Server 2005 Standard Edition
vCPU: 4
CPU Util: 55%
Memory: 10.74 GB (Peak: 4.55 GB)
```

---

### 2. Storage (470 discos)
**Archivo**: `Storage.csv`

**Columnas principales**:
- Group Name / Asset
- Server Name / Disk
- Observed Disk Capacity (GB)
- Observed Disk Occupancy (GB)
- Observed Throughput (MBps)
- Peak IOPS
- ID (server name + uid)

**Ejemplo**:
```
Server: BGR186Q05
Disk: C:
Capacity: 75.2 GB
Occupancy: 56.1 GB
Throughput: 31.8 MBps
Peak IOPS: 1071
```

---

### 3. Network (122 interfaces)
**Archivo**: `Network.csv`

**Columnas principales**:
- Group Name / Asset
- Server Name / IP Address
- GB/month leaving server
- GB/month from other Servers/Devices
- Predicted Peak (%)
- ID (server name + uid)

**Ejemplo**:
```
Server: BGR186Q05
IP: 172.20.1.64
Outbound: 1244.89 GB/month
Inbound: 14.05 GB/month
Peak: 10.51%
```

---

## 🔍 Comparación con RVTools

| Métrica | RVTools | Cloudamize |
|---------|---------|------------|
| VMs Producción | 383 | 122 |
| Fuente | VMware vCenter | Agent-based monitoring |
| Datos | Configuración estática | Métricas observadas |
| CPU | vCPUs configurados | vCPUs + utilización real |
| Memoria | Provisioned | Provisioned + Peak Used |
| Storage | Discos configurados | Discos + IOPS + Throughput |
| Network | Interfaces | Tráfico real GB/month |

---

## 💡 Insights Clave

### Ventajas de Cloudamize
- ✅ **Utilización real**: CPU, memoria, IOPS, throughput
- ✅ **Patrones de uso**: On Time %, Peak usage
- ✅ **Tráfico de red**: Inbound/Outbound real
- ✅ **Performance**: IOPS, MBps por disco
- ✅ **Rightsizing**: Datos para optimización

### Limitaciones
- ⚠️ Solo 122 servidores vs 383 en RVTools
- ⚠️ Requiere agentes instalados
- ⚠️ Período de observación limitado

---

## 🎯 Próximos Pasos

1. ✅ Parser creado y funcionando
2. ⏭️ Análisis de utilización real vs provisioned
3. ⏭️ Identificar servidores sobre/sub-provisionados
4. ⏭️ Recomendaciones de rightsizing
5. ⏭️ Correlación con datos de RVTools
6. ⏭️ Análisis de patrones de IOPS para EBS
7. ⏭️ Análisis de tráfico de red para Data Transfer

---

## 📁 Ubicación de Archivos

```
training/map-bgr/assesment/Cloudamize/
├── Observed-Infrastructure.xlsx          # Original
└── Observed-Infrastructure_csv/          # CSVs generados
    ├── Compute.csv                       # 122 servidores
    ├── Storage.csv                       # 470 discos
    └── Network.csv                       # 122 interfaces
```

---

**Última actualización**: 2025-12-02
