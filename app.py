import os
import boto3

from flask import Flask
app = Flask(__name__)

PROFESSORS_TABLE = os.environ['PROFESSORS_TABLE']
client = boto3.client('dynamodb')

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/users/<string:user_id>")
def get_user(user_id):
    res = client.get_item(
        TableName = PROFESSORS_TABLE,
        Key = {
            'userId': {'S': user_id}
        }
    )
    item = res.get('Item')
    if not item:
        return jsonify({'error': 'User does not exist'}), 404

    return jsonify({
        'userId': item.get('userId').get('S'),
        'name': item.get('name').get('S')
    })

@app.route("/users", methods = ["POST"])
def create_user():
    user_id = request.json.get('userId')
    name = request.json.get('name')
    if not user_id or not name:
        return jsonify({'error': 'Please provide userId and name'}), 400

    res = client.put_item(
        TableName = USER_TABLE,
        Item = {
            'userId': {'S': user_id},
            'name': {'S': name}
        }
    )

    return jsonify({
        'userId': user_id,
        'name': name
    })
