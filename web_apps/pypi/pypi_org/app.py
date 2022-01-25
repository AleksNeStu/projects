"""Flask application run."""
import logging

import flask
import sys

import settings
from bin import load_data
from bin import run_migrations
from data import db_session
from utils import py as py_utils

app = flask.Flask(__name__)


def main():
    # Logging
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    # logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
    # logging.getLogger("sqlalchemy.pool").setLevel(logging.DEBUG)

    register_blueprints()
    setup_db()
    app.run(port=5000, debug=True)


def register_blueprints():
    # from views import (
    #     home_views, packages_views, cms_views
    # )
    #
    # app.register_blueprint(home_views.blueprint)
    # app.register_blueprint(packages_views.blueprint)
    # app.register_blueprint(cms_views.blueprint)
    views, _ = py_utils.import_modules(
        'views/__init__.py', 'views', w_classes=False)
    for view in views.values():
        app.register_blueprint(view.blueprint)


def setup_db():
    db_session.global_init(settings.DB_CONNECTION)
    load_data.run()
    # enable for flask app not in debug mode to avoid auto apply
    # run_migrations.run()


if __name__ in ('__main__', 'pypi_org.app'):
    main()
else:
    register_blueprints()