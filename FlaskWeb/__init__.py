from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from FlaskWeb.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_mng = LoginManager()
login_mng.login_view = 'users.login'
login_mng.login_message_category = 'info'
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_mng.init_app(app)
    mail.init_app(app)

    from FlaskWeb.users.routes import users
    from FlaskWeb.posts.routes import posts
    from FlaskWeb.main.routes import main
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)

    return app