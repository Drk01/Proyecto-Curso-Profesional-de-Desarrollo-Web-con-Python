from flask import Flask
from .views import page
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap()


def createApp(config):
    app.config.from_object(config)
    bootstrap.init_app(app)
    app.register_blueprint(page)
    return app
