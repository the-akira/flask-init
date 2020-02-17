from project import db
from datetime import datetime

"""
from project import create_app
from project import db
app = create_app()
app.app_context().push()
db.create_all()
"""

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)

	def __repr__(self):
		return f"User('{self.username}', '{self.email}')"

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    publisher = db.Column(db.String(50), nullable=False)
    director = db.Column(db.String(50), nullable=False)
    genres = db.relationship('Genres', backref='game', lazy=True)

    def __repr__(self):
    	return f"Game('{self.id}: {self.name}', '{self.publisher}')"

class Genres(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'),
        nullable=False)