import boto3
from botocore.exceptions import ClientError

bucket_name = "your_unique_bucket_name"  # must be globally unique
folder_prefix = "your_folder_within_the_bucket/" 

s3 = boto3.resource("s3")
bucket = s3.Bucket(bucket_name)

try:
    objects_to_delete = bucket.objects.filter(Prefix=folder_prefix)
    deleted = objects_to_delete.delete()
    print(f"Deleted objects in folder '{folder_prefix}'")
except ClientError as e:
    print("Error deleting folder:", e)
    exit(1)

try:
    bucket.delete()
    print(f"Bucket '{bucket_name}' deleted successfully.")
except ClientError as e:
    print("Error deleting bucket:", e)

