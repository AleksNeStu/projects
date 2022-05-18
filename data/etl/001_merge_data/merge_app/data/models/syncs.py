import datetime
import json
from dataclasses import dataclass
from typing import List, Text

import sqlalchemy as sa
import sqlalchemy.orm as orm

from data.models.modelbase import SqlAlchemyBase
from enums.sa import SyncStatus, SyncEndReason, NotSyncedItemReason, SyncType


@dataclass
class NotSyncedItem(SqlAlchemyBase):
    __tablename__ = 'not_synced_items'
    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    sync_id: int = sa.Column(
        sa.Integer, sa.ForeignKey('syncs.id'), nullable=False, index=True)
    item_data: Text = sa.Column(sa.JSON, nullable=False)
    reason: str = sa.Column(sa.Enum(NotSyncedItemReason), nullable=False)

    sync = orm.relationship('Sync')


@dataclass
class Sync(SqlAlchemyBase):
    __tablename__ = 'syncs'

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    start_date: datetime.datetime = sa.Column(
        sa.DateTime, index=True, nullable=False)
    end_date: datetime.datetime = sa.Column(
        sa.DateTime, index=True)
    status: str = sa.Column(sa.Enum(SyncStatus), nullable=False)
    resp_headers: str = sa.Column(sa.JSON, default=json.dumps({}))
    parsing_results: str = sa.Column(sa.JSON, default=json.dumps({}))
    errors: str = sa.Column(sa.JSON, default=json.dumps([]))
    end_reason: str = sa.Column(sa.Enum(SyncEndReason))
    type: str = sa.Column(sa.Enum(SyncType))

    # extracted transactions per sync
    from data.models.transactions import Transaction
    transactions: List[Transaction] = orm.relationship(
        Transaction.__name__, back_populates='sync', order_by=[
            Transaction.sender_id.desc(), Transaction.operation_type.desc(),
        ])

    # not synced items (transactions) per sync
    not_synced_items: List[NotSyncedItem] = orm.relationship(
        NotSyncedItem.__name__, back_populates='sync')