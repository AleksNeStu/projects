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

    # Package rel
    # from data.models.package import Package
    package_id: int = sa.Column(sa.Integer, sa.ForeignKey('packages.id'))
    package = orm.relationship('Package')

    @property
    def version_text(self):
        return '{}.{}.{}'.format(
            self.major_ver, self.minor_ver, self.build_ver)