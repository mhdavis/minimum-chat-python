from datetime import datetime
from app.models.database import db
from app.models.user import User

# Many-to-Many relation between User and UserGroup
user_group_association = db.Table('user_group_association',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('group_id', db.Integer, db.ForeignKey('user_group.id'))
)

class UserGroup(db.Model):
    __tablename__ = 'user_group'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(256), nullable=True)
    timestamp_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    # Establishing the many-to-many relationship with User model
    members = db.relationship('User', secondary=user_group_association, backref=db.backref('groups', lazy='dynamic'))

    def __repr__(self):
        return '<UserGroup: {}>'.format(self.name)