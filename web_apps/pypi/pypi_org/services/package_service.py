from typing import List, Optional

import sqlalchemy.orm as orm

from data import db_session
from data.models.package import Package


def get_packages() -> orm.Query:
    with db_session.create_session() as session:
        return session.query(Package).options(
            orm.joinedload(Package.releases))


def get_latest_packages(num, packages: orm.Query = None) -> List[Package]:
    packages = packages or get_packages()
    res = packages.order_by(Package.created_date.desc()).limit(num).all()
    packages.session.close()

    return res


def get_package(id: str, packages: orm.Query = None) -> Optional[Package]:
    packages = packages or get_packages()
    res = packages.filter(Package.id == id).first()
    packages.session.close()

    return res