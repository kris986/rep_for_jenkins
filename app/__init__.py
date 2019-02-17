from flask import Flask
from flask_uploads import UploadSet, IMAGES, configure_uploads
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration


sentry_sdk.init(
    dsn="https://17882f9f9064472698e0f6b35210e1cf@sentry.io/1395740",
    integrations=[FlaskIntegration()]
)
app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config.from_object('config')
photos = UploadSet('photos', IMAGES)
# app.config['UPLOADED_PHOTOS_DEST'] = 'users_files'
configure_uploads(app, photos)


    # @property
    # def imgsrc(self):
    #     return photos.url(self.filename)

    # all = ViewField('photolog', '''\
    #     function (doc) {
    #         if (doc.doc_type == 'post')
    #             emit(doc.published, doc);
    #     }''', descending=True)


# end of uploading
from app import views
