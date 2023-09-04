from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.secret_key = "Secret Key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:codilar@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    grade = db.Column 
    section = db.Column  

@app.route('/signup')
def render_signup():
    return render_template('signup.html')

@app.route('/register', methods = ['POST'])
def insert():
    if request.method == 'POST':
        username = request.form['name']
        email = request.form['email']
        user = Data.query.filter_by(username=username).first()
        if user and user.email == email:
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('hello_world'))
        else:
            my_data = Data(username=username, email=email)
            db.session.add(my_data)
            db.session.commit()
            flash('Data inserted successful!', 'success')

    return redirect(url_for('hello_world'))
@app.route('/login')
def insertData():
    my_data = Data(username="viveksdf", email="vivsadaek@gmail.com")
    db.session.add(my_data)
    db.session.commit()

@app.route('/')
def hello_world():
    return render_template('home.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
