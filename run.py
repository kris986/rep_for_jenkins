#!flask/bin/python
from app import app
import config


app.run(port=9999, debug=True)
app.config['UPLOAD_FOLDER'] = config.UPLOAD_FOLDER
