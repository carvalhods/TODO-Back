from flask_api import FlaskAPI
from flask_cors import CORS, cross_origin

app = FlaskAPI(__name__)
CORS(app)
app.config.from_pyfile("../config.py")

from app.controllers import todoController
