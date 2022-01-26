from typing import Optional

import sqlalchemy.orm as orm

from data import db_session
from data.models.users import User
from utils import data as data_utils


def get_users() -> orm.Query:
    with db_session.create_session() as session:
        return session.query(User)

def create_user(name: str, email: str, password: str) -> Optional[User]:
    u = User(
        name=name,
        email=email,
        hashed_password=data_utils.to_hash(password),
    )

    return u