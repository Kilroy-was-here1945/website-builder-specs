from flask import Flask
from os import path
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
DB_NAME = "database.db"


# Your app flask name & secret key
SECRET_KEY = os.urandom(32)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://dalli:December!999@localhost:5432/database.db'
print(SECRET_KEY)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dalli:December!999@localhost:5432/database.db'
app.config['SECRET_KEY'] = SECRET_KEY



# from (name of data base) import (name of data base)
# from (name of data base) import (name of data base) -- if you have multiple one create more imports


app.register_blueprint('database', url_prefix='/')
app.register_blueprint('database', url_prefix='/')

from database import User#,  (name)


login_manager = LoginManager()
login_manager.login_databasename = 'data base + login name'# -- example(database.login)
print(login_manager.login_databasename)
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

    return app
#[10:40 AM]
def create_database(app):
    if not path.exists('./testcap/' + DB_NAME):
        db.create_all(app=app)
        print('Database')


