from moto import mock_s3, mock_dynamodb2
import boto3


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
        

        
def test_mock_s3(mock_s3):
    available_buckets = create_bucket(mock_s3)
    for bucket in available_buckets:
        assert bucket["Name"] == bucket_name
 

def create_bucket(s3_client):
    bucket_name = "testbucket"
    s3_client.create_bucket(Bucket='testbucket')
    available_buckets = s3_client.list_buckets()
    return available_buckets

          
