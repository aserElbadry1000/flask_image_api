from flask import Blueprint

bp = Blueprint('filters', __name__, url_prefix='/filters')

@bp.route('/grayscale', methods=['POST'])
def grayscale():
    pass
@bp.route('/blur', methods=['POST'])
def blur():
    pass
@bp.route('/contrast', methods=['POST'])
def contrast():   
    pass
@bp.route('/brightness', methods=['POST'])
def brightness():
    pass