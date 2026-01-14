# PortalGuiaBGR - Plan de Modernización
## Guía Telefónica del Banco

**Fecha**: 2026-01-06  
**Aplicación**: PortalGuiaBGR  
**Estrategia Recomendada**: Consolidar con Backoffice Sistemas  
**Timeline**: 1 semana

---

## 🎯 Información de la Aplicación

### Descripción
Guía telefónica interna del banco. Permite a los 685 colaboradores consultar información de contacto de sus pares y proveedores.

### Situación Actual (On-Premise)

| Atributo | Valor |
|----------|-------|
| **Servidores** | ECBRPRW44, ECBRPRW45 (compartidos con Backoffice Sistemas) |
| **Framework** | .NET Framework 4.7.1 |
| **Base de Datos** | SQL Server 2016 Enterprise (PORTAL_ADMINISTRATIVO_BGR - compartida) |
| **Usuarios** | 685 colaboradores |
| **Criticidad** | Baja |
| **Disponibilidad** | 0.14% (uso muy bajo) |

### ⚠️ Hallazgo Clave
Esta aplicación **comparte infraestructura** con Backoffice Sistemas:
- Mismos servidores (ECBRPRW44, ECBRPRW45)
- Misma base de datos (PORTAL_ADMINISTRATIVO_BGR)
- Costo marginal actual: ~$0/mes (ya incluido en Backoffice)

---

## 🏗️ Opciones de Arquitectura

### Opción 1: Consolidar con Backoffice Sistemas (RECOMENDADA)

![Arquitectura Consolidada](./diagrams/generated-diagrams/portal_guia_consolidate.png)

#### Descripción
Mantener la aplicación consolidada con Backoffice Sistemas en la migración a AWS. Costo incremental mínimo.

#### Componentes Adicionales
| Servicio | Configuración | Costo/mes |
|----------|---------------|-----------|
| Incluido en Backoffice Sistemas | Ya migrado | $0 |
| CloudWatch (logs adicionales) | ~1 GB | $2 |
| **TOTAL INCREMENTAL** | | **$2/mes** |

#### Ventajas
- ✅ Costo casi nulo ($2/mes)
- ✅ Sin esfuerzo de migración adicional
- ✅ Misma arquitectura híbrida
- ✅ Ya incluido en wave de Backoffice

#### Desventajas
- ❌ Dependencia de Backoffice Sistemas
- ❌ Sin modernización del código
- ❌ Mantiene .NET Framework legacy

#### 💡 Tips y Recomendaciones IA

**Cuándo elegir:**
- Aplicaciones con uso muy bajo (<1%)
- Cuando comparten infraestructura con otra app
- Presupuesto limitado para modernización

**Consideraciones:**
- Ya está incluida en la migración de Backoffice Sistemas
- No requiere esfuerzo adicional
- Evaluar desacoplamiento futuro si crece el uso

**Recomendaciones:**
- Migrar junto con Backoffice Sistemas
- Monitorear uso post-migración
- Planificar modernización solo si aumenta criticidad

**Ideal para:**
- Aplicaciones de bajo uso
- Consolidación de workloads

#### 📋 Esfuerzo Escala24x7

| Tarea | Horas | Equipo |
|-------|-------|--------|
| CloudWatch Logs | 4 | Infra |
| Testing integración | 4 | QA |
| Knowledge transfer | 2 | Infra |
| **TOTAL** | **10** | |

**Costo implementación**: 10 horas × $150/hora = **$1,500 USD**
- Optimización de costos

---

### Opción 2: Serverless API + Angular SPA

![Arquitectura Serverless](./diagrams/generated-diagrams/portal_guia_serverless.png)

#### Componentes
| Servicio | Configuración | Costo/mes |
|----------|---------------|-----------|
| CloudFront | CDN | $1 |
| S3 | Angular SPA | $0.50 |
| API Gateway | REST API | $3 |
| Lambda | Directory API | $2 |
| DynamoDB | Directory data | $5 |
| Cognito | Auth + AD sync | $0 |
| **TOTAL** | | **$11.50/mes** |

#### 💡 Tips y Recomendaciones IA

**Cuándo elegir:**
- Si se requiere modernización completa
- Equipos con experiencia en Angular/React
- Cuando se busca independencia de Backoffice

**Consideraciones:**
- Requiere desarrollo de nuevo frontend Angular
- Sincronización con Active Directory via Cognito
- DynamoDB para datos de directorio

**Recomendaciones:**
- Usar AWS Amplify para acelerar desarrollo
- Implementar búsqueda con DynamoDB GSI
- Configurar sync automático con AD

**Ideal para:**
- Modernización completa del stack
- Independencia de otras aplicaciones

#### 📋 Esfuerzo Escala24x7

| Tarea | Horas | Equipo |
|-------|-------|--------|
| CloudFront Distribution | 2 | Infra |
| S3 Bucket (static) | 2 | Infra |
| API Gateway | 8 | Infra |
| Lambda Functions | 16 | Infra |
| DynamoDB Table | 2 | Infra |
| VPN Site-to-Site | 16 | Infra |
| Desarrollo Frontend | 24 | Delivery |
| Desarrollo Lambdas | 16 | Delivery |
| Application pipeline (SAM) | 4 | Delivery |
| CloudWatch Dashboard | 8 | Infra |
| Testing y validación | 16 | QA |
| Knowledge transfer | 8 | Infra |
| **TOTAL** | **122** | |

**Costo implementación**: 122 horas × $150/hora = **$18,300 USD**

---

### Opción 3: ECS Microservicio Independiente

![Arquitectura ECS](./diagrams/generated-diagrams/portal_guia_ecs.png)

#### Componentes
| Servicio | Configuración | Costo/mes |
|----------|---------------|-----------|
| ECS Fargate | 1 task x 0.5 vCPU, 1 GB | $18 |
| Aurora PostgreSQL | db.t3.small | $45 |
| Application Load Balancer | HTTPS | $22.50 |
| ECR | Registry | $2 |
| CloudWatch | Logs | $3 |
| **TOTAL** | | **$90.50/mes** |

#### 💡 Tips y Recomendaciones IA

**Cuándo elegir:**
- Si se requiere desacoplamiento total
- Cuando Backoffice Sistemas no migra
- Equipos con experiencia en contenedores

**Consideraciones:**
- Costo alto para aplicación de bajo uso
- Requiere migración de datos a PostgreSQL
- Overhead de infraestructura independiente

**Recomendaciones:**
- Solo si hay requisito de independencia
- Considerar serverless como alternativa más económica
- Evaluar ROI vs consolidación

**Ideal para:**
- Desacoplamiento obligatorio
- Equipos que prefieren contenedores

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
| **Costo/mes** | $2 | $11.50 | $90.50 |
| **Esfuerzo** | Ninguno | Alto | Medio |
| **Timeline** | 0 (incluido) | 4 semanas | 3 semanas |
| **Modernización** | Ninguna | Total | Parcial |
| **Recomendado** | ✅ Sí | Si requiere independencia | No recomendado |

---

## ✅ Recomendación Final

**Consolidar con Backoffice Sistemas** por:
1. Costo casi nulo ($2/mes incremental)
2. Ya comparte infraestructura
3. Uso muy bajo (0.14%)
4. Sin esfuerzo adicional de migración
5. Incluido en wave de Backoffice Sistemas

---

**Última actualización**: 2026-01-06
