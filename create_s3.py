import boto3
from botocore.exceptions import ClientError

bucket_name = "your_unique_bucket_name"  # must be globally unique
folder_prefix = "your_folder_within_the_bucket/" 

s3 = boto3.client("s3", region_name="us-east-1")

try:
    s3.create_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' created.")
except ClientError as e:
    if e.response["Error"]["Code"] == "BucketAlreadyOwnedByYou":
        print("Bucket already exists.")
    else:
        raise

s3.put_object(Bucket=bucket_name, Key=folder_prefix)
print(f"Folder '{folder_prefix}' created.")
