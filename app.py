from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "Secret Key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:codilar@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

@app.route('/insert')
def insertData():
    my_data = Data(username="viveksdf", email="vivsadaek@gmail.com")
    db.session.add(my_data)
    db.session.commit()

@app.route('/')
def hello_world():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
