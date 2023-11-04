import datetime

import sqlalchemy as sa

from data.models.modelbase import SqlAlchemyBase


class Audit(SqlAlchemyBase):
    __tablename__ = 'audit'

    id: str = sa.Column(sa.String, primary_key=True)
    created_date: datetime.datetime = sa.Column(
        sa.DateTime, default=datetime.datetime.now, index=True)
    description: str = sa.Column(sa.String)
