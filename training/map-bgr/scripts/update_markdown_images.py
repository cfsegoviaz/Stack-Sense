#!/usr/bin/env python3
import os
import re

base_path = "/Users/christian/Projects/escala/stack-sense/training/map-bgr"
reports_path = f"{base_path}/reports"
s3_base_url = "https://stack-sense.s3.us-east-1.amazonaws.com/map-bgr/diagrams"

# Image mappings
image_mappings = {
    "../diagrams/bgr_aws_architecture.png": f"{s3_base_url}/bgr_aws_architecture.png",
    "../diagrams/migration_flow.png": f"{s3_base_url}/migration_flow.png",
    "../diagrams/app_portalguiabgr.png": f"{s3_base_url}/app_portalguiabgr.png",
    "../diagrams/app_apiportal.png": f"{s3_base_url}/app_apiportal.png",
    "../diagrams/app_portaladministrativo.png": f"{s3_base_url}/app_portaladministrativo.png",
    "../diagrams/app_backoffice_sistemas.png": f"{s3_base_url}/app_backoffice_sistemas.png",
    "../diagrams/app_backoffice_banca.png": f"{s3_base_url}/app_backoffice_banca.png",
    "../diagrams/app_saras.png": f"{s3_base_url}/app_saras.png",
    "../../diagrams/bgr_aws_architecture.png": f"{s3_base_url}/bgr_aws_architecture.png",
    "../../diagrams/migration_flow.png": f"{s3_base_url}/migration_flow.png",
    "../../diagrams/app_portalguiabgr.png": f"{s3_base_url}/app_portalguiabgr.png",
    "../../diagrams/app_apiportal.png": f"{s3_base_url}/app_apiportal.png",
    "../../diagrams/app_portaladministrativo.png": f"{s3_base_url}/app_portaladministrativo.png",
    "../../diagrams/app_backoffice_sistemas.png": f"{s3_base_url}/app_backoffice_sistemas.png",
    "../../diagrams/app_backoffice_banca.png": f"{s3_base_url}/app_backoffice_banca.png",
    "../../diagrams/app_saras.png": f"{s3_base_url}/app_saras.png",
}

def update_markdown_file(filepath):
    """Update image URLs in a markdown file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        updated = False
        
        # Replace image URLs
        for old_path, new_url in image_mappings.items():
            if old_path in content:
                content = content.replace(old_path, new_url)
                updated = True
                print(f"   ✓ Replaced: {old_path}")
        
        # Save if updated
        if updated:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return False

# Find and update all markdown files
updated_count = 0
for root, dirs, files in os.walk(reports_path):
    for file in files:
        if file.endswith('.md'):
            filepath = os.path.join(root, file)
            rel_path = os.path.relpath(filepath, reports_path)
            print(f"\n📄 {rel_path}")
            if update_markdown_file(filepath):
                updated_count += 1
                print(f"   ✅ Updated")
            else:
                print(f"   ⏭️  No images to update")

print(f"\n✅ Updated {updated_count} markdown files with S3 URLs")
print(f"   Base URL: {s3_base_url}")
