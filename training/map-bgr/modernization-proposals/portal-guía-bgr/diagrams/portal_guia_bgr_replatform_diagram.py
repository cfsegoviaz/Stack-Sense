from diagrams import Diagram, Cluster
from diagrams.aws.compute import Fargate, ECR
from diagrams.aws.database import Aurora, ElastiCache
from diagrams.aws.network import ALB
from diagrams.aws.storage import S3
from diagrams.aws.management import Cloudwatch
from diagrams.onprem.client import Users

with Diagram("Portal Guia Bgr - Containerización ECS", filename="portal_guia_bgr_containers", show=False, direction="LR"):
    users = Users("Users")
    
    with Cluster("AWS Cloud"):
        with Cluster("VPC"):
            alb = ALB("Application\nLoad Balancer")
            
            with Cluster("ECS Fargate"):
                ecs_tasks = [
                    Fargate("Task 1"),
                    Fargate("Task 2")
                ]
            
            with Cluster("Data Layer"):
                aurora = Aurora("Aurora\nPostgreSQL")
                elasticache = ElastiCache("ElastiCache\nRedis")
        
        ecr = ECR("ECR\nContainer\nRegistry")
        s3 = S3("S3\nAssets")
        cw = Cloudwatch("CloudWatch")
    
    users >> alb >> ecs_tasks
    ecs_tasks >> aurora
    ecs_tasks >> elasticache
    ecs_tasks >> s3
    ecr >> ecs_tasks
    ecs_tasks >> cw
