# BGR Migration Showcase

Dashboard interactivo para visualizar la estrategia de migración a AWS del Banco General Rumiñahui.

## 🎯 Características

- **5 Aplicaciones Analizadas**: Api Portal, SARAS, SonarQube, Backoffice Sistemas, Seq
- **Diagramas de Arquitectura**: Visualización de arquitecturas actuales y objetivo
- **Análisis de Costos**: Comparación de costos on-premise vs AWS
- **Estrategias de Migración**: Refactor, Replatform, Rehost
- **Insights del Arquitecto**: Recomendaciones técnicas y financieras

## 📁 Estructura del Proyecto

```
stack-sense-showcase/
├── src/
│   ├── App.tsx          # Componente principal del dashboard
│   ├── main.tsx         # Entry point
│   └── index.css        # Estilos globales
├── public/
│   └── diagrams/        # Diagramas de arquitectura
│       ├── app_apiportal.png
│       ├── app_saras.png
│       ├── arch_sonarqube.png
│       ├── app_backoffice_sistemas.png
│       ├── arch_seq_cloudwatch.png
│       ├── bgr_aws_architecture.png
│       └── migration_flow.png
└── package.json
```

## 🚀 Desarrollo Local

```bash
# Instalar dependencias
npm install

# Iniciar servidor de desarrollo
npm run dev

# Abrir en el navegador
# http://localhost:5173
```

## 📦 Build para Producción

```bash
npm run build
```

Los archivos estáticos se generarán en la carpeta `dist/` listos para desplegar en cualquier hosting estático (S3, Netlify, Vercel, etc).

## 🌐 Despliegue

### Opción 1: AWS S3 + CloudFront
```bash
# Build
npm run build

# Subir a S3
aws s3 sync dist/ s3://tu-bucket --delete

# Invalidar caché de CloudFront (opcional)
aws cloudfront create-invalidation --distribution-id YOUR_DIST_ID --paths "/*"
```

### Opción 2: Netlify
```bash
# Opción A: Drag & Drop
# Arrastra la carpeta `dist/` a https://app.netlify.com/drop

# Opción B: CLI
npm install -g netlify-cli
netlify deploy --prod --dir=dist
```

### Opción 3: Vercel
```bash
npm install -g vercel
vercel --prod
```

## 🔄 Actualizar Diagramas

Para agregar o actualizar diagramas:

1. Coloca los archivos PNG en `public/diagrams/`
2. Actualiza la propiedad `diagram` en `src/App.tsx`:

```typescript
{
  id: 'nueva-app',
  name: 'Nueva Aplicación',
  // ... otras propiedades
  diagram: '/diagrams/nueva_app.png'
}
```

## 🛠️ Tecnologías

- **React 18** - Framework UI
- **TypeScript** - Type safety
- **Vite** - Build tool
- **Tailwind CSS** - Styling
- **Lucide React** - Iconos

## 📊 Aplicaciones Incluidas

1. **Api Portal** - Refactor a Serverless (99.9% ahorro)
2. **SARAS** - Replatform con ECS + Babelfish (35% ahorro)
3. **SonarQube** - Replatform optimizado (73% ahorro)
4. **Backoffice Sistemas** - Rehost híbrido
5. **Seq** - Refactor a CloudWatch (85% ahorro)

## 📝 Notas

- Los diagramas se copian automáticamente desde `../../diagrams/`
- El proyecto es completamente estático, no requiere backend
- Optimizado para despliegue en CDN
