import pymongo
import pandas as pd
from scipy.spatial.distance import pdist, squareform
import scipy.spatial.distance as distance
from bson.json_util import dumps
from src.create import *
from src.errorHandler import errorHandler, Error404
from flask import Flask, request
from src.app import app
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download("vader_lexicon")

#Recommend friends based on the sentiments
def recommendUser(user_name):
    querynames = list(db.distinct("user_name"))
    lst = []
    sia = SentimentIntensityAnalyzer()
    for name in querynames:
        queryquotes = list(db.find({"user_name": name},{"_id":0, "message_text":1}))
        querysent = sia.polarity_scores(str(queryquotes).strip('[]'))
        lst.append({"User": name, "Negative": querysent['neg'],  "Neutral": querysent['neu'], "Positive": querysent['pos']})
    df = pd.DataFrame.from_dict(lst).set_index('User').T
    distances = pd.DataFrame(1/(1+ squareform(pdist(df.T, 'euclidean'))), index=df.columns, columns=df.columns)
    similarities = distances[user_name].sort_values(ascending=False)[1:4].index
    return {f"The friends recommended for {user_name} are": dumps(similarities)}