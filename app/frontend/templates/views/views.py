from glob import glob
from io import BytesIO
from zipfile import ZipFile
from app import app
from flask import render_template, request, send_file, after_this_request, redirect
import os
import pandas as pd

from app.backend.CRUD.create import saveFile
from app.backend.CRUD.update import writeFile

@app.route('/')
@app.route('/index')
def index():
    files = os.listdir(app.config['UPLOAD_DIRECTORY'])
    cases = pd.DataFrame()
    return render_template('index.html', files = files, cases = cases, isDebug = app.debug)



"""
Takes a file uploaded by the user and applies the filter chosen by the user to it using arguments provided by the user.
"""
@app.route('/upload', methods=['POST'])
def upload():
    file_path = saveFile(request.files['datei'])
    if not file_path:
        return redirect('/')
    else:
        cases, var = writeFile(file_path)
    return render_template('index.html', cases = cases, var = var, isDebug = app.debug)


"""
Download the processed file and delete it after the file download is complete
"""
@app.route('/result', methods=['POST'])
def download():
    @after_this_request
    def delete(response):
        try:
            os.remove(os.path.join(app.config['UPLOAD_DIRECTORY'], 'result.xes'))
        except PermissionError as error:
            print(error)
        return response
    stream = BytesIO()
    with ZipFile(stream, 'w') as zf:
        for file in glob(os.path.join(app.config['UPLOAD_DIRECTORY'], '*.xes')):
            zf.write(file, os.path.basename(file))
    stream.seek(0)
    return send_file(stream,
        as_attachment=True,
        download_name='archive.zip')

