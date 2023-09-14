from flask import Flask, render_template
from flask_login import LoginManager
from datetime import timedelta
from models import db, Students
from controllers.auth_controller import auth_blueprint
from datetime import timedelta
from controllers.utils import getAllDetails
from flask_login import login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.secret_key = "Secret Key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:codilar@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

app.register_blueprint(auth_blueprint)


@login_manager.user_loader
def load_user(user_id):
    return Students.query.get(int(user_id))


@app.route('/')
def home_page():
    if current_user.is_authenticated:
        return render_template('home.html', data=getAllDetails)
    else:
        return render_template('home.html')


@app.route('/login')
def logIn():
    select_user_type = ["Students", "Teachers"]
    return render_template('login.html', select_choices=select_user_type)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
