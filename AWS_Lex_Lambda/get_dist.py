import boto3
import json
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    client = boto3.resource("dynamodb")
    cityTable = client.Table('Cities')
    source = event['currentIntent']['slots']['source']
    destination = event['currentIntent']['slots']['destination']

    #query_result = cityTable.query(
    #    KeyConditionExpression=Key('source').eq(source) & Key('destination').eq(destination)
    #)
    query_result = cityTable.get_item(Key={'source':source, 'destination':destination})
    distance = query_result['Item']['distance']

    response = {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
                "contentType": "PlainText",
                "content": distance
            },
        }
    }
    return response

    