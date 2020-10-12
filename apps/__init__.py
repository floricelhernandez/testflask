import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Resource,  Api

app = Flask(__name__)
api_router = Api(app=app, doc='/docs')
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from apps.api.routes import *
