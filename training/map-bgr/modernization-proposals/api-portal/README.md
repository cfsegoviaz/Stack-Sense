# Api Portal - Static Site con Amplify y Azure DevOps

**Estrategia**: Static Site Hosting  
**Timeline**: 5 días  
**Costo AWS**: $1.50/mes  
**Ahorro**: 99.9% ($1,998/mes)

---

## 📄 Documentos

- **[API_PORTAL_AZURE_DEVOPS_AMPLIFY.md](./API_PORTAL_AZURE_DEVOPS_AMPLIFY.md)**: Plan completo con Azure DevOps CI/CD

---

## 🎯 Resumen Ejecutivo

### Transformación
- **De**: 5 VMs Windows (42 vCPUs, 144GB RAM)
- **A**: AWS Amplify Hosting (serverless)

### Arquitectura Multi-Cloud
- **CI/CD**: Azure DevOps Pipelines
- **Hosting**: AWS Amplify (S3 + CloudFront)
- **DNS**: Route 53
- **SSL**: Certificate Manager (gratis)

### Beneficios Clave
- ✅ 99.9% reducción de costos ($2,000 → $1.50)
- ✅ Deploy automático con cada commit
- ✅ CDN global (400+ edge locations)
- ✅ SSL/TLS automático
- ✅ Zero maintenance

---

## 🏗️ Arquitectura

![Arquitectura Api Portal](./diagrams/api_portal_azure_devops_amplify.png)

### Flujo CI/CD
```
Developer → Azure Repos (git push)
              ↓
         Azure Pipelines (build)
              ↓
         AWS S3 (deploy)
              ↓
         CloudFront (CDN)
              ↓
         Users (global)
```

---

## 💰 Costos

| Servicio | Costo/mes |
|----------|-----------|
| Azure DevOps (5 usuarios) | $0 |
| AWS S3 + CloudFront | $1.50 |
| **TOTAL** | **$1.50** |

**Comparativa**: $2,000 → $1.50 = $1,998/mes ahorro (99.9%)

---

## 🚀 Pipeline Azure DevOps

```yaml
trigger: [main, develop, staging]

stages:
  - Build
  - Deploy_Dev
  - Deploy_Staging
  - Deploy_Production (manual approval)
```

### Ambientes
- **Development**: Auto-deploy desde `develop`
- **Staging**: Auto-deploy desde `staging`
- **Production**: Manual approval desde `main`

---

## 📋 Estado

- [x] Plan completo con Azure DevOps
- [x] Pipeline YAML definido
- [x] Arquitectura multi-cloud
- [x] Costos calculados
- [ ] Aprobación pendiente
- [ ] Implementación pendiente

---

**Última actualización**: 2025-12-04
