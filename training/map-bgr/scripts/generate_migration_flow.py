#!/usr/bin/env python3
from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server
from diagrams.onprem.database import Mssql
from diagrams.aws.compute import ECS, Fargate
from diagrams.aws.database import RDS
from diagrams.aws.network import ALB
from diagrams.custom import Custom

base_path = "/Users/christian/Projects/escala/stack-sense/training/map-bgr/diagrams"
graph_attr = {"fontsize": "12", "bgcolor": "white", "pad": "0.5", "ranksep": "2.0"}

# Migration Flow Diagram
with Diagram("BGR Applications - Migration Flow (On-Premise → AWS)", 
             filename=f"{base_path}/migration_flow",
             direction="LR", graph_attr=graph_attr, show=False):
    
    with Cluster("On-Premise Infrastructure"):
        with Cluster("ECBRTSW21\n(Windows Server 2016)\n4 vCPU, 8GB RAM, 300GB"):
            onprem_apps = [
                Server("PortalGuiaBGR\n.NET 4.7.1"),
                Server("Api Portal\n.NET 4.7.1"),
                Server("PortalAdmBGR\n.NET 4.7.1"),
                Server("Backoffice Sistemas\n.NET 4.7.1")
            ]
        
        with Cluster("Windows Server 2019"):
            onprem_modern = [
                Server("Backoffice Banca\n.NET Core 8"),
                Server("Saras\n.NET Core 8")
            ]
        
        with Cluster("Database Servers"):
            db_2016 = Mssql("SQL Server 2016\nEnterprise")
            db_2019 = Mssql("SQL Server 2019\nEnterprise")
    
    with Cluster("AWS Cloud - Target Architecture"):
        with Cluster("ECS Fargate - Modernized Apps"):
            aws_apps = [
                Fargate("PortalGuiaBGR\n.NET 8\n3 tasks"),
                Fargate("Api Portal\n.NET 8\n5 tasks"),
                Fargate("PortalAdmBGR\n.NET 8\n2 tasks"),
                Fargate("Backoffice Sistemas\n.NET 8\n3 tasks")
            ]
        
        with Cluster("ECS Fargate - Containerized Apps"):
            aws_modern = [
                Fargate("Backoffice Banca\n.NET 8\n3 tasks"),
                Fargate("Saras\n.NET 8\n2 tasks")
            ]
        
        with Cluster("RDS Multi-AZ"):
            rds_shared = RDS("RDS SQL Server\nStandard\ndb.m5.large")
            rds_2019 = RDS("RDS SQL Server 2019\nStandard\ndb.m5.large")
        
        alb = ALB("Application\nLoad Balancers")
    
    # Migration arrows
    onprem_apps[0] >> Edge(label="Modernize\n+ Container", color="blue", style="bold") >> aws_apps[0]
    onprem_apps[1] >> Edge(label="Modernize\n+ Container", color="blue", style="bold") >> aws_apps[1]
    onprem_apps[2] >> Edge(label="Modernize\n+ Container", color="blue", style="bold") >> aws_apps[2]
    onprem_apps[3] >> Edge(label="Modernize\n+ Container", color="blue", style="bold") >> aws_apps[3]
    
    onprem_modern[0] >> Edge(label="Container\nOnly", color="green", style="bold") >> aws_modern[0]
    onprem_modern[1] >> Edge(label="Container\nOnly", color="green", style="bold") >> aws_modern[1]
    
    db_2016 >> Edge(label="Migrate", color="orange", style="dashed") >> rds_shared
    db_2019 >> Edge(label="Migrate", color="orange", style="dashed") >> rds_2019
    
    aws_apps >> alb
    aws_modern >> alb

print("✅ Migration flow diagram generated")
print(f"   Location: {base_path}/migration_flow.png")
