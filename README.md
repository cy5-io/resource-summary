# aws-resource-summary
This command line utility generates a summary of resources across the AWS regions provided by the user.

It is a simple Python script that will count resources across different regions and display them on the command line. It first takes the input of regions from the user and then displays the resource count for each of the following resource on the screen. At last, it also shows the total resource count of region-specefic resources and also, the global resources such as IAM, Cloudfront etc. 

Following are the resources that the utility generates a summary for:

* IAM Users
* IAM Groups
* IAM Roles
* Cloudfront Distributions
* S3 buckets
* Subnets
* VPCs
* VPC Endpoints
* EC2 Instances
* Security Groups
* Route Tables
* EBS Volumes
* EBS Snapshots
* Network Load Balancers
* Application Load Balancers
* Lambda functions
* SQS Queues
* DynamoDB Tables
* DynamoDB Global Tables
* RDS Clusters
* RDS Instances
* RDS DB Snapshots
* ElasticSearch Domain Names
* Elasticache Clusters
* Redshift Clusters
* ECR Repositories
* EKS Clusters
* ECS Clusters
* DocumentDB Clusters
* Neptune DB Clusters
* Kinesis Streams
* API Gateway Rest APIs
* Kafka Clusters

## Usage:

Installation:

	git clone https://github.com/cy5-io/resource-summary.git
	cd resource-summary
	pip install -r requirements.txt

Execution:

	python resource_count.py 

## Required Permissions:

The sript uses AWS credentials that are configured via the AWS CLI. Please ensure the user / IAM principal being used has the required permissions on the AWS account for which the resource summary is being requested.

The script requires read-only access via the AWS managed policy "SecurityAudit".

## Sample Output:

Enter the regions:
(press Enter twice, when you’re done providing regions)

us-east-1
eu-central-1


Collecting global resource count for Account XXXXXXXXXXXX

Users: 5
Groups: 1
Roles: 76
Cloudfront Distributions: 1

Collecting region-specific resource count for Account XXXXXXXXXXXX in region us-east-1

s3 buckets: 17
Subnets: 10
VPCs: 4
VPC Endpoints: 2
EC2 Instances: 4
Security Groups: 18
Route Tables: 5
EBS Volumes: 4
EBS Snapshots: 2
Network Load Balancers: 0
Application Load Balancers: 2
Lambda functions: 10
SQS Queues: 1
DynamoDB Tables: 0
DynamoDB Global Tables: 0
RDS Clusters: 0
RDS Instances: 1
RDS DB Snapshots: 11
ElasticSearch Domain Names: 1
Elasticache Clusters: 0
Redshift Clusters: 0
ECR Repositories: 1
EKS Clusters: 0
ECS Clusters: 0
DocumentDB Clusters: 0
Neptune DB Clusters: 0
Kinesis Streams: 0
API Gateway Rest APIs: 1
Kafka Clusters: 0


Account ID: XXXXXXXXXXXX
Total count of resources in 'us-east-1' region: 94


Collecting region-specific resource count for Account XXXXXXXXXXXX in region eu-central-1

s3 buckets: 17
Subnets: 3
VPCs: 1
VPC Endpoints: 0
EC2 Instances: 0
Security Groups: 1
Route Tables: 1
EBS Volumes: 0
EBS Snapshots: 0
Network Load Balancers: 0
Application Load Balancers: 0
Lambda functions: 0
SQS Queues: 0
DynamoDB Tables: 0
DynamoDB Global Tables: 0
RDS Clusters: 0
RDS Instances: 0
RDS DB Snapshots: 0
ElasticSearch Domain Names: 0
Elasticache Clusters: 0
Redshift Clusters: 0
ECR Repositories: 0
EKS Clusters: 0
ECS Clusters: 0
DocumentDB Clusters: 0
Neptune DB Clusters: 0
Kinesis Streams: 0
API Gateway Rest APIs: 0
Kafka Clusters: 0


Account ID: XXXXXXXXXXXX
Total count of resources in 'eu-central-1' region: 23

Total count of global resources: 83
