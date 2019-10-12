import click
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from api import create_app

db = SQLAlchemy()
migrate = Migrate()





