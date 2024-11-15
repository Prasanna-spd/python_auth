from pymongo import MongoClient
from config import MONGODB_URI, DATABASE_NAME

mongo_client = None
db = None


def connect_to_mongo():
    global mongo_client, db
    mongo_client = MongoClient(MONGODB_URI)
    db = mongo_client[DATABASE_NAME]
    try:
        mongo_client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
        print("Connected to MongoDB")


def close_mongo_connection():
    global mongo_client
    mongo_client.close()
    print("Closed connection to MongoDB")


connect_to_mongo()