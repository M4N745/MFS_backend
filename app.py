import os
from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_smorest import Api
from flask_cors import CORS

from db import db

from resources.users import blp as UsersBlueprint
from resources.movies import blp as MoviesBlueprint
from resources.covers import blp as CoversBlueprint

def create_app(db_url=None):
    app = Flask(__name__)
    CORS(app)
    # config
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = os.getenv("APP_NAME")
    app.config["API_VERSION"] = "v1.0"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

    db.init_app(app)
    
    migrate = Migrate(app, db)

    jwt = JWTManager(app)

    api = Api(app)

    api.register_blueprint(UsersBlueprint)
    api.register_blueprint(MoviesBlueprint)
    api.register_blueprint(CoversBlueprint)

    return app
