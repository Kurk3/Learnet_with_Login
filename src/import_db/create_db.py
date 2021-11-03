from os import path

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "AppData"

def create_engine(app):
   app.config['SECRET_KEY'] = 'abcdefghfijklmnoprsqxyz'  # ked stranka ide do produkcie (heslo)
   app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql:///{DB_NAME}'  # ulozeny nazov databazy
   db.init_app(app)


def create_tables(app):
      print('table was created! ')
      db.create_all(app=app) #create all tables
