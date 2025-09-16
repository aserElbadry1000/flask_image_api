from flask import Blueprint, request, redirect, url_for
from PIL import Image
from helpers import get_secure_filename_filepath
bp = Blueprint('actions', __name__, url_prefix='/actions')



@bp.route('/resize', methods=['POST'])
def resize():
    filename = request.json['filename']
    filename, filepath = get_secure_filename_filepath(filename)
    try:
        width = int(request.json['width'])
        height = int(request.json['height'])
        image = Image.open(filepath)
        out = image.resize((width, height))
        out.save(filepath)
        return redirect(url_for('download_file', filename=filename))

    except FileNotFoundError:
        return {'error': 'File not found'}, 404

@bp.route('/presets/<preset_name>', methods=['POST'])
def preset(preset_name):
    presets = {
        'thumbnail': (150, 150),
        'small': (320, 240),
        'medium': (640, 480),
        'large': (1024, 768)
    }
    if preset_name not in presets:
        return {'error': 'Preset not found'}, 404
    filename = request.json['filename']
    filename, filepath = get_secure_filename_filepath(filename)
    try:
        size = presets[preset_name]
        image = Image.open(filepath)
        out = image.resize(size)
        out.save(filepath)
        return redirect(url_for('download_file', filename=filename))
    except FileNotFoundError:
        return {'error': 'File not found'}, 404

@bp.route('/rotate', methods=['POST'])
def rotate():    
    filename = request.json['filename']
    filename, filepath = get_secure_filename_filepath(filename)
    try:
        angle = float(request.json['angle'])
        image = Image.open(filepath)
        out = image.rotate(angle)
        out.save(filepath)
        return redirect(url_for('download_file', filename=filename))

    except FileNotFoundError:
        return {'error': 'File not found'}, 404

@bp.route('/flip', methods=['POST'])
def flip():
    filename = request.json['filename']
    filename, filepath = get_secure_filename_filepath(filename)
    try:
        image = Image.open(filepath)
        out =  None
        if request.json['direction'] == 'horizontal':
            out = image.transpose(Image.FLIP_TOP_BOTTOM)
        elif request.json['direction'] == 'vertical':
            out = image.transpose(Image.FLIP_LEFT_RIGHT)
        if out:
            out.save(filepath)
            return redirect(url_for('download_file', filename=filename))
    except FileNotFoundError:
        return {'error': 'File not found'}, 404
