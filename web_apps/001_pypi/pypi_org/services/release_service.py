from typing import List

import app


if app.is_sql_ver:
    import sqlalchemy.orm as orm
    from data import db_session
    from data.models.releases import Release

    def get_releases() -> orm.Query:
        with db_session.create_session() as session:
            return session.query(Release).options(orm.joinedload(Release.package))


    def get_latest_releases(num, releases: orm.Query = None) -> List[Release]:
        releases = releases or get_releases()

        # if simulate will be an err: https://sqlalche.me/e/14/bhk3
        # fix is: options(orm.joinedload(Release.package))
        # releases.session.close()

        res = releases.order_by(Release.created_date.desc()).limit(num).all()
        releases.session.close()

        return res

else:
    from mongoengine import QuerySet
    from data.models_no_sql.releases import Release

    def get_releases() -> QuerySet:
        return Release.objects()


    def get_latest_releases(num, releases: QuerySet = None) -> List[Release]:
        releases = releases or get_releases()
        return releases.order_by('-created_date').limit(num).all()