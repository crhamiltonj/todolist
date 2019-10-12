import click
from flask.cli import with_appcontext
from flask import Flask



def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    from api.db import db, migrate
    from api.models.todoitems import ma

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    from api.routes import todo
    app.register_blueprint(todo.td_bp)

    @app.cli.command('init-db')
    @with_appcontext
    def init_db():
        db.create_all()
        click.echo('Database created')

    return app



