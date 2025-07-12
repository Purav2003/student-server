from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from loguru import logger
from db.connect_db import get_db
from schemas.user_schema import UserCreate, UserLogin
from service.user_service import create_user,login

user_router = APIRouter()

@user_router.post("/signup")
def signup_user(user: UserCreate, db: Session = Depends(get_db)):
    logger.info(f"Signing up user: {user.email}")
    return create_user(db, user)

@user_router.post("/login")
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    logger.info(f"Logging in user: {user.email}")
    # Implement login logic here
    return login(db,user)
