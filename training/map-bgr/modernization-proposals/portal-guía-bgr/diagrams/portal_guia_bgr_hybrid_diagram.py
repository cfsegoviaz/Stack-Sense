from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.network import ALB, VpnGateway
from diagrams.aws.database import Database
from diagrams.aws.management import Cloudwatch
from diagrams.onprem.client import Users

with Diagram("Portal Guia Bgr - Híbrido", filename="portal_guia_bgr_hybrid", show=False, direction="LR"):
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
