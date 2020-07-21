from app import createApp
from flask_script import Manager
from config import config

config_class = config['development']
app = createApp(config_class)

if __name__ == '__main__':
    manager = Manager(app)
    manager.run()
