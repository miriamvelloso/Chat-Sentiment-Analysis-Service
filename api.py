from src.app import app
from flask import request
from src.config import PORT


app.run("0.0.0.0", PORT, debug=True)