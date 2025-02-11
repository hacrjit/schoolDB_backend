from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    email: str
    role: str  # admin, student, teacher, parent
    password: str  # Store hashed passwords in production
