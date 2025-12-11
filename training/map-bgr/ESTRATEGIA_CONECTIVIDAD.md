# Estrategia de Conectividad Híbrida - BGR

**Fecha**: 2025-12-04  
**Decisión**: VPN Site-to-Site como solución principal (implementación inmediata)

---

## 🎯 Problema

**Direct Connect** tiene lead time de **2-4 semanas**, lo cual retrasa la implementación del proyecto.

---

## ✅ Solución: VPN Site-to-Site

### Fase 1: VPN Site-to-Site (Inmediato)
**Implementación**: 1-3 días  
**Costo**: $73/mes  
**Latencia**: 20-50ms  
**Ancho de banda**: Hasta 1.25 Gbps por túnel  

### Fase 2: Direct Connect (Opcional - Futuro)
**Implementación**: 2-4 semanas (cuando sea necesario)  
**Costo**: +$228/mes  
**Latencia**: < 10ms  
**Upgrade path**: Sin downtime  

---

## 📊 Comparativa de Opciones

| Característica | VPN Site-to-Site | Direct Connect |
|----------------|------------------|----------------|
| **Lead Time** | 1-3 días ✅ | 2-4 semanas ❌ |
| **Costo Setup** | $0 | $0 |
| **Costo Mensual** | $73 | $228 + $0.02/GB |
| **Latencia** | 20-50ms | < 10ms |
| **Ancho Banda** | 1.25 Gbps/túnel | 1-10 Gbps |
| **SLA** | 99.95% | 99.95% |
| **Redundancia** | 2 túneles | Requiere 2 conexiones |
| **Encriptación** | IPSec (incluido) | MACsec (opcional) |

---

## 🏗️ Arquitectura VPN Site-to-Site

### Componentes

**AWS Side:**
- Virtual Private Gateway (VGW)
- 2 túneles IPSec (redundancia automática)
- Route tables hacia on-premise

**On-Premise Side:**
- Customer Gateway (router/firewall)
- BGP routing (recomendado)
- Firewall rules

### Topología

```
AWS VPC (EC2 Instances)
        ↓
Private Subnets → Virtual Private Gateway
        ↓
    VPN Tunnel 1 (IPSec) ──┐
    VPN Tunnel 2 (IPSec) ──┤
        ↓                   │
Customer Gateway (On-Premise)
        ↓
On-Premise Datacenter (SQL Server, PostgreSQL)
```

---

## 💰 Impacto en Costos

### Eliminado (Direct Connect)
- Port Fee: -$228/mes
- Data Transfer: -$100/mes (ahora incluido en VPN)
- **Total eliminado**: -$328/mes

### Agregado (VPN Site-to-Site)
- VPN Connection: +$73/mes (2 túneles)
- Data Transfer Out: +$90/GB (primeros 10 TB)
- **Total agregado**: +$163/mes (estimado)

### Balance
- **Ahorro**: $165/mes vs Direct Connect
- **Ahorro anual**: $1,980/año

---

## 📊 Costos Actualizados por Aplicación

### Distribución de Conectividad (25% cada app)

| Aplicación | VPN (25%) | Data Transfer | Total Híbrido |
|------------|-----------|---------------|---------------|
| Saras | $18 | $10 | $28 |
| SonarQube | $18 | $15 | $33 |
| API Portal | $18 | $20 | $38 |
| Portal Guía | $19 | $20 | $39 |
| **TOTAL** | **$73** | **$65** | **$138/mes** |

### Comparativa

| Concepto | Direct Connect | VPN Site-to-Site | Ahorro |
|----------|----------------|------------------|--------|
| Conectividad | $401/mes | $138/mes | **-$263/mes** |
| Lead Time | 2-4 semanas | 1-3 días | **Inmediato** |

---

## 🎯 Nuevos Costos Totales

### Por Aplicación

| Aplicación | Antes (DC) | Ahora (VPN) | Ahorro |
|------------|------------|-------------|--------|
| Saras | $296 | $249 | -$47 |
| SonarQube | $511 | $469 | -$42 |
| API Portal | $1,387 | $1,345 | -$42 |
| Portal Guía | $1,386 | $1,347 | -$39 |
| **TOTAL** | **$3,580** | **$3,410** | **-$170/mes** |

### Proyección Anual

| Escenario | Mensual | Anual |
|-----------|---------|-------|
| **VPN On-Demand** | $3,410 | $40,920 |
| **VPN + RI (1 año)** | $3,026 | $36,312 |
| **VPN + RI (3 años)** | $2,480 | $29,760 |

---

## ⚡ Performance con VPN

### Latencia Esperada
- **VPN**: 20-50ms (aceptable para la mayoría de aplicaciones)
- **Queries simples**: < 100ms total
- **Queries complejas**: 200-500ms

### Optimizaciones Requeridas

1. **Connection Pooling** (obligatorio)
   ```
   Min Pool Size: 10
   Max Pool Size: 100
   Connection Timeout: 30s
   ```

2. **Caching Agresivo** (ElastiCache)
   - Session data: 100% en cache
   - Queries frecuentes: 80% hit rate
   - TTL: 5-15 minutos

3. **Query Optimization**
   - Reducir round-trips
   - Batch operations
   - Stored procedures

4. **Async Operations**
   - Background jobs para operaciones pesadas
   - Queue-based processing

---

## 📈 Plan de Migración

### Fase 1: Setup VPN (Semana 1)
**Duración**: 1-3 días

- [ ] Crear Virtual Private Gateway en AWS
- [ ] Configurar Customer Gateway on-premise
- [ ] Establecer 2 túneles VPN
- [ ] Configurar BGP routing
- [ ] Probar conectividad
- [ ] Validar latencia (< 50ms)
- [ ] Configurar monitoring

### Fase 2: Migración Piloto (Semanas 2-4)
**Aplicaciones**: Saras + SonarQube

- [ ] Migrar Saras
- [ ] Validar performance con VPN
- [ ] Ajustar connection pooling
- [ ] Optimizar queries críticas
- [ ] Migrar SonarQube
- [ ] Monitoreo 24/7

### Fase 3: Migración Producción (Semanas 5-8)
**Aplicaciones**: API Portal + Portal Guía

- [ ] Migrar API Portal
- [ ] Validar con usuarios
- [ ] Migrar Portal Guía
- [ ] Monitoreo intensivo

### Fase 4: Optimización (Semana 9+)
**Opcional**: Upgrade a Direct Connect si necesario

- [ ] Evaluar métricas de latencia
- [ ] Evaluar utilización de ancho de banda
- [ ] Decisión: mantener VPN o upgrade a DC
- [ ] Si upgrade: solicitar Direct Connect (2-4 semanas)

---

## 🎯 Criterios para Upgrade a Direct Connect

### Evaluar después de 2-3 meses

**Upgrade SI:**
- ✅ Latencia promedio > 40ms
- ✅ Utilización VPN > 70%
- ✅ Quejas de performance de usuarios
- ✅ Queries críticas > 500ms

**Mantener VPN SI:**
- ✅ Latencia promedio < 30ms
- ✅ Utilización VPN < 50%
- ✅ Performance aceptable
- ✅ Usuarios satisfechos

---

## ⚠️ Consideraciones

### Ventajas VPN
✅ Implementación inmediata (1-3 días)  
✅ Costo menor ($138/mes vs $401/mes)  
✅ Sin compromiso de largo plazo  
✅ Fácil upgrade a Direct Connect después  
✅ 2 túneles redundantes  
✅ Encriptación incluida  

### Desventajas VPN
⚠️ Latencia mayor (20-50ms vs < 10ms)  
⚠️ Ancho de banda limitado (1.25 Gbps/túnel)  
⚠️ Latencia variable (depende de internet)  
⚠️ Requiere optimizaciones en aplicaciones  

### Mitigaciones
✅ Connection pooling agresivo  
✅ ElastiCache para reducir queries  
✅ Query optimization  
✅ Async operations  
✅ Monitoring continuo  

---

## 📋 Checklist de Implementación

### Pre-requisitos On-Premise
- [ ] Router/Firewall compatible con IPSec
- [ ] IP pública estática
- [ ] BGP ASN (opcional pero recomendado)
- [ ] Firewall rules preparadas
- [ ] Equipo de red disponible

### AWS Setup
- [ ] VPC creado
- [ ] Subnets configuradas
- [ ] Route tables preparadas
- [ ] Security Groups definidos
- [ ] Virtual Private Gateway creado

### Testing
- [ ] Ping test (latencia)
- [ ] Bandwidth test (iperf)
- [ ] DB connectivity test
- [ ] Application test
- [ ] Failover test (túnel 1 → túnel 2)

---

## 🚀 Timeline Actualizado

| Fase | Duración | Actividades |
|------|----------|-------------|
| **Semana 1** | 3 días | Setup VPN + Testing |
| **Semanas 2-4** | 3 semanas | Migración Piloto (Saras, SonarQube) |
| **Semanas 5-8** | 4 semanas | Migración Producción (API Portal, Portal Guía) |
| **Semana 9+** | Continuo | Monitoreo y Optimización |

**Total**: 8 semanas vs 10-12 semanas con Direct Connect

**Ahorro de tiempo**: 2-4 semanas

---

**Última actualización**: 2025-12-04  
**Estado**: Estrategia VPN Site-to-Site definida  
**Decisión**: Implementación inmediata sin Direct Connect
