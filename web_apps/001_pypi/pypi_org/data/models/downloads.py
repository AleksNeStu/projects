import datetime

import sqlalchemy as sa

from data.models.modelbase import SqlAlchemyBase


class Download(SqlAlchemyBase):
    __tablename__ = 'downloads'

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    created_date: datetime.datetime = sa.Column(
        sa.DateTime, default=datetime.datetime.now, index=True)

    package_id: str = sa.Column(sa.String, index=True)
    release_id: int = sa.Column(sa.BigInteger, index=True)

    ip_address: str = sa.Column(sa.String)
    user_agent: str = sa.Column(sa.String)
