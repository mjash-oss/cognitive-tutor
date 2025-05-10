from flask import Flask 
from flask_cors import CORS
from .db import db 
from .routes.auth import auth_bp
from .routes.lessons import lessons_bp
from flask_jwt_extended import JWTManager 

def create_app():
    app = Flask(__name__)
    CORS(app, origins=["https://deft-mooncake-094a90.netlify.app"], supports_credentials=True, methods=['GET', 'POST'])

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'QZ1_Kf3jmqFddXhN82uXfG63bX9JhZUl-nUi3V_ZiHg'

    db.init_app(app)
    jwt = JWTManager(app) 

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(lessons_bp, url_prefix='/api/lessons')

    return app 