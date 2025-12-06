# Análisis de SQL Server - Proyecto MAP-BGR

**Fecha**: 2025-12-02  
**Fuente**: Cloudamize Observed Infrastructure

---

## 📊 Resumen de Ediciones SQL Server

### Servidores con SQL Server Enterprise (15 servidores)

| Servidor | SQL Version | Edición | Aplicación Potencial |
|----------|-------------|---------|---------------------|
| ECBRPRCL1 | SQL Server 2016 SP3 | **Enterprise** | Cluster/HA |
| ECBRPRCL2 | SQL Server 2016 SP3 | **Enterprise** | Cluster/HA |
| ECBRPRCL5 | SQL Server 2016 SP3 | **Enterprise** | Cluster/HA |
| ECBRPRCL6 | SQL Server 2016 SP3 | **Enterprise** | Cluster/HA |
| ECBRPRCL9 | SQL Server 2019 RTM | **Enterprise** | Cluster/HA |
| ECBRPRCL10 | SQL Server 2019 RTM | **Enterprise** | Cluster/HA |
| ECBRPRCL11 | SQL Server 2016 SP3 | **Enterprise** | Cluster/HA |
| ECBRPRCL12 | SQL Server 2016 SP3 | **Enterprise** | Cluster/HA |
| ECBRPRCL13 | SQL Server 2016 SP3 | **Enterprise** | Cluster/HA |
| ECBRPRCL14 | SQL Server 2016 SP3 | **Enterprise** | Cluster/HA |
| ECBRPRQ48 | SQL Server 2016 SP3 | **Enterprise** | Producción |
| ECBRPRQ52 | SQL Server 2016 SP3 | **Enterprise** | Producción |
| ECBRPRQ64 | SQL Server 2019 RTM | **Enterprise** | Producción |
| ECBRPRQ69 | SQL Server 2019 RTM | **Enterprise** | Producción |
| ecbrprq74 | SQL Server 2022 RTM | **Enterprise** | Producción |
| ECBRPRB01 | SQL Server 2022 RTM | **Enterprise** | Backup/Multi-version |

**Total**: 15 servidores con Enterprise Edition

---

### Servidores con SQL Server Standard (13 servidores)

| Servidor | SQL Version | Edición | Aplicación Potencial |
|----------|-------------|---------|---------------------|
| BGR186Q05 | SQL Server 2005 SP4 | Standard | Legacy |
| ECBRPRQ21 | SQL Server 2008 R2 SP3 | Standard | Legacy |
| ECBRPRQ24 | SQL Server 2012 SP4 | Standard | Producción |
| ECBRPRQ30 | SQL Server 2008 R2 SP3 | Standard | Producción |
| ECBRPRAP4 | SQL Server 2012 SP# | Standard | Producción |
| ecbrprq44 | SQL Server 2016 SP3 | Standard | Producción |
| ecbrprq45 | SQL Server 2016 SP3 | Standard | Producción |
| ecbrprq46 | SQL Server 2016 SP3 | Standard | Producción |
| ecbrprq49 | SQL Server 2016 SP3 | Standard | Producción |
| ecbrprq50 | SQL Server 2016 SP3 | Standard | Producción |
| ecbrprq55 | SQL Server 2016 SP3 | Standard | Producción |
| ecbrprq58 | SQL Server 2019 RTM | Standard | Producción |
| ecbrprq59 | SQL Server 2019 RTM | Standard | Producción |
| ECBRPRQ38 | SQL Server 2022 RTM | Standard | Producción |
| ECBRPRQ68 | SQL Server 2022 RTM | Standard | Producción |
| ECBRPRQ71 | SQL Server 2022 RTM | Standard | Producción |
| ECBRPRQ72 | SQL Server 2022 RTM | Standard | Producción |
| ECBRPRQ73 | SQL Server 2022 RTM | Standard | Producción |

**Total**: 18 servidores con Standard Edition

---

### Servidores con SQL Server Express (2 servidores)

| Servidor | SQL Version | Edición | Aplicación Potencial |
|----------|-------------|---------|---------------------|
| ECBRPRF02 | SQL Server 2008 R2 RTM | Express | Dev/Test |
| ECBRPRSRM1 | SQL Server 2016 SP2 | Express | Herramientas |

**Total**: 2 servidores con Express Edition

---

## 🎯 Análisis por Aplicación EBA

### Aplicaciones Críticas que Requieren Enterprise

#### 1. **Backoffice Banca Digital** - REQUIERE ENTERPRISE
**Razón**: Aplicación crítica de banca, probablemente usa:
- Always On Availability Groups (Enterprise only)
- Particionamiento de tablas (Enterprise only)
- Compresión de datos (Enterprise only)

**Servidores identificados**: 
- Cluster ECBRPRCL* (10 nodos Enterprise)
- Producción ECBRPRQ64, ECBRPRQ69

**Recomendación**: **RDS SQL Server Enterprise Multi-AZ**

---

#### 2. **Api Portal** - REQUIERE ENTERPRISE
**Razón**: API crítica con alta disponibilidad, probablemente usa:
- Always On Availability Groups
- Replicación transaccional
- Compresión de datos

**Servidores identificados**:
- ECBRPRQ48, ECBRPRQ52 (Enterprise)
- ecbrprq74 (Enterprise 2022)

**Recomendación**: **RDS SQL Server Enterprise Multi-AZ**

---

### Aplicaciones que Pueden Usar Standard/Web

#### 3. **Portal Guía BGR** - STANDARD/WEB OK
**Servidores identificados**: No aparecen servidores SQL específicos
**Recomendación**: **RDS SQL Server Web Single-AZ** (mantener)

---

#### 4. **Portal Adm BGR** - STANDARD/WEB OK
**Servidores identificados**: No aparecen servidores SQL específicos
**Recomendación**: **RDS SQL Server Web Single-AZ** (mantener)

---

## 💰 Impacto en Costos EBA

### Precios RDS SQL Server (us-east-1)

| Edición | Tipo | Multi-AZ | Precio/hora | Precio/mes |
|---------|------|----------|-------------|------------|
| Web | db.t3.medium | No | $0.166 | $121 |
| Web | db.t3.large | Sí | $0.3964 | $289 |
| **Enterprise** | **db.t3.large** | **Sí** | **$1.836** | **$1,340** |

---

### Costos Actualizados por Aplicación

| Aplicación | Edición Actual | Edición Requerida | Costo Actual | Costo Nuevo | Diferencia |
|------------|----------------|-------------------|--------------|-------------|------------|
| Portal Guía BGR | Web | Web | $121 | $121 | $0 |
| Portal Adm BGR | Web | Web | $121 | $121 | $0 |
| **Backoffice Banca** | **Web** | **Enterprise** | **$289** | **$1,340** | **+$1,051** |
| **Api Portal** | **Web** | **Enterprise** | **$289** | **$1,340** | **+$1,051** |

---

### Nuevo Total Mensual EBA

| Categoría | Costo Anterior | Costo Nuevo | Diferencia |
|-----------|----------------|-------------|------------|
| Compute (EC2) | $1,579 | $1,579 | $0 |
| **Database (RDS)** | **$821** | **$2,923** | **+$2,102** |
| Storage | $176 | $176 | $0 |
| Networking | $206 | $206 | $0 |
| Monitoring | $154 | $154 | $0 |
| Backup | $75 | $75 | $0 |
| Security | $32 | $32 | $0 |
| **Subtotal** | **$3,043** | **$5,145** | **+$2,102** |
| Contingencia (10%) | $304 | $515 | +$211 |
| **TOTAL MENSUAL** | **$3,347** | **$5,660** | **+$2,313** |

---

## ⚠️ PROBLEMA: Excede Presupuesto EBA

**Presupuesto EBA**: $5,000/mes  
**Costo con Enterprise**: $5,660/mes  
**Exceso**: $660/mes (13% sobre presupuesto)

---

## 💡 Opciones de Mitigación

### Opción 1: Usar SQL Server Standard en lugar de Enterprise
**Precio**: db.t3.large Standard Multi-AZ = $0.544/hora = $397/mes

| Aplicación | Edición | Costo/mes |
|------------|---------|-----------|
| Portal Guía BGR | Web | $121 |
| Portal Adm BGR | Web | $121 |
| Backoffice Banca | **Standard** | **$397** |
| Api Portal | **Standard** | **$397** |
| **Total RDS** | - | **$1,036** |
| **Total EBA** | - | **$3,560** |

**Resultado**: $3,560/mes (29% bajo presupuesto) ✅

**Limitaciones de Standard**:
- No soporta Always On Availability Groups
- No soporta particionamiento de tablas
- No soporta compresión de datos avanzada

---

### Opción 2: Solo Api Portal con Enterprise
**Justificación**: API es más crítica que Backoffice

| Aplicación | Edición | Costo/mes |
|------------|---------|-----------|
| Portal Guía BGR | Web | $121 |
| Portal Adm BGR | Web | $121 |
| Backoffice Banca | **Standard** | **$397** |
| Api Portal | **Enterprise** | **$1,340** |
| **Total RDS** | - | **$1,979** |
| **Total EBA** | - | **$4,503** |

**Resultado**: $4,503/mes (10% bajo presupuesto) ✅

---

### Opción 3: Ambas con Enterprise + Reducir otras apps
**Mantener**: Solo 6 aplicaciones en EBA (eliminar Seq y SonarQube)

| Aplicación | Edición | Costo/mes |
|------------|---------|-----------|
| Portal Guía BGR | Web | $121 |
| Portal Adm BGR | Web | $121 |
| Backoffice Banca | **Enterprise** | **$1,340** |
| Api Portal | **Enterprise** | **$1,340** |
| Saras | - | $280 |
| Backoffice Sistemas | - | $350 |
| **Total** | - | **~$4,800** |

**Resultado**: $4,800/mes (4% bajo presupuesto) ✅

---

## 🎯 Recomendación Final

### **Opción 2: Api Portal con Enterprise, Backoffice Banca con Standard**

**Justificación**:
1. ✅ **Api Portal** es crítica para integraciones → Enterprise necesario
2. ✅ **Backoffice Banca** puede funcionar con Standard + RDS Multi-AZ
3. ✅ **Costo**: $4,503/mes (10% bajo presupuesto)
4. ✅ **8 aplicaciones** completas en EBA
5. ✅ **Margen**: $497 para ajustes

**Features Enterprise que Api Portal necesita**:
- Always On Availability Groups
- Replicación transaccional
- Compresión de datos
- Particionamiento

**Features Standard suficientes para Backoffice Banca**:
- Multi-AZ (HA nativa de RDS)
- Backups automáticos
- Read replicas
- Encryption at rest

---

**Última actualización**: 2025-12-02
