#!/usr/bin/env python3
from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.database import ElasticacheForRedis
from diagrams.aws.network import Route53, ElbApplicationLoadBalancer, CloudFront, VpnGateway, VpnConnection
from diagrams.aws.security import WAF, SecretsManager, Shield
from diagrams.aws.storage import S3, ElasticFileSystemEFS
from diagrams.aws.management import Cloudwatch
from diagrams.aws.integration import SimpleNotificationServiceSnsTopic
from diagrams.aws.devtools import Codedeploy, XRay
from diagrams.aws.mobile import APIGateway
from diagrams.onprem.client import User
from diagrams.onprem.vcs import Github
from diagrams.onprem.database import Mssql, Postgresql
from diagrams.onprem.network import Internet

# 1. Saras Architecture
with Diagram("Saras - Arquitectura AWS Híbrida (VPN)", show=False, direction="LR", filename="../diagrams/saras_architecture"):
    users = User("Usuarios Internos")
    azdo = Github("Azure DevOps")
    
    with Cluster("On-Premise Datacenter BGR"):
        db_onprem = Mssql("SQL Server\nOn-Premise")
        customer_gw = Internet("Customer\nGateway")
    
    with Cluster("AWS Cloud"):
        with Cluster("VPC"):
            vpn_gw = VpnGateway("Virtual Private\nGateway")
            vpn_conn = VpnConnection("VPN Site-to-Site\n2 Túneles IPSec")
            
            with Cluster("Public Subnet"):
                alb = ElbApplicationLoadBalancer("ALB")
            
            with Cluster("Auto Scaling Group\nMin:2 Des:2 Max:4"):
                with Cluster("Private Subnet - AZ1"):
                    ec2_1 = EC2("App Server 1\nt3.medium")
                
                with Cluster("Private Subnet - AZ2"):
                    ec2_2 = EC2("App Server 2\nt3.medium")
            
            with Cluster("Storage"):
                s3 = S3("S3\nBackups")
        
        with Cluster("CI/CD"):
            codedeploy = Codedeploy("CodeDeploy")
            s3_artifacts = S3("S3 Artifacts")
        
        with Cluster("Security & Monitoring"):
            secrets = SecretsManager("Secrets Manager")
            cw = Cloudwatch("CloudWatch")
            sns = SimpleNotificationServiceSnsTopic("SNS Alerts")
        
        route53 = Route53("Route 53")
    
    users >> route53 >> alb >> [ec2_1, ec2_2]
    [ec2_1, ec2_2] >> Edge(label="DB Query") >> vpn_gw
    vpn_gw >> vpn_conn >> Edge(label="IPSec\n20-50ms") >> customer_gw >> db_onprem
    [ec2_1, ec2_2] >> s3
    [ec2_1, ec2_2] >> secrets
    [ec2_1, ec2_2] >> cw >> sns
    azdo >> Edge(label="Deploy") >> s3_artifacts >> codedeploy >> [ec2_1, ec2_2]

# 2. SonarQube Architecture
with Diagram("SonarQube - Arquitectura AWS Híbrida (VPN)", show=False, direction="LR", filename="../diagrams/sonarqube_architecture"):
    devs = User("Developers")
    azdo = Github("Azure DevOps")
    
    with Cluster("On-Premise Datacenter BGR"):
        db_onprem = Postgresql("PostgreSQL\nOn-Premise")
        customer_gw = Internet("Customer\nGateway")
    
    with Cluster("AWS Cloud"):
        with Cluster("VPC"):
            vpn_gw = VpnGateway("Virtual Private\nGateway")
            vpn_conn = VpnConnection("VPN Site-to-Site\n2 Túneles IPSec")
            
            with Cluster("Public Subnet"):
                alb = ElbApplicationLoadBalancer("ALB\nSticky Sessions")
            
            with Cluster("Auto Scaling Group\nMin:2 Des:2 Max:4"):
                with Cluster("Private Subnet - AZ1"):
                    ec2_1 = EC2("SonarQube 1\nt3.large")
                
                with Cluster("Private Subnet - AZ2"):
                    ec2_2 = EC2("SonarQube 2\nt3.large")
            
            with Cluster("Storage"):
                s3 = S3("S3\nAnalysis Reports")
                efs = ElasticFileSystemEFS("EFS\nShared Data")
        
        with Cluster("CI/CD"):
            codedeploy = Codedeploy("CodeDeploy")
            s3_artifacts = S3("S3 Artifacts")
        
        with Cluster("Security & Monitoring"):
            secrets = SecretsManager("Secrets Manager")
            cw = Cloudwatch("CloudWatch")
        
        route53 = Route53("Route 53")
    
    devs >> route53 >> alb >> [ec2_1, ec2_2]
    [ec2_1, ec2_2] >> Edge(label="DB Query") >> vpn_gw
    vpn_gw >> vpn_conn >> Edge(label="IPSec\n20-50ms") >> customer_gw >> db_onprem
    [ec2_1, ec2_2] >> efs
    [ec2_1, ec2_2] >> s3
    [ec2_1, ec2_2] >> secrets
    [ec2_1, ec2_2] >> cw
    azdo >> Edge(label="Deploy") >> s3_artifacts >> codedeploy >> [ec2_1, ec2_2]

# 3. API Portal Architecture
with Diagram("API Portal - Arquitectura AWS Híbrida (VPN)", show=False, direction="LR", filename="../diagrams/api_portal_architecture"):
    users = User("External Users")
    azdo = Github("Azure DevOps")
    
    with Cluster("On-Premise Datacenter BGR"):
        db_onprem = Mssql("SQL Server\nOn-Premise")
        customer_gw = Internet("Customer\nGateway")
    
    with Cluster("AWS Cloud"):
        waf = WAF("WAF")
        cf = CloudFront("CloudFront")
        
        with Cluster("VPC"):
            vpn_gw = VpnGateway("Virtual Private\nGateway")
            vpn_conn = VpnConnection("VPN Site-to-Site\n2 Túneles IPSec")
            
            with Cluster("Public Subnet"):
                alb = ElbApplicationLoadBalancer("ALB")
            
            with Cluster("Auto Scaling Group\nMin:2 Des:3 Max:8\nTarget: CPU 50%"):
                with Cluster("Private Subnet - AZ1"):
                    ec2_1 = EC2("API Server 1\nt3.medium")
                    ec2_2 = EC2("API Server 2\nt3.medium")
                
                with Cluster("Private Subnet - AZ2"):
                    ec2_3 = EC2("API Server 3\nt3.medium")
            
            with Cluster("Cache Layer"):
                elasticache = ElasticacheForRedis("ElastiCache\nRedis")
            
            with Cluster("Storage"):
                s3 = S3("S3\nStatic Assets")
        
        with Cluster("CI/CD"):
            codedeploy = Codedeploy("CodeDeploy")
            s3_artifacts = S3("S3 Artifacts")
        
        with Cluster("Security & Monitoring"):
            secrets = SecretsManager("Secrets Manager")
            cw = Cloudwatch("CloudWatch")
            xray = XRay("X-Ray")
        
        apigw = APIGateway("API Gateway")
        route53 = Route53("Route 53")
    
    users >> route53 >> waf >> cf >> apigw >> alb
    alb >> [ec2_1, ec2_2, ec2_3]
    [ec2_1, ec2_2, ec2_3] >> elasticache
    [ec2_1, ec2_2, ec2_3] >> Edge(label="DB Query") >> vpn_gw
    vpn_gw >> vpn_conn >> Edge(label="IPSec\n20-50ms") >> customer_gw >> db_onprem
    [ec2_1, ec2_2, ec2_3] >> s3
    [ec2_1, ec2_2, ec2_3] >> secrets
    [ec2_1, ec2_2, ec2_3] >> xray >> cw
    azdo >> Edge(label="Deploy") >> s3_artifacts >> codedeploy >> [ec2_1, ec2_2, ec2_3]

# 4. Portal Guía BGR Architecture
with Diagram("Portal Guía BGR - Arquitectura AWS Híbrida (VPN)", show=False, direction="LR", filename="../diagrams/portal_guia_architecture"):
    users = User("Clientes BGR")
    azdo = Github("Azure DevOps")
    
    with Cluster("On-Premise Datacenter BGR"):
        db_onprem = Mssql("SQL Server\nOn-Premise")
        customer_gw = Internet("Customer\nGateway")
    
    with Cluster("AWS Cloud"):
        waf = WAF("WAF")
        cf = CloudFront("CloudFront")
        
        with Cluster("VPC"):
            vpn_gw = VpnGateway("Virtual Private\nGateway")
            vpn_conn = VpnConnection("VPN Site-to-Site\n2 Túneles IPSec")
            
            with Cluster("Public Subnet"):
                alb = ElbApplicationLoadBalancer("ALB")
            
            with Cluster("Auto Scaling Group\nMin:2 Des:3 Max:8\nTarget: CPU 50%"):
                with Cluster("Private Subnet - AZ1"):
                    ec2_1 = EC2("Web Server 1\nt3.medium")
                    ec2_2 = EC2("Web Server 2\nt3.medium")
                
                with Cluster("Private Subnet - AZ2"):
                    ec2_3 = EC2("Web Server 3\nt3.medium")
            
            with Cluster("Cache Layer"):
                elasticache = ElasticacheForRedis("ElastiCache\nRedis Multi-AZ")
            
            with Cluster("Storage"):
                s3_static = S3("S3\nStatic Content")
                s3_backup = S3("S3\nBackups")
        
        with Cluster("CI/CD"):
            codedeploy = Codedeploy("CodeDeploy")
            s3_artifacts = S3("S3 Artifacts")
        
        with Cluster("Security & Monitoring"):
            secrets = SecretsManager("Secrets Manager")
            cw = Cloudwatch("CloudWatch")
            shield = Shield("Shield Advanced")
        
        route53 = Route53("Route 53")
    
    users >> route53 >> shield >> waf >> cf >> alb
    alb >> [ec2_1, ec2_2, ec2_3]
    [ec2_1, ec2_2, ec2_3] >> elasticache
    [ec2_1, ec2_2, ec2_3] >> Edge(label="DB Query") >> vpn_gw
    vpn_gw >> vpn_conn >> Edge(label="IPSec\n20-50ms") >> customer_gw >> db_onprem
    cf >> s3_static
    [ec2_1, ec2_2, ec2_3] >> s3_backup
    [ec2_1, ec2_2, ec2_3] >> secrets
    [ec2_1, ec2_2, ec2_3] >> cw
    azdo >> Edge(label="Deploy") >> s3_artifacts >> codedeploy >> [ec2_1, ec2_2, ec2_3]

print("✅ Diagramas híbridos con VPN generados exitosamente en ../diagrams/")
