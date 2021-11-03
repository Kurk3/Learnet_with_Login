from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user

from src.import_db.tables import User, Contents

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("after_login/home.html", user=current_user)


@views.route('/vysledky', methods=['GET', 'POST'])
@login_required
def vysledky():
    name_second_login = request.form.get('name')
    password_second_login = request.form.get('password')

    if request.method == 'POST':
        if name_second_login == "admin" and password_second_login == "admin":
            user_from_db = User.query.all()
            tests_from_db = Contents.query.all()

            print('uspesne si sa prihlasil')
            flash('Uspesne si sa prihlasil!', category='success')
            # presmerovanie na adresu az ked sa tento uzivatel znovu prihlasi.
            return render_template("after_login/table_of_tests.html", user=current_user, data=user_from_db,
                                   tests=tests_from_db)  # redirectne aktualneuzivatela

        else:
            print('nemas udaje k prihlaseniu')
            flash('Nemas udaje k zobrazeniu.', category='error')

    return render_template("after_login/second_login.html", user=current_user)
