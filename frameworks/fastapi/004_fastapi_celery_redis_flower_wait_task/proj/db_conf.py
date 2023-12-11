import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

load_dotenv(".env")

SQLALCHEMY_DATABASE_URL = os.environ["DATABASE_URL"]

# https://docs.sqlalchemy.org/en/20/errors.html#operationalerror
# https://docs.sqlalchemy.org/en/20/core/pooling.html#pool-disconnects
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, pool_pre_ping=True
)

db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()
