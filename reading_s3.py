import boto3
import pandas as pd
from io import StringIO

# Initialize a session using Amazon S3
s3_client = boto3.client('s3')

# Define the S3 bucket name and file key
bucket_name = 'ingestion-bucket-gdpr'
file_key = 'test_file.csv'

# Download the CSV file as an in-memory object
csv_obj = s3_client.get_object(Bucket=bucket_name, Key=file_key)

# Read the content of the file as a string
csv_data = csv_obj['Body'].read().decode('utf-8')

# Convert the string data into a pandas DataFrame
df = pd.read_csv(StringIO(csv_data))

# Now you can work with the DataFrame
print(df.head())
