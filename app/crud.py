from pymongo.database import Database
from config import USERS_COLLECTION
from schemas import UserCreate, UserUpdate
from app.auth import get_password_hash


def get_user_by_username(db: Database, username: str):
    user = db[USERS_COLLECTION].find_one({"username": username})
    if user:
        user['_id'] = str(user['_id'])
    return user


def get_user_by_email(db: Database, email: str):
    user = db[USERS_COLLECTION].find_one({"email": email})
    if user:
        user['_id'] = str(user['_id'])
    return user


def create_user(db: Database, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    user_dict = user.dict()
    user_dict["hashed_password"] = hashed_password
    user_dict["role"] = "user"
    del user_dict["password"]
    result = db[USERS_COLLECTION].insert_one(user_dict)
    user_dict["_id"] = str(result.inserted_id)
    return user_dict


def update_user(db: Database, username: str, user_update: UserUpdate):
    update_data = {k: v for k, v in user_update.dict()
                   if v is not None}
    db[USERS_COLLECTION].update_one(
        {"username": username}, {"$set": update_data})
    user = db[USERS_COLLECTION].find_one({"username": username})
    if user:
        user['_id'] = str(user['_id'])
    return user


def delete_user(db: Database, username: str):
    db[USERS_COLLECTION].delete_one({"username": username})


def get_users(db: Database, skip: int = 0, limit: int = 10):
    users = list(db[USERS_COLLECTION].find().skip(skip).limit(limit))
    for user in users:
        user['_id'] = str(user['_id'])
    return users
