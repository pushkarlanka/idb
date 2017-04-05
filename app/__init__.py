from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

application = Flask(__name__, static_url_path='/app/static')

config = Config()
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.config['SQLALCHEMY_DATABASE_URI'] = config.get_db_url()

db = SQLAlchemy(application)

from app import views

