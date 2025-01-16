from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from app.database import get_db
from app.models.conversation import Conversation
from pydantic import BaseModel
from typing import List

router = APIRouter()

class ConversationBase(BaseModel):
   user_id: int
   participants: list
   friend_id: int

class ConversationResponse(ConversationBase):
   id: int
   timestamp_created: datetime

   class Config:
       from_attributes = True

@router.get("/conversations", response_model=List[ConversationResponse])
def get_conversations(db: Session = Depends(get_db)):
   return db.query(Conversation).all()

@router.get("/conversations/{id}", response_model=ConversationResponse)
def get_conversation(id: int, db: Session = Depends(get_db)):
   conversation = db.query(Conversation).get(id)
   if not conversation:
       raise HTTPException(status_code=404, detail="Conversation not found")
   return conversation

@router.post("/conversations", status_code=201)
def add_conversation(conversation: ConversationBase, db: Session = Depends(get_db)):
   new_conversation = Conversation(**conversation.dict(), timestamp_created=datetime.utcnow())
   db.add(new_conversation)
   db.commit()
   return {"message": f"Conversation {new_conversation.id} created successfully!"}

@router.delete("/conversations/{id}")
def delete_conversation(id: int, db: Session = Depends(get_db)):
   conversation = db.query(Conversation).get(id)
   if not conversation:
       raise HTTPException(status_code=404, detail="Conversation not found")
   
   db.delete(conversation)
   db.commit()
   return {"message": f"Conversation {id} deleted successfully"}