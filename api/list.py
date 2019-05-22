import json, os
from api import decimalencoder

import boto3
dynamodb = boto3.resource('dynamodb')

def list(event, context):
    table = dynamodb.Table(os.environ['PROFESSORS_TABLE'])

    result = table.scan()

    res = {
        "statusCode": 200,
        "body": json.dumps(
            result['Items'],
            cls = decimalencoder.DecimalEncoder
        )
    }

    return res
