import datetime
from dataclasses import dataclass

import sqlalchemy as sa
import sqlalchemy.orm as orm

from data.models.modelbase import SqlAlchemyBase
from enums.sa import CurrencyType, OperationType


# TODO: Add hashes for transactions
@dataclass
class Transaction(SqlAlchemyBase):
    __tablename__ = 'transactions'

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    date: str = sa.Column(sa.DATE, nullable=False, index=True)
    operation_type: str = sa.Column(sa.Enum(OperationType))
    currency_type: str = sa.Column(sa.Enum(CurrencyType))
    sender_id: int = sa.Column(sa.Integer, nullable=False, index=True)
    recipient_id: int = sa.Column(sa.Integer, nullable=False, index=True)

    sync_id: int = sa.Column(
        sa.Integer, sa.ForeignKey('syncs.id'), nullable=False, index=True)

    created_date: datetime.datetime = sa.Column(
        sa.DateTime, default=datetime.datetime.utcnow)
    updated_date: datetime.datetime = sa.Column(sa.DateTime, nullable=True)

    sync = orm.relationship('Sync')