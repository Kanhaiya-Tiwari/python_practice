# Create an AWS Client
from tracemalloc import Snapshot

import boto3

ec2 = boto3.client("ec2")

# You can also create a resource object:

import boto3

ec2 = boto3.resource("ec2")

# List all instances:

import boto3

ec2 = boto3.client("ec2")

response = ec2.describe_instances()

print(response)
# Start an Instance
ec2.start_instances(
    InstanceIds=["i-0123456789abcdef"]
)
# Stop an Instance
ec2.stop_instances(
    InstanceIds=["i-0123456789abcdef"]
)
# Terminate an Instance
ec2.terminate_instances(
    InstanceIds=["i-0123456789abcdef"]
)


# 2. S3 Automation

# Amazon S3 is an object storage service used to store files.

# Upload a File
import boto3

s3 = boto3.client("s3")

s3.upload_file(
    "backup.zip",
    "my-backup-bucket",
    "backup.zip"
)
# Download a File
s3.download_file(
    "my-backup-bucket",
    "backup.zip",
    "backup.zip"
)
# List Objects
response = s3.list_objects_v2(
    Bucket="my-backup-bucket"
)

for obj in response.get("Contents", []):
    print(obj["Key"])


# 3. IAM Automation 
# IAM (Identity and Access Management) controls who can access AWS resources.

# Create a User
import boto3

iam = boto3.client("iam")

iam.create_user(
    UserName="kanha"
)
# List Users
response = iam.list_users()

for user in response["Users"]:
    print(user["UserName"])


# 4. Lambda Automation

# AWS Lambda runs code without managing servers.

# Invoke a Lambda Function
import boto3

lambda_client = boto3.client("lambda")

response = lambda_client.invoke(
    FunctionName="MyFunction"
)

# 5. CloudWatch Automation 
# CloudWatch monitors AWS resources and applications.
import boto3

cloudwatch = boto3.client("cloudwatch")

response = cloudwatch.get_metric_statistics(
    Namespace="AWS/EC2",
    MetricName="CPUUtilization",
    StartTime=start_time,
    EndTime=end_time,
    Period=300,
    Statistics=["Average"]
)

# Create an Alarm
cloudwatch.put_metric_alarm(
    AlarmName="HighCPU"
)

# 6. EKS Automation 
# Amazon EKS (Elastic Kubernetes Service) is AWS's managed Kubernetes service.

# List Clusters
import boto3

eks = boto3.client("eks")

response = eks.list_clusters()

print(response["clusters"])

# Describe a Cluster
eks.describe_cluster(
    name="production-cluster"
)

# 8.RDS Automation 
# Amazon RDS is a managed relational database service.

# List Databases
import boto3

rds = boto3.client("rds")

response = rds.describe_db_instances()

print(response)
# Create a Snapshot
rds.create_db_snapshot(
    DBSnapshotIdentifier="backup1",
    DBInstanceIdentifier="mydatabase"
)