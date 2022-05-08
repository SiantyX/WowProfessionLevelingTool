from flask import Flask
from config import Config

class PrefixMiddleware(object):
    def __init__(self, app, prefix=''):
        self.app = app
        self.prefix = prefix

    def __call__(self, environ, start_response):

        if environ["PATH_INFO"].startswith(self.prefix):
            environ["PATH_INFO"] = environ["PATH_INFO"][len(self.prefix):]
            environ["SCRIPT_NAME"] = self.prefix
            return self.app(environ, start_response)
        else:
            start_response("404", [("Content-Type", "text/plain")])
            return ["This url does not belong to the app.".encode()]

app = Flask(__name__)
app.config.from_object(Config)
app.config["APPLICATION_ROOT"] = "/wplt"
app.wsgi_app = PrefixMiddleware(app.wsgi_app, prefix="/wplt")

from app import routes