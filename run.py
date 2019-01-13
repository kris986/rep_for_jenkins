#!flask/bin/python
from app import app
import config
from werkzeug.utils import secure_filename

app.run(port=9999, debug=True)
app.config['UPLOAD_FOLDER'] = config.UPLOAD_FOLDER
