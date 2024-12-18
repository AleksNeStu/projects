"""Flask application run."""
import logging
import os
import sys

import flask
import flask_mail

import settings
from bin import load_data
from bin import run_migrations
from data import db_session
from migrations import utils as migrations_utils

app = flask.Flask(__name__)
app.deploying = bool(int(os.getenv('IS_DEPLOY', '0')))
app.is_sql_ver = bool(int(os.getenv('IS_SQL_VERSION', '0')))

email = None
admin = None
toolbar = None

def main():
    configure()

    if not app.testing and not app.deploying:
        app.run(debug=True, host='0.0.0.0')


def configure():
    global admin, email, toolbar

    init_logging()
    update_cfg()
    register_blueprints()
    setup_db()

    if app.is_sql_ver:
        all_db_models = generate_all_db_models()
        admin = add_admin()

    add_appmap()
    add_sijax()
    email = add_email()
    toolbar = add_debug_toolbar()
    #TODO: Add http://docs.mongoengine.org/projects/flask-mongoengine/
    run_actions()


def register_blueprints():
    from views import (
        home_views, packages_views, cms_views, account_views, seo_views
    )
    app.register_blueprint(home_views.blueprint)
    app.register_blueprint(packages_views.blueprint)
    app.register_blueprint(cms_views.blueprint)
    app.register_blueprint(account_views.blueprint)
    app.register_blueprint(seo_views.blueprint)

    # from utils import py as py_utils
    # views, _ = py_utils.import_modules(
    #     'views/__init__.py', 'views', w_classes=False)
    # for view in views.values():
    #     app.register_blueprint(view.blueprint)


def setup_db():
    if app.is_sql_ver:
        db_session.init_sql(settings.DB_CONNECTION)
        # enable for flask app not in debug mode to avoid auto apply
        run_migrations.run()
        load_data.run()
    else:
        db_session.init_no_sql(**settings.NOSQL_DB_CONNECTION)
        # user = User(name='Fie Sds2', email='lol@gmail.com')
        # try:
        #     user.save()
        #     #TODO:  load_data_no_sql.run()
        # except me.errors.NotUniqueError as err:
        #     logging.error(
        #         f'Error: "{err}" on try to save duplicate unique keys. '
        #         f'Possible reason 2 time app load in debug mode')
        #     # raise err


def generate_all_db_models():
    db_models = migrations_utils.get_models(os.path.join(
        os.path.dirname(__file__), 'data', 'generated_all_db_models.py'))
    return db_models


def run_actions():
    global email
    if settings.RUN_ACTIONS:
        send_emails(email)


def send_emails(email):
    from smtplib import SMTPNotSupportedError
    from ssl import SSLError
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
            email.send(msg)
        except (SMTPNotSupportedError, SSLError) as err:
            logging.error('Email was not send due to "%s"', err)


def init_logging():
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    # logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
    # logging.getLogger("sqlalchemy.pool").setLevel(logging.DEBUG)


def update_cfg():
    global app
    # flask_cfg.from_pyfile('settings.py') # no needed 'flask.py'
    app.config.update({
        **settings.FLASK_ENV_CFG,
        **settings.FLASK_SEC_ENV_CFG,
        **settings.FLASK_SEC_ENV_CFG_ME,
    })


def add_appmap():
    # APPMAP
    #TODO: Fix an error if APPMAP=true and try to rec remote or local session
    # ```
    # File "projects/web_apps/pypi/.venv/lib/python3.10/site-packages/appmap/_implementation/recording.py", line 254, in do_import
    # mod = args[0]
    # IndexError: tuple index out of range
    # ```
    # from appmap.flask import AppmapFlask
    # appmap = AppmapFlask(app)
    pass


def add_email():
    global email
    mail = flask_mail.Mail(app)
    #  If multiple applications running in the same process but with different
    #  configuration options.
    # mail = Mail()
    # app = Flask(__name__)
    # mail.init_app(app)
    return mail


def add_sijax():
    import flask_sijax
    flask_sijax.Sijax(app)


# http://localhost:5000/admin/audit/
def add_admin():
    global admin
    import flask_admin
    from flask_admin.contrib.sqla import ModelView
    admin = flask_admin.Admin(
        app, name='pypi_org', template_mode='bootstrap3')

    from data.models.audit import Audit
    with db_session.create_session() as session:
        admin.add_view(ModelView(Audit, session))

    return admin


def add_debug_toolbar():
    global toolbar
    # error: AttributeError: module 'jinja2.ext' has no attribute 'with_'
    # toolbar = flask_debugtoolbar.DebugToolbarExtension(app)

    return toolbar


if __name__ in ('__main__', 'pypi_org.app'):
    main()