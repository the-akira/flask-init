from flask import Blueprint
from project.models import User, Game, Genres
from project import admin, db
from flask_admin.contrib.sqla import ModelView

adm = Blueprint('adm', __name__)

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Game, db.session))
admin.add_view(ModelView(Genres, db.session))