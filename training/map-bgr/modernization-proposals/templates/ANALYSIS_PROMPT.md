# Prompt de Análisis de Aplicación

> **Uso:** Copia este prompt y reemplaza `{APP_NAME}` con el nombre de la aplicación a analizar.

---

## Prompt

```
Analiza la aplicación "{APP_NAME}" del portafolio MAP-BGR y genera su propuesta de modernización completa.

## 1. Extracción de Datos

Busca la aplicación en estos archivos:

1. **Matriz de aplicaciones** - `training/map-bgr/applications/raw-data/matriz-aplicaciones-completa.csv`
   - Columna: APLICACION
   - Extraer: DESCRIPCION, FRAMEWORK_APLICACION, MOTOR_BASE, SO, CRITICIDAD_BASE, SERVIDORES_APLICACION, SERVIDORES_BDD, BDD, ESTRATEGIA, CAMBIOS_PROPUESTOS

2. **RVTools vInfo** - `training/map-bgr/assesment/RVTools_export_all_250709_064325_DCP_csv/vInfo.csv`
   - Buscar VMs por IP de SERVIDORES_APLICACION
   - Extraer: VM, CPUs, Memory, Provisioned MB, OS according to the configuration file

3. **Cloudamize Compute** - `training/map-bgr/assesment/Cloudamize/Observed-Infrastructure_csv/Compute.csv`
   - Buscar por nombre de VM o IP
   - Extraer: CPU Usage %, Memory Usage %

## 2. Generar Propuesta de Modernización

Crear archivo: `training/map-bgr/modernization-proposals/{app-slug}/{APP_NAME}_MODERNIZATION.md`

Estructura:
- Resumen Ejecutivo (métricas clave)
- Estado Actual (VMs, specs, uso)
- Tech Stack (framework, BD, dependencias)
- 3 Opciones de Arquitectura con:
  - Componentes AWS y costos (usar MCP aws-pricing)
  - **Horas de implementación SIEMPRE en números** (de pricing/escala24x7_effort_matrix.json)
  - **Timeline SIEMPRE en semanas concretas** (nunca "incluido en X" o asunciones)
  - Ventajas/Desventajas
  - **💡 Tips y Recomendaciones IA** (formato legible, NO JSON):
    ```markdown
    #### 💡 Tips y Recomendaciones IA
    
    **¿Cuándo elegir esta opción?**
    - Punto 1
    - Punto 2
    
    **Consideraciones importantes:**
    - Punto 1
    - Punto 2
    
    **Recomendaciones:**
    - Punto 1
    - Punto 2
    
    **Ideal para:**
    - Punto 1
    - Punto 2
    ```
- Comparativa TCO (12/24 meses)
- Recomendación

### ⚠️ REGLA: Migración SQL Server → PostgreSQL

**OBLIGATORIO** cuando se proponga migrar de SQL Server a PostgreSQL/Aurora:

1. **AWS SCT (Schema Conversion Tool):** Incluir en componentes para conversión de esquema T-SQL → PostgreSQL
2. **Babelfish for Aurora PostgreSQL:** Evaluar si la app puede usar Babelfish para compatibilidad T-SQL nativa
3. **AWS DMS (Database Migration Service):** Incluir para migración de datos con CDC (Change Data Capture)

**En el diagrama incluir:**
- Nodo de AWS SCT
- Nodo de AWS DMS con flecha desde SQL Server on-prem hacia Aurora/RDS PostgreSQL
- Si aplica Babelfish, indicarlo en el nodo de Aurora

**En costos incluir:**
- DMS replication instance: ~$50-150/mes durante migración
- SCT: Sin costo (herramienta gratuita)

**En horas de implementación agregar:**
- DMS replication task: 4 hrs (de effort_matrix)
- SCT schema conversion: 8-16 hrs según complejidad

## 3. Generar Diagramas (OBLIGATORIO - 1 POR ARQUITECTURA)

Crear en: `training/map-bgr/modernization-proposals/{app-slug}/diagrams/`

**REGLA: Generar 1 diagrama PNG por cada opción de arquitectura (mínimo 3)**

Usar MCP generate_diagram para crear PNG de cada opción.

**Nomenclatura:** `{app_slug}_{option_id}.png`
- Ejemplo: `visor_historico_cheques_consolidate.png`
- Ejemplo: `visor_historico_cheques_microservice.png`
- Ejemplo: `visor_historico_cheques_s3archive.png`

**Template de código por tipo de arquitectura:**

### Lift & Shift / Rehost
```python
with Diagram("AppName - Lift Shift", show=False, direction="LR"):
    users = Users("N Usuarios")
    with Cluster("On-Premise"):
        ad = TraditionalServer("Active Directory")
    with Cluster("AWS Cloud"):
        with Cluster("VPC"):
            lb = ELB("ALB")
            ec2 = EC2("EC2 tX.size\nWindows/Linux")
            rds = RDS("RDS SQL Server")
        vpn = VPN("Site-to-Site VPN")
    users >> lb >> ec2 >> rds
    ec2 >> vpn >> ad
```

### Containers / ECS Fargate
```python
with Diagram("AppName - ECS Fargate", show=False, direction="LR"):
    users = Users("N Usuarios")
    with Cluster("AWS Cloud"):
        with Cluster("VPC"):
            lb = ELB("ALB")
            with Cluster("ECS Cluster"):
                ecs = ECS("Fargate\nService")
            rds = RDS("RDS PostgreSQL")
            cache = ElastiCache("Redis")
    users >> lb >> ecs >> rds
    ecs >> cache
```

### Serverless / Lambda
```python
with Diagram("AppName - Serverless", show=False, direction="LR"):
    users = Users("N Usuarios")
    with Cluster("AWS Cloud"):
        apigw = APIGateway("API Gateway")
        lambda_fn = Lambda("Function")
        dynamo = DynamoDB("DynamoDB")  # o RDS
        s3 = S3("S3 Storage")
    users >> apigw >> lambda_fn >> dynamo
    lambda_fn >> s3
```

### Data Lake / Analytics
```python
with Diagram("AppName - Data Lake", show=False, direction="LR"):
    users = Users("N Usuarios")
    with Cluster("AWS Cloud"):
        athena = Athena("Athena")
        glue = Glue("Glue Catalog")
        s3 = S3("S3 Data Lake")
        s3_glacier = S3Glacier("S3 Glacier")
    users >> athena >> glue >> s3 >> s3_glacier
```

**Iconos disponibles:**
- Compute: EC2, ECS, Lambda, EKS
- Network: ELB, ALB, APIGateway, VPN, Route53, CloudFront
- Database: RDS, DynamoDB, ElastiCache, Redshift
- Storage: S3, S3Glacier, EBS, EFS
- Analytics: Athena, Glue, Kinesis
- Security: Cognito, IAM, WAF
- General: Users, TraditionalServer

**Después de generar:**
1. Copiar TODOS a: `apps/stack-sense-showcase/public/diagrams/`
2. Agregar `diagramUrl` en CADA arquitectura del JSON

## 4. Generar JSON para Showcase

Crear: `apps/stack-sense-showcase/public/data/bgr/apps/{app-slug}.json`

Seguir estructura de Application interface en types.ts. 

**Campos obligatorios:**
- `keyFinding`: Hallazgo clave en 1-2 oraciones (se muestra destacado en UI)
- `tips` en cada arquitectura

Incluir tips en cada arquitectura.

## 5. Actualizar Índices

- Actualizar `apps/stack-sense-showcase/public/data/bgr/apps/index.json`
- Actualizar `training/map-bgr/modernization-proposals/INDEX.md`
- Marcar como ✅ en `training/map-bgr/modernization-proposals/ANALYSIS_CHECKLIST.md`

## 6. Copiar Diagramas a Showcase

Copiar diagramas relevantes a: `apps/stack-sense-showcase/public/diagrams/`
```

---

## Ejemplo de Uso

```bash
# En Kiro CLI chat:
Analiza la aplicación "ADMINISTRADOR DE PAGOS" del portafolio MAP-BGR...
```

---

## Aplicaciones Pendientes (Prioridad 1)

| App | Slug | Ponderación |
|-----|------|-------------|
| Visor Histórico de Cheques | visor-historico-cheques | 52 |
| Calculadora Inmobiliaria | calculadora-inmobiliaria | 52 |
| Administrador de Pagos | administrador-pagos | 50 |
| Librarian | librarian | 45 |
| Cuadre y Compensación ATMs | cuadre-compensacion-atms | 45 |
| PortalGuiaBGR | portal-guia-bgr | 43 |
| PortalAdministrativoBGR | portal-administrativo-bgr | 43 |
| BGRTuCuenta | bgr-tu-cuenta | 43 |
| Acciones y Accionistas | acciones-accionistas | 42 |
| Estructuras de Control | estructuras-control | 40 |
