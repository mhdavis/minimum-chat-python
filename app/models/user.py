from datetime import datetime
from database import db;

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    first_name = db.Column(db.String(500), nullable=False)
    last_name = db.Column(db.String(500), nullable=False)
    username = db.Column(db.String(64), nullable=False, unique=True)
    email=db.Column(db.String(120), nullable=False, unique=True)
    password_hash = db.Column(db.String(128))
    timestamp_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<User {}>'.format(self.username)  