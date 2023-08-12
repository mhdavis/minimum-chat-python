from datetime import datetime
from database import db
from app.models.user import User

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    friend_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', foreign_keys=[user_id], backref=db.backref('contacts', lazy='dynamic'))
    friend = db.relationship('User', foreign_keys=[friend_id], backref=db.backref('friends_of', lazy='dynamic'))
    timestamp_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    __table_args__ = (db.UniqueConstraint('user_id', 'friend_id', name='unique_contact'),)
    
    def __repr__(self):
        return '<Contact: User {} - Friend {}>'.format(self.user_id, self.friend_id)