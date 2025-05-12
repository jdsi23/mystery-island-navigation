# app.py
from flask import Flask, send_from_directory, jsonify
import os
import json

app = Flask(__name__, static_folder='webapp', static_url_path='')

@app.route('/')
def serve_index():
    return send_from_directory('webapp', 'index.html')

@app.route('/<path:path>')
def serve_static_file(path):
    return send_from_directory('webapp', path)

@app.route('/data/attractions.json')
def serve_attractions():
    with open('data/attractions.json') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
