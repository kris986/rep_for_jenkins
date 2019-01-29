import os

from app import create_app
from flask_heroku import Heroku


app = create_app(os.getenv('FLASK_CONFIG') or 'dev')
if __name__ == "__main__":
    app.run()
