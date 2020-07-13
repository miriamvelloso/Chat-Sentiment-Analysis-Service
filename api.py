from src.app import app
from src.config import PORT
from  src.create import *
from  src.sentimental import *
from  src.errorHandler import errorHandler
 
#Create users
@app.route("/user/create/<username>")
@errorHandler
def Createuser(username):
    usuario = Createuser(username)
    return usuario

#Create chats
@app.route("/chat/create/<chatname>")
@errorHandler
def createchat(chatname):
    grupo = createChats(chatname)
    return grupo

#Add user to a chat
@app.route("/chat/<chatname>/adduser/<username>")
@errorHandler
def addUser(chat, username):
    add_users = adduser(chat,username)
    return add_users

#Add message to a chat
@app.route("/chat/<chatname>/user/<username>/addmessage/<message>")
@errorHandler
def addmessage(chat, username, message):
    add_message = addMessage(chat, username, message)
    return add_message

#Get all the messages from a chat
@app.route("/chat/<chatname>/list")
@errorHandler
def getchats(chatname):
    gc = GetsMsg(chatname)
    return gc

#Analyze sentiment of a chat
@app.route("/chat/<chatname>/sentiment")
@errorHandler
def sentanalysis(chatname):
    sentiments = sentAnalysis(chatname)
    return sentiments

app.run("0.0.0.0", PORT, debug=True)