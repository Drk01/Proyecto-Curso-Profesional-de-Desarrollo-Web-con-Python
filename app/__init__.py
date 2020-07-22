from flask import Flask
from .views import page
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from .models import User

app = Flask(__name__)
bootstrap = Bootstrap()
csrf = CSRFProtect()
db = SQLAlchemy()


def createApp(config):
    app.config.from_object(config)
    csrf.init_app(app)
    bootstrap.init_app(app)
    app.register_blueprint(page)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app
