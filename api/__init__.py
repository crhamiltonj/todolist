from flask import Flask
from flask_jwt_extended import (
    JWTManager,
    jwt_required,
    create_access_token,
    get_jwt_identity,
)
from flask_security import Security, login_required, SQLAlchemySessionUserDatastore
from api.models.auth import User, Role


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    from api.db import db, migrate
    from api.models.todoitems import ma

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    jwt = jwt = JWTManager(app)
    user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
    security = Security(app, user_datastore)

    from api.routes import todo

    app.register_blueprint(todo.td_bp)

    with app.app_context():
        db.create_all()

    return app
