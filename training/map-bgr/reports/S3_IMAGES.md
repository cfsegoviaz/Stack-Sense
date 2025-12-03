# BGR Diagrams - S3 Storage

**Bucket:** stack-sense  
**Prefix:** map-bgr/diagrams/  
**Region:** us-east-1  
**Total Images:** 18 images (3.4 MB)  
**Access:** ✅ Public Read (HTTPS)

---

## 🌐 Public URLs (Direct Access)

**Base URL:** `https://stack-sense.s3.us-east-1.amazonaws.com/map-bgr/diagrams/`

### Main Diagrams
- **BGR AWS Architecture:** https://stack-sense.s3.us-east-1.amazonaws.com/map-bgr/diagrams/bgr_aws_architecture.png
- **Migration Flow:** https://stack-sense.s3.us-east-1.amazonaws.com/map-bgr/diagrams/migration_flow.png

### Individual Application Architectures
- **PortalGuiaBGR:** https://stack-sense.s3.us-east-1.amazonaws.com/map-bgr/diagrams/app_portalguiabgr.png
- **Api Portal:** https://stack-sense.s3.us-east-1.amazonaws.com/map-bgr/diagrams/app_apiportal.png
- **PortalAdministrativoBGR:** https://stack-sense.s3.us-east-1.amazonaws.com/map-bgr/diagrams/app_portaladministrativo.png
- **Backoffice Sistemas:** https://stack-sense.s3.us-east-1.amazonaws.com/map-bgr/diagrams/app_backoffice_sistemas.png
- **Backoffice Banca Digital:** https://stack-sense.s3.us-east-1.amazonaws.com/map-bgr/diagrams/app_backoffice_banca.png
- **Saras:** https://stack-sense.s3.us-east-1.amazonaws.com/map-bgr/diagrams/app_saras.png

---

## ✅ Access Status

**Public Access:** Enabled  
**Block Public Access:** Disabled  
**Bucket Policy:** Applied  
**Status:** ✅ All images publicly accessible via HTTPS

**Test URL:**
```bash
curl -I https://stack-sense.s3.us-east-1.amazonaws.com/map-bgr/diagrams/bgr_aws_architecture.png
# Returns: HTTP/1.1 200 OK
```

---

## 📝 Markdown Files Updated

The following markdown files have been updated with public S3 URLs:

✅ `reports/README.md`  
✅ `reports/01_executive_summary/bgr_migration_summary.md`  
✅ `reports/05_architectures/bgr_individual_architectures.md`  
✅ `reports/05_architectures/ARCHITECTURE_CATALOG.md`

**All images now display correctly in markdown viewers!**

---

## 📤 S3 Upload Summary

| Category | Files | Size |
|----------|-------|------|
| Main Diagrams | 2 | 642 KB |
| Individual Apps | 6 | 1.3 MB |
| Legacy Diagrams | 10 | 1.5 MB |
| **Total** | **18** | **3.4 MB** |

---

## 🔧 AWS CLI Commands

### List all images
```bash
aws s3 ls s3://stack-sense/map-bgr/diagrams/ \
  --profile 176861563173_AdministratorAccess \
  --region us-east-1
```

### Upload new image
```bash
aws s3 cp new_diagram.png s3://stack-sense/map-bgr/diagrams/ \
  --profile 176861563173_AdministratorAccess \
  --region us-east-1
```

### Download an image
```bash
aws s3 cp s3://stack-sense/map-bgr/diagrams/bgr_aws_architecture.png . \
  --profile 176861563173_AdministratorAccess \
  --region us-east-1
```

### Sync entire directory
```bash
aws s3 sync ../diagrams/ s3://stack-sense/map-bgr/diagrams/ \
  --exclude "*" \
  --include "*.png" \
  --profile 176861563173_AdministratorAccess \
  --region us-east-1
```

---

## 📊 Storage Costs

**Total Size:** 3.4 MB  
**S3 Standard Storage:** ~$0.08/month  
**Data Transfer Out:** First 100 GB free/month  
**Requests:** Minimal cost

**Estimated Monthly Cost:** < $0.10

---

## 🔒 Bucket Policy Applied

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::stack-sense/map-bgr/diagrams/*"
    }
  ]
}
```

**Scope:** Only `map-bgr/diagrams/*` is public  
**Security:** Rest of bucket remains private

---

## ✅ Verification

**Test public access:**
```bash
# Should return HTTP 200 OK
curl -I https://stack-sense.s3.us-east-1.amazonaws.com/map-bgr/diagrams/bgr_aws_architecture.png
```

**View in browser:**
Open any URL directly in browser - image should display without authentication.

---

## 📋 Image Inventory

### Main Architecture Diagrams
1. `bgr_aws_architecture.png` - Complete AWS infrastructure (321 KB)
2. `migration_flow.png` - On-premise to AWS migration flow (321 KB)

### Individual Application Architectures
3. `app_portalguiabgr.png` - PortalGuiaBGR architecture (228 KB)
4. `app_apiportal.png` - Api Portal architecture (269 KB)
5. `app_portaladministrativo.png` - PortalAdministrativoBGR (186 KB)
6. `app_backoffice_sistemas.png` - Backoffice Sistemas (223 KB)
7. `app_backoffice_banca.png` - Backoffice Banca Digital (193 KB)
8. `app_saras.png` - Saras architecture (175 KB)

### Legacy Diagrams (Primera Ola)
9. `primera_ola_general.png` - First wave overview (131 KB)
10. `arch_portalguiabgr.png` - Legacy Portal Guia (231 KB)
11. `arch_portaladmbgr.png` - Legacy Portal Adm (232 KB)
12. `arch_api_portal.png` - Legacy API Portal (230 KB)
13. `arch_backoffice_sistemas.png` - Legacy Backoffice (121 KB)
14. `arch_backoffice_banca_digital.png` - Legacy Banca (121 KB)
15. `arch_saras.png` - Legacy Saras (112 KB)
16. `arch_seq_cloudwatch.png` - Seq CloudWatch option (97 KB)
17. `arch_seq_ec2.png` - Seq EC2 option (99 KB)
18. `arch_sonarqube.png` - SonarQube architecture (159 KB)

---

## 🎯 Next Steps

1. ✅ Images uploaded to S3
2. ✅ Public access enabled
3. ✅ Markdown files updated
4. ✅ URLs verified working
5. ⏭️ Share documentation with team
6. ⏭️ Consider CloudFront for CDN (optional)

---

**Last Updated:** 2025-12-01  
**Status:** ✅ Fully Operational  
**Profile Used:** 176861563173_AdministratorAccess  
**Region:** us-east-1
