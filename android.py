from datetime import datetime
import shutil
from flask import Blueprint, jsonify, redirect, request, url_for, current_app
import os
from os.path import basename
from helpers import get_secure_filename_filepath
from PIL import Image
from zipfile import ZipFile

bp = Blueprint('android', __name__, url_prefix='/android')

ICON_SIZES = [29, 40, 57, 58, 60, 80, 87, 114, 120, 180, 1024]

@bp.route('/create_image', methods=['POST'])
def create_image():
    filename = request.json.get('filename')
    filename, filepath = get_secure_filename_filepath(filename)
    
    temp_folder = os.path.join(current_app.config['UPLOAD_FOLDER'], 'temp')
    os.makedirs(temp_folder, exist_ok=True)

    for size in ICON_SIZES:
        outfile = os.path.join(temp_folder, f'{size}.png')
        image = Image.open(filepath)
        out = image.resize((size, size))
        out.save(outfile, "PNG")

    now = datetime.now()
    timestamp = str(datetime.timestamp(now)).rsplit('.')[0]
    zipfilename = f'{timestamp}.zip'
    zipfilepath = os.path.join(current_app.config['UPLOAD_FOLDER'], zipfilename)
    with ZipFile(zipfilepath, 'w') as zipf:
        for foldername, subfoldernames, filenames in os.walk(temp_folder):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                zipf.write(file_path, basename(file_path))
        shutil.rmtree(temp_folder)
        return redirect(url_for('download_file', filename=zipfilename))
