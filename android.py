from flask import Blueprint

bp = Blueprint('android', __name__, url_prefix='/android')

@bp.route('/create_image', methods=['POST'])
def create_image():
    pass
