import boto3
from core.config import settings
from botocore.exceptions import ClientError

s3_client = boto3.client(
    "s3",
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
)


def upload_file_to_s3(file, filename):
    try:
        s3_client.upload_fileobj(
            file.file, settings.AWS_S3_BUCKET_NAME, filename)
        return f"https://{settings.AWS_S3_BUCKET_NAME}.s3.amazonaws.com/{filename}"
    except ClientError:
        return None


def delete_file_from_s3(filename):
    try:
        s3_client.delete_object(
            Bucket=settings.AWS_S3_BUCKET_NAME, Key=filename)
        return True
    except ClientError:
        return False
