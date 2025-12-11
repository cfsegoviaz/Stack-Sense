# Configuración de Diagramas

Para que los diagramas se muestren correctamente en el showcase, necesitas copiar los archivos PNG a la carpeta `public/diagrams/`.

## Estructura requerida:

```
public/
├── logo.png                              # Logo de BGR
└── diagrams/
    ├── app_apiportal.png                 # Diagrama Api Portal
    ├── app_saras.png                     # Diagrama SARAS
    ├── arch_sonarqube.png                # Diagrama SonarQube
    ├── app_backoffice_sistemas.png       # Diagrama Backoffice
    ├── arch_seq_cloudwatch.png           # Diagrama Seq CloudWatch
    └── arch_seq_ec2.png                  # Diagrama Seq EC2
```

## Comandos para copiar desde generated-diagrams:

```bash
# Desde la raíz del proyecto stack-sense-showcase
mkdir -p public/diagrams

# Copia los diagramas existentes (ajusta los nombres según corresponda)
cp ../../../../generated-diagrams/api_portal_architecture public/diagrams/app_apiportal.png
cp ../../../../generated-diagrams/saras_architecture public/diagrams/app_saras.png
cp ../../../../generated-diagrams/sonarqube_architecture public/diagrams/arch_sonarqube.png
cp ../../../../generated-diagrams/portal_guia_architecture public/diagrams/app_backoffice_sistemas.png

# Para Seq, necesitarás generar o copiar los diagramas correspondientes
```

## Nota:
Si algún diagrama no existe aún, puedes:
1. Generarlo usando las herramientas del proyecto
2. Usar un placeholder temporal
3. Comentar la propiedad `diagram` en el código para esa aplicación
