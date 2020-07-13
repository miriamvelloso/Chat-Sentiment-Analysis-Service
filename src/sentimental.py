from pymongo import MongoClient
from src.errorHandler import  errorHandler
from src.app import app_
from bson.json_util import dumps
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from src.config import DBURL
nltk.download("vader_lexicon")


#Conect to Mongodb
client = MongoClient(DBURL)
print(f"Connected to {DBURL}")
db = client.get_default_database()["conversation"]

@app_.route("/chat/<chat_type>/list")
@errorHandler
#Get all mesages
def GetsMsg(chat_type):
    chat = db.find({"chat_type": f"{chat_type}"},{"_id":0, "message_text":1})
    if not chat_type:
        return f"Error this chat doesn't exists"
    else:
        print("Success!")
        return dumps(chat)

@app_.route("/chat/<chat_type>/sentiment")
@errorHandler
def sentAnalysis(chat_type):
    quotes= list(db.find({"chat_type": chat_type},{"_id":0, "message_text":1}))
    sentiment = SentimentIntensityAnalyzer().polarity_scores(str(quotes).strip('[]'))
    if sentiment["neg"] > sentiment["pos"]:
        return {"Score":sentiment, "Resume":"Mostly negative"}
    else:
        return {"Score":sentiment, "Resume":"Mostly positive"}