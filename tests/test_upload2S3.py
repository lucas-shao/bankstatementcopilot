import boto3
import logging
from botocore.exceptions import ClientError
import os


def list_buckets():
    s3 = boto3.resource("s3")
    for bucket in s3.buckets.all():
        print(bucket.name)


def upload_file(file_name, bucket, object_name=None):
    """
    Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name.split("/")[-1]

    # Upload the file
    s3_client = boto3.client("s3")
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
        print("upload_file response: ", response)
    except ClientError as e:
        logging.error(e)
        return False
    return True


if __name__ == "__main__":
    upload_file("/Users/shaoshuai.shao/Desktop/IMG_7397.HEIC", "nw-dev-s3")
