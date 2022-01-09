import os

from utils import data as data_utils


# FLASK
FLASK_DEBUG = int(os.getenv('FLASK_DEBUG', 0))

# DB
DB_NAME = os.getenv('DB_NAME', 'pypi_org')
DB_MYSQL_CLIENT = os.getenv('DB_MYSQL_CLIENT', 'mysql+mysqldb')

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
    '{}://root:rootroot@localhost/{}'.format(DB_MYSQL_CLIENT, DB_NAME))
# # Default
# # Py2: https://pypi.org/project/MySQL-python/
# DB_CONNECTION_MYSQL = os.environ.get(
#     'DB_CONNECTION_MYSQL',
#     '{}://root:rootroot@localhost/{}'.format('mysql', DB_NAME))
# # mysqlclient (a maintained fork of MySQL-Python)
# # Py3: https://github.com/PyMySQL/mysqlclient
# DB_CONNECTION_MYSQL = os.environ.get(
#     'DB_CONNECTION_MYSQL',
#     '{}://root:rootroot@localhost/{}'.format('mysql+mysqldb', DB_NAME))
# # PyMySQL
# # https://github.com/PyMySQL/PyMySQL
# DB_CONNECTION_MYSQL = os.environ.get(
#     'DB_CONNECTION_MYSQL',
#     '{}://root:rootroot@localhost/{}'.format('mysql+pymysql', DB_NAME))
# Active DB connection
DB_CONNECTION = DB_CONNECTION_MYSQL

# SQLAlchemy
# InvalidRequestError: VARCHAR requires a length on dialect mysql
STR_LENGTH = os.environ.get('STR_LENGTH', 255)