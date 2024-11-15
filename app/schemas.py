from typing import Optional
from pydantic import BaseModel, EmailStr
from models import Role


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    full_name: Optional[str] = None


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None


class UserInDB(BaseModel):
    username: str
    email: EmailStr
    hashed_password: str
    full_name: Optional[str] = None
    role: Role


class Token(BaseModel):
    access_token: str
    token_type: str
