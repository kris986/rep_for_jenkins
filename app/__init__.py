from flask import Flask


app = Flask(__name__, static_url_path='/users_files', static_folder='static')
app.config.from_object('config')
from app import views


def create_app():
    app = Flask(__name__, static_url_path='/users_files', static_folder='static')
    app.config.from_object('config')
    from app import views
