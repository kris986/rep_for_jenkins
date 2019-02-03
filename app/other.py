from app.db.connect_web import ConnectDataBase
from config import ALLOWED_EXTENSIONS

from_db = ConnectDataBase()


def list_of_sex_nms():
    tuples_sex_nms = from_db.select_sex()
    list_of_sex_nm = list()
    for item in tuples_sex_nms:
        list_of_sex_nm.append((''.join(item)).strip())
    return list_of_sex_nm


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

