from flask import Flask 
from flask_cors import CORS
from .db import db 
from .routes.auth import auth_bp
from .routes.lessons import lessons_bp
from flask_jwt_extended import JWTManager
from config import Config  

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    jwt = JWTManager(app) 

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(lessons_bp, url_prefix='/api/lessons')

    CORS(app, origins="https://deft-mooncake-094a90.netlify.app", allow_headers=["Content-Type", "Authorization"], methods=["GET", "POST", "OPTIONS"])

    return app 