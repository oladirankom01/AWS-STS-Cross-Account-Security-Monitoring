import boto3
import os

def lambda_handler(event, context):

    print("Starting cross-account S3 access")

    role_arn = os.environ["CROSS_ACCOUNT_ROLE_ARN"]
    bucket_name = os.environ["S3_BUCKET_NAME"]
    object_key = os.environ["S3_OBJECT_KEY"]

    sts = boto3.client("sts")

    print("Requesting temporary credentials from STS")

    response = sts.assume_role(
        RoleArn=role_arn,
        RoleSessionName="CrossAccountSession"
    )
    
    print("Successfully assumed cross-account role")

    credentials = response["Credentials"]

    s3 = boto3.client(
        "s3",
        aws_access_key_id=credentials["AccessKeyId"],
        aws_secret_access_key=credentials["SecretAccessKey"],
        aws_session_token=credentials["SessionToken"]
    )

    print("Attempting to read S3 object")

    response = s3.get_object(
        Bucket=bucket_name,
        Key=object_key
    )

    content = response["Body"].read().decode("utf-8")
    
    print("Successfully retrieved S3 object")

    print(content)

    return {
        "statusCode": 200,
        "body": content
    }