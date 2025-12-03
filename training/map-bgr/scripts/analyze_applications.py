#!/usr/bin/env python3
"""
Análisis de aplicaciones BGR desde archivos HTML
"""
import re
import json
from pathlib import Path
from bs4 import BeautifulSoup
import pandas as pd

BASE_DIR = Path(__file__).parent.parent
REPORTS_DIR = BASE_DIR / "reports"
DOCS_DIR = BASE_DIR / "docs"
DOCS_DIR.mkdir(exist_ok=True)

# Cargar inventario de VMs
vms_df = pd.read_csv(REPORTS_DIR / "01_inventario_vms_produccion.csv")

def extract_app_info(html_file):
    """Extraer información de aplicación desde HTML"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    
    # Extraer texto completo
    text = soup.get_text()
    
    # Buscar patrones comunes
    info = {
        "nombre": html_file.stem.replace("G.I.-", "").replace("G.I-", ""),
        "archivo": html_file.name,
        "servidores": [],
        "tecnologias": [],
        "puertos": [],
        "urls": [],
        "bases_datos": [],
        "descripcion": ""
    }
    
    # Buscar nombres de servidores (patrones comunes BGR)
    server_patterns = [
        r'(ecbr[a-z0-9]+)',
        r'(bgr[a-z0-9]+)',
        r'(srv[a-z0-9]+)',
        r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    ]
    
    for pattern in server_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        info["servidores"].extend(matches)
    
    # Buscar tecnologías
    tech_keywords = ['IIS', 'Apache', 'Tomcat', 'Java', '.NET', 'SQL Server', 
                     'Oracle', 'PostgreSQL', 'MySQL', 'Redis', 'MongoDB',
                     'Angular', 'React', 'Vue', 'Node.js', 'Python', 'PHP']
    
    for tech in tech_keywords:
        if tech.lower() in text.lower():
            info["tecnologias"].append(tech)
    
    # Buscar puertos
    port_matches = re.findall(r':(\d{2,5})', text)
    info["puertos"] = list(set([int(p) for p in port_matches if 80 <= int(p) <= 65535]))
    
    # Buscar URLs
    url_matches = re.findall(r'https?://[^\s<>"]+', text)
    info["urls"] = list(set(url_matches))
    
    # Buscar bases de datos
    db_patterns = [r'(database|db|base de datos)[:\s]+([a-zA-Z0-9_]+)', 
                   r'(schema)[:\s]+([a-zA-Z0-9_]+)']
    for pattern in db_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        info["bases_datos"].extend([m[1] for m in matches])
    
    # Limpiar duplicados
    info["servidores"] = list(set([s.lower() for s in info["servidores"]]))
    info["tecnologias"] = list(set(info["tecnologias"]))
    info["bases_datos"] = list(set(info["bases_datos"]))
    
    return info

def match_vms_to_servers(server_names):
    """Buscar VMs que coincidan con nombres de servidores"""
    matched_vms = []
    
    for server in server_names:
        # Buscar coincidencias parciales en nombres de VMs
        matches = vms_df[vms_df['nombre'].str.lower().str.contains(server.lower(), na=False)]
        
        for _, vm in matches.iterrows():
            matched_vms.append({
                "vm_nombre": vm['nombre'],
                "vcpus": int(vm['vcpus']),
                "memory_gb": float(vm['memory_gb']),
                "os": vm['os'],
                "powerstate": vm['powerstate'],
                "ip": vm.get('ip', ''),
                "match_pattern": server
            })
    
    return matched_vms

def categorize_application(app_info):
    """Categorizar aplicación y definir arquitectura"""
    nombre = app_info['nombre'].lower()
    techs = [t.lower() for t in app_info['tecnologias']]
    
    # Determinar tipo de aplicación
    if 'portal' in nombre or 'web' in nombre:
        tipo = 'Portal Web'
        componentes = ['Load Balancer', 'Web Tier', 'App Tier', 'Database']
    elif 'api' in nombre:
        tipo = 'API/Microservicio'
        componentes = ['API Gateway', 'App Tier', 'Database', 'Cache']
    elif 'backoffice' in nombre:
        tipo = 'Aplicación Backoffice'
        componentes = ['Web Tier', 'App Tier', 'Database', 'File Storage']
    elif 'sonar' in nombre:
        tipo = 'Herramienta DevOps'
        componentes = ['App Server', 'Database']
    else:
        tipo = 'Aplicación Empresarial'
        componentes = ['App Tier', 'Database']
    
    # Determinar stack tecnológico
    if any(t in techs for t in ['java', 'tomcat']):
        stack = 'Java/Tomcat'
    elif any(t in techs for t in ['.net', 'iis']):
        stack = '.NET/IIS'
    elif any(t in techs for t in ['node.js', 'node']):
        stack = 'Node.js'
    elif any(t in techs for t in ['python']):
        stack = 'Python'
    else:
        stack = 'Unknown'
    
    # Determinar base de datos
    if any(t in techs for t in ['sql server']):
        database = 'SQL Server'
    elif any(t in techs for t in ['oracle']):
        database = 'Oracle'
    elif any(t in techs for t in ['postgresql', 'postgres']):
        database = 'PostgreSQL'
    elif any(t in techs for t in ['mysql']):
        database = 'MySQL'
    else:
        database = 'Unknown'
    
    return {
        "tipo": tipo,
        "stack": stack,
        "database": database,
        "componentes": componentes
    }

def recommend_aws_architecture(app_info, categoria):
    """Recomendar arquitectura AWS"""
    
    tipo = categoria['tipo']
    stack = categoria['stack']
    database = categoria['database']
    num_vms = len(app_info['vms_matched'])
    
    arquitectura = {
        "compute": [],
        "database": [],
        "storage": [],
        "networking": [],
        "security": [],
        "monitoring": []
    }
    
    # Compute
    if tipo in ['Portal Web', 'API/Microservicio']:
        arquitectura["compute"] = [
            "Application Load Balancer (ALB)",
            "EC2 Auto Scaling Group (min 2 instancias)",
            "Considerar: ECS Fargate para containerización"
        ]
    else:
        arquitectura["compute"] = [
            "EC2 instances (2+ para HA)",
            "Considerar: ECS si es containerizable"
        ]
    
    # Database
    if database == 'SQL Server':
        arquitectura["database"] = [
            "RDS SQL Server (Multi-AZ para HA)",
            "Automated backups (7-35 días)",
            "Read replicas si es necesario"
        ]
    elif database == 'Oracle':
        arquitectura["database"] = [
            "RDS Oracle (Multi-AZ) o EC2 con Oracle",
            "Evaluar migración a Aurora PostgreSQL"
        ]
    elif database in ['PostgreSQL', 'MySQL']:
        arquitectura["database"] = [
            "Aurora PostgreSQL/MySQL (Multi-AZ)",
            "Serverless v2 para cargas variables"
        ]
    else:
        arquitectura["database"] = [
            "Evaluar tipo de BD en discovery",
            "RDS o Aurora según sea el caso"
        ]
    
    # Storage
    arquitectura["storage"] = [
        "EBS gp3 para discos de aplicación",
        "S3 para archivos estáticos y backups",
        "EFS si requiere file sharing entre instancias"
    ]
    
    # Networking
    arquitectura["networking"] = [
        "VPC con subnets públicas y privadas",
        "NAT Gateway para salida a internet",
        "VPC Endpoints para servicios AWS",
        "Route 53 para DNS"
    ]
    
    # Security
    arquitectura["security"] = [
        "Security Groups (least privilege)",
        "WAF en ALB (si es web pública)",
        "Secrets Manager para credenciales",
        "IAM roles para EC2",
        "KMS para encriptación"
    ]
    
    # Monitoring
    arquitectura["monitoring"] = [
        "CloudWatch Logs y Metrics",
        "CloudWatch Alarms",
        "X-Ray para tracing (APIs)",
        "SNS para notificaciones"
    ]
    
    return arquitectura

def main():
    print("🔍 Analizando aplicaciones BGR...")
    print("=" * 70)
    
    html_files = list(BASE_DIR.glob("G.I*.html"))
    
    if not html_files:
        print("❌ No se encontraron archivos HTML de aplicaciones")
        return
    
    aplicaciones = []
    
    for html_file in sorted(html_files):
        print(f"\n📱 Analizando: {html_file.name}")
        
        # Extraer información
        app_info = extract_app_info(html_file)
        
        # Buscar VMs relacionadas
        vms_matched = match_vms_to_servers(app_info['servidores'])
        app_info['vms_matched'] = vms_matched
        
        # Categorizar aplicación
        categoria = categorize_application(app_info)
        app_info['categoria'] = categoria
        
        # Recomendar arquitectura AWS
        arquitectura_aws = recommend_aws_architecture(app_info, categoria)
        app_info['arquitectura_aws'] = arquitectura_aws
        
        # Calcular recursos totales
        total_vcpus = sum(vm['vcpus'] for vm in vms_matched)
        total_memory = sum(vm['memory_gb'] for vm in vms_matched)
        
        app_info['recursos_totales'] = {
            "vms": len(vms_matched),
            "vcpus": total_vcpus,
            "memory_gb": round(total_memory, 2)
        }
        
        # Determinar criticidad
        if 'banca' in app_info['nombre'].lower() or 'portal' in app_info['nombre'].lower():
            criticidad = 'Alta'
        elif 'backoffice' in app_info['nombre'].lower():
            criticidad = 'Media'
        else:
            criticidad = 'Media'
        
        app_info['criticidad'] = criticidad
        
        aplicaciones.append(app_info)
        
        print(f"   ✅ {len(vms_matched)} VMs identificadas")
        print(f"   📊 Recursos: {total_vcpus} vCPUs, {total_memory:.1f} GB RAM")
        print(f"   🎯 Tipo: {categoria['tipo']}")
        print(f"   ⚠️  Criticidad: {criticidad}")
    
    # Guardar reporte JSON
    output_file = REPORTS_DIR / "02_mapa_aplicaciones.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(aplicaciones, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Reporte generado: {output_file}")
    
    # Generar documentación por aplicación
    for app in aplicaciones:
        doc_file = DOCS_DIR / f"APP_{app['nombre'].replace(' ', '_')}.md"
        generate_app_documentation(app, doc_file)
    
    print(f"✅ Documentación generada en: {DOCS_DIR}")
    
    # Resumen
    print("\n" + "=" * 70)
    print("📊 RESUMEN DE APLICACIONES")
    print("=" * 70)
    
    total_vms = sum(app['recursos_totales']['vms'] for app in aplicaciones)
    total_vcpus = sum(app['recursos_totales']['vcpus'] for app in aplicaciones)
    total_memory = sum(app['recursos_totales']['memory_gb'] for app in aplicaciones)
    
    print(f"\n📱 Total aplicaciones: {len(aplicaciones)}")
    print(f"🖥️  Total VMs identificadas: {total_vms}")
    print(f"💻 Total vCPUs: {total_vcpus}")
    print(f"💾 Total RAM: {total_memory:.1f} GB")
    
    print("\n📋 Por aplicación:")
    for app in sorted(aplicaciones, key=lambda x: x['recursos_totales']['vms'], reverse=True):
        print(f"   {app['nombre']:30} | {app['recursos_totales']['vms']:2} VMs | "
              f"{app['recursos_totales']['vcpus']:3} vCPUs | "
              f"{app['recursos_totales']['memory_gb']:6.1f} GB | "
              f"{app['criticidad']}")
    
    print("\n" + "=" * 70)

def generate_app_documentation(app, output_file):
    """Generar documentación detallada por aplicación"""
    
    doc = f"""# {app['nombre']}

**Criticidad**: {app['criticidad']}  
**Tipo**: {app['categoria']['tipo']}  
**Stack**: {app['categoria']['stack']}  
**Base de Datos**: {app['categoria']['database']}

---

## 📊 Recursos Actuales

| Métrica | Valor |
|---------|-------|
| VMs | {app['recursos_totales']['vms']} |
| vCPUs | {app['recursos_totales']['vcpus']} |
| RAM | {app['recursos_totales']['memory_gb']} GB |

### Servidores Identificados

"""
    
    if app['vms_matched']:
        doc += "| VM | vCPUs | RAM (GB) | OS | Estado |\n"
        doc += "|-------|-------|----------|-----|--------|\n"
        for vm in app['vms_matched']:
            os_str = str(vm['os'])[:30] if vm['os'] else 'Unknown'
            doc += f"| {vm['vm_nombre']} | {vm['vcpus']} | {vm['memory_gb']} | {os_str} | {vm['powerstate']} |\n"
    else:
        doc += "*No se identificaron VMs específicas. Requiere mapeo manual.*\n"
    
    doc += f"""

---

## 🛠️ Stack Tecnológico

**Tecnologías detectadas:**
"""
    
    if app['tecnologias']:
        for tech in app['tecnologias']:
            doc += f"- {tech}\n"
    else:
        doc += "- *No detectadas automáticamente*\n"
    
    if app['puertos']:
        doc += f"\n**Puertos identificados:** {', '.join(map(str, sorted(app['puertos'])))}\n"
    
    doc += f"""

---

## 🏗️ Arquitectura AWS Propuesta

### Componentes Recomendados

**Compute:**
"""
    
    for item in app['arquitectura_aws']['compute']:
        doc += f"- {item}\n"
    
    doc += "\n**Database:**\n"
    for item in app['arquitectura_aws']['database']:
        doc += f"- {item}\n"
    
    doc += "\n**Storage:**\n"
    for item in app['arquitectura_aws']['storage']:
        doc += f"- {item}\n"
    
    doc += "\n**Networking:**\n"
    for item in app['arquitectura_aws']['networking']:
        doc += f"- {item}\n"
    
    doc += "\n**Security:**\n"
    for item in app['arquitectura_aws']['security']:
        doc += f"- {item}\n"
    
    doc += "\n**Monitoring:**\n"
    for item in app['arquitectura_aws']['monitoring']:
        doc += f"- {item}\n"
    
    doc += f"""

---

## 📐 Diagrama de Arquitectura

```
┌─────────────────────────────────────────────────────────────┐
│                         Internet                             │
└────────────────────────┬────────────────────────────────────┘
                         │
                    ┌────▼────┐
                    │   WAF   │ (si es público)
                    └────┬────┘
                         │
                    ┌────▼────┐
                    │   ALB   │ Application Load Balancer
                    └────┬────┘
                         │
        ┌────────────────┼────────────────┐
        │                │                │
   ┌────▼────┐      ┌────▼────┐     ┌────▼────┐
   │  EC2    │      │  EC2    │     │  EC2    │
   │ App 1   │      │ App 2   │     │ App N   │
   └────┬────┘      └────┬────┘     └────┬────┘
        │                │                │
        └────────────────┼────────────────┘
                         │
                    ┌────▼────┐
                    │   RDS   │ Multi-AZ
                    │ {app['categoria']['database']} │
                    └─────────┘
```

---

## 🎯 Estrategia de Migración

### Fase 1: Preparación
- [ ] Documentar dependencias con otras aplicaciones
- [ ] Identificar datos sensibles y requisitos de compliance
- [ ] Definir ventana de mantenimiento
- [ ] Preparar plan de rollback

### Fase 2: Infraestructura AWS
- [ ] Crear VPC y subnets
- [ ] Configurar Security Groups
- [ ] Provisionar RDS (si aplica)
- [ ] Configurar ALB/NLB

### Fase 3: Migración
- [ ] Migrar base de datos (DMS si es necesario)
- [ ] Migrar servidores de aplicación (MGN)
- [ ] Configurar Auto Scaling
- [ ] Pruebas funcionales

### Fase 4: Cutover
- [ ] Actualizar DNS
- [ ] Monitoreo intensivo 24-48h
- [ ] Validación con usuarios
- [ ] Desmantelar on-premise

---

## 📋 Dependencias

**Aplicaciones relacionadas:**
- *Pendiente de identificar*

**Servicios externos:**
- *Pendiente de identificar*

**Integraciones:**
"""
    
    if app['urls']:
        doc += "\n**URLs identificadas:**\n"
        for url in app['urls'][:5]:
            doc += f"- {url}\n"
    
    doc += """

---

## ⚠️ Riesgos y Consideraciones

- **Downtime**: Planificar ventana de mantenimiento
- **Datos**: Validar estrategia de migración de BD
- **Performance**: Realizar pruebas de carga en AWS
- **Costos**: Monitorear durante primeros 30 días

---

## 💰 Estimación de Costos (Preliminar)

*Pendiente de cálculo detallado en Fase 3*

**Componentes principales:**
- Compute (EC2): $XXX/mes
- Database (RDS): $XXX/mes
- Storage (EBS/S3): $XXX/mes
- Networking: $XXX/mes
- **Total estimado**: $XXX/mes

---

**Última actualización**: 2025-12-01  
**Estado**: En análisis
"""
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(doc)

if __name__ == '__main__':
    main()
