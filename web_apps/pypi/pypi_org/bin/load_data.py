import json
import logging
import os
import re
import sys
import time
from typing import List, Dict, Optional

# noinspection PyPackageRequirements,PyPackageRequirements
import progressbar
import sqlalchemy.orm as orm
from dateutil import parser

# add_module_to_sys_path
directory = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, directory)

import settings
import data.db_session as db_session
from data.models.users import User
from data.models.package import Package
from data.models.maintainers import Maintainer
from data.models.releases import Release
from utils import py as py_utils


def main():
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    init_db()

    with db_session.create_session() as session:
        user_count = session.query(User).count()

    if user_count == 0:
        packages_data: List[dict] = load_top_packages_data_from_json_files(
            'top_packages')

        users_data: dict = get_users_data_from_packages_data(packages_data)

        db_users_map: Dict[str, User] = insert_users_data_to_db(
                users_data, in_bulk=False)
        # further will be skipped bulk processing
        db_packages_map: Dict[str, Package] = insert_packages_to_db(
            db_users_map, packages_data)

    #     do_import_languages(packages_data)
    #     do_import_licenses(packages_data)
    #
    # do_summary()


def load_top_packages_data_from_json_files(
        packages_dir_path_part) -> List[dict]:
    top_packages_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), packages_dir_path_part))

    logging.info(
        "Loading top packages json data from the dir: '{}' ...".format(
            top_packages_dir))
    file_paths = get_file_paths(top_packages_dir)

    logging.info("Found {:,} file paths, loading files data...".format(
        len(file_paths)))
    time.sleep(1)
    files_data = []

    with progressbar.ProgressBar(max_value=len(file_paths)) as bar:

        for file_idx, file_path in enumerate(file_paths, start=1):
            files_data.append(load_file_data(file_path))
            bar.update(file_idx)

    sys.stderr.flush()
    sys.stdout.flush()
    logging.info("Loaded {:,} top packages json files".format(
        len(files_data)))

    return files_data


def get_file_paths(files_dir_path: str) -> List[str]:
    file_paths = []

    for f_name in os.listdir(files_dir_path):
        if f_name.endswith('.json'):
            file_paths.append(
                os.path.abspath(os.path.join(files_dir_path, f_name)))

    return sorted(file_paths)


def load_file_data(file_path: str) -> dict:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as err:
        logging.error(
            "Error on try to deserialize JSON file: {}, details: {}".format(
                  file_path, err))
        raise err


def get_users_data_from_packages_data(packages_data: List[dict]) -> dict:
    logging.info("Getting users data from the packages data ...")
    got_users_data = {}

    with progressbar.ProgressBar(max_value=len(packages_data)) as bar:
        for package_idx, package_data in enumerate(packages_data, start=1):
            p_info = package_data.get('info')
            got_users_data.update(
                get_email_and_name_from_package_info(
                    p_info, email_name_map={
                        'author_email': 'author',
                        'maintainer_email': 'maintainer',
                    }))
            bar.update(package_idx)

    sys.stderr.flush()
    sys.stdout.flush()
    logging.info("Got {:,} users data items".format(len(got_users_data)))

    return got_users_data

def get_email_and_name_from_package_info(
        package_info: dict, email_name_map: dict) -> dict:
    got_email_name = {}

    for e, n in email_name_map.items():
        email = package_info.get(e)
        name = package_info.get(n)
        if {email, name}.intersection({'', None}):
            continue

        else:
            emails = re.split(', |;', email.strip().lower())
            if all(py_utils.is_email_valid(e) for e in emails):
                names = re.split(', |;', name.strip().lower())
                if len(emails) > len(names):
                    logging.error(
                        "Error [Different length]: length of emails: '{}' should "
                        "be >= names: '{}', package info: '{}'. ".format(
                            emails, names, package_info))
                    raise Exception

                for email, name in zip(emails, names):
                    got_email_name[email.strip()] = name.strip()

    return got_email_name


def insert_users_data_to_db(users_data: Dict[str, str],
                            in_bulk:bool = False) -> Dict[str, User]:
    logging.info("Inserting users data to DB [in_bulk]={}...".format(in_bulk))
    users_count = len(users_data)

    if not in_bulk:
        with db_session.create_session() as session:
            with progressbar.ProgressBar(max_value=users_count) as bar:

                for user_data_idx, (u_email, u_name) in enumerate(
                        users_data.items(), start=1):
                    u = User(name=u_name, email=u_email)
                    session.add(u)
                    session.commit()
                    # sqlalchemy.orm.exc.DetachedInstanceError: Instance
                    # <User at 0x7f9f7b3caa40> is not bound to a Session; attribute
                    # refresh operation cannot proceed (Background on this error at:
                    # https://sqlalche.me/e/14/bhk3)
                    # inserted_users[u_email] = u
                    # fix:
                    # inserted_users = {u.email: u for u in session.query(User)}
                    bar.update(user_data_idx)
    else:
        with db_session.create_session() as session:
            session.bulk_insert_mappings(
                User, [dict(name=u_name, email=u_email)
                       for u_email, u_name in users_data.items()])
            # session.add_all([User()])
            session.commit()

    sys.stderr.flush()
    sys.stdout.flush()

    inserted_users = {u.email: u for u in session.query(User)}
    logging.info("Inserted {:,} users to DB".format(len(inserted_users)))
    return inserted_users


def insert_packages_to_db(db_users_map: Dict[str, User],
                          packages_data: List[dict]) -> Dict[str, Package]:
    logging.info("Inserting packages to DB ...")
    packages_count = len(packages_data)
    inserted_packages = {}
    not_inserted_packages = []

    with db_session.create_session() as session:
        with progressbar.ProgressBar(max_value=len(packages_data)) as bar:
            for package_idx, package_data in enumerate(packages_data, start=1):
                try:
                    db_package_map = insert_package_data_to_db(
                        session, db_users_map, package_data)
                    if db_package_map:
                        inserted_packages.update(db_package_map)
                    else:
                        not_inserted_packages.append(package_data)
                    bar.update(package_idx)
                except Exception as err:
                    logging.error(
                        "Error on try to insert package data to DB: {}, "
                        "details: {}".format(package_data, err))
                    not_inserted_packages.append(
                        {package_data.get('package_name'): err})
                    raise err

    sys.stderr.flush()
    sys.stdout.flush()

    inserted_packages = {p.id: p for p in session.query(Package)}
    logging.info(
        "All {:,}, inserted {:,}, not inserted {:,} packages to DB "
        "[not inserted packages details: {}]".format(
            packages_count, len(inserted_packages),
            len(not_inserted_packages), not_inserted_packages))

    return inserted_packages


def insert_package_data_to_db(
        session: orm.Session, db_users_map: Dict[str, User],
        package: Dict) -> Dict[str, Package]:
    try:
        # Package start
        p_info = package.get('info', {})
        p = Package(id=package.get('package_name', '').strip())
        p_id = p.id
        if not p_id:
            return {}

        # Releases
        p_releases = sorted(build_package_releases(
            p_id, package.get("releases", {})),
            key=lambda r: r.created_date)
        if p_releases:
            p.created_date = p_releases[0].created_date

        # Maintainers
        p_maintainers = build_package_maintainers(
            p_id, p_info, db_users_map)

        # Package end
        py_utils.set_obj_attr_values(
            p, p_info, [
                'summary', 'description', 'home_page', 'docs_url',
                'package_url', 'author', 'author_email', 'license',
            ])
        p.license = detect_license(p_info.get('license'))

        session.add(p)
        session.add_all(p_releases)
        if p_maintainers:
            session.add_all(p_maintainers)
        session.commit()

        return dict(p_id=p)

    except OverflowError:
        # Arithmetic operation has exceeded the limits of the current Python
        pass
    except Exception as err:
        raise err


def build_package_releases(package_id: str,
                           package_releases_data: dict) -> List[Release]:
    return [
        Release(
            package_id=package_id,
            created_date=parser.parse(r_ver_m.get('upload_time')),
            comment=r_ver_m.get('comment_text'),
            url=r_ver_m.get('url'),
            size=int(r_ver_m.get('size', 0)),
            **get_release_version_map(r_ver_num)
        )
        for r_ver_num, r_ver_meta in package_releases_data.items()
        if (r_ver_meta and (r_ver_m := r_ver_meta[-1]))]


def get_release_version_map(p_version_num: str) -> dict:
    p_version_num = ''.join([p for p in p_version_num if p not in ['a', 'b']])
    p_version_num_parts = p_version_num.split('.')
    p_version_num_parts.extend([0, 0, 0])

    return {
        'major_ver': py_utils.str_to_int(p_version_num_parts[0]),
        'minor_ver': py_utils.str_to_int(p_version_num_parts[1]),
        'build_ver': py_utils.str_to_int(p_version_num_parts[2]),
    }


def build_package_maintainers(
        package_id: str, package_info: dict,
        db_users_map: Dict[str, User]) -> List[Maintainer]:
    p_maintainers_data = (
        get_email_and_name_from_package_info(
            package_info, email_name_map={
                'maintainer_email': 'maintainer',
            }))
    return [
        Maintainer(
            package_id=package_id,
            user_id=maintainer_user.id,
        )
        for p_maintainer_email, p_maintainer_name in p_maintainers_data.items()
        if (maintainer_user := db_users_map.get(p_maintainer_email))]


# TODO: Refactor
def detect_license(license_text: str) -> Optional[str]:
    if not license_text:
        return None

    license_text = license_text.strip()

    if len(license_text) > 100 or '\n' in license_text:
        return "CUSTOM"

    license_text = license_text \
        .replace('Software License', '') \
        .replace('License', '')

    if '::' in license_text:
        # E.g. 'License :: OSI Approved :: Apache Software License'
        return license_text \
            .split(':')[-1] \
            .replace('  ', ' ') \
            .strip()

    return license_text.strip()


def init_db():
    db_session.global_init(settings.DB_CONNECTION)


if __name__ == '__main__':
    main()
