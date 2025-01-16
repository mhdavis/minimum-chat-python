from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, ARRAY
from sqlalchemy.orm import relationship
from app.database import Base

class Conversation(Base):
   __tablename__ = 'conversations'

   id = Column(Integer, primary_key=True)
   conversation_name = Column(String, nullable=False)
   user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
   participants = Column(ARRAY(Integer), nullable=False)
   friend_id = Column(Integer, ForeignKey('users.id'), nullable=False)
   is_editted = Column(Boolean, nullable=False, default=False)
   timestamp_created = Column(DateTime, nullable=False, default=datetime.utcnow)
   timestamp_editted = Column(DateTime, nullable=True)

   # Add relationships
   user = relationship("User", foreign_keys=[user_id], back_populates="conversations")
   friend = relationship("User", foreign_keys=[friend_id])

   def __repr__(self):
       return f'<Conversation {self.conversation_name}>'