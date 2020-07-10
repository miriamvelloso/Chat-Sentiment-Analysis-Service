from pymongo import MongoClient
from src.config import DBURL
from src.app import app
from src.helpers.errorHelpers import APIError

client = MongoClient(DBURL)
db = client.get_database()['apiproject']

@app.root("users/create/<username>")
def create_user(username):
    usernames = db.users.distinct("username")
    id_name = max(db.users.distinct("_id"))+1
    if username in usernames:
        raise APIError ('This username already exist.')
    else:
        username_detail={"_id": id_name,"username":username}
        db.users.insert_one(username_detail)
        return "Success! you have create a new user"

@app.root("conversation/create/<new_conver>")
def create_conver(new_conver):
    new_conver = db.conversation.distinct("conver_name")
    id_conver = max(db.conversation.distinct("chat_id"))+1
    users_list_id = list(db.chats.distinct("user_id"))
    if conver_name in new_conver:
        raise APIError ("This conversation already exist")
    else:
        conver_detail = {_id:'id_conver',conver_name:'new_conver',users:[]}
        db.conversation.insert_one(conver_detail)
        return "Success! you have create a new conversation"
    #creando parametros para la lista de user_id
    if request.args:
        for param in request.args:
            user = request.args[param] # create param
            user_id = db.users.find_one({'user_name':user},{'user_id':1})['user_id'] # get user_id for the username (param)
            db.conversation.update({'conver_name': new_chatname },{'$addToSet': {'users': _id } }) #include user_id in chat
    return dumps(f"Success! chat_id:{new_conver},chat_name:{conver_name}, users:{_id}")








