from app import create_app
from flask_heroku import Heroku


app = create_app()
# Heroku(app)