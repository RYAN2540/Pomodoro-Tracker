from . import main
from .. import db
from ..models import User, Todos, Timer, Feedbacks
from flask import render_template, redirect, url_for, session, request, flash
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

@main.route('/pomodoro', methods = ['GET', 'POST'])
def pomodoro():
    if request.method == 'POST':
        inputTimerTarget = request.form['pomodoroInterval']
        inputBreakTarget = request.form['breakInterval']

        # Converyting tmes to minutes
        timeTarget = inputTimerTarget[3:]
        breakTarget = inputBreakTarget[3:]

        newTimerDetails = Timer(username = current_user.username, pomodoro_interval = timeTarget,
        break_interval = breakTarget)

        db.session.add(newTimerDetails)
        db.session.commit()

        todos = getTodos()

        return render_template('pomodoro.html', todos = todos, timeTarget = timeTarget, breakTarget = breakTarget,
        inputTimerTarget = inputTimerTarget, inputBreakTarget = inputBreakTarget)

    else:
        timerDetails = Timer.query.filter_by(username = current_user.username).first()
        todos = getTodos()
        if(timerDetails):
            inputTimerTarget = ('00:' + str(timerDetails.pomodoro_interval))
            inputBreakTarget = ('00:' + str(timerDetails.break_interval))

            return render_template('pomodoro.html', todo = todos, timerTarget = timerDetails.pomodoro_interval, breakTarget = timerDetails.break_interval,
            inputTimerTarget = inputTimerTarget, inputBreakTarget = inputBreakTarget)

        else:
            timerTarget = '25'
            breakTarget = '5'

            return render_template('pomodoro.html', todos = todos, timerTarget = timerTarget, breakTarget = breakTarget,
            inputTimerTarget = timerTarget, inputBreakTarget = breakTarget)

#todos manager
@main.route('/todos', methods = ['GET', 'POST'])
@login_required
def add_todo():
    if request.method =='POST':
        category = request.form['category']
        description = request.form['description']

        if category and (len(str(description).strip()) != 0):
            newTodo = Todos(username = current_user.username, category = category, description = description, completed = False)

            db.session.add(newTodo)
            db.session.commit()
            todos = getTodos()
            return redirect(url_for('todos', todos = todos))
        else:
            flash('Please enter complete details')
            return render_template(add_todo.html)
    else:
        return render_template('add_todo.html')

@main.route('/edit_todo/<int:id>', methods = ['GET' 'POST'])
@login_required
def edit_todo(id):
    editTodo = Todos.query.filter_by(id = id).first()
    if request.method == 'POST':
        editTodo.category = request.form['category']
        editTodo.description = request.form['description']

        if request.form['status'] == 'Done':
            editTodo.completed = True
        else:
            editTodo.completed = False
        db.session.commit()

        todos = getTodos()
        return redirect(url_for('todos', todos = todos))
    else:
        if editTodo and editTodo.user == current_user.username:
            return render_template('edit_todo.html', editTodo = editTodo)

@main.route('/delete_todo/<int:id>')
@login_required
def delete_todo(id):
    delTodo = Todos.query.filter_by(id = id).first()
    db.session.delete(delTodo)
    db.session.commit()
    todos = getTodos()

    return redirect(url_for('todos', todos = todos))