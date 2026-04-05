from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import User
from schemas import UserCreate, UserUpdate
from sqlalchemy.exc import IntegrityError

def create_user(db: Session, user: UserCreate):
    db_user = User(
        name=user.name,
        email=user.email,
        role=user.role,
        status=user.status
    )
    db.add(db_user)
    try:
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Email already exists")

def get_users(db: Session):
    return db.query(User).all()

def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted"}

def update_user(db: Session, user_id: int, updated_data: UserUpdate):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if updated_data.name is not None:
        user.name = updated_data.name
    if updated_data.email is not None:
        user.email = updated_data.email
    if updated_data.role is not None:
        user.role = updated_data.role
    if updated_data.status is not None:
        user.status = updated_data.status

    db.commit()
    db.refresh(user)
    return user

def get_user_by_id(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user