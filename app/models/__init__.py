from app import app
from mongoengine import connect

connect(**app.config['MONGO_SETTINGS'])
