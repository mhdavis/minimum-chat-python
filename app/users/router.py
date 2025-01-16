from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from pydantic import BaseModel
from typing import List

router = APIRouter()

class UserBase(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str
    
class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    username: str | None = None
    email: str | None = None

@router.get("/users", response_model=List[UserBase])
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.get("/users/{id}", response_model=UserBase)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(User).get(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/users", status_code=201)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    return {"message": f"User {new_user.id} created successfully!"}

@router.put("/users/{id}")
def update_user(id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    user = db.query(User).get(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    for field, value in user_update.dict(exclude_unset=True).items():
        setattr(user, field, value)
    
    db.commit()
    return {"message": f"User {user.id} updated successfully!"}

@router.delete("/users/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    user = db.query(User).get(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(user)
    db.commit()
    return {"message": f"User {user.id} deleted successfully!"}