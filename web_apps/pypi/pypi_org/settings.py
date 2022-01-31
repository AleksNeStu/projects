import os
from utils import db as db_utils
import dotenv

# APP
APP_ROOT_DIR = os.getenv('APP_ROOT_DIR', os.path.dirname(__file__))
PROJECT_ROOT_DIR = os.getenv(
    'PROJECT_ROOT_DIR', os.path.join(APP_ROOT_DIR, '../'))
ALEMBIC_INI = os.getenv(
    'ALEMBIC_INI', os.path.join(PROJECT_ROOT_DIR, 'alembic.ini'))
LOCAL_ENV_PATH = os.getenv(
    'LOCAL_ENV_PATH', os.path.join(PROJECT_ROOT_DIR, 'configs/local.env'))
FLASK_ENV_PATH = os.getenv(
    'FLASK_ENV_PATH', os.path.join(PROJECT_ROOT_DIR, 'configs/flask.env'))
# Get dict of vars from .env and set to LOCAL_ENV_PATH.py
LOCAL_ENV_CFG = dotenv.dotenv_values(LOCAL_ENV_PATH)
locals().update(LOCAL_ENV_CFG)
# for k, v in LOCAL_ENV_CFG.items():
#     exec(k + '=v')
# Make .env vars like os vars
dotenv.load_dotenv(LOCAL_ENV_PATH)

# FLASK
FLASK_DEBUG = int(os.getenv('FLASK_DEBUG', 0))

# DB
DB_NAME = os.getenv('DB_NAME', 'pypi_org')
DB_MYSQL_CLIENT = os.getenv('DB_MYSQL_CLIENT', 'mysql+mysqldb')

# SQLite
DB_SQLITE_FILE_NAME = os.environ.get(
    'DB_SQLITE_FILE_NAME', '{}.db'.format(DB_NAME))
DB_SQLITE_FILE = os.environ.get('DB_SQLITE_FILE', os.path.join(
    APP_ROOT_DIR, 'db', DB_SQLITE_FILE_NAME))
DB_CONNECTION_SQLITE = os.environ.get(
    'DB_CONNECTION_SQLITE', db_utils.get_sql_lite_conn_str(DB_SQLITE_FILE))
# MySQL
DB_CONNECTION_MYSQL = os.environ.get(
    'DB_CONNECTION_MYSQL',
    '{}://root:rootroot@localhost/{}'.format(DB_MYSQL_CLIENT, DB_NAME))

# 1) Py2 (Default): https://pypi.org/project/MySQL-python/
# DB_CONNECTION_MYSQL = os.environ.get(
#     'DB_CONNECTION_MYSQL',
#     '{}://root:rootroot@localhost/{}'.format('mysql', DB_NAME))

# 2) mysqlclient (a maintained fork of MySQL-Python)
# # Py3: https://github.com/PyMySQL/mysqlclient
# DB_CONNECTION_MYSQL = os.environ.get(
#     'DB_CONNECTION_MYSQL',
#     '{}://root:rootroot@localhost/{}'.format('mysql+mysqldb', DB_NAME))

# 3) PyMySQL
# # https://github.com/PyMySQL/PyMySQL
# DB_CONNECTION_MYSQL = os.environ.get(
#     'DB_CONNECTION_MYSQL',
#     '{}://root:rootroot@localhost/{}'.format('mysql+pymysql', DB_NAME))
# Active DB connection
DB_CONNECTION = DB_CONNECTION_SQLITE

# SQLAlchemy
# InvalidRequestError: VARCHAR requires a length on dialect mysql
STR_LENGTH = os.environ.get('STR_LENGTH', 255)