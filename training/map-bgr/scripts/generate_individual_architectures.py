#!/usr/bin/env python3
from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import Fargate
from diagrams.aws.network import ALB, Route53
from diagrams.aws.database import RDS
from diagrams.aws.security import SecretsManager, CertificateManager, IAM, Cognito
from diagrams.aws.management import Cloudwatch, SystemsManager
from diagrams.aws.integration import SNS
from diagrams.aws.general import Users

base_path = "/Users/christian/Projects/escala/stack-sense/training/map-bgr/diagrams"
graph_attr = {"fontsize": "13", "bgcolor": "white", "pad": "0.5"}

# 1. PortalGuiaBGR
with Diagram("PortalGuiaBGR - Target Architecture", 
             filename=f"{base_path}/app_portalguiabgr",
             direction="LR", graph_attr=graph_attr, show=False):
    
    users = Users("Bank Employees")
    
    with Cluster("AWS Cloud - us-east-1"):
        dns = Route53("Route 53\nguiabgr.bgr.com")
        
        with Cluster("VPC - Multi-AZ"):
            with Cluster("Public Subnet"):
                alb = ALB("Application LB\nHTTPS:443")
                acm = CertificateManager("ACM\nSSL Certificate")
            
            with Cluster("Private Subnet - Compute"):
                with Cluster("ECS Fargate Cluster"):
                    app1 = Fargate("Task 1\n2 vCPU, 4GB")
                    app2 = Fargate("Task 2\n2 vCPU, 4GB")
                    app3 = Fargate("Task 3\n2 vCPU, 4GB")
            
            with Cluster("Private Subnet - Data"):
                db = RDS("RDS SQL Server\ndb.m5.large\nMulti-AZ")
            
            with Cluster("Shared Services"):
                ad = IAM("Managed AD\nAuthentication")
                secrets = SecretsManager("Secrets")
                ssm = SystemsManager("Parameter Store")
                cw = Cloudwatch("CloudWatch")
                sns = SNS("SNS")
    
    users >> dns >> alb >> acm
    alb >> app1
    alb >> app2
    alb >> app3
    app1 >> db
    app2 >> db
    app3 >> db
    app1 >> ad >> secrets >> ssm >> cw >> sns

# 2. Api Portal
with Diagram("Api Portal - Target Architecture", 
             filename=f"{base_path}/app_apiportal",
             direction="LR", graph_attr=graph_attr, show=False):
    
    clients = Users("API Clients")
    
    with Cluster("AWS Cloud - us-east-1"):
        dns = Route53("Route 53\napi.bgr.com")
        
        with Cluster("VPC - Multi-AZ"):
            with Cluster("Public Subnet"):
                alb = ALB("Application LB\nHTTPS:443\nRate Limiting")
                acm = CertificateManager("ACM")
            
            with Cluster("Private Subnet - Compute"):
                with Cluster("ECS Fargate - Auto-scale 3-10"):
                    app1 = Fargate("Task 1\n2 vCPU, 4GB")
                    app2 = Fargate("Task 2\n2 vCPU, 4GB")
                    app3 = Fargate("Task 3\n2 vCPU, 4GB")
                    app4 = Fargate("Task 4\n2 vCPU, 4GB")
                    app5 = Fargate("Task 5\n2 vCPU, 4GB")
            
            with Cluster("Private Subnet - Data"):
                db = RDS("RDS SQL Server\ndb.m5.large\nMulti-AZ")
            
            with Cluster("Shared Services"):
                ad = IAM("Managed AD")
                secrets = SecretsManager("Secrets")
                ssm = SystemsManager("Parameter Store")
                cw = Cloudwatch("CloudWatch\nAPI Metrics")
                sns = SNS("SNS Alerts")
    
    clients >> dns >> alb >> acm
    alb >> app1
    alb >> app2
    alb >> app3
    alb >> app4
    alb >> app5
    app1 >> db
    app2 >> db
    app3 >> db
    app1 >> ad >> secrets >> ssm >> cw >> sns

# 3. PortalAdministrativoBGR
with Diagram("PortalAdministrativoBGR - Target Architecture", 
             filename=f"{base_path}/app_portaladministrativo",
             direction="LR", graph_attr=graph_attr, show=False):
    
    admins = Users("IT Admins")
    
    with Cluster("AWS Cloud - us-east-1"):
        dns = Route53("Route 53\nadmin.bgr.com")
        
        with Cluster("VPC - Multi-AZ"):
            with Cluster("Public Subnet"):
                alb = ALB("Application LB\nHTTPS:443")
                acm = CertificateManager("ACM")
            
            with Cluster("Private Subnet - Compute"):
                with Cluster("ECS Fargate Cluster"):
                    app1 = Fargate("Task 1\n1 vCPU, 2GB")
                    app2 = Fargate("Task 2\n1 vCPU, 2GB")
            
            with Cluster("Private Subnet - Data"):
                db = RDS("RDS SQL Server\ndb.m5.large\nMulti-AZ")
            
            with Cluster("Shared Services"):
                ad = IAM("Managed AD")
                secrets = SecretsManager("Secrets")
                ssm = SystemsManager("Parameter Store")
                cw = Cloudwatch("CloudWatch")
    
    admins >> dns >> alb >> acm
    alb >> app1
    alb >> app2
    app1 >> db
    app2 >> db
    app1 >> ad >> secrets >> ssm >> cw

# 4. Backoffice Sistemas BGR
with Diagram("Backoffice Sistemas BGR - Target Architecture", 
             filename=f"{base_path}/app_backoffice_sistemas",
             direction="LR", graph_attr=graph_attr, show=False):
    
    users = Users("Bank Staff")
    
    with Cluster("AWS Cloud - us-east-1"):
        dns = Route53("Route 53\nbackoffice.bgr.com")
        
        with Cluster("VPC - Multi-AZ"):
            with Cluster("Public Subnet"):
                alb = ALB("Application LB\nHTTPS:443")
                acm = CertificateManager("ACM")
            
            with Cluster("Private Subnet - Compute"):
                with Cluster("ECS Fargate Cluster"):
                    app1 = Fargate("Task 1\n2 vCPU, 4GB")
                    app2 = Fargate("Task 2\n2 vCPU, 4GB")
                    app3 = Fargate("Task 3\n2 vCPU, 4GB")
            
            with Cluster("Private Subnet - Data"):
                db = RDS("RDS SQL Server\ndb.m5.large\nMulti-AZ")
            
            with Cluster("Shared Services"):
                ad = IAM("Managed AD")
                secrets = SecretsManager("Secrets")
                ssm = SystemsManager("Parameter Store")
                cw = Cloudwatch("CloudWatch")
                sns = SNS("SNS")
    
    users >> dns >> alb >> acm
    alb >> app1
    alb >> app2
    alb >> app3
    app1 >> db
    app2 >> db
    app3 >> db
    app1 >> ad >> secrets >> ssm >> cw >> sns

# 5. Backoffice Banca Digital
with Diagram("Backoffice Banca Digital - Target Architecture", 
             filename=f"{base_path}/app_backoffice_banca",
             direction="LR", graph_attr=graph_attr, show=False):
    
    users = Users("Digital Banking Team")
    
    with Cluster("AWS Cloud - us-east-1"):
        dns = Route53("Route 53\nbanca.bgr.com")
        
        with Cluster("VPC - Multi-AZ"):
            with Cluster("Public Subnet"):
                alb = ALB("Application LB\nHTTPS:443")
                acm = CertificateManager("ACM")
            
            with Cluster("Private Subnet - Compute"):
                with Cluster("ECS Fargate Cluster"):
                    app1 = Fargate("Task 1\n.NET 8\n2 vCPU, 4GB")
                    app2 = Fargate("Task 2\n.NET 8\n2 vCPU, 4GB")
                    app3 = Fargate("Task 3\n.NET 8\n2 vCPU, 4GB")
            
            with Cluster("Private Subnet - Data"):
                db = RDS("RDS SQL Server 2019\ndb.m5.large\nMulti-AZ")
            
            with Cluster("Shared Services"):
                cognito = Cognito("Cognito\nUser Pool")
                secrets = SecretsManager("Secrets")
                ssm = SystemsManager("Parameter Store")
                cw = Cloudwatch("CloudWatch")
    
    users >> dns >> alb >> acm
    alb >> app1
    alb >> app2
    alb >> app3
    app1 >> db
    app2 >> db
    app3 >> db
    app1 >> cognito >> secrets >> ssm >> cw

# 6. Saras
with Diagram("Saras - Target Architecture", 
             filename=f"{base_path}/app_saras",
             direction="LR", graph_attr=graph_attr, show=False):
    
    users = Users("Risk Analysts")
    
    with Cluster("AWS Cloud - us-east-1"):
        dns = Route53("Route 53\nsaras.bgr.com")
        
        with Cluster("VPC - Multi-AZ"):
            with Cluster("Public Subnet"):
                alb = ALB("Application LB\nHTTPS:443")
                acm = CertificateManager("ACM")
            
            with Cluster("Private Subnet - Compute"):
                with Cluster("ECS Fargate Cluster"):
                    app1 = Fargate("Task 1\n.NET 8\n2 vCPU, 4GB")
                    app2 = Fargate("Task 2\n.NET 8\n2 vCPU, 4GB")
            
            with Cluster("Private Subnet - Data"):
                db = RDS("RDS SQL Server 2019\ndb.m5.large\nMulti-AZ\nShared")
            
            with Cluster("Shared Services"):
                cognito = Cognito("Cognito\nUser Pool")
                secrets = SecretsManager("Secrets")
                ssm = SystemsManager("Parameter Store")
                cw = Cloudwatch("CloudWatch")
    
    users >> dns >> alb >> acm
    alb >> app1
    alb >> app2
    app1 >> db
    app2 >> db
    app1 >> cognito >> secrets >> ssm >> cw

print("✅ Generated 6 individual application architecture diagrams")
print(f"   Location: {base_path}/")
print("   - app_portalguiabgr.png")
print("   - app_apiportal.png")
print("   - app_portaladministrativo.png")
print("   - app_backoffice_sistemas.png")
print("   - app_backoffice_banca.png")
print("   - app_saras.png")
