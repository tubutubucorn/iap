from dotenv import load_dotenv
from os import environ
load_dotenv('.env')

class Config:
    # General Config
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV') # development or production
    SECRET_KEY = environ.get('SECRET_KEY')

    # Flask-SQLAlchemy
    SQLALCHEMY_DATABASE_URI = environ.get('USERDB_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False