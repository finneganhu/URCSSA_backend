'''
query all professor items in the given Department
'''

import os, json
from api import decimalencoder
from boto3.dynamodb.conditions import Key

import boto3
dynamodb = boto3.resource('dynamodb')

def getProfs(event, context):
    table = dynamodb.Table(os.environ['PROFESSORS_TABLE'])

    department = event['pathParameters']['department'].replace("%20", " ")

    result = table.query(
        KeyConditionExpression = Key('Department').eq(department)
    )

    res = {
        "statusCode": 200,
        "body": json.dumps(
            result['Items'],
            cls = decimalencoder.DecimalEncoder
        )
    }

    return res
