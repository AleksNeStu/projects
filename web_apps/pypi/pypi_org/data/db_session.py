import logging

import sqlalchemy as sa
import sqlalchemy.orm as orm
import sqlalchemy_utils as sa_utils

from data.models.modebase import SQLAlchemyBase

session = None

def global_init(conn_str: str):
    global session
    if session:
        return

    # engine
    engine = sa.create_engine(conn_str, echo=True)
    logging.info(
        "Engine created w/ a connection string: '{}'".format(conn_str))
    # DB create (not required for SQLite)
    if not sa_utils.database_exists(engine.url):
        sa_utils.create_database(engine.url)

    # session
    session = orm.sessionmaker(bind=engine)

    # noinspection PyUnresolvedReferences
    import data.models
    SQLAlchemyBase.metadata.create_all(engine)



