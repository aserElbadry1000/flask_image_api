from flask import Flask, request, jsonify
from actions import bp as actions_bp
from android import bp as android_bp
from filters import bp as filters_bp

import os

from helpers import allowed_extension, get_secure_filename_filepath
app = Flask(__name__)

app.secret_key = 'SECRET_KEY'

ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS

app.register_blueprint(actions_bp)
app.register_blueprint(android_bp)
app.register_blueprint(filters_bp)

@app.route('/images/', methods=['POST'])
def upload_image():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        if not allowed_extension(file.filename):
            return jsonify({'error': 'File type not allowed'}), 400
        
        filename, filepath = get_secure_filename_filepath(file.filename)
        file.save(filepath)
        return jsonify({
            'message': 'File successfully uploaded',
            'filename': filename
        }), 201
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            return jsonify({'filename': file.filename}), 200