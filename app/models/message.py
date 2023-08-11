from datetime import datetime
from database import db;

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    content = db.Column(db.String(500), nullable=False)
    is_editted = db.Column(db.Boolean, nullable=False, default=False)
    timestamp_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    timestamp_editted = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Message {}>'.format(self.username)  