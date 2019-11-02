import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app import views

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

db = SQLAlchemy(app)
migrate = Migrate(app, db)


