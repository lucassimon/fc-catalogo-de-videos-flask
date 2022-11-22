from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db: SQLAlchemy = SQLAlchemy()
migrate = Migrate()


def configure_database(app):
    db.init_app(app)


def configure_migrate(app):
    migrate.init_app(app, db)
