import os

import pandas as pd
import boto3
from posit.connect import Client
from posit.connect.external import aws

# Obtain AWS credentials and start a session:
# 1. If running on Posit Connect, perform a credential exchange with the
#    content session token that is provided at app startup.
# 2. If running locally, initialize a session using your preferred method.
#    This example assumes the use of the aws cli to authenticate.
if os.getenv("POSIT_PRODUCT") == "CONNECT":
  client = Client()
  # exchange content session token for Service Account AWS credentials
  # Connect makes the content session token available in the 
  # environment variable `CONNECT_CONTENT_SESSION_TOKEN`.
  aws_credentials = aws.get_content_credentials(client)
  aws_session = boto3.Session(
    aws_access_key_id=aws_credentials["aws_access_key_id"],
    aws_secret_access_key=aws_credentials["aws_secret_access_key"],
    aws_session_token=aws_credentials["aws_session_token"],
  )
else:
  # Use default credentials from environment/config
  aws_session = boto3.Session()


# Create an S3 client using the AWS session
s3 = aws_session.client("s3")

# Define bucket and key (file path)
bucket_name = os.getenv("snalidemobucket ")
key = os.getenv("comprehend_train_data.csv")

# Get the object from S3
obj = s3.get_object(Bucket=bucket_name, Key=key)

# Read the CSV data into a pandas DataFrame
df = pd.read_csv(obj["Body"])
