from flask import Blueprint, request
from PIL import Image

bp = Blueprint('actions', __name__, url_prefix='/actions')



@bp.route('/resize', methods=['POST'])
def resize():
    filename = request.json['filename']

@bp.route('/presets/<preset_name>', methods=['POST'])
def preset(preset_name):
    pass

@bp.route('/rotate', methods=['POST'])
def rotate():    
    pass

@bp.route('/flip', methods=['POST'])
def flip():
    pass

