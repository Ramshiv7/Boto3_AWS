import boto3

dynamodb = boto3.client("dynamodb")

# Create a DynamoDB Table
create_response = dynamodb.create_table(
    TableName="crc_test",
    KeySchema=[{"AttributeName": "user", "KeyType": "HASH"}],
    AttributeDefinitions=[
        {"AttributeName": "user", "AttributeType": "S"},
    ],
    BillingMode="PAY_PER_REQUEST",
)

# Add Initial Data to the Table
data_response = dynamodb.put_item(
    TableName="crc_test", Item={"user": {"S": "visitor"}, "count": {"N": "0"}}
)


# Retrieve Data Using Primary Key
data_response = dynamodb.get_item(TableName="crc_test", Key={"user": {"S": "visitor"}})
print(data_response["Item"])


# Update Data in the Table
update_response = dynamodb.put_item(
    TableName="crc_test",
    Item={"user": {"S": "visitor"}, "count": {"N": "1"}},
)


# Delete Data from the Table
del_response = dynamodb.delete_item(
    TableName="crc_test", Key={"user": {"S": "visitor"}}
)


# Delete the DynamoDB Table
delete_response = dynamodb.delete_table(TableName="crc_test")
