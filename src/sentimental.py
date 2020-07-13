from pymongo import MongoClient
from errorHandler import Error404, errorHandler
from app import app
from bson.json_util import dumps
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from config import DBURL
nltk.download("vader_lexicon")


#Conect to Mongodb
client = MongoClient(DBURL)
print(f"Connected to {DBURL}")
db = client.get_default_database()["conversation"]

@app.route("/chat/<chatname>/list")
@errorHandler
#Get all mesages
def GetsMsg(chat_type):
    chat = db.find({"chat_type": chat_type},{"_id":0, "message_text":1})
    if not chat_type:
        return f"Error this chat doesn't exists"
    else:
        print("Success!")
        return dumps(chat)

@app.route("/chat/<chatname>/sentiment")
@errorHandler
def sentAnalysis(chat_type):
    quotes= list(db.find({"chat_type": chat_type},{"_id":0, "message_text":1}))
    sentiment = SentimentIntensityAnalyzer().polarity_scores(str(quotes).strip('[]'))
    if sentiment["neg"] > sentiment["pos"]:
        return {"Score":sentiment, "Resume":"Mostly negative"}
    else:
        return {"Score":sentiment, "Resume":"Mostly positive"}