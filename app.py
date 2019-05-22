import os
import boto3

from flask import Flask, jsonify, request
app = Flask(__name__)

PROFESSORS_TABLE = os.environ['PROFESSORS_TABLE']
client = boto3.client('dynamodb')

@app.route("/")
def hello():
    return "Hello World!"

# Query all professors in a given department
# @app.route("/profs/<string:department_name>")
# def get_profs(department_name):
#     res = client.query(
#         TableName = PROFESSORS_TABLE,
#         KeyConditionExpression = Key('Department').eq({'S': department_name})
#     )
#     items = res.get('Items')
#     if not items:
#         return jsonify({
#             'error': 'No information of professors in this department'
#         }), 404
#     return items

# # Create a new professor with given name, department, and info
# @app.route("/profs", methods = ["POST"])
# def create_prof():
#     department = request.json.get('Department')
#     name = request.json.get('Name')
#     if not department or not name:
#         return jsonify({'error': 'Please provide department and name'}), 400
#     res = client.put_item(
#         TableName = PROFESSORS_TABLE,
#         Item = {
#             'Department': {'S': department},
#             'Name': {'S': name}
#         }
#     )
#     return jsonify({
#         'Department': department,
#         'Name': name
#     })

# # Get a professor by its name
# @app.route("/profs/<string:prof_name>")
# def get_user(user_id):
#     res = client.get_item(
#         TableName = PROFESSORS_TABLE,
#         Key = {
#             'Name': {'S': prof_name}
#         }
#     )
#     item = res.get('Item')
#     if not item:
#         return jsonify({'error': 'User does not exist'}), 404
#
#     return jsonify({
#         'userId': item.get('userId').get('S'),
#         'name': item.get('name').get('S')
#     })
