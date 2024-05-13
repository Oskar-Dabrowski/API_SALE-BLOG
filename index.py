from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask Vercel API - Working!", 200

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"status": 404, "message": "Not Found"}), 404

# Vercel expects an ASGI or WSGI application for serverless Python functions
def app(environ, start_response):
    response_body = b'Hello world from Flask!\n'
    status = '200 OK'
    start_response(status, headers=[('Content-Type', 'text/plain')])
    return [response_body]
