# Backoffice Sistemas BGR - Lift & Shift Híbrido

**Estrategia**: Lift & Shift con Conectividad Híbrida  
**Timeline**: 3 semanas  
**Costo AWS**: $402/mes  
**Base de Datos**: On-Premise (VPN)

---

## 📄 Documentos

- **[BACKOFFICE_SISTEMAS_LIFT_SHIFT.md](./BACKOFFICE_SISTEMAS_LIFT_SHIFT.md)**: Plan completo de migración

---

## 🎯 Resumen Ejecutivo

### Estrategia
- **Aplicación**: Migrar a EC2 (sin cambios de código)
- **Base de Datos**: Mantener on-premise
- **Conectividad**: Site-to-Site VPN

### Beneficios Clave
- ✅ Migración rápida (3 semanas)
- ✅ Menor riesgo (sin cambios de código)
- ✅ Quick wins de AWS (escalabilidad, monitoreo)
- ✅ Roadmap de modernización futura

### Fases
1. **Networking** (1 semana): VPC + VPN
2. **Migración** (1 semana): EC2 + ALB
3. **Go-Live** (1 semana): Producción

---

## 🏗️ Arquitectura Híbrida

![Arquitectura Híbrida](./diagrams/backoffice_sistemas_hybrid.png)

### Componentes AWS
- **EC2**: 2x t3.xlarge (Windows Server 2019)
- **ALB**: Application Load Balancer
- **VPN**: Site-to-Site VPN (2 túneles)
- **NAT Gateway**: Salida a internet

### Networking (CRÍTICO)
```
AWS VPC (10.0.0.0/16)
    ↓
Site-to-Site VPN (AES-256)
    ↓
On-Premise (192.168.0.0/16)
    ↓
SQL Server
```

---

## 💰 Costos

| Componente | Costo/mes |
|------------|-----------|
| EC2 (2x t3.xlarge) | $243 |
| Networking (ALB, NAT, VPN) | $101 |
| Storage | $17 |
| Monitoring | $4 |
| **TOTAL** | **$402** |

**Nota**: SQL Server mantiene costo on-premise

---

## 🔄 Roadmap de Modernización Futura

### Fase 2: Modernización (6 meses)
- **Amazon Q for .NET Transform**: Migrar a .NET 8
- **Containerización**: ECS Fargate
- **CI/CD**: Pipeline automatizado

### Fase 3: Migración BD (3 meses)
- **Opción 1**: RDS SQL Server (~$300/mes)
- **Opción 2**: Aurora Babelfish (~$150/mes) ✅ Recomendado

---

## 📋 Estado

- [x] Plan Lift & Shift completo
- [x] Arquitectura híbrida definida
- [x] Networking detallado
- [x] Roadmap de modernización
- [ ] Aprobación pendiente
- [ ] Implementación pendiente

---

**Última actualización**: 2025-12-04
