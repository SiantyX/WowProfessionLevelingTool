from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.config["APPLICATION_ROOT"] = "/wplt"

from app import routes