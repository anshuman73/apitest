from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
db = SQLAlchemy(app)

# Have to go against PEP 8 to avoid circular imports, flask documentation also recommends this method.
from apitest import models, endpoints

db.engine.execute("CREATE EXTENSION cube;"
                  "CREATE EXTENSION earthdistance;")

db.create_all()
