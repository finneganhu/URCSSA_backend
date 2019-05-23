import json, os, logging, time
from api import decimalencoder

import boto3
dynamodb = boto3.resource('dynamodb')

def update(event, context):
    data = json.loads(event['body'])
