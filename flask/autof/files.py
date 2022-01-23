import os.path
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from flask_autoindex import AutoIndex
from werkzeug.utils import secure_filename


files = Blueprint('files', __name__)
UPLOAD_FOLDER = os.path.abspath('autof/dir')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv'}
files_index = AutoIndex(files, os.path.curdir + '/autof/dir', add_url_rules=False)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@files.route('/files')
@files.route('/files/<path:path>')
@login_required
def autoindex(path='.'):
    return files_index.render_autoindex(path)

@files.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            return redirect(url_for('files.upload', filename=filename))
    return render_template('upload.html')
