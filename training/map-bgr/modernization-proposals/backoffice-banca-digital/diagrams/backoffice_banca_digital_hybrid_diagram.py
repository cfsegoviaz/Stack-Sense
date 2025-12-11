with Diagram("Backoffice Banca Digital - Híbrido", filename="backoffice_banca_digital_hybrid", show=False, direction="LR"):
    users = Users("Users")
    
    with Cluster("AWS Cloud"):
        with Cluster("VPC"):
            alb = ALB("Application\nLoad Balancer")
            
            with Cluster("Private Subnet"):
                ec2_group = [
                    EC2("EC2 Instance 1"),
                    EC2("EC2 Instance 2")
                ]
            
            vpn = VpnGateway("VPN\nGateway")
        
        cw = Cloudwatch("CloudWatch")
    
    with Cluster("On-Premise"):
        db_onprem = Database("SQL Server\nOn-Premise")
    
    users >> alb >> ec2_group
    ec2_group >> vpn >> db_onprem
    ec2_group >> cw
