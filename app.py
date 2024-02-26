from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/info', methods=['GET'])
def get_info():
    return jsonify({'name': 'Moje API', 'version': '1.0'})

if __name__ == '__main__':
    app.run(debug=True)
