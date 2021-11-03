from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from src import db
from src.import_db.tables import User

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))

            else:

                flash('Incorrect password try again.', category='error')
        else:

            flash('This email does not exist.', category='error')

    return render_template("before_login/login.html", user=current_user)


# login##########################################################################################

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


# logout##########################################################################################

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already in use.', category='error')
        elif len(email) < 4:
            flash('Email must be longer thant 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be longer than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be longer thant 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))  # sha je hashing alghoritm
            db.session.add(new_user)
            db.session.commit()  # 'potvrdenie'
            login_user(new_user, remember=True)
            flash('Account successfully created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("before_login/register.html",
                           user=current_user)
