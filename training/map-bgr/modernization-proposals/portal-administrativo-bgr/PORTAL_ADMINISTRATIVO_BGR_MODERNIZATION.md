# PortalAdministrativoBGR - Plan de Modernización
## Gestión de Usuarios Siglo 21

**Fecha**: 2026-01-06  
**Aplicación**: PortalAdministrativoBGR  
**Estrategia Recomendada**: Consolidar con Backoffice Sistemas  
**Timeline**: 1 semana

---

## 🎯 Información de la Aplicación

### Descripción
Permite realizar tareas de desbloqueo y deslogueo de usuarios del core bancario Siglo 21. Herramienta administrativa crítica para soporte de usuarios.

### Situación Actual

| Atributo | Valor |
|----------|-------|
| **Servidores** | ECBRPRW44, ECBRPRW45 (compartidos) |
| **Framework** | .NET Framework 4.7.1 |
| **Base de Datos** | SQL Server 2016 Standard (PORTAL_ADMINISTRATIVO_BGR) |
| **Integración** | Siglo 21 Core Banking |
| **Usuarios** | ~20 administradores |
| **Criticidad** | Baja (pero crítica para soporte) |

### ⚠️ Hallazgo Clave
- Comparte infraestructura con **Backoffice Sistemas** y **PortalGuiaBGR**
- Requiere conectividad con **Siglo 21** (core bancario on-premise)
- Costo marginal actual: ~$0/mes

---

## 🏗️ Opciones de Arquitectura

### Opción 1: Consolidar con Backoffice Sistemas (RECOMENDADA)

![Arquitectura Consolidada](./diagrams/generated-diagrams/portal_admin_consolidate.png)

| Servicio | Costo/mes |
|----------|-----------|
| Incluido en Backoffice | $0 |
| CloudWatch adicional | $2 |
| **TOTAL** | **$2/mes** |

#### 💡 Tips y Recomendaciones IA

**Cuándo elegir:**
- Aplicaciones que comparten infraestructura
- Bajo uso y criticidad
- Requiere conectividad híbrida con Siglo 21

**Consideraciones:**
- Ya incluida en migración de Backoffice
- Mantiene conectividad con Siglo 21 via VPN
- Sin esfuerzo adicional

**Recomendaciones:**
- Migrar junto con Backoffice Sistemas
- Validar conectividad con Siglo 21 post-migración
- Monitorear tiempos de respuesta

**Ideal para:**
- Consolidación de workloads
- Aplicaciones con dependencias on-premise

#### 📋 Esfuerzo Escala24x7

| Tarea | Horas | Equipo |
|-------|-------|--------|
| CloudWatch Logs | 4 | Infra |
| Testing integración | 4 | QA |
| Knowledge transfer | 2 | Infra |
| **TOTAL** | **10** | |

**Costo implementación**: 10 horas × $150/hora = **$1,500 USD**

---

### Opción 2: Lambda + API Gateway Híbrido

![Arquitectura Serverless](./diagrams/generated-diagrams/portal_admin_serverless.png)

| Servicio | Costo/mes |
|----------|-----------|
| API Gateway | $3 |
| Lambda | $2 |
| Cognito | $0 |
| VPN (compartido) | $5 |
| CloudWatch | $2 |
| **TOTAL** | **$12/mes** |

#### 💡 Tips y Recomendaciones IA

**Cuándo elegir:**
- Si se requiere modernización
- Equipos con experiencia serverless
- Cuando se busca independencia

**Consideraciones:**
- Requiere VPN para conectar con Siglo 21
- Lambda puede tener cold starts
- Cognito para autenticación con AD

**Recomendaciones:**
- Usar Provisioned Concurrency si latencia crítica
- Implementar retry logic para Siglo 21
- Configurar timeouts adecuados

**Ideal para:**
- Modernización gradual
- APIs de administración

#### 📋 Esfuerzo Escala24x7

| Tarea | Horas | Equipo |
|-------|-------|--------|
| API Gateway | 8 | Infra |
| Lambda Functions | 16 | Infra |
| DynamoDB Table | 2 | Infra |
| VPN Site-to-Site | 16 | Infra |
| Desarrollo Lambdas | 16 | Delivery |
| Application pipeline (SAM) | 4 | Delivery |
| CloudWatch Dashboard | 8 | Infra |
| Testing y validación | 8 | QA |
| Knowledge transfer | 4 | Infra |
| **TOTAL** | **82** | |

**Costo implementación**: 82 horas × $150/hora = **$12,300 USD**

---

### Opción 3: ECS Microservicio Híbrido

![Arquitectura ECS](./diagrams/generated-diagrams/portal_admin_ecs.png)

| Servicio | Costo/mes |
|----------|-----------|
| ECS Fargate | $18 |
| ALB | $22.50 |
| ECR | $2 |
| VPN (compartido) | $5 |
| CloudWatch | $3 |
| **TOTAL** | **$50.50/mes** |

#### 💡 Tips y Recomendaciones IA

**Cuándo elegir:**
- Si se requiere desacoplamiento
- Equipos con experiencia en contenedores
- Cuando hay requisitos de aislamiento

**Consideraciones:**
- Costo alto para app de bajo uso
- Requiere containerización
- Mantiene dependencia de Siglo 21

**Recomendaciones:**
- Solo si hay requisito de independencia
- Evaluar ROI vs consolidación
- Considerar serverless como alternativa

**Ideal para:**
- Desacoplamiento obligatorio
- Equipos container-first

#### 📋 Esfuerzo Escala24x7

| Tarea | Horas | Equipo |
|-------|-------|--------|
| VPC/Redes | 4 | Infra |
| Fargate Cluster | 2 | Infra |
| Fargate Service | 4 | Infra |
| ALB | 2 | Infra |
| Aurora PostgreSQL | 2 | Infra |
| ECR | 1 | Infra |
| VPN Site-to-Site | 16 | Infra |
| DMS replication instance | 4 | Data |
| DMS replication task | 4 | Data |
| Application pipeline (ECS) | 4 | Infra |
| CloudWatch Dashboard | 8 | Infra |
| Testing y validación | 16 | QA |
| Knowledge transfer | 8 | Infra |
| **TOTAL** | **75** | |

**Costo implementación**: 75 horas × $150/hora = **$11,250 USD**

---

## 📊 Comparativa

| Criterio | Consolidar | Serverless | ECS |
|----------|------------|------------|-----|
| **Costo/mes** | $2 | $12 | $50.50 |
| **Esfuerzo** | Ninguno | Medio | Medio |
| **Timeline** | 0 | 3 semanas | 2 semanas |
| **Recomendado** | ✅ Sí | Si moderniza | No |

---

## ✅ Recomendación Final

**Consolidar con Backoffice Sistemas** por:
1. Costo mínimo ($2/mes)
2. Comparte infraestructura existente
3. Mantiene conectividad con Siglo 21
4. Sin esfuerzo adicional

---

**Última actualización**: 2026-01-06
