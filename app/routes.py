from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

@main.route('/')
def hello_world():
    return 'Hello, World!'

@main.route('/api/info', methods=['GET'])
def get_info():
    return jsonify({'name': 'Moje API', 'version': '1.0'})