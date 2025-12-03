#!/usr/bin/env python3
"""
Genera diagramas de arquitectura para EBA (Early Business Adoption)
"""
from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import EC2, AutoScaling
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB, VPC, InternetGateway, NATGateway
from diagrams.aws.security import SecretsManager, IAM
from diagrams.aws.management import Cloudwatch, SystemsManager
from diagrams.aws.storage import S3
from diagrams.onprem.client import Users, Client

# Configuración
output_dir = "training/map-bgr/diagrams"
graph_attr = {
    "fontsize": "14",
    "bgcolor": "white",
    "pad": "0.5"
}

# 1. Arquitectura General EBA
with Diagram("EBA - Arquitectura General BGR", 
             filename=f"{output_dir}/eba_general_architecture",
             show=False,
             direction="LR",
             graph_attr=graph_attr):
    
    users = Users("Usuarios")
    
    with Cluster("AWS Cloud - EBA Environment"):
        with Cluster("VPC 10.0.0.0/16"):
            igw = InternetGateway("Internet Gateway")
            
            with Cluster("Public Subnets"):
                alb_public = ELB("ALB Público")
                alb_internal = ELB("ALB Interno")
                nat = NATGateway("NAT Gateway")
            
            with Cluster("Private Subnets - Apps No Críticas"):
                with Cluster("Seq (Logging)"):
                    seq_ec2 = [EC2("Seq-1"), EC2("Seq-2")]
                
                with Cluster("SonarQube"):
                    sonar_ec2 = [EC2("Sonar-1"), EC2("Sonar-2")]
                
                with Cluster("Saras"):
                    saras_ec2 = [EC2("Saras-1"), EC2("Saras-2")]
                
                with Cluster("Backoffice Sistemas"):
                    bo_sys_ec2 = [EC2("BO-Sys-1"), EC2("BO-Sys-2")]
            
            with Cluster("Private Subnets - Apps Críticas"):
                with Cluster("Portal Guía BGR"):
                    portal_guia_ec2 = [EC2("Web-1"), EC2("Web-2")]
                    portal_guia_rds = RDS("SQL Server")
                
                with Cluster("Portal Adm BGR"):
                    portal_adm_ec2 = [EC2("Web-1"), EC2("Web-2")]
                    portal_adm_rds = RDS("SQL Server")
                
                with Cluster("Backoffice Banca"):
                    bo_banca_ec2 = [EC2("Web-1"), EC2("Web-2"), EC2("App-1")]
                    bo_banca_rds = RDS("SQL Server\nMulti-AZ")
                
                with Cluster("Api Portal"):
                    api_ec2 = [EC2("API-1"), EC2("API-2"), EC2("API-3")]
                    api_rds = RDS("SQL Server\nMulti-AZ")
            
            with Cluster("Shared Services"):
                cw = Cloudwatch("CloudWatch")
                sm = SecretsManager("Secrets Manager")
                ssm = SystemsManager("Systems Manager")
                s3 = S3("S3 Backups")
    
    users >> igw >> alb_public
    users >> igw >> alb_internal
    
    alb_public >> seq_ec2
    alb_public >> sonar_ec2
    alb_internal >> saras_ec2
    alb_internal >> bo_sys_ec2
    
    alb_public >> portal_guia_ec2 >> portal_guia_rds
    alb_internal >> portal_adm_ec2 >> portal_adm_rds
    alb_internal >> bo_banca_ec2 >> bo_banca_rds
    alb_public >> api_ec2 >> api_rds
    
    for ec2_group in [seq_ec2, sonar_ec2, saras_ec2, bo_sys_ec2, portal_guia_ec2, 
                      portal_adm_ec2, bo_banca_ec2, api_ec2]:
        for ec2 in ec2_group:
            ec2 >> cw
    
    portal_guia_rds >> sm
    portal_adm_rds >> sm
    bo_banca_rds >> sm
    api_rds >> sm


# 2. Arquitectura de Red EBA
with Diagram("EBA - Arquitectura de Red",
             filename=f"{output_dir}/eba_network_architecture",
             show=False,
             direction="TB",
             graph_attr=graph_attr):
    
    internet = Client("Internet")
    
    with Cluster("AWS Region: us-east-1"):
        with Cluster("VPC 10.0.0.0/16"):
            igw = InternetGateway("IGW")
            
            with Cluster("Availability Zone A"):
                with Cluster("Public Subnet 10.0.1.0/24"):
                    alb_a = ELB("ALB")
                    nat_a = NATGateway("NAT-A")
                
                with Cluster("Private Subnet 10.0.10.0/24"):
                    ec2_a = [EC2("App-1"), EC2("App-2")]
                
                with Cluster("Data Subnet 10.0.20.0/24"):
                    rds_a = RDS("RDS Primary")
            
            with Cluster("Availability Zone B"):
                with Cluster("Public Subnet 10.0.2.0/24"):
                    alb_b = ELB("ALB")
                
                with Cluster("Private Subnet 10.0.11.0/24"):
                    ec2_b = [EC2("App-3"), EC2("App-4")]
                
                with Cluster("Data Subnet 10.0.21.0/24"):
                    rds_b = RDS("RDS Standby")
    
    internet >> igw >> [alb_a, alb_b]
    alb_a >> ec2_a
    alb_b >> ec2_b
    ec2_a >> rds_a
    ec2_b >> rds_a
    rds_a - Edge(style="dashed") - rds_b


# 3. Arquitectura App Crítica (Ejemplo: Api Portal)
with Diagram("EBA - Api Portal (Aplicación Crítica)",
             filename=f"{output_dir}/eba_api_portal_detailed",
             show=False,
             direction="LR",
             graph_attr=graph_attr):
    
    apps = Client("Apps/Services")
    
    with Cluster("AWS Cloud"):
        with Cluster("VPC"):
            alb = ELB("Application\nLoad Balancer")
            
            with Cluster("Auto Scaling Group"):
                api_servers = [
                    EC2("API-1\nt3.large"),
                    EC2("API-2\nt3.large"),
                    EC2("API-3\nt3.large")
                ]
                asg = AutoScaling("Auto Scaling")
            
            with Cluster("Services Layer"):
                services = [
                    EC2("Service-1\nt3.large"),
                    EC2("Service-2\nt3.large")
                ]
            
            with Cluster("Database Layer"):
                rds = RDS("SQL Server\ndb.t3.large\nMulti-AZ")
            
            with Cluster("Management"):
                cw = Cloudwatch("CloudWatch\nMetrics & Logs")
                sm = SecretsManager("Secrets\nManager")
                s3 = S3("S3\nBackups")
    
    apps >> alb >> api_servers[0] >> services[0] >> rds
    
    for api in api_servers:
        api >> cw
    for svc in services:
        svc >> cw
    rds >> cw
    
    for api in api_servers:
        api >> sm
    for svc in services:
        svc >> sm
    rds >> s3


# 4. Arquitectura App No Crítica (Ejemplo: SonarQube)
with Diagram("EBA - SonarQube (Aplicación No Crítica)",
             filename=f"{output_dir}/eba_sonarqube_detailed",
             show=False,
             direction="LR",
             graph_attr=graph_attr):
    
    devs = Users("Developers")
    
    with Cluster("AWS Cloud"):
        with Cluster("VPC"):
            alb = ELB("Application\nLoad Balancer")
            
            with Cluster("Application Layer"):
                sonar = [
                    EC2("SonarQube-1\nt3.medium"),
                    EC2("SonarQube-2\nt3.medium")
                ]
            
            with Cluster("Database Layer"):
                db = EC2("PostgreSQL\nt3.medium")
            
            with Cluster("Management"):
                cw = Cloudwatch("CloudWatch")
                ssm = SystemsManager("Systems\nManager")
    
    devs >> alb >> sonar[0] >> db
    for s in sonar:
        s >> cw
    db >> cw
    for s in sonar:
        s >> ssm
    db >> ssm


# 5. Flujo de Migración EBA
with Diagram("EBA - Flujo de Migración",
             filename=f"{output_dir}/eba_migration_flow",
             show=False,
             direction="TB",
             graph_attr=graph_attr):
    
    with Cluster("On-Premise"):
        vm_source = EC2("VM Source")
    
    with Cluster("AWS Migration"):
        mgn = EC2("Application\nMigration Service")
        
        with Cluster("Target AWS"):
            with Cluster("Fase 1: Apps No Críticas (Sem 3-4)"):
                app1 = EC2("Seq")
                app2 = EC2("SonarQube")
                app3 = EC2("Saras")
                app4 = EC2("BO Sistemas")
            
            with Cluster("Fase 2: Apps Críticas (Sem 5-8)"):
                app5 = EC2("Portal Guía")
                app6 = EC2("Portal Adm")
                app7 = EC2("BO Banca")
                app8 = EC2("Api Portal")
            
            cw = Cloudwatch("Monitoring")
    
    vm_source >> mgn
    mgn >> Edge(label="Semana 3-4") >> app1
    mgn >> Edge(label="Semana 3-4") >> app2
    mgn >> Edge(label="Semana 3-4") >> app3
    mgn >> Edge(label="Semana 3-4") >> app4
    mgn >> Edge(label="Semana 5-8") >> app5
    mgn >> Edge(label="Semana 5-8") >> app6
    mgn >> Edge(label="Semana 5-8") >> app7
    mgn >> Edge(label="Semana 5-8") >> app8
    
    for app in [app1, app2, app3, app4, app5, app6, app7, app8]:
        app >> cw


print("✅ Diagramas EBA generados exitosamente!")
print(f"📁 Ubicación: {output_dir}/")
print("\nDiagramas creados:")
print("  1. eba_general_architecture.png - Arquitectura general")
print("  2. eba_network_architecture.png - Arquitectura de red")
print("  3. eba_api_portal_detailed.png - App crítica detallada")
print("  4. eba_sonarqube_detailed.png - App no crítica detallada")
print("  5. eba_migration_flow.png - Flujo de migración")
