# 02. Technical Analysis

**Audiencia:** Arquitectos, Ingenieros, Equipo Técnico  
**Propósito:** Análisis técnico detallado de infraestructura y aplicaciones

---

## 📄 Documentos

### 02_RESUMEN_APLICACIONES.md
**Descripción:** Análisis de 8 aplicaciones BGR  
**Contenido:**
- Stack tecnológico por aplicación
- Estado de obsolescencia
- Dependencias y servidores
- Recomendaciones de modernización

### 02_mapa_aplicaciones.json (27 KB)
**Descripción:** Mapa estructurado de aplicaciones  
**Formato:** JSON  
**Contenido:**
- Metadata de aplicaciones
- Relaciones y dependencias
- Configuraciones técnicas

### 01_inventario_produccion.json (129 KB)
**Descripción:** Inventario completo de 383 VMs  
**Formato:** JSON  
**Contenido:**
- Especificaciones de VMs
- Recursos (vCPU, RAM, Storage)
- Sistema operativo
- Estado y ubicación

### 01_inventario_vms_produccion.csv (49 KB)
**Descripción:** Inventario en formato tabular  
**Formato:** CSV  
**Uso:** Análisis en Excel, importación a herramientas

---

## 🔍 Hallazgos Clave

### Aplicaciones
- **Total:** 8 aplicaciones BGR
- **Obsoletas:** 6 apps (.NET Framework 4.7.1)
- **Modernas:** 2 apps (.NET Core 8)

### Infraestructura
- **VMs Total:** 383 VMs
- **Servidor Principal:** ECBRTSW21 (4 vCPU, 8GB RAM)
- **Bases de Datos:** SQL Server 2016/2019 Enterprise

### Deuda Técnica
- ⚠️ 75% de aplicaciones con stack obsoleto
- ⚠️ Windows Server 2016 (EOL cercano)
- ⚠️ SQL Server 2016 (soporte extendido hasta 2026)
