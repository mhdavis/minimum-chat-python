from datetime import datetime
from database import db;

class Conversation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    conversation_name = db.Column(db.String, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    participants = db.Column(db.Array, nullable=False)
    friend_id = db.Column(db.Integer, nullable=False)
    is_editted = db.Column(db.Boolean, nullable=False, default=False)
    timestamp_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    timestamp_editted = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Conversation {}>'.format(self.username)  