import sqlalchemy as sa

from data.models.modelbase import SqlAlchemyBase


class Maintainer(SqlAlchemyBase):
    __tablename__ = 'maintainers'

    user_id: int = sa.Column(sa.Integer, primary_key=True)
    package_id: str = sa.Column(sa.String, primary_key=True)
