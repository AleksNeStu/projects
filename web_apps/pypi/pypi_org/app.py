"""Flask application run."""
import logging

import flask
import sys

import settings
from data import db_session

app = flask.Flask(__name__)


def main():
    # Logging
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)

    register_blueprints()
    setup_db()
    app.run(port=5000, debug=True)


def register_blueprints():
    from views import (
        home_views, packages_views, cms_views
    )

    app.register_blueprint(home_views.blueprint)
    app.register_blueprint(packages_views.blueprint)
    app.register_blueprint(cms_views.blueprint)


def setup_db():
    db_session.global_init(settings.DB_CONNECTION)


if __name__ in ('__main__', 'pypi_org.app'):
    main()
else:
    register_blueprints()