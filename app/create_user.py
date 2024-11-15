import os
from pymongo import MongoClient
from config import MONGODB_URI, DATABASE_NAME, USERS_COLLECTION
from auth import get_password_hash
from models import Role


def create_initial_user():
    client = MongoClient(MONGODB_URI)
    db = client[DATABASE_NAME]
    username = os.getenv("INIT_USERNAME", "admin")
    email = os.getenv("INIT_EMAIL", "admin@example.com")
    password = os.getenv("INIT_PASSWORD", "adminpass")
    hashed_password = get_password_hash(password)
    role = Role.admin

    user = {
        "username": username,
        "email": email,
        "hashed_password": hashed_password,
        "role": role,
        "full_name": "Administrator"
    }

    if db[USERS_COLLECTION].find_one({"username": username}):
        print("User already exists.")
    else:
        db[USERS_COLLECTION].insert_one(user)
        print("Initial user created.")

    client.close()


if __name__ == "__main__":
    create_initial_user()
