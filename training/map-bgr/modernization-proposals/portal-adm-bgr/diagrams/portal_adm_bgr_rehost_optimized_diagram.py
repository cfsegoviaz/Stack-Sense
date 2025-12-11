with Diagram("Portal Adm Bgr - Lift & Shift Optimizado", filename="portal_adm_bgr_optimized", show=False, direction="LR"):
    users = Users("Users")
    
    with Cluster("AWS Cloud"):
        with Cluster("VPC"):
            alb = ALB("Application\nLoad Balancer")
            
            with Cluster("Private Subnet - App"):
                ec2_group = [
                    EC2("EC2 Instance 1"),
                    EC2("EC2 Instance 2")
                ]
            
            with Cluster("Private Subnet - Data"):
                rds = RDS("RDS\nMulti-AZ")
        
        s3 = S3("S3\nBackups")
        cw = Cloudwatch("CloudWatch")
        sm = SecretsManager("Secrets\nManager")
    
    users >> alb >> ec2_group >> rds
    rds >> s3
    ec2_group >> cw
    ec2_group >> sm
