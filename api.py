from src.app import app
from src.config import PORT
import src.controllers.get
import src.controllers.create
 

app.run("0.0.0.0", PORT, debug=True)