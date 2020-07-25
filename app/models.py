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

    @classmethod
    def create_element(cls, username, password, email):
        user = User(username=username, password=password, email=email)

        db.session.add(user)
        db.session.commit()

        return user

    @classmethod
    def get_by_username(cls, username):
        return User.query.filter_by(username=username).first()

    @classmethod
    def get_by_email(cls, email):
        return User.query.filter_by(email=email).first()

