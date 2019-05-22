import json, logging, os

import boto3
dynamodb = boto3.resource('dynamodb')

def create(event, context):
    data = json.loads(event['body'])
    if 'Department' not in data or 'Name' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the professor item.")

    table = dynamodb.Table(os.environ['PROFESSORS_TABLE'])

    item = {
        'Department': data['Department'],
        'Name': data['Name']
    }

    table.put_item(Item = item)

    res = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return res
