from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


# Define a new database and give it the name databasbe.db
db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'kjshkjdhjs'
    # Define the location of our sqlite database.
    # which is within our website folder.
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # Initialize the database and give it our flask app
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Importing the functions in the models.py file into this file.
    # This file needs to run before we initialize the database,
    # so the classes get defined and we can then use them.
    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

# A function to create our database.


def create_database(app):
    # Check if the database already exist.
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            # Create our database if it doesn't exist.
            db.create_all()
            print('Created Database!')
