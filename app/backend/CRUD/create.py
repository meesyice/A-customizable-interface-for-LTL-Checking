from app import app
from werkzeug.utils import secure_filename
from flask import flash
import os


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
    