from app import app
from flask import render_template, request, redirect
from werkzeug.utils import secure_filename
import os

@app.route('/')
@app.route('/index')
def index():
    files = os.listdir(app.config['UPLOAD_DIRECTORY'])
    return render_template('index.html', files = files)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['datei']
    file.save(os.path.join(app.config['UPLOAD_DIRECTORY'], secure_filename(file.filename)))
    return redirect('/index')

@app.route('/delete/<file>', methods=['POST','GET'])
def delete(file):
    os.unlink(os.path.join(app.config['UPLOAD_DIRECTORY'], secure_filename(file)))
    return redirect('/index')