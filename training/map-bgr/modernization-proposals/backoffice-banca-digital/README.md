# Backoffice Banca Digital - Propuesta de Modernización

## 📋 Resumen

| Atributo | Valor |
|----------|-------|
| **Aplicación** | Backoffice Banca Digital |
| **VMs** | 3 (2 PROD + 1 TEST) |
| **vCPUs** | 10 |
| **RAM** | 20 GB |
| **Framework** | .NET Core 8 ✅ |
| **Estrategia Recomendada** | ECS Fargate (Containerización) |
| **Ahorro Estimado** | 75% vs On-Premise |

## 📁 Contenido

- [BACKOFFICE_BANCA_DIGITAL_MODERNIZATION.md](./BACKOFFICE_BANCA_DIGITAL_MODERNIZATION.md) - Propuesta completa
- [diagrams/](./diagrams/) - Diagramas de arquitectura

## 🏗️ Opciones de Arquitectura

| Opción | Costo/Mes | Timeline | Recomendación |
|--------|-----------|----------|---------------|
| Lift & Shift | $547.91 | 2-3 sem | ❌ |
| Replatform Linux | $380.50 | 3-4 sem | ⚠️ |
| **ECS Fargate** | **$295.80** | **4-6 sem** | **✅ Recomendada** |
| Modernización Completa | $420.00 | 8-12 sem | ⚠️ |

## 🎯 Por qué ECS Fargate

1. **.NET Core 8** ya está modernizado - ideal para containers
2. **RDS existente** en AWS - reduce complejidad
3. **S3 existente** - ya usan buckets en AWS
4. **46% ahorro** vs Lift & Shift
5. **Sin gestión de servidores** - operaciones simplificadas

## 📊 Diagramas

- `backoffice_banca_digital_lift_shift.png` - Arquitectura Lift & Shift
- `backoffice_banca_digital_ecs_fargate.png` - Arquitectura ECS Fargate
- `backoffice_banca_digital_modernization.png` - Modernización completa

## 📅 Próximos Pasos

1. [ ] Revisión con stakeholders
2. [ ] Aprobación de presupuesto
3. [ ] Creación de Dockerfile
4. [ ] Provisioning de infraestructura
5. [ ] Migración y testing

---

**Fecha**: 2026-01-02  
**Responsable**: Erik Palma (erik.palma@bgr.com.ec)
