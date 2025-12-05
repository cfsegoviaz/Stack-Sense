# SARAS - Modernización con ECS y Babelfish

**Estrategia**: Modernización Completa (Containerización)  
**Timeline**: 11 semanas  
**Costo AWS**: $904/mes  
**Ahorro**: 35% ($496/mes)

---

## 📄 Documentos

- **[SARAS_MODERNIZATION_PLAN.md](./SARAS_MODERNIZATION_PLAN.md)**: Plan completo de modernización

---

## 🎯 Resumen Ejecutivo

### Transformación
- **De**: 2 VMs Windows + SQL Server
- **A**: ECS Fargate + Aurora PostgreSQL con Babelfish

### Beneficios Clave
- ✅ Contenedores serverless (ECS Fargate)
- ✅ Auto-scaling automático
- ✅ Aurora Babelfish (compatibilidad SQL Server)
- ✅ Sin cambios de código de aplicación
- ✅ 35% reducción de costos

### Fases
1. **Assessment** (2 semanas): Análisis de código y BD
2. **Containerización** (3 semanas): Docker + ECR
3. **Migración BD** (3 semanas): SCT + DMS a Babelfish
4. **Testing** (2 semanas): QA completo
5. **Go-Live** (1 semana): Producción

---

## 🏗️ Arquitectura

![Arquitectura SARAS](./diagrams/saras_modernization_complete.png)

### Componentes
- **ECS Fargate**: 2-4 tasks (auto-scaling)
- **Aurora PostgreSQL + Babelfish**: db.r5.large Multi-AZ
- **Application Load Balancer**: HTTPS
- **ElastiCache Redis**: Cache distribuido
- **Amazon ECR**: Container registry

---

## 💰 Costos

| Componente | Costo/mes |
|------------|-----------|
| ECS Fargate | $117 |
| Aurora Babelfish | $594 |
| Cache & Storage | $62 |
| Networking | $43 |
| Monitoring | $6 |
| **TOTAL** | **$904** |

**Comparativa**: $1,400 → $904 = $496/mes ahorro (35%)

---

## 🔧 Herramientas de Migración

- **AWS Schema Conversion Tool (SCT)**: Convierte schema SQL Server
- **AWS Database Migration Service (DMS)**: Migra datos con CDC
- **Docker**: Containerización de aplicación
- **Amazon ECR**: Registry de imágenes

---

## 📋 Estado

- [x] Plan de modernización completo
- [x] Arquitectura definida
- [x] Costos calculados
- [ ] Aprobación pendiente
- [ ] Implementación pendiente

---

**Última actualización**: 2025-12-04
