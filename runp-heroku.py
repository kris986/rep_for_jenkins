from app import run_app
from flask_heroku import Heroku


app = run_app()
Heroku(app=app)
