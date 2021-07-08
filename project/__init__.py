from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from project.config import Config

db = SQLAlchemy()
admin = Admin()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    admin.init_app(app)

    from project.main.routes import main
    from project.adm.routes import adm
    app.register_blueprint(main)
    app.register_blueprint(adm)

    return app