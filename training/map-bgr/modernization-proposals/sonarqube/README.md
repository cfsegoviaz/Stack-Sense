# SonarQube - Lift & Shift Optimizado

**Estrategia**: Lift & Shift con Optimizaciones  
**Timeline**: 2 semanas  
**Costo AWS**: $404/mes  
**Ahorro**: 73% ($1,096/mes)

---

## 📄 Documentos

- **[SONARQUBE_LIFT_SHIFT.md](./SONARQUBE_LIFT_SHIFT.md)**: Plan completo de migración

---

## 🎯 Resumen Ejecutivo

### Transformación
- **De**: 3 VMs Windows + SQL Server
- **A**: 1 EC2 Linux + RDS PostgreSQL

### Optimizaciones Clave
- ✅ **SQL Server → PostgreSQL**: Gratis + mejor performance
- ✅ **Windows → Linux**: Sin licencias + menor overhead
- ✅ **3 VMs → 1 EC2**: Rightsizing adecuado
- ✅ **Multi-AZ**: Alta disponibilidad

### Beneficios
- ✅ 73% reducción de costos
- ✅ Mejor performance (PostgreSQL)
- ✅ Sin licencias (PostgreSQL + Linux)
- ✅ Migración rápida (2 semanas)

---

## 🏗️ Arquitectura

![Arquitectura SonarQube](./diagrams/sonarqube_lift_shift.png)

### Componentes
- **EC2**: t3.xlarge (Amazon Linux 2)
- **RDS PostgreSQL**: db.t3.large Multi-AZ
- **EFS**: Shared storage para plugins
- **ALB**: HTTPS con SSL/TLS
- **S3**: Backups diarios

---

## 💰 Costos

| Componente | Costo/mes |
|------------|-----------|
| EC2 (t3.xlarge) | $121 |
| RDS PostgreSQL Multi-AZ | $158 |
| Storage (EFS + S3 + EBS) | $23.50 |
| Networking (ALB + NAT) | $61 |
| Monitoring | $4 |
| **TOTAL** | **$404** |

**Comparativa**: $1,500 → $404 = $1,096/mes ahorro (73%)

---

## 🔄 Integraciones CI/CD

### Azure DevOps
```yaml
- SonarQubePrepare
- Build/Test
- SonarQubeAnalyze
- SonarQubePublish
```

### GitHub Actions
```yaml
- Checkout
- SonarQube Scan
- Quality Gate
```

---

## 🔧 Configuración

### SonarQube
- **Versión**: Latest stable (10.3+)
- **Java**: OpenJDK 17
- **Database**: PostgreSQL 15

### Optimizaciones
```properties
sonar.search.javaOpts=-Xmx4G
sonar.web.javaOpts=-Xmx2G
sonar.ce.javaOpts=-Xmx2G
```

---

## 📋 Estado

- [x] Plan completo de migración
- [x] Arquitectura optimizada
- [x] Integraciones CI/CD definidas
- [x] Scripts de backup
- [ ] Aprobación pendiente
- [ ] Implementación pendiente

---

**Última actualización**: 2025-12-04
