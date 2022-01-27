from typing import Optional

import sqlalchemy.orm as orm

from data import db_session
from data.models.users import User
from utils import data as data_utils


def get_users() -> orm.Query:
    with db_session.create_session() as session:
        return session.query(User)


def get_user(email: str, password: str = None,
             users: orm.Query = None) -> Optional[User]:
    users = users or get_users()
    user = users.filter(User.email == email).first()
    if (password and
            user and
            not data_utils.is_hash_correct(user.hashed_password, password)):
        return

    users.session.close()

    return user

def create_user(name: str, email: str, password: str) -> Optional[User]:
    if get_user(email=email):
        return

    with db_session.create_session() as session:
        pass_hash = data_utils.to_hash(password)
        user = User(
            name=name,
            email=email,
            hashed_password=pass_hash
        )
        session.add(user)
        session.commit()

    return user