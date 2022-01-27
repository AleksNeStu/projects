from typing import Optional

import sqlalchemy.orm as orm

from data import db_session
from data.models.users import User
from utils import data as data_utils


def get_users() -> orm.Query:
    with db_session.create_session() as session:
        return session.query(User)


def get_user(email: str, users: orm.Query = None) -> Optional[User]:
    users = users or get_users()
    res = users.filter(User.email == email).first()
    users.session.close()

    return res

def create_user(name: str, email: str, password: str) -> Optional[User]:
    if get_user(email=email):
        return

    with db_session.create_session() as session:
        pass_hash = data_utils.to_hash(password)
        u = User(
            name=name,
            email=email,
            hashed_password=pass_hash
        )
        session.add(u)
        session.commit()

    return u