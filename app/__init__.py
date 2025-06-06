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

    with app.app_context():
        db.create_all()

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(lessons_bp, url_prefix='/api/lessons')

    CORS(app, 
         origins=["https://deft-mooncake-094a90.netlify.app"], 
         allow_headers=["Content-Type", "Authorization"],
         expose_headers=['Authorization'], 
         methods=["GET", "POST", "OPTIONS"],
         supports_credentials=False)

    return app 