from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Message(Base):
   __tablename__ = 'messages'

   id = Column(Integer, primary_key=True)
   user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
   content = Column(String(500), nullable=False)
   is_editted = Column(Boolean, nullable=False, default=False)
   timestamp_created = Column(DateTime, nullable=False, default=datetime.utcnow)
   timestamp_editted = Column(DateTime, nullable=True)

   # Add relationship to User
   user = relationship("User", back_populates="messages")

   def __repr__(self):
       return f'<Message {self.id}>'