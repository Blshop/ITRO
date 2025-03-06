import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.secret_key = "secret"
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "postgresql://postgres:postgres@localhost:5432/ITRO"
    )
    app.config["UPLOAD_FOLDER"] = "all_documents"
    db.init_app(app)

    with app.app_context():
        from . import models

        db.create_all()

    from .blueprints.settings import settings as settings_blueprint
    from .blueprints.basic import basic
    from .blueprints.units import units as units_blueprint
    from .blueprints.documents import documents as document_blueprint
    from .blueprints.calendar import calendar as calendar_blueprint

    app.register_blueprint(calendar_blueprint, url_prefix="/calendar")
    app.register_blueprint(settings_blueprint, url_prefix="/settings")
    app.register_blueprint(units_blueprint, url_prefix="/units")
    app.register_blueprint(document_blueprint, url_prefix="/documents")
    app.register_blueprint(basic)
    return app
