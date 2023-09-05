from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "Secret Key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:codilar@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(
    minutes=30)  # Set the session timeout to 30 minutes
db = SQLAlchemy(app)
app.app_context().push()

login_manager = LoginManager(app)

login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    # This function is called to load a user based on the user_id stored in the session
    return Students.query.get(int(user_id))


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


class Students(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(30))
    grade = db.Column(db.Integer)
    password = db.Column(db.String(60))


def getUser(email):  # verifying Email exist in database
    return Students.query.filter_by(email=email).first()


def is_active(self):
    return True  # You can customize this based on your requirements


def is_authenticated(self):
    return True  # You can customize this based on your requirements


@app.route('/signup')
def render_signup():  # Renders REGISTER page
    return render_template('signup.html')


@app.route('/')  # Renders HOME page
def home_page():
    return render_template('home.html')


@app.route('/register', methods=['POST'])  # registering the user
def insert():
    if request.method == 'POST':
        username = request.form['name']
        formemail = request.form['email']
        grade = request.form['grade']
        password = request.form['password']
        confirmpassword = request.form['confirmpassword']
        user = getUser(formemail)
        if user:
            flash('account already exist please login!', 'error')
            return redirect(url_for('home_page'))
        elif password != confirmpassword:
            flash('Invalid password!', 'error')
            return redirect(url_for('home_page'))

        else:
            my_data = Students(name=username, email=formemail,
                               grade=grade, password=password)
            db.session.add(my_data)
            db.session.commit()
            flash('Data inserted successful!', 'success')
            return redirect(url_for('home_page'))


@app.route('/login')  # Renders LOGIN page
def login_page():
    return render_template('login.html')


@app.route('/postlogin', methods=['POST'])  # verify user for LOGIN process
def postLogin():
    if (request.method == 'POST'):
        email = request.form['email']
        password = request.form['password']
        user = getUser(email)
        if (user and user.password == password):
            flash('Login successful!', 'success')
            login_user(user)
            return login_page()
        else:
            flash('Invalid Details!', 'error')
            return login_page()
    else:
        return render_template('home.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('login_page'))


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
