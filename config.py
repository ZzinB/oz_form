from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/mini_form"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = 10
    SQLALCHEMY_POOL_TIMEOUT = 5
    SQLALCHEMY_POOL_RECYCLE = 1800
    SQLALCHEMY_MAX_OVERFLOW = 5
    SQLALCHEMY_ECHO = False
    reload = True