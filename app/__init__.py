from flask import Flask

app = Flask(__name__, template_folder='./frontend/templates', static_folder='./frontend/static')
app.config['UPLOAD_DIRECTORY'] = 'app/import_files'

from app.frontend.templates.views import views