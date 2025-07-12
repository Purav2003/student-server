from pydantic import BaseModel, EmailStr
from datetime import datetime

class CourseCreate(BaseModel):
    id: str = None  
    courseName: str

    class Config:
        extra = "forbid"  
        error_msg_templates = {
            "value_error.missing": "The field '{loc}' is required but was not provided.",
        }


