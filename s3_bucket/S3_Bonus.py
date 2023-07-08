import boto3 


s3 = boto3.client('s3')

# BONUS

# list the Buckets

responseBucket = s3.list_buckets()

for bucket in responseBucket["Buckets"]:
    print(bucket["Name"])


# Download Group of Files 

# Copy Between the Buckets


# Display MetaObjects


# Pre-Signed Url
