import os

from flask import send_from_directory
from werkzeug.utils import secure_filename

from app import app
from app.db.connect_web import ConnectDataBase
from config import ALLOWED_EXTENSIONS, UPLOAD_FOLDER

from_db = ConnectDataBase()


def list_of_sex_nms():
    tuples_sex_nms = from_db.select_sex()
    list_of_sex_nm = list()
    for item in tuples_sex_nms:
        list_of_sex_nm.append((''.join(item)).strip())
    return list_of_sex_nm


def uploaded_file(filename):
    some = send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
    print(some)
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def save_file(filename):
    if allowed_file(filename):
        filename = secure_filename(filename)
        path_to_pic = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        # if file.save(path_to_pic):
        print(path_to_pic)

# save_file('eih8wtgho3cm.png')