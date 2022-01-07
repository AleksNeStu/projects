import logging

import sqlalchemy as sa
import sqlalchemy.orm as orm

from data.modebase import SQLAlchemyBase

session = None

def global_init(conn_str: str):
    # DATA
    global session
    if session:
        return
    # engine
    engine = sa.create_engine(conn_str, echo=True)
    logging.info("DB connection string: '{}'".format(conn_str))
    # session
    session = orm.sessionmaker(bind=engine)

    # noinspection PyUnresolvedReferences
    from data.package import Package
    SQLAlchemyBase.metadata.create_all(engine)



