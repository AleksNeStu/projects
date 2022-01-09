import datetime

import sqlalchemy as sa
import sqlalchemy.orm as orm

from data.models.modelbase import SqlAlchemyBase


class Release(SqlAlchemyBase):
    __tablename__ = 'releases'

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)

    major_ver: int = sa.Column(sa.BigInteger, index=True)
    minor_ver: int = sa.Column(sa.BigInteger, index=True)
    build_ver: int = sa.Column(sa.BigInteger, index=True)

    created_date: datetime.datetime = sa.Column(
        sa.DateTime, default=datetime.datetime.now, index=True)
    comment: str = sa.Column(sa.String)
    url: str = sa.Column(sa.String)
    size: int = sa.Column(sa.BigInteger)