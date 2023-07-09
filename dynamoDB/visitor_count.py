import boto3

dynamodb = boto3.client("dynamodb")

create_response = dynamodb.create_table(
    TableName="crc_test",
    KeySchema=[{"AttributeName": "user", "KeyType": "HASH"}],
    AttributeDefinitions=[
        {"AttributeName": "user", "AttributeType": "S"},
    ],
    BillingMode="PAY_PER_REQUEST"
)

# Add Initial Data to the Table

data_response = dynamodb.put_item(TableName="crc_test", Item={
"user":{"S":"visitor"},
"count": {"N":"0"}
}
)

# Read Data from the Table and Increment the Visitor Count

data_response = dynamodb.get_item(TableName="crc_test", Key={"user":{"S":"visitor"}})

print(data_response.keys())

print(data_response['Item'])

visited_count = int(data_response["Item"]["count"]["N"])

print(visited_count)

visited_count += 1 

print(f"You have Visited the page with Count : {visited_count}")

update_response = dynamodb.put_item(TableName="crc_test", Item={"user":{"S":"visitor"}, "count":{"N": f"{visited_count}"}})

print(update_response)
