#!/usr/bin/env python3
"""
Generador de diagramas de arquitectura AWS para aplicaciones BGR
"""
from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import EC2, EC2AutoScaling
from diagrams.aws.database import RDS, Aurora
from diagrams.aws.network import ELB, ALB, NLB, Route53, CloudFront, VPC, NATGateway
from diagrams.aws.security import WAF, SecretsManager, IAM
from diagrams.aws.storage import S3, EBS, EFS
from diagrams.aws.management import Cloudwatch, CloudwatchAlarm
from diagrams.aws.integration import SNS
from diagrams.onprem.client import Users, Client
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DIAGRAMS_DIR = BASE_DIR / "diagrams"
DIAGRAMS_DIR.mkdir(exist_ok=True)

def generate_portal_web_diagram(app_name):
    """Diagrama para portales web (PortalAdmBGR, PortalGuiaBGR, Api Portal)"""
    
    filename = f"arch_{app_name.replace(' ', '_').lower()}"
    
    with Diagram(f"Arquitectura AWS - {app_name}", 
                 filename=str(DIAGRAMS_DIR / filename),
                 show=False,
                 direction="TB"):
        
        users = Users("Usuarios")
        
        with Cluster("AWS Cloud"):
            dns = Route53("Route 53")
            cdn = CloudFront("CloudFront CDN")
            waf = WAF("AWS WAF")
            
            with Cluster("VPC"):
                with Cluster("Public Subnet"):
                    alb = ALB("Application\nLoad Balancer")
                
                with Cluster("Private Subnet - App Tier"):
                    asg = EC2AutoScaling("Auto Scaling\nGroup")
                    app_servers = [
                        EC2("App Server 1"),
                        EC2("App Server 2"),
                        EC2("App Server N")
                    ]
                
                with Cluster("Private Subnet - Data Tier"):
                    db = RDS("RDS Multi-AZ\nSQL Server")
                
                nat = NATGateway("NAT Gateway")
            
            s3 = S3("S3\nStatic Assets")
            secrets = SecretsManager("Secrets\nManager")
            cw = Cloudwatch("CloudWatch")
            sns = SNS("SNS Alerts")
        
        # Flujo
        users >> dns >> cdn >> waf >> alb
        alb >> Edge(label="distribute") >> asg
        asg >> app_servers
        app_servers >> db
        app_servers >> s3
        app_servers >> secrets
        app_servers >> nat
        app_servers >> cw >> sns

def generate_backoffice_diagram(app_name):
    """Diagrama para aplicaciones backoffice"""
    
    filename = f"arch_{app_name.replace(' ', '_').lower()}"
    
    with Diagram(f"Arquitectura AWS - {app_name}",
                 filename=str(DIAGRAMS_DIR / filename),
                 show=False,
                 direction="TB"):
        
        users = Client("Usuarios\nInternos")
        
        with Cluster("AWS Cloud"):
            with Cluster("VPC"):
                with Cluster("Private Subnet - LB"):
                    alb = ALB("Internal ALB")
                
                with Cluster("Private Subnet - App Tier"):
                    app1 = EC2("App Server 1")
                    app2 = EC2("App Server 2")
                
                with Cluster("Private Subnet - Data Tier"):
                    db = RDS("RDS Multi-AZ\nSQL Server")
                
                efs = EFS("EFS\nShared Files")
                nat = NATGateway("NAT Gateway")
            
            secrets = SecretsManager("Secrets\nManager")
            cw = Cloudwatch("CloudWatch")
        
        # Flujo
        users >> Edge(label="VPN/DX") >> alb
        alb >> [app1, app2]
        app1 >> db
        app2 >> db
        [app1, app2] >> efs
        [app1, app2] >> secrets
        [app1, app2] >> nat
        [app1, app2] >> cw

def generate_sonarqube_diagram():
    """Diagrama para SonarQube"""
    
    with Diagram("Arquitectura AWS - SonarQube",
                 filename=str(DIAGRAMS_DIR / "arch_sonarqube"),
                 show=False,
                 direction="TB"):
        
        devs = Users("Developers")
        cicd = Client("Jenkins/GitLab")
        
        with Cluster("AWS Cloud"):
            with Cluster("VPC"):
                with Cluster("Public Subnet"):
                    alb = ALB("Application\nLoad Balancer")
                
                with Cluster("Private Subnet - App"):
                    asg = EC2AutoScaling("Auto Scaling")
                    sonar1 = EC2("SonarQube 1\nt3.xlarge")
                    sonar2 = EC2("SonarQube 2\nt3.xlarge")
                
                with Cluster("Private Subnet - Database"):
                    db = RDS("RDS PostgreSQL\nMulti-AZ\ndb.r5.2xlarge")
                
                nat = NATGateway("NAT Gateway")
            
            ebs = EBS("EBS gp3\n500 GB")
            secrets = SecretsManager("Secrets")
            cw = Cloudwatch("CloudWatch")
        
        # Flujo
        devs >> alb
        cicd >> alb
        alb >> asg
        asg >> [sonar1, sonar2]
        [sonar1, sonar2] >> db
        [sonar1, sonar2] >> ebs
        [sonar1, sonar2] >> secrets
        [sonar1, sonar2] >> nat
        [sonar1, sonar2] >> cw

def generate_seq_cloudwatch_diagram():
    """Diagrama para Seq migrado a CloudWatch"""
    
    with Diagram("Arquitectura AWS - Logging (CloudWatch)",
                 filename=str(DIAGRAMS_DIR / "arch_seq_cloudwatch"),
                 show=False,
                 direction="LR"):
        
        with Cluster("Aplicaciones"):
            app1 = EC2("App 1")
            app2 = EC2("App 2")
            app3 = EC2("App 3")
        
        with Cluster("AWS Logging Services"):
            cw_logs = Cloudwatch("CloudWatch\nLogs")
            cw_insights = Cloudwatch("CloudWatch\nInsights")
            
            with Cluster("Long-term Storage"):
                s3 = S3("S3\nArchive")
        
        cw_alarms = CloudwatchAlarm("CloudWatch\nAlarms")
        sns = SNS("SNS\nNotifications")
        
        # Flujo
        [app1, app2, app3] >> Edge(label="logs") >> cw_logs
        cw_logs >> cw_insights
        cw_logs >> Edge(label="archive") >> s3
        cw_logs >> cw_alarms >> sns

def generate_seq_ec2_diagram():
    """Diagrama para Seq en EC2 (opción alternativa)"""
    
    with Diagram("Arquitectura AWS - Seq (EC2)",
                 filename=str(DIAGRAMS_DIR / "arch_seq_ec2"),
                 show=False,
                 direction="LR"):
        
        with Cluster("Aplicaciones"):
            app1 = EC2("App 1")
            app2 = EC2("App 2")
            app3 = EC2("App 3")
        
        with Cluster("AWS Cloud"):
            with Cluster("VPC"):
                with Cluster("Public Subnet"):
                    nlb = NLB("Network\nLoad Balancer")
                
                with Cluster("Private Subnet"):
                    seq1 = EC2("Seq Server 1\nt3.xlarge")
                    seq2 = EC2("Seq Server 2\nt3.xlarge")
                
                ebs = EBS("EBS gp3\n1 TB")
        
        # Flujo
        [app1, app2, app3] >> nlb
        nlb >> [seq1, seq2]
        [seq1, seq2] >> ebs

def generate_saras_diagram():
    """Diagrama para Saras"""
    
    with Diagram("Arquitectura AWS - Saras",
                 filename=str(DIAGRAMS_DIR / "arch_saras"),
                 show=False,
                 direction="TB"):
        
        users = Client("Usuarios")
        
        with Cluster("AWS Cloud"):
            with Cluster("VPC"):
                with Cluster("Private Subnet - App"):
                    app1 = EC2("Saras App 1\nt3.large")
                    app2 = EC2("Saras App 2\nt3.large")
                
                with Cluster("Private Subnet - Database"):
                    db = RDS("RDS SQL Server\nMulti-AZ\ndb.t3.medium")
                
                nat = NATGateway("NAT Gateway")
            
            ebs = EBS("EBS gp3\n100 GB")
            secrets = SecretsManager("Secrets")
            cw = Cloudwatch("CloudWatch")
        
        # Flujo
        users >> Edge(label="VPN") >> [app1, app2]
        [app1, app2] >> db
        [app1, app2] >> ebs
        [app1, app2] >> secrets
        [app1, app2] >> nat
        [app1, app2] >> cw

def generate_primera_ola_diagram():
    """Diagrama general de la primera ola de migración"""
    
    with Diagram("Primera Ola de Migración - Arquitectura General",
                 filename=str(DIAGRAMS_DIR / "primera_ola_general"),
                 show=False,
                 direction="TB",
                 graph_attr={"fontsize": "20"}):
        
        with Cluster("On-Premise"):
            onprem = EC2("12 VMs\n96 vCPUs\n306 GB RAM")
        
        with Cluster("AWS Cloud (us-east-1)"):
            with Cluster("VPC 10.0.0.0/16"):
                
                with Cluster("Ola 0 - Piloto (3 Aplicaciones)"):
                    
                    with Cluster("SonarQube"):
                        sq_alb = ALB("ALB")
                        sq_ec2 = EC2AutoScaling("2x t3.xlarge")
                        sq_rds = RDS("PostgreSQL")
                        sq_alb >> sq_ec2 >> sq_rds
                    
                    with Cluster("Saras"):
                        sr_ec2_1 = EC2("t3.large")
                        sr_ec2_2 = EC2("t3.large")
                        sr_rds = RDS("SQL Server")
                        [sr_ec2_1, sr_ec2_2] >> sr_rds
                    
                    with Cluster("Seq (CloudWatch)"):
                        seq_cw = Cloudwatch("CloudWatch\nLogs")
                        seq_s3 = S3("S3 Archive")
                        seq_cw >> seq_s3
        
        # Migración
        onprem >> Edge(label="AWS MGN", style="dashed") >> sq_ec2
        onprem >> Edge(label="Migration", style="dashed") >> sr_ec2_1

def main():
    print("🎨 Generando diagramas de arquitectura AWS...")
    print("=" * 70)
    
    # Portales Web
    print("\n📱 Generando diagramas de Portales Web...")
    generate_portal_web_diagram("PortalAdmBGR")
    print("   ✅ PortalAdmBGR")
    
    generate_portal_web_diagram("PortalGuiaBGR")
    print("   ✅ PortalGuiaBGR")
    
    generate_portal_web_diagram("Api Portal")
    print("   ✅ Api Portal")
    
    # Backoffice
    print("\n🏢 Generando diagramas de Backoffice...")
    generate_backoffice_diagram("Backoffice Banca Digital")
    print("   ✅ Backoffice Banca Digital")
    
    generate_backoffice_diagram("Backoffice Sistemas")
    print("   ✅ Backoffice Sistemas")
    
    # DevOps
    print("\n🔧 Generando diagrama de SonarQube...")
    generate_sonarqube_diagram()
    print("   ✅ SonarQube")
    
    # Logging
    print("\n📊 Generando diagramas de Logging...")
    generate_seq_cloudwatch_diagram()
    print("   ✅ Seq (CloudWatch)")
    
    generate_seq_ec2_diagram()
    print("   ✅ Seq (EC2 alternativo)")
    
    # Aplicación simple
    print("\n📦 Generando diagrama de Saras...")
    generate_saras_diagram()
    print("   ✅ Saras")
    
    # Diagrama general
    print("\n🎯 Generando diagrama general de Primera Ola...")
    generate_primera_ola_diagram()
    print("   ✅ Primera Ola General")
    
    print("\n" + "=" * 70)
    print(f"✅ Diagramas generados en: {DIAGRAMS_DIR}")
    print(f"📁 Total: 10 diagramas")
    print("=" * 70)

if __name__ == '__main__':
    main()
