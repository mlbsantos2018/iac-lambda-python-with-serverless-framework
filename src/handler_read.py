import json
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ItemsTable')

def read(event, context):
    item_id = event['pathParameters']['id']
    try:
        result = table.get_item(Key={'id': item_id})
        if 'Item' in result:
            response = {
                "statusCode": 200,
                "body": json.dumps(result['Item'])
            }
        else:
            response = {
                "statusCode": 404,
                "body": json.dumps({"error": "Item not found"})
            }
    except ClientError as e:
        response = {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
    return response
