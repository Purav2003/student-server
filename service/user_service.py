from fastapi import HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
import random
import string
from schemas.user_schema import UserCreate, UserLogin
from utils.auth import hash_password, verify_password
from models.user_model import Users
from utils.jwt import create_access_token
from datetime import timedelta, datetime

def create_user(db: Session, user: UserCreate):
    if not user.email or not user.password:
        raise HTTPException(status_code=400, detail="Email and password are required")
    
    exisiting_user = db.query(Users).filter(Users.email == user.email).first()
    if exisiting_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    # hash the password
    hashed_password = hash_password(user.password)  # Assume hash_password is a function that hashes the password
    if not hashed_password:
        raise HTTPException(status_code=500, detail="Error hashing password")
    # random 10 characters as ID
    def generate_random_id(length=10):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    db_user = Users(
        id=generate_random_id(),
        email=user.email,
        password=hashed_password
    )
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return JSONResponse(
            status_code=201,
            content={
                "message": "User created successfully"
            }
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error creating user")
    
def login(db: Session, user: UserLogin):
    db_user = db.query(Users).filter(Users.email == user.email).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    if not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid email or password")
    # If the password is correct, return a jwt token 
   
    try:
        db_user.last_login = datetime.utcnow()  # Update last login time
        db.commit()
        db.refresh(db_user)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error updating last login time")
    
    access_token = create_access_token(
        data={"sub": db_user.email, "user_id": db_user.id}, 
        expires_delta=timedelta(minutes=60)
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "id": db_user.id,
            "email": db_user.email
    }
    }

    
