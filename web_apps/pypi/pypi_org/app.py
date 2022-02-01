"""Flask application run."""
import logging
import os
from smtplib import SMTPNotSupportedError
from ssl import SSLError
import flask
import sys

import settings
from bin import load_data
from bin import run_migrations
from data import db_session
from migrations import utils as migrations_utils
from utils import py as py_utils

app = flask.Flask(__name__)
# APPMAP
#TODO: Fix an error if APPMAP=true and try to rec remote or local session
# ```
# File "projects/web_apps/pypi/.venv/lib/python3.10/site-packages/appmap/_implementation/recording.py", line 254, in do_import
# mod = args[0]
# IndexError: tuple index out of range
# ```
# from appmap.flask import AppmapFlask
# appmap = AppmapFlask(app)

# CFG
# flask_cfg.from_pyfile('settings.py') # no needed 'flask.py'
app.config.update({
    **settings.FLASK_ENV_CFG,
    **settings.FLASK_SEC_ENV_CFG
})

# MAIL
import flask_mail
mail = flask_mail.Mail(app)
#  If multiple applications running in the same process but with different
#  configuration options.
# mail = Mail()
# app = Flask(__name__)
# mail.init_app(app)

# SIJAX
import flask_sijax
flask_sijax.Sijax(app)


def main():
    # Logging
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    # logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
    # logging.getLogger("sqlalchemy.pool").setLevel(logging.DEBUG)

    register_blueprints()
    setup_db()
    all_db_models = generate_all_db_models()
    execute_flask_test_options()
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
    run_migrations.run()

def generate_all_db_models():
    db_models = migrations_utils.get_models(os.path.join(
        os.path.dirname(__file__), 'data', 'generated_all_db_models.py'))
    return db_models

def execute_flask_test_options():
    if settings.EXECUTE_FLASK_TEST_OPTIONS:
        send_emails()

def send_emails():
    with app.app_context():
        msg = flask_mail.Message(
            subject='Test message from pypi_org demo web app',
            sender=app.config.get('MAIL_USERNAME'),
            recipients=[
                'email1@gmail.com',
            ],
            body='Hi bro:) It\'s Test message from pypi_org demo web app.'
        )
        msg.add_recipient("email2@gmail.com")
        # smtplib.SMTPNotSupportedError: STARTTLS extension not supported by server.
        # [SSL: WRONG_VERSION_NUMBER] wrong version number (_ssl.c:997)"
        try:
            mail.send(msg)
        except (SMTPNotSupportedError, SSLError) as err:
            logging.error(f'Email was not send due to "{err}"')


if __name__ in ('__main__', 'pypi_org.app'):
    main()
else:
    register_blueprints()