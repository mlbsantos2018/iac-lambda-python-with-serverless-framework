import json
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ItemsTable')

def update(event, context):
    item_id = event['pathParameters']['id']
    body = json.loads(event['body'])
    try:
        table.update_item(
            Key={'id': item_id},
            UpdateExpression="set nome=:n, idade=:i",
            ExpressionAttributeValues={
                ':n': body['nome'],
                ':i': body['idade']
            },
            ReturnValues="UPDATED_NEW"
        )
        response = {
            "statusCode": 200,
            "body": json.dumps({"message": "Item updated successfully"})
        }
    except ClientError as e:
        response = {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
    return response
