from flask_api import FlaskAPI

app = FlaskAPI(__name__)
app.config.from_pyfile("../config.py")

from app.controllers import todoController
