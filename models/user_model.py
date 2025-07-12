from sqlalchemy import Column, String, DateTime as SQLDateTime
from config.database import Base
from datetime import datetime

class Users(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    email= Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(SQLDateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(SQLDateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_login = Column(SQLDateTime, nullable=True)
    
    def __repr__(self):
        return f"<User(id={self.id}, email={self.email})>"