from flask import Flask
from .main import main
from .users import users 
from .messages import messages
from dotenv import load_dotenv
from .models.database import db;

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Register the users blueprint
    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(messages)

    return app