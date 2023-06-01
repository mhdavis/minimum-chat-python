from flask import Flask
from .main.routes import main
from .users.routes import users 
from .messages.routes import messages

def create_app():
    app.config.from_object('app.config.Config')
    app = Flask(__name__)

    # Register the users blueprint
    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(messages)

    return app