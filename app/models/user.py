from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(500), nullable=False)
    last_name = db.Column(db.String(500), nullable=False)
    user_name = db.Column(db.String(500), nullable=False)
    timestamp_created = db.Column(db.DateTime, nullable=False)