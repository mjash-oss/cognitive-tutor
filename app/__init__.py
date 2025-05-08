from flask import Flask 
from flask_cors import CORS
from .db import db 
from .routes.auth import auth_bp
from .routes.lessons import logicwordpuzzles
from .routes.attempts import attempts_bp

def create_app():
    app = Flask(__name__)
    CORS(app, origins=["https://deft-mooncake-094a90.netlify.app"])

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(logicwordpuzzles, url_prefix='/api/lessons')
    app.register_blueprint(attempts_bp, url_prefix='/api/attempts')

    return app 