from werkzeug.security import check_password_hash
from . import db 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    role = db.Column(db.String(100), nullable=False)
    last_login = db.Column(db.DateTime, nullable=True)

    def check_password(self, password):
        return check_password_hash(self.password, password)