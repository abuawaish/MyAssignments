from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from app import mongo
from app.forms import SignupForm, SigninForm
from werkzeug.security import generate_password_hash, check_password_hash

main = Blueprint('main', __name__)

@main.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        users = mongo.db.users
        existing_user = users.find_one({'email': form.email.data})

        if existing_user is None:
            hashpass = generate_password_hash(form.password.data)
            users.insert_one({
                'name': form.name.data,
                'email': form.email.data,
                'password': hashpass
            })
            flash('Signup successful! Please login.')
            return redirect(url_for('main.signin'))
        flash('Email address already exists.')
    return render_template('signup.html', form=form)

@main.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SigninForm()
    if form.validate_on_submit():
        users = mongo.db.users
        login_user = users.find_one({'email': form.email.data})

        if login_user and check_password_hash(login_user['password'], form.password.data):
            session['user'] = login_user['name']
            return redirect(url_for('main.dashboard'))

        flash('Invalid email/password combination')
    return render_template('signin.html', form=form)

@main.route('/dashboard')
def dashboard():
    if 'user' in session:
        return f"Hello Geeks, {session['user']}!"
    return redirect(url_for('main.signin'))

@main.route('/signout')
def signout():
    session.pop('user', None)
    return redirect(url_for('main.signin'))
