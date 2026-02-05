import boto3

s3_client = boto3.client('s3')#create an S3 client using boto3
#set a breakpoint to debug the code
for bucket in s3_client.list_buckets()['Buckets']:#list all the buckets in the S3 account
    print(bucket['Name'])#print the name of each bucketq
