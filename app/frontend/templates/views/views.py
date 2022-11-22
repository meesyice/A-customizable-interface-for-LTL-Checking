from app import app
from flask import render_template, request, redirect

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['datei']
    print(file)
    file.save(f'app/import_files/{file.filename}')
    return redirect('/index')