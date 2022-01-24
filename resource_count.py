#!/usr/bin/python3
import boto3
from sys import stdin

print("Enter the regions:")
print("(press Enter twice, when you’re done providing regions)\n")
regions = []
while True:
    region = input()    
    if region:
        regions.append(region)
    else:
        break

try:
        session = boto3.Session()
except:
        print("Couldn't connect")

sts = session.client('sts')
account_id = sts.get_caller_identity()['Account']

print("\nCollecting global resource count for Account " + str(account_id) + "\n")

iam = session.client('iam')
users = iam.list_users()['Users']
print("Users: " + str(len(users)))
groups = iam.list_groups()['Groups']
print("Groups: " + str(len(groups)))
roles = iam.list_roles()['Roles']
print("Roles: " + str(len(roles)))
policies = iam.list_policies()['Policies']
print("Policies: " + str(len(policies)))

s3 = session.client('s3')
try:
    buckets = s3.list_buckets()['Buckets']
except:
    buckets = []
print("s3 buckets: " + str(len(buckets)))        


cfront = session.client('cloudfront')
try:
    distributions = cfront.list_distributions()['DistributionList']['Items']
except:
    distributions = []
print("Cloudfront Distributions: " + str(len(distributions)))

total_global = len(users+roles+groups+policies+buckets+distributions)

for region in regions:
        print("\nCollecting region-specific resource count for Account " + str(account_id) + " in region " + region + "\n" )

        ec2 = session.client('ec2', region_name = region)
        try:
            subnets = ec2.describe_subnets()['Subnets']
        except:
            subnets = []
        print("Subnets: " + str(len(subnets)))
        try:
            vpc = ec2.describe_vpcs()['Vpcs']
        except:
            vpc = []
        print("VPCs: " + str(len(vpc)))
        try:
            endpoints = ec2.describe_vpc_endpoints()['VpcEndpoints']
        except:
            endpoints = []
        print("VPC Endpoints: " + str(len(endpoints)))
        try:
            instance_count = 0
            instances = ec2.describe_instances()['Reservations']                
            for instance in instances:
                for i in instance['Instances']:
                    instance_count += 1
        except:
            instance_count = 0
        print("EC2 Instances: " + str(instance_count))
        try:
            sec_groups = ec2.describe_security_groups()['SecurityGroups']
        except:
            sec_groups = []
        print("Security Groups: " + str(len(sec_groups)))
        try:
            rtables = ec2.describe_route_tables()['RouteTables']
        except:
            rtables = []
        print("Route Tables: " + str(len(rtables)))
        try:
            ebs_volumes = ec2.describe_volumes()['Volumes']
        except:
            ebs_volumes = []
        print("EBS Volumes: " + str(len(ebs_volumes)))
        try:
            ebs_snapshots = ec2.describe_snapshots(OwnerIds=[account_id])['Snapshots']
        except:
            ebs_snapshots = []
        print("EBS Snapshots: " + str(len(ebs_snapshots)))

        elb = session.client('elbv2', region_name = region)
        try:
            lb = elb.describe_load_balancers()['LoadBalancers']
            alb = 0
            nlb = 0
            for i in lb:
                if i['Type'] ==  'application':
                    alb += 1
                elif i['Type'] == 'network':
                    nlb += 1
        except:
            alb = 0
            nlb = 0
        print("Network Load Balancers: " + str(nlb))
        print("Application Load Balancers: " + str(alb))
        
        lamda = session.client('lambda', region_name = region)
        try:
            functions = lamda.list_functions()['Functions']
        except:
            functions = []
        print("Lambda functions: " + str(len(functions)))

        sqs = session.client('sqs', region_name = region)
        try:
            queues = sqs.list_queues()['QueueUrls']
        except:
            queues = []
        print("SQS Queues: " + str(len(queues)))

        dynamodb = session.client('dynamodb', region_name = region)
        try:
            tables = dynamodb.list_tables()['TableNames']
            global_tables = dynamodb.list_global_tables()['GlobalTables']
        except:
            tables = []
            global_tables = []
        print("DynamoDB Tables: " + str(len(tables)))
        print("DynamoDB Global Tables: " + str(len(global_tables)))
        
        rds = session.client('rds', region_name = region)
        try:
            clusters = rds.describe_db_clusters()['DBClusters']
        except:
            clusters = []
        print("RDS Clusters: " + str(len(clusters)))
        try:
            instances = rds.describe_db_instances()['DBInstances']
        except:
            instances = []
        print("RDS Instances: " + str(len(instances)))
        try:
            db_snapshots = rds.describe_db_snapshots()['DBSnapshots']
        except:
            db_snapshots = []
        print("RDS DB Snapshots: " + str(len(db_snapshots)))

        es = session.client('es', region_name = region)
        try:
            domains = es.list_domain_names()['DomainNames']
        except:
            domains = []
        print("ElasticSearch Domain Names: " + str(len(domains)))

        ecache = session.client('elasticache', region_name=region)
        try:
            ecache_clusters = ecache.describe_cache_clusters()['CacheClusters']
        except:
            ecache_clusters = []
        print("Elasticache Clusters: " + str(len(ecache_clusters)))

        rshift = session.client('redshift', region_name=region)
        try:
            r_clusters = rshift.describe_clusters()['Clusters']
        except:
            r_clusters = []
        print("Redshift Clusters: " + str(len(r_clusters)))

        ecr = session.client('ecr', region_name=region)
        try:
            repos = ecr.describe_repositories()['repositories']
        except:
            repos = []
        print("ECR Repositories: " + str(len(repos)))

        eks = session.client('eks', region_name=region)
        try:
            eks_clusters = eks.list_clusters()['clusters']
        except:
            eks_clusters = []
        print("EKS Clusters: " + str(len(eks_clusters)))

        ecs = session.client('ecs', region_name=region)
        try:
            ecs_clusters = ecs.describe_clusters()['clusters']
        except:
            ecs_clusters = []
        print("ECS Clusters: " + str(len(ecs_clusters)))

        docdb = session.client('docdb', region_name=region)
        try:
            docdb_clusters = docdb.describe_db_clusters()['DBClusters']
        except:
            docdb_clusters = []
        print("DocumentDB Clusters: " + str(len(docdb_clusters)))

        neptune = session.client('neptune', region_name=region)
        try:
            neptune_clusters = neptune.describe_db_clusters()['DBClusters']
        except:
            neptune_clusters = []
        print("Neptune DB Clusters: " + str(len(neptune_clusters)))

        kinesis = session.client('kinesis', region_name=region)
        try:
            streams = kinesis.list_streams()['StreamNames']
        except:
            streams = []
        print("Kinesis Streams: " + str(len(streams)))

        api_gw = session.client('apigateway', region_name=region)
        try:
            api_list = api_gw.get_rest_apis()['items']
        except:
            api_list = []
        print("API Gateway Rest APIs: " + str(len(api_list)))

        msk = session.client('kafka', region_name=region)
        try:
            kafka_clusters = msk.list_clusters()['ClusterInfoList']
        except:
            kafka_clusters = []
        print("Kafka Clusters: " + str(len(kafka_clusters)))

        total_region = len(subnets+vpc+endpoints+sec_groups+rtables+ebs_volumes+ebs_snapshots+functions+queues+tables+global_tables+clusters+instances+db_snapshots+domains+ecache_clusters+r_clusters+repos+eks_clusters+ecs_clusters+docdb_clusters+neptune_clusters+streams+api_list+kafka_clusters) + alb +nlb + instance_count

        print("\n\nAccount ID: " + str(account_id))
        print("Total count of resources in '" + region + "' region: " + str(total_region) + "\n")

print("Total count of global resources: " + str(total_global))
