from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config.from_object('config.Config')
    db.init_app(app)
    Session(app)

    from .main import main
    app.register_blueprint(main)
    return app