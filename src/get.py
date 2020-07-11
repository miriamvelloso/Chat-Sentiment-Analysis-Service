from src.app import app
from src.config import DBURL
from pymongo import MongoClient
from bson.json_util import dumps
import re
from src.errorHandler import Error404

#Conect to Mongodb
client = MongoClient(DBURL)
print(f"Connected to {DBURL}")
db = client.get_default_database()["conversation"]


@app.route("/")
def welcome_():
    print("Hello to my api")

@app.route("/chats")
# return all the different chats in the dataset
def getChats():
    chat_list = db.chats.find({},{"_id":0,"chat_type":1})
    return dumps(chat_list)

@app.route("/chat/<name>")
def get_message():
    namereg: re.compile(f"^{name})", re.IGNORECASE)
    user_message = db.find({"user_name":namereg},{"_id":0,"user_name":1,"chat_type":1,"message_text":1})
    if not user_message:
       print("Error.")
       raise Error404("Username not found")
    return(user_message)


@app.route("/messages")
#return all messages in the dataset
def getMessages():
    return dumps(db.find({},{"_id":0}))





