from flask import Flask


app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config.from_object('config')
app.config['UPLOADED_PHOTOS_DEST'] = 'users_files'

from app import views
