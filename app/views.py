import os

import psycopg2
from flask import render_template, redirect, request, session, url_for, send_from_directory
from werkzeug.utils import secure_filename

from app import app
from app.users import DataUser
from app.db.connect_web import ConnectDataBase
from app.pets import DataPets
from app.other import list_of_sex_nms
from config import ALLOWED_EXTENSIONS

from_db = ConnectDataBase()
data_user = DataUser()
data_pets = DataPets()


@app.route('/')
@app.route('/index')
def index():
    test_user = {'nickname': 'Miguel'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    dogs = data_pets.parse_to_json(from_db.select_all_users_dogs())
    return render_template("index.html",
                           title='Home',
                           user=test_user,
                           posts=posts,
                           dogs=dogs)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user_name = request.form['username']
        password = request.form['password']
        if not data_user.login_user(user_name=user_name, password=password):
            error = 'Invalid username or password'
            return render_template('login.html', error=error)
        else:
            session['user_name'] = user_name
            return redirect_to_main_page()
    return render_template('login.html')


@app.route('/users_files/<filename>')
def uploaded_file(filename):
    some = send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
    print(some)
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/my-page', methods=['GET', 'POST'])
def personal_page():
    message = request.args.get('message')
    username = session['user_name']
    path_to_pic = None
    city = from_db.parse_users()[username]['city']
    dogs = data_pets.parse_to_json(from_db.select_users_dogs(username))
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            path_to_pic = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            print(path_to_pic)
            if file.save(path_to_pic):
                path_to_pic = uploaded_file(filename=filename)
    else:
        return render_template('personal_page.html',
                               path_to_pic=path_to_pic,
                               username=username,
                               city=city,
                               dogs=dogs,
                               message=message)
    return render_template('personal_page.html',
                           path_to_pic=path_to_pic,
                           username=username,
                           city=city,
                           dogs=dogs,
                           message=message)


@app.route('/add-dog', methods=['GET', 'POST'])
def form_for_adding_dog():
    if request.method == 'POST':
        owner = session['user_name']
        breed = request.form['breed']
        sex = request.form['sex']
        dog_bday = request.form['dog_bday']
        pet_name = request.form['pet_name']
        kennel = request.form['kennel']
        if data_pets.add_dog(owner=owner,
                             breed=breed,
                             sex=sex,
                             dog_bday=dog_bday,
                             pet_name=pet_name,
                             kennel=kennel):
            return redirect(url_for('personal_page', message='Success'))

    else:
        username = session['user_name']
        city = from_db.parse_users()[username]['city']
        sex_nms = list_of_sex_nms()
        breeds = data_pets.parse_to_json_breeds()
        return render_template('add_dog.html',
                               username=username,
                               city=city,
                               breeds=breeds,
                               sex_nms=sex_nms)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


def redirect_to_main_page():
    return redirect(url_for('index'))


@app.route('/logout')
def logout():
    data_user.logout_user()
    return redirect_to_main_page()


def registration(user_name, user_email, password, country=None, city=None):
    try:
        from_db.insert_user_in_db(user_name, user_email, password, country, city)
    except psycopg2.Error as e:
        return render_template('registration.html', error=e.pgerror)
    return redirect_to_main_page()


@app.route('/registration', methods=['GET', 'POST'])
def registration_page():
    # for registration user on app bd
    error = None
    if request.method == 'POST':
        user_name = request.form['username']
        user_email = request.form['email']
        password = request.form['password']
        country = request.form['country']
        city = request.form['city']
        return registration(user_name, user_email, password, country, city)
    return render_template('registration.html', error=error)


app.secret_key = 'test'
