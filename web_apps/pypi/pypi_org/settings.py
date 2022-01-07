import os

from utils import data as data_utils


# FLASK
FLASK_DEBUG = int(os.getenv('FLASK_DEBUG', 0))

# DB
DB_NAME = os.getenv('DB_NAME', 'pypi_org')
# SQLite
DB_SQLITE_FILE_NAME = os.environ.get(
    'DB_SQLITE_FILE_NAME', '{}.db'.format(DB_NAME))
DB_SQLITE_FILE = os.environ.get('DB_SQLITE_FILE', os.path.join(
    os.path.dirname(__file__), 'db', DB_SQLITE_FILE_NAME))
DB_CONNECTION_SQLITE = os.environ.get(
    'DB_CONNECTION_SQLITE', data_utils.get_sql_lite_conn_str(DB_SQLITE_FILE))
# MySQL
DB_CONNECTION_MYSQL = os.environ.get(
    'DB_CONNECTION_MYSQL',
    'mysql://root:rootroot@localhost/{}'.format(DB_NAME))
# Active DB connection
DB_CONNECTION = DB_CONNECTION_SQLITE
