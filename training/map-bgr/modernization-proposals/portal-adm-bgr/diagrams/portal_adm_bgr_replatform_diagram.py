with Diagram("Portal Adm Bgr - Containerización ECS", filename="portal_adm_bgr_containers", show=False, direction="LR"):
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
