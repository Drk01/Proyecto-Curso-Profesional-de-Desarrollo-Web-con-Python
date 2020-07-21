from app import createApp
from flask_script import Manager


app = createApp()

if __name__ == '__main__':
    manager = Manager(app)
    manager.run()