"""Flask application run."""
import flask


app = flask.Flask(__name__)


def register_blueprints():
    from views import (
        home_views, packages_views, cms_views
    )

    app.register_blueprint(home_views.blueprint)
    app.register_blueprint(packages_views.blueprint)
    app.register_blueprint(cms_views.blueprint)


def main():
    register_blueprints()
    app.run(port=5000, debug=True)


if __name__ == '__main__':
    main()
else:
    register_blueprints()