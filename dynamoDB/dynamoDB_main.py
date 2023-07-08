import boto3


dynamodb = boto3.client("dynamodb")


# Create a DynamoDB Table
response = dynamodb.create_table(
    TableName="Ramshiv_test",
    AttributeDefinitions=[{"AttributeName": "user", "AttributeType": "S"}],
    KeySchema=[
        {"AttributeName": "user", "KeyType": "HASH"},
    ],
    BillingMode="PAY_PER_REQUEST",
)

print(response)
