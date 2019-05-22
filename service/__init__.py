import os

from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from config import Config


# Init SQL Alchemy
db = SQLAlchemy()

# Init App
config_name = os.getenv('APP_SETTINGS')
app = FlaskAPI(__name__, instance_relative_config=True)
app.config.from_object(Config[config_name])
app.config.from_pyfile('config.py')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


from service import routes, models
