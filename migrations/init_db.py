from app.database import Base, engine
from app.models.user import User
from app.models.message import Message
from app.models.conversation import Conversation
from app.models.contact import Contact
from app.models.usergroup import UserGroup

def init_db():
    Base.metadata.create_all(bind=engine)