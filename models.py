from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class Students(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    phone_no = db.Column(db.Integer)
    password = db.Column(db.String(60))
    user_role = db.Column(db.String(60))
    parent_phone =  db.Column(db.Integer)
    registratation_no = db.Column(db.Text)
    faculty_id = db.Column(db.Integer)

class Teachers(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(60))

class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    classno = db.Column(db.String(3))
    section = db.Column(db.Integer)
    marks = db.Column(db.String(60))
