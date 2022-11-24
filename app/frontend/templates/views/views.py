from app import app
from flask import render_template, request, redirect, flash, send_file, after_this_request
from werkzeug.utils import secure_filename
from pm4py import write_xes, read_xes
import os

from app.backend.ltlcalls import apply_filter, choose_filter

@app.route('/')
@app.route('/index')
def index():
    files = os.listdir(app.config['UPLOAD_DIRECTORY'])
    return render_template('index.html', files = files)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['datei']
    ltl_rule = request.form['LTL_rule']
    events = request.form.getlist('activity')
    print(events)
    file_type = os.path.splitext(file.filename)[1]
    if file_type.lower() not in app.config['ALLOWED_FILE_TYPE']:
        flash("Please upload a XES file")
    else:
        file_path = os.path.join(app.config['UPLOAD_DIRECTORY'], secure_filename('result.xes'))
        file.save(file_path)
     
    filterd_log = apply_filter(read_xes(file_path), choose_filter(ltl_rule), events)
    write_xes(filterd_log, file_path)
    
    return redirect('/')

@app.route('/<path:path>')
def content(path):
    with open(path, "r") as f: 
        content = f.read() 
        return render_template("content.html", content=content) 
    
@app.route('/downloads/<file>', methods=['GET', 'POST'])
def downloads(file):
    @after_this_request
    def delete(response):
        os.remove(os.path.join(app.config['UPLOAD_DIRECTORY'], file))
        return response
    return send_file(os.path.join('imported_files', file))
