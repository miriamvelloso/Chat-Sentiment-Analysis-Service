from src.app import app_
from src.config import PORT 
import src.create 
import src.sentimental 
import src.recommend
from  src.errorHandler import  errorHandler
 

app_.run("0.0.0.0", PORT, debug=True)