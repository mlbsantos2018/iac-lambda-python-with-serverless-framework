import json
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ItemsTable')

def create(event, context):
    body = json.loads(event['body'])
    item = {
        'id': body['id'],
        'nome': body['nome'],
        'idade': body['idade']
    }
    try:
        table.put_item(Item=item)
        response = {
            "statusCode": 200,
            "body": json.dumps({"message": "Item created successfully"})
        }
    except ClientError as e:
        response = {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
    return response
