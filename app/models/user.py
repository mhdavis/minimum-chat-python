from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from database import db;

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    first_name = db.Column(db.String(500), nullable=False)
    last_name = db.Column(db.String(500), nullable=False)
    username = db.Column(db.String(64), nullable=False, unique=True)
    email=db.Column(db.String(120), nullable=False, unique=True)
    timestamp_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username,
            'email': self.email,
            'timestamp_created': self.timestamp_created,
        }

    def __repr__(self):
        return '<User {}>'.format(self.username)  