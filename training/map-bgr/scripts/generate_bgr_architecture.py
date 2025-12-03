#!/usr/bin/env python3
from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import ECS, Fargate
from diagrams.aws.network import ALB, VPC, NATGateway, InternetGateway
from diagrams.aws.database import RDS
from diagrams.aws.security import SecretsManager, CertificateManager, IAM
from diagrams.aws.management import Cloudwatch, SystemsManager
from diagrams.aws.integration import SNS, SQS
from diagrams.aws.devtools import Codepipeline, Codebuild
from diagrams.aws.general import Users
from diagrams.aws.storage import SimpleStorageServiceS3Bucket as S3

graph_attr = {
    "fontsize": "14",
    "bgcolor": "white",
    "pad": "0.5"
}

with Diagram("BGR Applications - AWS Modernization Architecture", 
             filename="/Users/christian/Projects/escala/stack-sense/training/map-bgr/diagrams/bgr_aws_architecture",
             direction="TB",
             graph_attr=graph_attr,
             show=False):
    
    users = Users("End Users")
    
    with Cluster("AWS Cloud - us-east-1"):
        igw = InternetGateway("Internet Gateway")
        
        with Cluster("VPC (10.0.0.0/16)"):
            
            with Cluster("Public Subnets (3 AZs)"):
                alb_wave1 = ALB("ALB Wave 1\n(Portal + API)")
                alb_wave2 = ALB("ALB Wave 2\n(Backoffice)")
                nat = NATGateway("NAT Gateway\n(Multi-AZ)")
            
            with Cluster("Private Subnets - Compute (3 AZs)"):
                
                with Cluster("Wave 1 - ECS Cluster"):
                    ecs1 = ECS("ECS Fargate")
                    app1 = Fargate("PortalGuiaBGR\n2 vCPU, 4GB")
                    app2 = Fargate("Api Portal\n2 vCPU, 4GB")
                    app3 = Fargate("PortalAdmBGR\n1 vCPU, 2GB")
                
                with Cluster("Wave 2 - ECS Cluster"):
                    ecs2 = ECS("ECS Fargate")
                    app4 = Fargate("Backoffice Sistemas\n2 vCPU, 4GB")
                    app5 = Fargate("Backoffice Banca\n2 vCPU, 4GB")
                    app6 = Fargate("Saras\n2 vCPU, 4GB")
            
            with Cluster("Private Subnets - Data (3 AZs)"):
                rds1 = RDS("RDS SQL Server\ndb.m5.large\nMulti-AZ\n500GB")
                rds2 = RDS("RDS SQL Server 2019\ndb.m5.large\nMulti-AZ\n300GB")
            
            with Cluster("Shared Services"):
                with Cluster("Security & Identity"):
                    secrets = SecretsManager("Secrets Manager")
                    acm = CertificateManager("ACM")
                    iam = IAM("IAM + AD")
                
                with Cluster("Configuration & Messaging"):
                    ssm = SystemsManager("Parameter Store")
                    sns = SNS("SNS")
                    sqs = SQS("SQS")
                
                with Cluster("Observability"):
                    cw = Cloudwatch("CloudWatch\nLogs + Metrics")
        
        with Cluster("CI/CD Pipeline"):
            pipeline = Codepipeline("CodePipeline")
            build = Codebuild("CodeBuild")
            ecr = S3("ECR")
    
    # User flow
    users >> Edge(label="HTTPS") >> igw
    igw >> alb_wave1
    igw >> alb_wave2
    
    # Wave 1 apps
    alb_wave1 >> app1
    alb_wave1 >> app2
    alb_wave1 >> app3
    
    # Wave 2 apps
    alb_wave2 >> app4
    alb_wave2 >> app5
    alb_wave2 >> app6
    
    # Database connections
    app1 >> rds1
    app2 >> rds1
    app3 >> rds1
    app4 >> rds1
    app5 >> rds2
    app6 >> rds2
    
    # Shared services
    [app1, app2, app3, app4] >> iam
    [app1, app2, app3, app4, app5, app6] >> secrets
    [app1, app2, app3, app4, app5, app6] >> ssm
    [app1, app2, app3, app4, app5, app6] >> cw
    [app1, app2] >> sns
    
    # CI/CD
    pipeline >> build >> ecr >> [ecs1, ecs2]
    
    # NAT for outbound
    [app1, app2, app3, app4, app5, app6] >> nat >> igw

print("✅ Diagram generated: /Users/christian/Projects/escala/stack-sense/training/map-bgr/diagrams/bgr_aws_architecture.png")
