from flask import request, session
from app.db.connect_web import ConnectDataBase
from kafka_integration import sending_msg_to_topic as to_topic


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
            print(data_user.get('user_email'))
            to_topic.send_msg('login', 'success', data_user.get('user_email'))
            return data_user
        else:
            to_topic.send_msg('login', 'fail', '{0}:{1}'.format(user_name, password))
            return False

    def get_user(self):
        from_db.parse_users()

    def update_user(self):
        pass

    def logout_user(self):
        print(session['user_name'])
        session.pop('user_name')

    def delete_user(self):
        pass
