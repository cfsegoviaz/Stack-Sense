# Guía de Despliegue - BGR Migration Showcase

## ⚠️ IMPORTANTE: Cómo Servir la Aplicación

Las imágenes y assets **SÍ están incluidos** en el build (`dist/diagrams/`), pero **NO puedes abrir `dist/index.html` directamente en el navegador** (protocolo `file://`). Necesitas un servidor HTTP.

## Opciones para Servir la Aplicación

### Opción 1: Usar Vite Preview (Recomendado para Testing Local)

```bash
npm run preview
```

Esto iniciará un servidor en `http://localhost:4173` con el build de producción.

### Opción 2: Usar Python HTTP Server

```bash
cd dist
python3 -m http.server 8000
```

Abre `http://localhost:8000` en tu navegador.

### Opción 3: Usar Node.js http-server

```bash
npx http-server dist -p 8000
```

Abre `http://localhost:8000` en tu navegador.

### Opción 4: Usar PHP Built-in Server

```bash
cd dist
php -S localhost:8000
```

Abre `http://localhost:8000` en tu navegador.

## Verificar que las Imágenes Están en el Build

```bash
ls -la dist/diagrams/
```

Deberías ver:
- `app_apiportal.png`
- `app_backoffice_sistemas.png`
- `app_saras.png`
- `arch_seq_cloudwatch.png`
- `arch_seq_ec2.png`
- `arch_sonarqube.png`
- `bgr_aws_architecture.png`
- `migration_flow.png`
- `logo.png` (en dist/)

## Despliegue en Producción

### AWS S3 + CloudFront

```bash
# 1. Build
npm run build

# 2. Subir a S3
aws s3 sync dist/ s3://tu-bucket-name/ --delete

# 3. Invalidar CloudFront cache
aws cloudfront create-invalidation --distribution-id TU_DISTRIBUTION_ID --paths "/*"
```

### Netlify

```bash
# Instalar Netlify CLI
npm install -g netlify-cli

# Deploy
netlify deploy --prod --dir=dist
```

### Vercel

```bash
# Instalar Vercel CLI
npm install -g vercel

# Deploy
vercel --prod
```

## Troubleshooting

### Las imágenes no se ven

1. **Verifica que estás usando un servidor HTTP**, no abriendo el archivo directamente
2. Verifica que las imágenes están en `dist/diagrams/`:
   ```bash
   ls -la dist/diagrams/
   ```
3. Abre la consola del navegador (F12) y busca errores 404
4. Verifica que el build se completó correctamente:
   ```bash
   npm run build
   ```

### Error de CORS

Si ves errores de CORS, asegúrate de estar usando un servidor HTTP local, no el protocolo `file://`.

## Configuración de Vite

El proyecto usa `base: './'` en `vite.config.ts` para que funcione con rutas relativas. Esto permite que la aplicación funcione en cualquier subdirectorio sin necesidad de configuración adicional.
