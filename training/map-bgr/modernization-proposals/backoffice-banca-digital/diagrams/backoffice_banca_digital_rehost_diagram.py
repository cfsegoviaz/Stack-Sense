with Diagram("Backoffice Banca Digital - Lift & Shift", filename="backoffice_banca_digital_lift_shift", show=False, direction="LR"):
    users = Users("Users")
    
    with Cluster("AWS Cloud"):
        with Cluster("VPC"):
            alb = ALB("Application\nLoad Balancer")
            
            with Cluster("Private Subnet"):
                ec2_group = [
                    EC2("EC2 Instance 1"),
                    EC2("EC2 Instance 2")
                ]
            
            ebs = EBS("EBS Volumes")
        
        cw = Cloudwatch("CloudWatch\nMonitoring")
        sm = SecretsManager("Secrets\nManager")
    
    users >> alb >> ec2_group
    ec2_group >> ebs
    ec2_group >> cw
    ec2_group >> sm
