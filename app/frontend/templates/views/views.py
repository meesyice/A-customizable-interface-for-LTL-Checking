from app import app
from flask import render_template, request, send_file, after_this_request, redirect
import os

from app.backend.CRUD.create import saveFile
from app.backend.CRUD.update import writeFile

@app.route('/')
@app.route('/index')
def index():
    files = os.listdir(app.config['UPLOAD_DIRECTORY'])
    return render_template('index.html', files = files)



"""
Takes a file uploaded by the user and applies the filter chosen by the user to it using arguments provided by the user.
"""
@app.route('/upload', methods=['POST'])
def upload():
    file_path = saveFile(request.files['datei'])
    if not file_path:
        return redirect('/')
    else:
        writeFile(file_path)
    return redirect('/result', code=307)


"""
Download the processed file and delete it after the file download is complete
"""
@app.route('/result', methods=['POST'])
def download():
    @after_this_request
    def delete(response):
        os.remove(os.path.join(app.config['UPLOAD_DIRECTORY'], 'result.xes'))
        return response
    return send_file(os.path.join('imported_files', 'result.xes'))

