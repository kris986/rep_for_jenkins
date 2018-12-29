import psycopg2
from flask import render_template, redirect, request, session, url_for
from app import app
from app.users import DataUser
from app.db.connect_web import ConnectDataBase

data_user = DataUser()
from_db = ConnectDataBase()


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
    return render_template("index.html",
                           title='Home',
                           user=test_user,
                           posts=posts)


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
            # data_user.login_user(user_name=user_name, password=password)
            session['user_name'] = user_name
            print(session['user_name'])
            return redirect(url_for('personal_page', username=user_name))
    return render_template('login.html')


@app.route('/my-page')
def personal_page():
    username = session['user_name']
    city = from_db.parse_users()[username]['city']
    return render_template('personal_page.html',
                           username=username,
                           city=city)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


@app.route('/logout')
def logout():
    data_user.logout_user()
    return redirect(url_for('index'))


def registration(user_name, user_email, password, city=None):
    try:
        from_db.insert_user_in_db(user_name, user_email, password, city)
    except psycopg2.Error as e:
        print(e.pgerror)
        return render_template('registration.html', error=e.pgerror)
    return render_template('personal_page.html',
                           user_name=user_name,
                           city=city)


@app.route('/registration', methods=['GET', 'POST'])
def registration_page():
    # for registration user on app bd
    error = None
    if request.method == 'POST':
        user_name = request.form['username']
        user_email = request.form['email']
        password = request.form['password']
        city = request.form['city']
        return registration(user_name, user_email, password, city)
    return render_template('registration.html', error=error)


app.secret_key = 'test'
