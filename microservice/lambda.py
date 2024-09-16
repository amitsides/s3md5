import boto3
import hashlib

s3 = boto3.client('s3')

def lambda_handler(event, context):
    for record in event['Records']:
        # Parse S3 event
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']

        # Get object from S3
        response = s3.get_object(Bucket=bucket, Key=key)
        data = response['Body'].read()

        # Calculate MD5 checksum
        md5_hash = hashlib.md5(data).hexdigest()

        print(f"File: {key}, MD5: {md5_hash}")

        # TODO: Store or forward the MD5 checksum as needed