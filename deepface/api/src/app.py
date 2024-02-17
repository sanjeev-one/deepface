# 3rd parth dependencies
from flask import Flask
from deepface.api.src.modules.core.routes import blueprint
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(blueprint)
    return app

