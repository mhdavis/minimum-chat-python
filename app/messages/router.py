from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from app.database import get_db
from app.models.message import Message
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

class MessageBase(BaseModel):
    user_id: int
    content: str

class MessageResponse(MessageBase):
    id: int
    timestamp_created: datetime
    is_editted: bool = False
    timestamp_editted: Optional[datetime] = None

    class Config:
        from_attributes = True

@router.get("/messages", response_model=List[MessageResponse])
def get_messages(db: Session = Depends(get_db)):
    return db.query(Message).all()

@router.get("/messages/{id}", response_model=MessageResponse)
def get_message(id: int, db: Session = Depends(get_db)):
    message = db.query(Message).get(id)
    if not message:
        raise HTTPException(status_code=404, detail="Message not found")
    return message

@router.post("/messages", status_code=201)
def add_message(message: MessageBase, db: Session = Depends(get_db)):
    new_message = Message(**message.dict(), timestamp_created=datetime.utcnow())
    db.add(new_message)
    db.commit()
    return {"message": f"Message {new_message.id} created successfully!"}

@router.put("/messages/{id}")
def update_message(id: int, content: str, db: Session = Depends(get_db)):
    message = db.query(Message).get(id)
    if not message:
        raise HTTPException(status_code=404, detail="Message not found")
    
    message.content = content
    message.is_editted = True
    message.timestamp_editted = datetime.utcnow()
    db.commit()
    return {"message": f"Message {id} updated successfully!"}

@router.delete("/messages/{id}")
def delete_message(id: int, db: Session = Depends(get_db)):
    message = db.query(Message).get(id)
    if not message:
        raise HTTPException(status_code=404, detail="Message not found")
    
    db.delete(message)
    db.commit()
    return {"message": f"Message {id} deleted successfully"}
