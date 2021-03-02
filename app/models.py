from enum import unique
from app import db
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String(50), unique = True, nullable = False)
    password = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(50))

class Todos(db.MOdel):
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String(50))
    category = db.Column(db.String(50), nullable = True)
    description = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean(), default=False)
    create_date = db.Column(db.DateTime(), default=datetime.now())

class Timer(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(50))
    pomodoro_interval = db.Column(db.Integer())
    break_interval = db.Column(db.Integer())

class Feedbacks(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
	member_username = db.Column(db.String(50))
	feedback = db.Column(db.String(100))