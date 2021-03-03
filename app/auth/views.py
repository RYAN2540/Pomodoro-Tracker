from werkzeug.security import generate_password_hash, check_password_hash
from flask import render_template, redirect, url_for, flash, request, session
from . import auth
from flask_login import login_user, logout_user, login_required
from ..models import User
from .forms import RegisterForm, LoginForm
from .. import db

# Login page
@auth.route('/login', methods=["GET", "POST"])
def login():
	form = LoginForm()

	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user:
			if check_password_hash(user.password, form.password.data):
				login_user(user, remember=form.remember.data)
				session['logged_in'] = True
				return redirect(url_for('pomodoro'))
		else:
			flash('Incorrect username or password. Please try again.', 'danger')

	return render_template('auth/login.html',form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been successfully logged out')
    return redirect(url_for('main.index'))


# user registration page
@auth.route('/register', methods=["GET", "POST"])
def register():
	form = RegisterForm()

	if form.validate_on_submit():
		# check if username already exists
		existingUser = User.query.filter_by(username=form.username.data).first()
		if existingUser:
			flash('Username already exists. Please enter a different username.', 'danger')
			return render_template('auth/register.html',form=form)
		else:
			hashed_password = generate_password_hash(form.password.data, method='sha256')
			new_user = User(username=form.username.data, password=hashed_password, email=form.email.data)
			db.session.add(new_user)
			db.session.commit()
			session['registrationRedirect'] = True
			return redirect(url_for('login'))
	else:
		return render_template('auth/register.html',form=form)