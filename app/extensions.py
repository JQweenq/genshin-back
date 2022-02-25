from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
#from flask_login import LoginManager

db: SQLAlchemy = SQLAlchemy()
bcrypt: Bcrypt = Bcrypt()
# login: LoginManager = LoginManager()


def setupExtensions(app: Flask) -> None:
    db.init_app(app)
    bcrypt.init_app(app)
    # login.init_app(app)
