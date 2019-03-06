from flask import Flask
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration


sentry_sdk.init(
    dsn="https://17882f9f9064472698e0f6b35210e1cf@sentry.io/1395740",
    integrations=[FlaskIntegration()]
)
app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config.from_object('config')
app.config['UPLOADED_PHOTOS_DEST'] = 'users_files'


from app import views
