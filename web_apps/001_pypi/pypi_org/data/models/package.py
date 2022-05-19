import datetime
from typing import List

import sqlalchemy as sa
import sqlalchemy.orm as orm

import settings
from data.models.modelbase import SqlAlchemyBase

STR_L = settings.STR_LENGTH


class Package(SqlAlchemyBase):
    __tablename__ = 'packages'
    
    id: str = sa.Column(sa.String(STR_L), primary_key=True)
    created_date: datetime.datetime = sa.Column(
        sa.DateTime, default=datetime.datetime.now, index=True)
    last_updated_date: datetime.datetime = sa.Column(
        sa.DateTime, default=datetime.datetime.now, index=True)
    summary: str = sa.Column(sa.String(STR_L), nullable=False)
    description: str = sa.Column(sa.String(STR_L), nullable=True)

    home_page: str = sa.Column(sa.String(STR_L))
    docs_url: str = sa.Column(sa.String(STR_L))
    package_url: str = sa.Column(sa.String(STR_L))

    author_name: str = sa.Column(sa.String(STR_L))
    author_email: str = sa.Column(sa.String(STR_L), index=True)

    license: str = sa.Column(sa.String(STR_L), index=True)

    # Releases rel
    from data.models.releases import Release
    releases: List[Release] = orm.relationship(
        # 'Release'
        Release.__name__, order_by=[
            Release.major_ver.desc(),
            Release.minor_ver.desc(),
            Release.build_ver.desc(),
        ],
        # cls Package.package - rel attr name
        back_populates='package')

    # back_populates has the same meaning as backref, except that the
    # complementing relationship property is not created automatically.
    # Using back_populates makes the model code more explicit, with
    # no hidden/implicit properties.
    # releases = orm.relationship('Release', backref='package')

    def __repr__(self):
        return '<Package {}>'.format(self.id)