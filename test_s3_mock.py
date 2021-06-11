from moto import mock_s3, mock_dynamodb2
import boto3
import pytest
import os


@pytest.fixture(scope='function')
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
    os.environ['AWS_SECURITY_TOKEN'] = 'testing'
    os.environ['AWS_SESSION_TOKEN'] = 'testing'
    os.environ["aws_region"] = "us-east-1"


@pytest.fixture(scope="function")
def dynamodb_client(aws_credentials):
    with mock_dynamodb2():
        yield boto3.client('dynamodb', region_name="us-east-1")


@pytest.fixture(scope='function')
def s3(aws_credentials):
    with mock_s3():
        yield boto3.client('s3', region_name='us-east-1')


def test_mock_s3(s3):
    bucket_name = "test_bucket"
    available_buckets = create_bucket(s3, bucket_name)
    for bucket in available_buckets["Buckets"]:
        assert bucket["Name"] == bucket_name


def create_bucket(s3_client, bucket_name):
    s3_client.create_bucket(Bucket=bucket_name)
    available_buckets = s3_client.list_buckets()
    return available_buckets
