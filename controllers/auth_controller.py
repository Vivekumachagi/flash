from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from models import Students
from .utils import getUser

auth_blueprint = Blueprint('auth', __name__)


@auth_blueprint.route('/login', methods=['GET', 'POST'])
def postLogin():
    if current_user.is_authenticated:  # If the user is already logged in, you can redirect them to a different page
        return render_template('home.html')
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = getUser(email)
        if user and user.password == password:
            flash('Login successful!', 'success')
            login_user(user)
            return render_template('login.html')
        else:
            flash('Invalid Details!', 'error')
            return render_template('login.html')
    return render_template('login.html')


@auth_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['name']
        formemail = request.form['email']
        grade = request.form['grade']
        password = request.form['password']
        confirmpassword = request.form['confirmpassword']
        if not username or not formemail or not grade or not password or not confirmpassword:
            flash('Please fill in all the form fields.', 'error')
            return render_template('signup.html')
        user = getUser(formemail)
        if user:
            flash('Account already exists. Please login!', 'error')
            return render_template('login.html')
        elif password != confirmpassword:
            flash('Invalid password!', 'error')
            return render_template('signup.html')
        else:
            from app import db
            my_data = Students(name=username, email=formemail,
                               grade=grade,  password=password)
            db.session.add(my_data)
            db.session.commit()
            flash('Data inserted successfully!', 'success')
            return render_template('login.html')
    return render_template('signup.html')


@auth_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return render_template('login.html')


def getUser(email):
    return Students.query.filter_by(email=email).first()
