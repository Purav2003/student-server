from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    
    class Config:
        extra = "forbid"  # Forbids extra fields
        error_msg_templates = {
            "value_error.missing": "The field '{loc}' is required but was not provided.",
            "type_error.email": "The email '{loc}' is not valid. Please provide a correct email.",
        }

class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
    class Config:
        extra = "forbid"  # Forbids extra fields
        error_msg_templates = {
            "value_error.missing": "The field '{loc}' is required but was not provided.",
            "type_error.email": "The email '{loc}' is not valid. Please provide a correct email.",
        }

