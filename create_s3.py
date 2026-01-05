import boto3
from botocore.exceptions import ClientError

bucket_name = "terra-backend235"  # must be globally unique
folder_name = "terraform/" 

s3 = boto3.client("s3", region_name="us-east-1")

try:
    s3.create_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' created.")
except ClientError as e:
    if e.response["Error"]["Code"] == "BucketAlreadyOwnedByYou":
        print("Bucket already exists.")
    else:
        raise

s3.put_object(Bucket=bucket_name, Key=folder_name)
print(f"Folder '{folder_name}' created.")
