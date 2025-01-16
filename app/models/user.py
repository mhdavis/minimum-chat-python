from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from passlib.context import CryptContext
from app.database import Base

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, unique=True)
    first_name = Column(String(500), nullable=False)
    last_name = Column(String(500), nullable=False)
    username = Column(String(64), nullable=False, unique=True)
    email = Column(String(120), nullable=False, unique=True)
    timestamp_created = Column(DateTime, nullable=False, default=datetime.utcnow)
    password_hash = Column(String(128))

    def set_password(self, password):
        self.password_hash = pwd_context.hash(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def __repr__(self):
        return f'<User {self.username}>'