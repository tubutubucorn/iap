#!/usr/local/bin/python
import csv
from server import create_app, db
from server.models import User
from werkzeug.security import generate_password_hash

app = create_app()
with app.app_context():
    db.create_all()

with open('csv/User.csv') as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        if not i==0:
            with app.app_context():
                u = User(name=row[0], password=generate_password_hash(row[1], method='sha256'), email=row[2], role=row[3])
                db.session.add(u)
                db.session.commit()