#__init__.py
from flask import Flask
app = Flask(__name__)
UPLOAD_FOLDER = "flask_app/static/assets/user_images/"
app.secret_key = 'keepitsecretkeepitsafe'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024