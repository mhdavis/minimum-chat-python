from flask import Flask
from .main import main
from .users import users 
from .messages import messages

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Register the users blueprint
    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(messages)

    return app