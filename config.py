CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]
UPLOADED_PHOTOS_DEST = "static/users_files"
# IMAGES = set(['png', 'jpg', 'jpeg', 'gif'])
DB_HOST = 'ec2-54-247-82-210.eu-west-1.compute.amazonaws.com'
DB_NAME = 'dfqtsqais64fjm'
DB_USER = 'yxiqyvzagxrdjm'
DB_PORT = 5432
DB_PASSWORD = 'c003c5e23a420aa307286620861d89d3929319c8f8c21d041c3fb6b30f5fc71f'
DB_URL = 'postgresql-parallel-30170'
DB_URI = 'postgres://yxiqyvzagxrdjm:c003c5e23a420aa307286620861d89d3929319c8f8c21d041c3fb6b30f5fc71f@ec2-54-247-82-210.eu-west-1.compute.amazonaws.com:5432/dfqtsqais64fjm'