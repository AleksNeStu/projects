import contextlib
import logging

import sqlalchemy as sa
import sqlalchemy.orm as orm
import sqlalchemy_utils as sa_utils

from data.models.modelbase import SqlAlchemyBase

# https://docs.sqlalchemy.org/en/14/orm/session_basics.html
__session = None

def global_init(conn_str: str):
    global __session
    if __session:
        return

    # engine
    # debug sql queries
    # logger = logging.getLogger('sqlalchemy.engine')
    # logger.setLevel(logging.DEBUG)
    engine = sa.create_engine(conn_str, echo=True)

    db_url = engine.url
    logging.info(
        "Engine created w/ a connection string: '{}'".format(conn_str))
    # DB create (not required for SQLite)
    # TODO: avoid delete DB every time
    # if not sa_utils.database_exists(engine.url):
    #     sa_utils.create_database(engine.url)
    if sa_utils.database_exists(db_url):
        sa_utils.drop_database(db_url)
    sa_utils.create_database(engine.url)

    # session
    __session = orm.sessionmaker(bind=engine)

    # noinspection PyUnresolvedReferences
    import data.models
    SqlAlchemyBase.metadata.create_all(engine)

#TODO: Add list of used sessions with state
def create_session() -> orm.Session:
    # With this configuration, each time we call our sessionmaker instance,
    # we get a new Session instance back each time.
    global __session
    return __session()


@contextlib.contextmanager
def session(expire_on_commit=True):
    session = create_session()
    session.expire_on_commit = expire_on_commit
    try:
        yield session
    finally:
        session.expire_on_commit = True
        session.close()