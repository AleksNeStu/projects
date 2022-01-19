import sqlalchemy.orm as orm

from data import db_session
from data.models.users import User


def get_users() -> orm.Query:
    with db_session.create_session() as session:
        return session.query(User)