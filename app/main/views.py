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