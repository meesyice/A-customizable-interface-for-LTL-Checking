from app import app
from flask import render_template, request, flash, send_file, after_this_request, redirect
from werkzeug.utils import secure_filename
from pm4py import write_xes, read_xes
import os

from app.backend.ltlcalls import apply_filter, choose_filter

@app.route('/')
@app.route('/index')
def index():
    files = os.listdir(app.config['UPLOAD_DIRECTORY'])
    return render_template('index.html', files = files)


"""
Save the uploaded file
"""
def saveFile(file):
    file_type = os.path.splitext(file.filename)[1]
    if file_type.lower() not in app.config['ALLOWED_FILE_TYPE']:
        flash("Please upload a XES file")
        return ""
    else:
        file_path = os.path.join(app.config['UPLOAD_DIRECTORY'], secure_filename('result.xes'))
        file.save(file_path)
        return file_path
    

"""
Apply LTL rules to process the file and overwrite the original file with the processed file
"""    
def writeFile(file_path):
    ltl_rule = request.form['LTL_rule']
    events = request.form.getlist('activity')
    filterd_log = apply_filter(read_xes(file_path), choose_filter(ltl_rule), events)
    write_xes(filterd_log, file_path)

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
    return redirect('/result')


"""
Download the processed file and delete it after the file download is complete
"""
@app.route('/result')
def download():
    @after_this_request
    def delete(response):
        os.remove(os.path.join(app.config['UPLOAD_DIRECTORY'], 'result.xes'))
        return response
    return send_file(os.path.join('imported_files', 'result.xes'))

