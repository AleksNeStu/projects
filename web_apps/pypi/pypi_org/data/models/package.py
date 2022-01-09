import datetime

import sqlalchemy as sa

import settings
from data.models.modelbase import SqlAlchemyBase


STR_L = settings.STR_LENGTH


class Package(SqlAlchemyBase):
    __tablename__ = 'packages'
    
    id: str = sa.Column(sa.String(STR_L), primary_key=True)
    created_date: datetime.datetime = sa.Column(
        sa.DateTime, default=datetime.datetime.now, index=True)
    summary: str = sa.Column(sa.String(STR_L), nullable=False)
    description: str = sa.Column(sa.String(STR_L), nullable=True)

    home_page: str = sa.Column(sa.String(STR_L))
    docs_url: str = sa.Column(sa.String(STR_L))
    package_url: str = sa.Column(sa.String(STR_L))

    author_name: str = sa.Column(sa.String(STR_L))
    author_email: str = sa.Column(sa.String(STR_L), index=True)

    license: str = sa.Column(sa.String(STR_L), index=True)

    # maintainers
    # releases

    def __repr__(self):
        return '<Package {}>'.format(self.id)