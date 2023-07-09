import boto3


dynamodb = boto3.client("dynamodb")


# Create a DynamoDB Table

response = dynamodb.create_table(
    TableName="Ramshiv_test",
    AttributeDefinitions=[
        {"AttributeName": "user", "AttributeType": "S"},
        {"AttributeName": "count", "AttributeType": "N"},
    ],
    KeySchema=[
        {"AttributeName": "user", "KeyType": "HASH"},
      #  {"AttributeName": "count", "KeyType": "RANGE"},
    ],
    BillingMode="PAY_PER_REQUEST",
)


# Insert data into DynamoDB

insert_data = dynamodb.put_item(
    TableName="Ramshiv_test", Item={"user": {"S": "default"}, "count": {"N": "0"}}
)

insert_data = dynamodb.put_item(
    TableName="Ramshiv_test", Item={"user": {"S": "test"}, "count": {"N": "1"}}
)

response_value = insert_data

print(response_value)


# Read from the DynamoDB
data_response = dynamodb.get_item(
    TableName="Ramshiv_test", Key={"user": {"S": "test"}, "count": {"N": "1"}}
)

print(data_response)


# Delete the Table

response = dynamodb.delete_table(TableName="Ramshiv_test")

print(response)
