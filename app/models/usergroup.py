from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

user_group_association = Table('user_group_association', Base.metadata,
   Column('user_id', Integer, ForeignKey('users.id')),
   Column('group_id', Integer, ForeignKey('user_groups.id'))
)

class UserGroup(Base):
   __tablename__ = 'user_groups'

   id = Column(Integer, primary_key=True)
   name = Column(String(128), nullable=False)
   description = Column(String(256), nullable=True)
   timestamp_created = Column(DateTime, nullable=False, default=datetime.utcnow)
   
   members = relationship('User', secondary=user_group_association, backref='groups')

   def __repr__(self):
       return f'<UserGroup: {self.name}>'