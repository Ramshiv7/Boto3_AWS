import os
import boto3

# Connect to AWS S3 through Boto3

s3 = boto3.client("s3")

# Create S3 Bucket
bucketResponse = s3.create_bucket(Bucket="ramshiv-bucket-global-test")

BUCKET_NAME = bucketResponse["Location"].replace("/", "")


# Upload Files to the S3 Bucket

filesPath = "/home/Documents/sampleTree/"

localFiles = [files for (root, direc, files) in os.walk(filesPath)]

for file in localFiles[0]:
    if "html" in file:
        fileToS3 = os.path.join(filesPath, file)

        s3.upload_file(fileToS3, BUCKET_NAME, file)


# Download Files from the S3 Bucket

s3.download_file(BUCKET_NAME, "index.html", "hello.html")


# List Files From S3 Bucket

# objectResponse = s3.list_objects_v2(Bucket=BUCKET_NAME)

# # print(objectResponse)

# for object in objectResponse["Contents"]:
#     print(object)


# s3 = boto3.client("s3")

# with open('new_file.html','wb') as data:
#     s3.download_fileobj(BUCKET_NAME,'hi.html', data)


# BONUS

# list the Buckets

# responseBucket = s3.list_buckets()

# for bucket in responseBucket["Buckets"]:
#     print(bucket["Name"])


# Copy Between the Buckets


# Display MetaObjects


# Pre-Signed Url
