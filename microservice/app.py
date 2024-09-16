#!/usr/bin/python

import hashlib
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/md5', methods=['POST'])
def calculate_md5():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected for uploading'}), 400

    md5_hash = hashlib.md5()
    for chunk in iter(lambda: file.read(4096), b""):
        md5_hash.update(chunk)

    return jsonify({'md5_checksum': md5_hash.hexdigest()})

if __name__ == '__main__':
    app.run(debug=True)