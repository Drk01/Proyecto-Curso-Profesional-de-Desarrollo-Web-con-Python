from flask import Flask
from .views import page

app = Flask(__name__)


def createApp(config):
    app.config.from_object(config)
    app.register_blueprint(page)
    return app
