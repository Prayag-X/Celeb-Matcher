from flask import Flask, flash, request, redirect, url_for, render_template
import urllib.request
import os
import shutil
from werkzeug.utils import secure_filename
from Utilities import *
from Jina_app import *

app = Flask(__name__,template_folder='templates',static_folder='static')

UPLOAD_FOLDER = 'static/uploads/'

app.secret_key = "Is_this_required?"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_image():

    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = "upload"+os.path.splitext(secure_filename(file.filename))[1]
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        filename2=Jina_run(filename)
        shutil.copyfile(filename2, UPLOAD_FOLDER+"Predict.jpg")
        flash(heading(filename2))
        flash(wiki(filename2.split('/')[1]))
        return render_template('index.html', filename=filename, filename2="Predict.jpg")

    else:
        flash('Allowed image types are - png, jpg, jpeg')
        return redirect(request.url)



@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)


if __name__ == "__main__":
    app.run()