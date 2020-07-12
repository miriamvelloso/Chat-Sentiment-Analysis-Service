from src.app import app
from pymongo import MongoClient
from src.config import DBURL
from bson.json_util import dumps
import re
from src.errorHandler import APIError, errorHandler
from flask import request


#Connection to Mongo
client = MongoClient(DBURL)
db = client.get_database()


def Createuser(new_username):
    usernames=(db.distinct("user_name")) # get all usernames that exist
    new_userid = max(db.distinct("user_id"))+1 # Create new user_id
    if new_username in usernames:
        raise APIError ("Sorry the username already exists")
    else:
        username_details={"user_id": new_userid,"user_name":new_username}
        db.users.insert_one(username_details)
        return dumps(f"Sucess! user_id:{new_userid},user_name:{new_username}")

# create new chat with users
def createChats(chatname):
    chats = db.distinct("chat_type")
    if chatname in chats:
        return f"Error: This chat already exists"
    else:
        db.insert_one({"chat_type": chatname})
        return f"New chat was created"


#add user to a chat 
def adduser(chat, username):
    queryuser = db.find({"user_name": username},{'_id':0})
    if queryuser.count() == 0:
        return f"Error: This user doesn't exist."
    else:
        query = db.find({"$and":[{"user_name": username},{"chat_type": chat}]},{'_id':0})

        if query.count() == 0:
            db.update({"user_name": username },{"$set":{"chat_type":chat}})
            return f"Great! The user were added to the chat."
        else:
            return f"This user is already in the chat."


#Add message to a chat

def addMessage(chatname, username, message):
    queryusers = db.find({"user_name": username},{'_id':0})
    if queryusers.count() == 0:
        return f"Error: This user doesn't exist."
    else:
        querymessage = db.find({"$and":[{"user_name": username},{"chat_type": chatname},{"message_text": message}]},{'_id':0})
        if querymessage.count() == 0:
            db.update({"user_name": username },{"$set":{"message_text":message}})
            return f"Great! The message were added to the chat."
        else:
            return f"This message is already in the chat."






