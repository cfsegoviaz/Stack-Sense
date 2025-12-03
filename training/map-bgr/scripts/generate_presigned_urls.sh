#!/bin/bash

PROFILE="176861563173_AdministratorAccess"
BUCKET="stack-sense"
PREFIX="map-bgr/diagrams"
EXPIRATION=604800  # 7 days in seconds

echo "Generating presigned URLs for diagrams..."
echo ""

# Array of image files
images=(
    "bgr_aws_architecture.png"
    "migration_flow.png"
    "app_portalguiabgr.png"
    "app_apiportal.png"
    "app_portaladministrativo.png"
    "app_backoffice_sistemas.png"
    "app_backoffice_banca.png"
    "app_saras.png"
)

# Generate presigned URLs
for img in "${images[@]}"; do
    url=$(aws s3 presign "s3://${BUCKET}/${PREFIX}/${img}" \
        --expires-in ${EXPIRATION} \
        --profile ${PROFILE} \
        --region us-east-1)
    echo "${img}: ${url}"
done

echo ""
echo "✅ Presigned URLs generated (valid for 7 days)"
