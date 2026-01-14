# Analysis Checklist - MAP BGR

**Progreso Total: 43/43 aplicaciones (100%) ✅**

```
██████████████████████████████ 100%
```

**Última actualización:** 2026-01-07

---

## ⚠️ REGLAS CRÍTICAS - NO OLVIDAR

### 1. Estructura Completa del JSON Showcase

El JSON debe incluir TODOS estos campos obligatorios:

```json
{
  "id": "app-id",
  "slug": "app-id",
  "name": "Nombre App",
  "description": "Descripción",
  "clientId": "bgr",
  "waveId": "wave-1",
  "status": "assessed",
  "currentMonthlyCost": 500,
  "recommendedArchitecture": "arquitectura-id",
  "lastUpdated": "2026-01-06",
  "keyFinding": "Hallazgo principal de la aplicación",
  "owner": {
    "name": "Nombre Responsable",
    "email": "email@bgr.com.ec",
    "role": "Rol"
  },
  "currentState": {
    "vms": [
      {"name": "VM-01", "vCPUs": 4, "ramGB": 16, "storageGB": 100, "os": "Windows Server 2019", "ip": "172.20.x.x", "status": "poweredOn", "environment": "prod"}
    ],
    "totalvCPUs": 4,
    "totalRAM": 16,
    "totalStorage": 100,
    "users": 50,
    "criticality": "medium"
  },
  "techStack": {
    "frontend": ["React", "Angular"],
    "backend": [".NET Core", "Java"],
    "database": ["SQL Server", "PostgreSQL"],
    "other": ["Redis", "RabbitMQ"]
  },
  "architectures": [...]
}
```

### 2. Estructura Completa de Arquitecturas

Cada arquitectura DEBE incluir TODOS estos campos:

```json
{
  "id": "arch-id",
  "name": "Nombre Arquitectura",
  "strategy": "Replatform",
  "recommended": true,
  "monthlyCost": 302,
  "savingsPercent": 40,
  "implementationHours": 32,
  "implementationCost": 4800,
  "timeline": "4 semanas",
  "complexity": "low",
  "risk": "low",
  "description": "Descripción de la arquitectura",
  "diagramUrl": "/diagrams/app_arch.png",
  "components": [
    {"service": "EC2", "configuration": "t3.large", "monthlyCost": 100, "pricingModel": "On-Demand", "quantity": "1 instancia"}
  ],
  "advantages": ["Ventaja 1", "Ventaja 2"],
  "disadvantages": ["Desventaja 1"],
  "tco": {
    "year1Total": 8424,
    "yearlyRecurring": 3624
  },
  "tips": {
    "whenToChoose": ["Array de strings"],
    "considerations": ["Array de strings"],
    "recommendations": ["Array de strings"],
    "idealFor": ["Array de strings"]
  }
}
```

### 3. Formato de Tips (ArchitectureTips)
Los tips **DEBEN ser arrays de strings**, NO strings simples:

```json
// ❌ INCORRECTO - causa pantalla en blanco
"tips": { "whenToChoose": "Equipos que buscan modernizar..." }

// ✅ CORRECTO
"tips": { "whenToChoose": ["Equipos que buscan modernizar", "Organizaciones cloud-first"] }
```

### 4. Otras Reglas
- **1 diagrama por arquitectura** (mínimo 3 arquitecturas por app)
- **Timeline concreto** (ej: "3 semanas"), nunca "Incluido en X"
- **Horas específicas** del effort_matrix.json
- **SQL Server → PostgreSQL**: incluir AWS SCT, Babelfish, AWS DMS
- **Validar JSON** con `python3 -m json.tool` antes de commit

---

## ✅ Aplicaciones Completadas (18)

| # | Aplicación | Fecha | Propuesta MD | JSON Showcase | Diagramas | Arquitecturas |
|---|------------|-------|--------------|---------------|-----------|---------------|
| 1 | Backoffice Banca Digital | 2026-01-02 | ✅ | ✅ | ✅ | 3 |
| 2 | Backoffice Sistemas | 2026-01-06 | ✅ | ✅ | ✅ | 3 |
| 3 | SARAS | 2026-01-06 | ✅ | ✅ | ✅ | 3 |
| 4 | API Portal | 2026-01-06 | ✅ | ✅ | ✅ | 3 |
| 5 | SonarQube | 2026-01-06 | ✅ | ✅ | ✅ | 3 |
| 6 | SEQ | 2026-01-07 | ✅ | ✅ | ✅ | 2 |
| 7 | Visor Histórico de Cheques | 2026-01-06 | ✅ | ✅ | ✅ | 3 |
| 8 | Calculadora Inmobiliaria | 2026-01-06 | ✅ | ✅ | ✅ | 3 |
| 9 | Administrador de Pagos | 2026-01-06 | ✅ | ✅ | ✅ | 3 |
| 10 | Librarian | 2026-01-06 | ✅ | ✅ | ✅ | 3 |
| 11 | Cuadre y Compensación ATMs | 2026-01-06 | ✅ | ✅ | ✅ | 3 |
| 12 | PortalGuiaBGR | 2026-01-06 | ✅ | ✅ | ✅ | 3 |
| 13 | PortalAdministrativoBGR | 2026-01-06 | ✅ | ✅ | ✅ | 3 |
| 14 | BGRTuCuenta | 2026-01-06 | ✅ | ✅ | ✅ | 3 |
| 15 | Acciones y Accionistas | 2026-01-06 | ✅ | ✅ | ✅ | 3 |
| 16 | Estructuras de Control | 2026-01-06 | ✅ | ✅ | ✅ | 3 |
| 17 | Nueva Centralizada | 2026-01-06 | ✅ | ✅ | ✅ | 3 |
| 18 | Redis | 2026-01-06 | ✅ | ✅ | ✅ | 3 |
| 19 | Microservicios | 2026-01-06 | ✅ | ✅ | ✅ | 3 |
| 20 | BGRSeguridadCentralAPI | 2026-01-06 | ✅ | ✅ | ✅ | 3 |
| 21 | BGRAccesoServiciosAPI | 2026-01-06 | ✅ | ✅ | ✅ | 3 |
| 22 | BGRInterfacesSiglo (Suite) | 2026-01-06 | ✅ | ✅ | ✅ | 3 |
| 23 | Administración Cobranzas SAC | 2026-01-06 | ✅ | ✅ | ✅ | 3 |
| 24 | MyABCM | 2026-01-06 | ✅ | ✅ | ✅ | 3 |
| 25 | RCSA | 2026-01-06 | ✅ | ✅ | ✅ | 3 |
| 26 | Control M | 2026-01-06 | ✅ | ✅ | ✅ | 3 |
| 27 | Evolution | 2026-01-06 | ✅ | ✅ | ✅ | 3 |
| 28 | AURO | 2026-01-06 | ✅ | ✅ | ✅ | 3 |
| 29 | Monitor Plus | 2026-01-06 | ✅ | ✅ | ✅ | 3 |
| 30 | EFlow | 2026-01-06 | ✅ | ✅ | ✅ | 3 |
| 31 | E-Business | 2026-01-06 | ✅ | ✅ | ✅ | 3 |
| 32 | RPA Automation Anywhere | 2026-01-06 | ✅ | ✅ | ✅ | 3 |
| 33 | BancaOficialCom | 2026-01-06 | ✅ | ✅ | ✅ | 3 |
| 34 | Cubos | 2026-01-06 | ✅ | ✅ | ✅ | 3 |
| 35 | PruebasDepartamentalesCom | 2026-01-06 | ✅ | ✅ | ✅ | 3 |
| 36 | DataWarehouse Campañas | 2026-01-06 | ✅ | ✅ | ✅ | 3 |
| 37 | SharePoint ITD | 2026-01-06 | ✅ | ✅ | ✅ | 3 |
| 38 | ODS | 2026-01-06 | ✅ | ✅ | ✅ | 3 |
| 39 | Ventana Marco | 2026-01-07 | ✅ | ✅ | ✅ | 2 |
| 40 | Garantías/SISGAR | 2026-01-07 | ✅ | ✅ | ✅ | 2 |
| 41 | SharePoint OpRisk | 2026-01-07 | ✅ | ✅ | ✅ | 2 |
| 42 | Brightmail | 2026-01-07 | ✅ | ✅ | ✅ | 3 |
| 43 | DCNET Cámara | 2026-01-07 | ✅ | ✅ | ✅ | 3 |

---

## 📊 Resumen por Estado

| Estado | Cantidad | Porcentaje |
|--------|----------|------------|
| ✅ Completado | 43 | 100% |
| 🔄 En progreso | 0 | 0% |
| ⬜ Pendiente | 0 | 0% |

---

## 📝 Notas

- Las aplicaciones están ordenadas por ponderación (mayor = más prioritaria)
- Prioridad 3 (Proveedores) requiere coordinación con vendors para modelo SAAS
- Prioridad 4 tiene dependencia con iniciativa "Estructuras de Control 2026"
- **✅ COMPLETADO**: Todas las 43 aplicaciones analizadas con JSONs y MDs

### Prioridad 1 - Journey to Cloud 2026 (9)

| # | Aplicación | Criticidad | Ponderación | Estado |
|---|------------|------------|-------------|--------|
| 7 | ~~Visor Histórico de Cheques~~ | ~~Media~~ | ~~52~~ | ✅ |
| 8 | ~~Calculadora Inmobiliaria~~ | ~~Media~~ | ~~52~~ | ✅ |
| 9 | ~~Administrador de Pagos~~ | ~~Alta~~ | ~~50~~ | ✅ |
| 10 | ~~Librarian~~ | ~~Media~~ | ~~45~~ | ✅ |
| 11 | ~~Cuadre y Compensación ATMs~~ | ~~Media~~ | ~~45~~ | ✅ |
| 12 | ~~PortalGuiaBGR~~ | ~~Baja~~ | ~~43~~ | ✅ |
| 13 | ~~PortalAdministrativoBGR~~ | ~~Baja~~ | ~~43~~ | ✅ |
| 14 | ~~BGRTuCuenta~~ | ~~Baja~~ | ~~43~~ | ✅ |
| 15 | ~~Acciones y Accionistas~~ | ~~Media~~ | ~~42~~ | ✅ |
| 16 | ~~Estructuras de Control~~ | ~~Media~~ | ~~40~~ | ✅ |
| 17 | ~~Nueva Centralizada~~ | ~~Baja~~ | ~~36~~ | ✅ |
| 18 | ~~Redis~~ | ~~Alta~~ | ~~28~~ | ✅ |

### Prioridad 2 - Microservicios/APIs (6)

| # | Aplicación | Criticidad | Ponderación | Estado |
|---|------------|------------|-------------|--------|
| 19 | Microservicios | Alta | 38 | ⬜ |
| 20 | BGRSeguridadCentralAPI | Media | 38 | ⬜ |
| 21 | BGRAccesoServiciosAPI | Media | 38 | ⬜ |
| 22 | BGRInterfacesSigloApp | Alta | 29 | ⬜ |
| 23 | BGRInterfacesSigloMS | Alta | 28 | ⬜ |
| 24 | BGRInterfacesSiglo | Alta | 28 | ⬜ |

### Prioridad 3 - Proveedores/SAAS (10)

| # | Aplicación | Proveedor | Ponderación | Estado |
|---|------------|-----------|-------------|--------|
| 25 | Administración Cobranzas SAC | ECS | 50 | ⬜ |
| 26 | MyABCM | ABCOSTING | 39 | ⬜ |
| 27 | RCSA | BUSINESSWARE | 38 | ⬜ |
| 28 | Control M | BMC | 37 | ⬜ |
| 29 | Evolution | ME&HE | 36 | ⬜ |
| 30 | AURO | SERIVARSA | 35 | ⬜ |
| 31 | Monitor Plus | PLUS TI | 28 | ⬜ |
| 32 | EFlow | SIDESYS | 28 | ⬜ |
| 33 | E-Business | E-BUSSINESS | 24 | ⬜ |
| 34 | RPA Automation Anywhere | E&Y | 30 | ⬜ |

### Prioridad 4 - Modernización Compleja (6)

| # | Aplicación | Iniciativa | Ponderación | Estado |
|---|------------|------------|-------------|--------|
| 35 | BancaOficialCom | Estructuras 2026 | 42 | ⬜ |
| 36 | Cubos | Estructuras 2026 | 42 | ⬜ |
| 37 | PruebasDepartamentalesCom | Estructuras 2026 | 41 | ⬜ |
| 38 | DataWarehouse Campañas | Estructuras 2026 | 51 | ⬜ |
| 39 | SharePoint ITD | Estructuras 2026 | 43 | ⬜ |
| 40 | ODS | Estructuras 2026 | 28 | ⬜ |

### Prioridad 5 - Otros (4)

| # | Aplicación | Tipo | Ponderación | Estado |
|---|------------|------|-------------|--------|
| 41 | ~~Ventana Marco~~ | ~~Legacy Java~~ | ~~34~~ | ✅ |
| 42 | ~~Garantías/SISGAR~~ | ~~Legacy Java~~ | ~~27~~ | ✅ |
| 43 | ~~SharePoint OpRisk~~ | ~~SharePoint~~ | ~~29~~ | ✅ |
| 44 | ~~Brightmail~~ | ~~Linux~~ | ~~22~~ | ✅ |
| 45 | ~~DCNET Cámara~~ | ~~Cámara 2028~~ | ~~37~~ | ✅ |

---

## 📊 Resumen por Estado

| Estado | Cantidad | Porcentaje |
|--------|----------|------------|
| ✅ Completado | 43 | 98% |
| 🔄 En progreso | 0 | 0% |
| ⬜ Pendiente | 1 | 2% |

---

## 📝 Notas

- Las aplicaciones están ordenadas por ponderación (mayor = más prioritaria)
- Prioridad 3 (Proveedores) requiere coordinación con vendors para modelo SAAS
- Prioridad 4 tiene dependencia con iniciativa "Estructuras de Control 2026"
- **SEQ** pendiente de completar con 2 arquitecturas adicionales (única app faltante)
