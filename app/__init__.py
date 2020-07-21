from flask import Flask
from .views import page

app = Flask(__name__)


def createApp():
    app.register_blueprint(page)
    return app
