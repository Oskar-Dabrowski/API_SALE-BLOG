from flask import Flask, jsonify
from asgiref.wsgi import WsgiToAsgi

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask Vercel API - Working!", 200

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"status": 404, "message": "Not Found"}), 404

# Convert WSGI app to ASGI app
asgi_app = WsgiToAsgi(app)
