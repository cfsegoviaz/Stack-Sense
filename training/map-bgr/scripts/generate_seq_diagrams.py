#!/usr/bin/env python3
from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import Lambda
from diagrams.aws.storage import S3
from diagrams.aws.management import Cloudwatch, CloudwatchLogs
from diagrams.aws.integration import SimpleNotificationServiceSnsTopic
from diagrams.aws.analytics import KinesisDataFirehose, AmazonOpensearchService
from diagrams.onprem.client import Users
from diagrams.onprem.database import Mssql
from diagrams.onprem.compute import Server

# 1. Arquitectura Actual (AS-IS)
with Diagram("Seq - Arquitectura Actual On-Premise", show=False, direction="TB", filename="../modernization-proposals/seq/diagrams/seq_current_architecture"):
    users = Users("685 Colaboradores BGR")
    
    with Cluster("On-Premise Datacenter"):
        with Cluster("Seq Application Servers"):
            seq1 = Server("ECBRPRW44\n4 vCPU, 20GB RAM")
            seq2 = Server("ECBRPRW45\n8 vCPU, 20GB RAM")
        
        with Cluster("Database Server"):
            db = Mssql("ECBRPRCL13\n24 vCPU, 80GB RAM\nSQL Server Enterprise")
        
        with Cluster("Test Environment"):
            test1 = Server("ECBRTSCC01")
    
    with Cluster("BGR Applications"):
        app1 = Server("Portal Guía")
        app2 = Server("Backoffice")
        app3 = Server("API Portal")
    
    users >> seq1
    users >> seq2
    seq1 >> db
    seq2 >> db
    app1 >> seq1
    app2 >> seq1
    app3 >> seq2

# 2. Arquitectura AWS Modernizada (TO-BE)
with Diagram("Seq - Arquitectura AWS Modernizada", show=False, direction="TB", filename="../modernization-proposals/seq/diagrams/seq_aws_modernized"):
    users = Users("BGR Users")
    
    with Cluster("AWS Cloud"):
        with Cluster("Log Processing"):
            cw_logs = CloudwatchLogs("CloudWatch Logs")
            lambda_fn = Lambda("Log Transformation")
            opensearch = AmazonOpensearchService("OpenSearch Service")
        
        with Cluster("Storage"):
            s3_archive = S3("S3 Glacier Archive")
        
        with Cluster("Monitoring"):
            cw_dashboards = Cloudwatch("CloudWatch Dashboards")
            sns = SimpleNotificationServiceSnsTopic("SNS Alerts")
    
    with Cluster("BGR Applications"):
        app1 = Server("Portal Guía")
        app2 = Server("Backoffice") 
        app3 = Server("API Portal")
    
    # Flujo de logs
    app1 >> cw_logs
    app2 >> cw_logs
    app3 >> cw_logs
    cw_logs >> lambda_fn >> opensearch
    cw_logs >> s3_archive
    opensearch >> cw_dashboards
    cw_logs >> sns
    users >> opensearch
    users >> cw_dashboards

# 3. Comparación de Costos
with Diagram("Seq - Comparación de Costos", show=False, direction="LR", filename="../modernization-proposals/seq/diagrams/seq_comparison"):
    
    with Cluster("On-Premise: $22,000/año"):
        onprem = Server("3 Servidores\n+ SQL Server Enterprise\n+ Windows Licenses")
    
    with Cluster("AWS Modernizado: $3,342/año"):
        aws_modern = CloudwatchLogs("CloudWatch + OpenSearch\n85% Ahorro")
    
    onprem >> Edge(label="Migración", style="dashed") >> aws_modern

# 4. Timeline de Migración
with Diagram("Seq - Timeline Migración (4 semanas)", show=False, direction="LR", filename="../modernization-proposals/seq/diagrams/seq_migration_timeline"):
    
    week1 = Server("Semana 1\nAnálisis + Setup")
    week2 = CloudwatchLogs("Semana 2\nMigración Logs")
    week3 = Cloudwatch("Semana 3\nDashboards")
    week4 = AmazonOpensearchService("Semana 4\nGo-Live")
    
    week1 >> week2 >> week3 >> week4

print("✅ Diagramas de Seq generados exitosamente")
