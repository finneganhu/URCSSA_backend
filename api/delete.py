'''
delete a specific professor item with given Department and Name
'''

import os, json

import boto3
dynamodb = boto3.resource('dynamodb')

def delete(event, context):
    table = dynamodb.Table(os.environ['PROFESSORS_TABLE'])

    department = event['pathParameters']['department'].replace("%20", " ")
    name = event['pathParameters']['name'].replace("%20", " ")

    try:
        result = table.delete_item(
            Key = {
                'Department': department,
                'Name': name
            }
        )
    except ClientError as e:
        return e.response['Error']['Message']
    else:
        res = {
            "statusCode": 204
        }
        return res
