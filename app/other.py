from flask import send_from_directory

from app import app
from app.db.connect_web import ConnectDataBase

from_db = ConnectDataBase()


def list_of_sex_nms():
    tuples_sex_nms = from_db.select_sex()
    list_of_sex_nm = list()
    for item in tuples_sex_nms:
        list_of_sex_nm.append((''.join(item)).strip())
    return list_of_sex_nm



