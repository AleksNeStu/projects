from typing import List, Optional

import app


if app.is_sql_ver:
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


    def get_package(p_id: str, packages: orm.Query = None) -> Optional[Package]:
        packages = packages or get_packages()
        res = packages.filter(Package.id == p_id).first()
        packages.session.close()

        return res

else:
    from mongoengine import QuerySet
    from data.models_no_sql.package import Package

    def get_packages() -> QuerySet:
        return Package.objects()


    def get_latest_packages(num, packages: QuerySet = None) -> List[Package]:
        packages = packages or get_packages()
        res = packages.order_by('-created_date').limit(num).all()

        return res


    def get_package(p_id: str, packages: QuerySet = None) -> Optional[Package]:
        packages = packages or get_packages()
        res = packages.filter(id=p_id).first()

        return res