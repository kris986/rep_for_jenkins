from app import app
from app.db.connect_web import ConnectDataBase
from flask import Flask, request


from_db = ConnectDataBase()


def is_production():
    """ Determines if app is running on the production server or not.
    Get Current URI.
    Extract root location.
    Compare root location against developer server value 127.0.0.1:5000.
    :return: (bool) True if code is running on the production server, and False otherwise.
    """
    root_url = request.url_root
    # developer_url = 'http://127.0.0.1:5000/'
    return root_url


def list_of_sex_nms():
    tuples_sex_nms = from_db.select_sex()
    list_of_sex_nm = list()
    for item in tuples_sex_nms:
        list_of_sex_nm.append((''.join(item)).strip())
    return list_of_sex_nm
