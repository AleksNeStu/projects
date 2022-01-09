import datetime

import sqlalchemy as sa

import settings
from data.models.modebase import SQLAlchemyBase


STR_L = settings.STR_LENGTH


class Package(SQLAlchemyBase):
    __tablename__ = 'packages'
    
    id = sa.Column(sa.String(STR_L), primary_key=True)
    created_date = sa.Column(
        sa.DateTime, default=datetime.datetime.now, index=True)
    summary = sa.Column(sa.String(STR_L), nullable=False)
    description = sa.Column(sa.String(STR_L), nullable=True)

    home_page = sa.Column(sa.String(STR_L))
    docs_url = sa.Column(sa.String(STR_L))
    package_url = sa.Column(sa.String(STR_L))

    author_name = sa.Column(sa.String(STR_L))
    author_email = sa.Column(sa.String(STR_L), index=True)

    license = sa.Column(sa.String(STR_L), index=True)

    # maintainers
    # releases

    def __repr__(self):
        return '<Package {}>'.format(self.id)