import os
import bcrypt

from flask import Flask
from flask_mail import Mail
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from libs import mailgun, token

mail = Mail()
marshmallow = Marshmallow()
cors = CORS()
jwtmanager = JWTManager()


def create_app(config: str):
    app = Flask(__name__)
    app.config.from_object(f'channelry.config.{config.title()}')

    mail.init_app(app)
    marshmallow.init_app(app)
    cors.init_app(app)
    jwtmanager.init_app(app)

    mailgun.api_key = app.config.get('MAILGUN_API_KEY')
    token.password_salt = bcrypt.gensalt()
    token.secret_key = app.config.get('SECRET_KEY')

    from .models import db
    db.init_app(app)

    from .models.account import User

    from .views.account import account_bp
    from .views.home import home_bp
    app.register_blueprint(account_bp)
    app.register_blueprint(home_bp)

    return app