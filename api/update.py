import json, os, logging, time
from api import decimalencoder
from decimal import *

import boto3
dynamodb = boto3.resource('dynamodb')

def update(event, context):
    table = dynamodb.Table(os.environ['PROFESSORS_TABLE'])

    department = event['pathParameters']['department'].replace("%20", " ")
    name = event['pathParameters']['name'].replace("%20", " ")

    data = json.loads(event['body'])
    if 'Class' not in data or 'Rating' not in data or 'Comments' not in data:
        logging.error("Validation Failed")
        raise Exception("Information missing.")

    eval = {
        'Class': data['Class'],
        'Rating': Decimal(data['Rating']),
        'Comments': data['Comments']
    }

    result = table.update_item(
        Key = {
            'Department': department,
            'Name': name
        },
        # ExpressionAttributeNames = {
        #     '#list': 'Evaluations'
        # },
        UpdateExpression = 'SET Evaluations = list_append(Evaluations, :addItem)',
        ExpressionAttributeValues = {
            ':addItem': [eval]
        },
        ReturnValues = "UPDATED_NEW"
    )

    res = {
        "statusCode": 200,
        "body": json.dumps(
            result,
            cls = decimalencoder.DecimalEncoder
        )
    }

    return res
