from flask import Flask
from actions import bp as actions_bp
from android import bp as android_bp
from filters import bp as filters_bp
app = Flask(__name__)

app.secret_key = 'SECRET_KEY'

app.register_blueprint(actions_bp)
app.register_blueprint(android_bp)
app.register_blueprint(filters_bp)