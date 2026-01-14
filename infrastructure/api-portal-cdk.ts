#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import * as ec2 from 'aws-cdk-lib/aws-ec2';
import * as ecs from 'aws-cdk-lib/aws-ecs';
import * as ecsPatterns from 'aws-cdk-lib/aws-ecs-patterns';
import * as rds from 'aws-cdk-lib/aws-rds';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as cloudfront from 'aws-cdk-lib/aws-cloudfront';
import * as origins from 'aws-cdk-lib/aws-cloudfront-origins';
import * as route53 from 'aws-cdk-lib/aws-route53';
import * as acm from 'aws-cdk-lib/aws-certificatemanager';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as logs from 'aws-cdk-lib/aws-logs';
import { Construct } from 'constructs';

/**
 * API Portal Infrastructure as Code
 * 
 * Aplicación: API Portal BGR
 * Descripción: Portal estático de APIs que define entrada y salida de peticiones
 * Stack Actual: ASP.NET C# (.NET Framework 4.7.1) + SQL Server 2016
 * Arquitectura Objetivo: Modernización a contenedores en AWS
 */

export interface ApiPortalStackProps extends cdk.StackProps {
  environment: 'dev' | 'test' | 'prod';
  domainName?: string;
  certificateArn?: string;
}

export class ApiPortalStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props: ApiPortalStackProps) {
    super(scope, id, props);

    // Tags comunes
    const commonTags = {
      Project: 'BGR-Migration',
      Application: 'API-Portal',
      Environment: props.environment,
      Owner: 'erik.palma@bgr.com.ec',
      CostCenter: 'IT-Architecture'
    };

    // VPC - Red privada para la aplicación
    const vpc = new ec2.Vpc(this, 'ApiPortalVpc', {
      maxAzs: 2,
      natGateways: 1,
      subnetConfiguration: [
        {
          cidrMask: 24,
          name: 'Public',
          subnetType: ec2.SubnetType.PUBLIC,
        },
        {
          cidrMask: 24,
          name: 'Private',
          subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS,
        },
        {
          cidrMask: 24,
          name: 'Database',
          subnetType: ec2.SubnetType.PRIVATE_ISOLATED,
        }
      ]
    });

    // Security Groups
    const albSecurityGroup = new ec2.SecurityGroup(this, 'AlbSecurityGroup', {
      vpc,
      description: 'Security group for API Portal ALB',
      allowAllOutbound: true
    });
    
    albSecurityGroup.addIngressRule(
      ec2.Peer.anyIpv4(),
      ec2.Port.tcp(443),
      'HTTPS traffic'
    );
    
    albSecurityGroup.addIngressRule(
      ec2.Peer.anyIpv4(),
      ec2.Port.tcp(80),
      'HTTP traffic (redirect to HTTPS)'
    );

    const ecsSecurityGroup = new ec2.SecurityGroup(this, 'EcsSecurityGroup', {
      vpc,
      description: 'Security group for API Portal ECS tasks',
      allowAllOutbound: true
    });
    
    ecsSecurityGroup.addIngressRule(
      albSecurityGroup,
      ec2.Port.tcp(80),
      'Traffic from ALB'
    );

    const dbSecurityGroup = new ec2.SecurityGroup(this, 'DbSecurityGroup', {
      vpc,
      description: 'Security group for API Portal database',
      allowAllOutbound: false
    });
    
    dbSecurityGroup.addIngressRule(
      ecsSecurityGroup,
      ec2.Port.tcp(1433),
      'SQL Server access from ECS'
    );

    // RDS SQL Server - Migración de base de datos existente
    const dbSubnetGroup = new rds.SubnetGroup(this, 'DbSubnetGroup', {
      vpc,
      description: 'Subnet group for API Portal database',
      vpcSubnets: {
        subnetType: ec2.SubnetType.PRIVATE_ISOLATED
      }
    });

    const database = new rds.DatabaseInstance(this, 'ApiPortalDatabase', {
      engine: rds.DatabaseInstanceEngine.sqlServerEx({
        version: rds.SqlServerEngineVersion.VER_16_00_4105_2_V1
      }),
      instanceType: ec2.InstanceType.of(ec2.InstanceClass.T3, ec2.InstanceSize.MEDIUM),
      vpc,
      subnetGroup: dbSubnetGroup,
      securityGroups: [dbSecurityGroup],
      databaseName: 'PORTAL_ADMINISTRATIVO_BGR',
      credentials: rds.Credentials.fromGeneratedSecret('apiportal-admin', {
        secretName: `api-portal-db-credentials-${props.environment}`
      }),
      allocatedStorage: 100,
      storageType: rds.StorageType.GP2,
      backupRetention: cdk.Duration.days(7),
      deletionProtection: props.environment === 'prod',
      multiAz: props.environment === 'prod',
      autoMinorVersionUpgrade: true,
      storageEncrypted: true
    });

    // ECS Cluster
    const cluster = new ecs.Cluster(this, 'ApiPortalCluster', {
      vpc,
      clusterName: `api-portal-${props.environment}`,
      containerInsights: true
    });

    // CloudWatch Log Group
    const logGroup = new logs.LogGroup(this, 'ApiPortalLogGroup', {
      logGroupName: `/aws/ecs/api-portal-${props.environment}`,
      retention: logs.RetentionDays.ONE_MONTH,
      removalPolicy: cdk.RemovalPolicy.DESTROY
    });

    // Task Definition
    const taskDefinition = new ecs.FargateTaskDefinition(this, 'ApiPortalTaskDef', {
      memoryLimitMiB: 2048,
      cpu: 1024,
      family: `api-portal-${props.environment}`
    });

    // Container Definition
    const container = taskDefinition.addContainer('ApiPortalContainer', {
      image: ecs.ContainerImage.fromRegistry('mcr.microsoft.com/dotnet/aspnet:6.0'), // Modernizado a .NET 6
      environment: {
        ASPNETCORE_ENVIRONMENT: props.environment.toUpperCase(),
        ConnectionStrings__DefaultConnection: `Server=${database.instanceEndpoint.hostname};Database=PORTAL_ADMINISTRATIVO_BGR;Integrated Security=false;User ID=apiportal-admin;Password={password};TrustServerCertificate=true`,
        ASPNETCORE_URLS: 'http://+:80'
      },
      secrets: {
        DB_PASSWORD: ecs.Secret.fromSecretsManager(database.secret!, 'password')
      },
      logging: ecs.LogDrivers.awsLogs({
        streamPrefix: 'api-portal',
        logGroup: logGroup
      }),
      healthCheck: {
        command: ['CMD-SHELL', 'curl -f http://localhost/health || exit 1'],
        interval: cdk.Duration.seconds(30),
        timeout: cdk.Duration.seconds(5),
        retries: 3,
        startPeriod: cdk.Duration.seconds(60)
      }
    });

    container.addPortMappings({
      containerPort: 80,
      protocol: ecs.Protocol.TCP
    });

    // Application Load Balancer + Fargate Service
    const fargateService = new ecsPatterns.ApplicationLoadBalancedFargateService(this, 'ApiPortalService', {
      cluster,
      taskDefinition,
      serviceName: `api-portal-${props.environment}`,
      desiredCount: props.environment === 'prod' ? 2 : 1,
      publicLoadBalancer: true,
      listenerPort: 443,
      protocol: ecsPatterns.ApplicationProtocol.HTTPS,
      domainName: props.domainName,
      domainZone: props.domainName ? route53.HostedZone.fromLookup(this, 'Zone', {
        domainName: props.domainName.split('.').slice(-2).join('.')
      }) : undefined,
      certificate: props.certificateArn ? acm.Certificate.fromCertificateArn(this, 'Certificate', props.certificateArn) : undefined,
      redirectHTTP: true,
      platformVersion: ecs.FargatePlatformVersion.LATEST
    });

    // Configurar Security Groups
    fargateService.service.connections.securityGroups.forEach(sg => {
      sg.addIngressRule(
        albSecurityGroup,
        ec2.Port.tcp(80),
        'ALB to ECS'
      );
    });

    // Auto Scaling
    const scaling = fargateService.service.autoScaleTaskCount({
      minCapacity: props.environment === 'prod' ? 2 : 1,
      maxCapacity: props.environment === 'prod' ? 10 : 3
    });

    scaling.scaleOnCpuUtilization('CpuScaling', {
      targetUtilizationPercent: 70,
      scaleInCooldown: cdk.Duration.minutes(5),
      scaleOutCooldown: cdk.Duration.minutes(2)
    });

    scaling.scaleOnMemoryUtilization('MemoryScaling', {
      targetUtilizationPercent: 80,
      scaleInCooldown: cdk.Duration.minutes(5),
      scaleOutCooldown: cdk.Duration.minutes(2)
    });

    // S3 Bucket para assets estáticos y logs
    const assetsBucket = new s3.Bucket(this, 'ApiPortalAssets', {
      bucketName: `api-portal-assets-${props.environment}-${this.account}`,
      versioned: true,
      encryption: s3.BucketEncryption.S3_MANAGED,
      blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
      removalPolicy: props.environment === 'prod' ? cdk.RemovalPolicy.RETAIN : cdk.RemovalPolicy.DESTROY
    });

    // CloudFront Distribution para contenido estático
    const distribution = new cloudfront.Distribution(this, 'ApiPortalCDN', {
      defaultBehavior: {
        origin: new origins.LoadBalancerV2Origin(fargateService.loadBalancer, {
          protocolPolicy: cloudfront.OriginProtocolPolicy.HTTPS_ONLY
        }),
        viewerProtocolPolicy: cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
        allowedMethods: cloudfront.AllowedMethods.ALLOW_ALL,
        cachedMethods: cloudfront.CachedMethods.CACHE_GET_HEAD_OPTIONS,
        cachePolicy: cloudfront.CachePolicy.CACHING_OPTIMIZED
      },
      additionalBehaviors: {
        '/assets/*': {
          origin: new origins.S3Origin(assetsBucket),
          viewerProtocolPolicy: cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
          cachePolicy: cloudfront.CachePolicy.CACHING_OPTIMIZED
        }
      },
      priceClass: cloudfront.PriceClass.PRICE_CLASS_100,
      enabled: true,
      comment: `API Portal CDN - ${props.environment}`
    });

    // IAM Role para ECS Task
    taskDefinition.taskRole.addManagedPolicy(
      iam.ManagedPolicy.fromAwsManagedPolicyName('service-role/AmazonECSTaskExecutionRolePolicy')
    );

    // Permisos para acceder a S3
    assetsBucket.grantReadWrite(taskDefinition.taskRole);

    // Aplicar tags a todos los recursos
    Object.entries(commonTags).forEach(([key, value]) => {
      cdk.Tags.of(this).add(key, value);
    });

    // Outputs
    new cdk.CfnOutput(this, 'LoadBalancerDNS', {
      value: fargateService.loadBalancer.loadBalancerDnsName,
      description: 'DNS name of the load balancer'
    });

    new cdk.CfnOutput(this, 'CloudFrontDomain', {
      value: distribution.distributionDomainName,
      description: 'CloudFront distribution domain name'
    });

    new cdk.CfnOutput(this, 'DatabaseEndpoint', {
      value: database.instanceEndpoint.hostname,
      description: 'RDS database endpoint'
    });

    new cdk.CfnOutput(this, 'S3BucketName', {
      value: assetsBucket.bucketName,
      description: 'S3 bucket for static assets'
    });
  }
}

// App principal
const app = new cdk.App();

// Stack de desarrollo
new ApiPortalStack(app, 'ApiPortalDevStack', {
  environment: 'dev',
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION || 'us-east-1'
  }
});

// Stack de producción
new ApiPortalStack(app, 'ApiPortalProdStack', {
  environment: 'prod',
  domainName: 'api-portal.bgr.com.ec',
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION || 'us-east-1'
  }
});