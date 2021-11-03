from flask import Blueprint, render_template
from flask_login import login_required, current_user

lectures = Blueprint('lectures', __name__)


@lectures.route('/lectures')
@login_required
def main_lectures():
    return render_template('lectures/lectures.html', user=current_user)

@lectures.route('/lecture1')
@login_required
def lecture_num1():
    return render_template('lectures/lecture_01.html',user=current_user)


