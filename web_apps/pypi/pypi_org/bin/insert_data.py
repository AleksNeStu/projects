import logging
import os
import sys

import settings

# add_module_to_sys_path
directory = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, directory)

from data import db_session
from data.models.package import Package
from data.models.releases import Release

PACKAGES = [
    {
        'id': 'flask',
        'author_name': 'Flask Author',
        'author_email': 'flask@dev.com',
        'summary': 'Flask summary',
        'license': 'MIT',
        'releases': [
            {
                'major_ver': 1,
                'minor_ver': 2,
                'build_ver': 3,
                'size': 523,
            },
            {
                'major_ver': 4,
                'minor_ver': 5,
                'build_ver': 6,
                'size': 5236,
            },
        ],
    },
    {
        'id': 'sqlalchemy',
        'author_name': 'SQLAlchemy Author',
        'author_email': 'sqlalchemy@dev.com',
        'summary': 'SQLAlchemy summary',
        'license': 'MIT',
        'releases': [
            {
                'major_ver': 7,
                'minor_ver': 8,
                'build_ver': 9,
                'size': 5223,
            },
        ],
    },
]


def main():
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    init_db()


def init_db():
    db_session.global_init(settings.DB_CONNECTION)
    insert_package()


def insert_package():
    # session: orm.Session = db_session.session()
    with db_session.create_session() as session:

        for package in PACKAGES:
            # package
            p = Package()
            p_items = package.items()
            logging.info('Inserting "{}" items: {}.'.format(
                Package.__name__, p_items))
            for k, v in package.items():
                is_releases = k == 'releases'
                if not is_releases:
                    setattr(p, k, v)

                if is_releases:
                    # package releases
                    releases = v
                    for release in releases:
                        r = Release()
                        r_items = release.items()
                        logging.info(
                            'Inserting "{}" items: {}.'.format(
                                Release.__name__, r_items))
                        for k, v in release.items():
                            setattr(r, k, v)

                        p.releases.append(r)

            session.add(p)

        session.commit()


if __name__ == '__main__':
    main()