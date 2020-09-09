#!/usr/bin/python3
"""Contains the class DBStorage"""
from api.v1.views import app_views
import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
from models import storage
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask
app = Flask(__name__)

app.register_blueprint(app_views)

host = getenv('HBNB_API_HOST', '0.0.0.0')
port = getenv('HBNB_API_PORT', 5000)
@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return { "error": "Not found"}

if __name__ == '__main__':
	app.run(host, port, threaded=True)




