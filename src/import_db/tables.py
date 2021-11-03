
from flask_login import UserMixin
from sqlalchemy.sql import func

#from run import app
from src import db

#admin = Admin(app)


class Contents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    test1 = db.Column(db.String(10000))
    test2 = db.Column(db.String(10000))
    test3 = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


#admin.add_view(ModelView(Contents, db.session))


class User(db.Model, UserMixin):  # implementacia metod pre flask login
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Contents')

# class Tests(db.Model):
#   id = db.Column(db.String(10), primary_key=True)
#  test1 = db.Column(db.String(10))
# test2 = db.Column(db.String(10))
# date = db.Column(db.DateTime(timezone=True), default=func.now())
# user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
