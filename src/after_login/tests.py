from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user

from src import db
from src.import_db.tables import Contents

tests = Blueprint('tests', __name__)


@tests.route('/tests', methods=['GET', 'POST'])
@login_required  # toto to musi obsahovat.
def main_tests():
    return render_template('tests/tests.html', user=current_user)


@tests.route('/test1', methods=['GET', 'POST'])
@login_required
def test_num01():
    pocet_spravnych_odpovedi = 0

    question_1 = request.form.get('question1')
    question_2 = request.form.get('question2')

    if request.method == 'POST':
        if question_1 == 'answer1':
            print('tvoja odpoved je spravna')
            pocet_spravnych_odpovedi = pocet_spravnych_odpovedi + 1
        else:
            print('tvoja odpoved je nespravna')

        if question_2 == 'answer2':
            print('tvoja odpoved je spravna')
            pocet_spravnych_odpovedi = pocet_spravnych_odpovedi + 1
        else:
            print('tvoja odpoved je nespravna')

        finale = pocet_spravnych_odpovedi / 2 * 100
        print('presmerovany na homepage/ test bol odoslany')
        print('vysledok testu je :', finale)

        test_answers = Contents(test1=finale, user_id=current_user.id)
        db.session.add(test_answers)
        db.session.commit()

        print('data boli uspesne ulozene')
        return redirect(url_for('views.home', user=current_user))

    return render_template('tests/test_01.html', user=current_user)
