from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from enum import Enum


class Role(str, Enum):
    admin = "admin"
    user = "user"


class User(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    username: str
    email: EmailStr
    hashed_password: str
    full_name: Optional[str] = None
    role: Role = Role.user


class TokenData(BaseModel):
    username: Optional[str] = None
    role: Optional[Role] = None
