# This file is where we create our database models
# for our users and our notes. In init.py there are
# functions that actually create the database.

# import the db variable from init.py
from . import db
# Used to help the user login
from flask_login import UserMixin
# func is used to add the date and time
from sqlalchemy.sql import func


class Note(db.Model):
    # id is used as the primary key which is a unique identifer
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # A foreignkey is keu on one of your databases that references an id
    # to another database column
    # For every single note we define which user created that note.
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # user.id is referencing the user class and id variable.


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    # unique=True ensures no user has the same email. Max string length 150
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    # Every time a note is created add into the users note relationship the
    # user notes id. Note is passing it the Notes class above.
    notes = db.relationship('Note')
