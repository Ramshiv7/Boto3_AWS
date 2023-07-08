import boto3

dynamodb = boto3.client('dynamodb')

UserTable = dynamodb.create_table()