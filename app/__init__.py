from flask import Flask

app = Flask(__name__, template_folder='./frontend/templates', static_folder='./frontend/static')
app.config['UPLOAD_DIRECTORY'] = 'app/import_files'
app.config['ALLOWED_FILE_TYPE'] = ['.xes']
app.secret_key = 'flash_key'

from app.frontend.templates.views import views