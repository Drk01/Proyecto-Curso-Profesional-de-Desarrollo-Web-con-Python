from . import db
import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(93), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    created_ad = db.Column(db.Datetime, default=datetime.datetime.now())

    def __str__(self):
        return self.username

