from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.network import ALB
from diagrams.aws.storage import EBS
from diagrams.aws.management import Cloudwatch
from diagrams.aws.security import SecretsManager
from diagrams.onprem.client import Users

with Diagram("Portal Guia Bgr - Lift & Shift", filename="portal_guia_bgr_lift_shift", show=False, direction="LR"):
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
