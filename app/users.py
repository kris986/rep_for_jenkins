from flask import request, session
from app.db.connect_web import ConnectDataBase

from_db = ConnectDataBase()


class DataUser:

    def __init__(self):
        pass

    def create_user(self):
        pass

    def valid_login(self, user_name, password):
        if user_name in from_db.parse_users():
            db_password = from_db.parse_users()[user_name]['password']
            return password == db_password
        else:
            return False

    def login_user(self, user_name, password):
        if self.valid_login(user_name, password):
            data_user = from_db.parse_users()[user_name]
            print(data_user)
            return data_user
        else:
            return False

    def get_user(self):
        from_db.parse_users()

    def update_user(self):
        pass

    def logout_user(self):
        session.pop('user_name')

    def delete_user(self):
        pass
