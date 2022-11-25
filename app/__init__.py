import os
from flask import Flask

app = Flask(__name__, template_folder='./frontend/templates', static_folder='./frontend/static')

if not os.path.exists('app/imported_files/'):
    os.makedirs('app/imported_files/')
app.config['UPLOAD_DIRECTORY'] = 'app/imported_files'
app.config['ALLOWED_FILE_TYPE'] = ['.xes']
app.secret_key = 'flash_key'

from app.frontend.templates.views import views