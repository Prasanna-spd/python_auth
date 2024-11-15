from fastapi import APIRouter, Depends, HTTPException
from typing import List
from schemas import UserCreate, UserUpdate
from models import User, Role
from auth import get_current_active_user
from database import db
from crud import (
    create_user, get_user_by_username,
    get_users, update_user, delete_user
)

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(get_current_active_user)],
    responses={404: {"description": "Not found"}},
)


def get_admin_user(current_user: User = Depends(get_current_active_user)):
    if current_user.role != Role.admin:
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return current_user


@router.post("/", response_model=User)
def create_new_user(user: UserCreate, admin_user: User = Depends(get_admin_user)):
    user_dict = get_user_by_username(db, user.username)
    if user_dict:
        raise HTTPException(
            status_code=400, detail="Username already registered")
    new_user = create_user(db, user)
    return User(**new_user)


@router.get("/", response_model=List[User])
def read_users(skip: int = 0, limit: int = 10):
    users = get_users(db, skip=skip, limit=limit)
    return [User(**user) for user in users]


@router.get("/{username}", response_model=User)
def read_user(username: str):
    user_dict = get_user_by_username(db, username)
    if user_dict is None:
        raise HTTPException(status_code=404, detail="User not found")
    return User(**user_dict)


@router.put("/{username}", response_model=User)
def update_existing_user(username: str, user_update: UserUpdate):
    updated_user = update_user(db, username, user_update)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return User(**updated_user)


@router.delete("/{username}")
def delete_existing_user(username: str):
    delete_user(db, username)
    return {"detail": "User deleted"}
