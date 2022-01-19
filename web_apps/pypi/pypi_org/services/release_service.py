import sqlalchemy.orm as orm

from data import db_session
from data.models.releases import Release


def get_releases() -> orm.Query:
    with db_session.create_session() as session:
        return session.query(Release)