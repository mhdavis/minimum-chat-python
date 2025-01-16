from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from app.database import get_db
from app.models.contact import Contact
from pydantic import BaseModel
from typing import List

router = APIRouter()

class ContactBase(BaseModel):
   user_id: int
   friend_id: int

class ContactResponse(ContactBase):
   id: int
   timestamp_created: datetime

   class Config:
       from_attributes = True

@router.get("/contacts", response_model=List[ContactResponse])
def get_contacts(db: Session = Depends(get_db)):
   return db.query(Contact).all()

@router.get("/contacts/{id}", response_model=ContactResponse)
def get_contact(id: int, db: Session = Depends(get_db)):
   contact = db.query(Contact).get(id)
   if not contact:
       raise HTTPException(status_code=404, detail="Contact not found")
   return contact

@router.post("/contacts", status_code=201)
def add_contact(contact: ContactBase, db: Session = Depends(get_db)):
   new_contact = Contact(**contact.dict(), timestamp_created=datetime.utcnow())
   db.add(new_contact)
   db.commit()
   return {"message": f"Contact {new_contact.id} created successfully!"}

@router.delete("/contacts/{id}")
def delete_contact(id: int, db: Session = Depends(get_db)):
   contact = db.query(Contact).get(id)
   if not contact:
       raise HTTPException(status_code=404, detail="Contact not found")
   
   db.delete(contact)
   db.commit()
   return {"message": f"Contact {id} deleted successfully"}