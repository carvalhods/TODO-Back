from flask_api import FlaskAPI
from flask_cors import CORS, cross_origin
from mongoengine import connect


def create_app():
    app = FlaskAPI(__name__)
    CORS(app)
    app.config.from_pyfile("config.py")
    connect(**app.config['MONGO_SETTINGS'])
    return app
