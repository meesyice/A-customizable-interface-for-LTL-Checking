from app import app
from flask import render_template, request, redirect
from werkzeug.utils import secure_filename
import os

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['datei']
    print(file)
    file.save(os.path.join('app/import_files/', secure_filename(file.filename)))
    return redirect('/index')