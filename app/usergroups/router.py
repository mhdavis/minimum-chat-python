from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from app.database import get_db
from app.models.usergroup import UserGroup
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

class UserGroupBase(BaseModel):
   name: str
   description: Optional[str] = ""

class UserGroupResponse(UserGroupBase):
   id: int
   timestamp_created: datetime
   
   class Config:
       from_attributes = True

@router.get("/usergroups", response_model=List[UserGroupResponse])
def get_usergroups(db: Session = Depends(get_db)):
   return db.query(UserGroup).all()

@router.get("/usergroups/{id}", response_model=UserGroupResponse)
def get_usergroup(id: int, db: Session = Depends(get_db)):
   usergroup = db.query(UserGroup).get(id)
   if not usergroup:
       raise HTTPException(status_code=404, detail="UserGroup not found")
   return usergroup

@router.post("/usergroups", status_code=201)
def add_usergroup(usergroup: UserGroupBase, db: Session = Depends(get_db)):
   new_usergroup = UserGroup(**usergroup.dict(), timestamp_created=datetime.utcnow())
   db.add(new_usergroup)
   db.commit()
   return {"message": f"UserGroup {new_usergroup.id} created successfully!"}

@router.put("/usergroups/{id}")
def update_usergroup(id: int, usergroup: UserGroupBase, db: Session = Depends(get_db)):
   db_usergroup = db.query(UserGroup).get(id)
   if not db_usergroup:
       raise HTTPException(status_code=404, detail="UserGroup not found")
   
   for field, value in usergroup.dict().items():
       setattr(db_usergroup, field, value)
   db.commit()
   return {"message": f"UserGroup {id} updated successfully!"}

@router.delete("/usergroups/{id}")
def delete_usergroup(id: int, db: Session = Depends(get_db)):
   usergroup = db.query(UserGroup).get(id)
   if not usergroup:
       raise HTTPException(status_code=404, detail="UserGroup not found")
   
   db.delete(usergroup)
   db.commit()
   return {"message": f"UserGroup {id} deleted successfully!"}