'''
create a new professor item with given Department and Name
'''

import json, logging, os, uuid

import boto3
dynamodb = boto3.resource('dynamodb')

def create(event, context):
    data = json.loads(event['body'])
    if 'Department' not in data or 'Name' not in data:
        logging.error("Validation Failed")
        raise Exception("Information missing.")

    table = dynamodb.Table(os.environ['PROFESSORS_TABLE'])

    item = {
        'id': str(uuid.uuid1()),
        'Department': data['Department'],
        'Name': data['Name']
    }

    if 'info' in data:
        item['info'] = data['info']

    table.put_item(Item = item)

    res = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return res
