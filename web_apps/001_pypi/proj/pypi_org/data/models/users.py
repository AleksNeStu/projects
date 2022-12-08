import datetime

import sqlalchemy as sa

from data.models.modelbase import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name: str = sa.Column(sa.String, nullable=True)
    email: str = sa.Column(
        sa.String, index=True, unique=True, nullable=True)
    hashed_password: str = sa.Column(sa.String, nullable=True, index=True)
    created_date: datetime.datetime = sa.Column(
        sa.DateTime, default=datetime.datetime.now, index=True)
    profile_image_url: str = sa.Column(sa.String)
    last_login: datetime.datetime = sa.Column(
        sa.DateTime, default=datetime.datetime.now, index=True)
