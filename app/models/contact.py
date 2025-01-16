from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from app.database import Base

class Contact(Base):
   __tablename__ = 'contacts'

   id = Column(Integer, primary_key=True)
   user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
   friend_id = Column(Integer, ForeignKey('users.id'), nullable=False)
   timestamp_created = Column(DateTime, nullable=False, default=datetime.utcnow)

   user = relationship('User', foreign_keys=[user_id], back_populates='contacts')
   friend = relationship('User', foreign_keys=[friend_id], back_populates='friends_of')

   __table_args__ = (UniqueConstraint('user_id', 'friend_id', name='unique_contact'),)

   def __repr__(self):
       return f'<Contact: User {self.user_id} - Friend {self.friend_id}>'