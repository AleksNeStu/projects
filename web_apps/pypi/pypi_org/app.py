"""Flask application run."""
import os

import flask

from data import db_session
from data import utils as data_utils


app = flask.Flask(__name__)


def main():
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
    sql_db_file = os.path.join(
        os.path.dirname(__file__),
        'db',
        'pypi_org.sqlite')
    conn_str = data_utils.get_sql_lite_conn_str(sql_db_file)
    db_session.global_init(conn_str)


if __name__ == '__main__':
    main()
else:
    register_blueprints()