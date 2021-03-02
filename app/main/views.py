from app import app, db
from app.model import User, Todos, Timer, Feedbacks
from flask import render_template, redirect, url_for, session, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

@main.route('/')
def index():
    return render_template('index.html')

def getTodos():
    todos = Todos.query.filter_by(username = current_user.username).all()

    for todo in todos:
        if todo.completed:
            todo.completed = 'Done'
        else:
            todo.completed = 'Pending'
        todo.create_date = str(todo.create_date)
        todo.create_date = todo.create_date[0:10]

        todos.sort(key = lambda x: x.completed, reverse = True)
    
        return todos