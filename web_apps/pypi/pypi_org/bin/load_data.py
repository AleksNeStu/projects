import json
import logging
import os
import re
import sys
import time
from typing import List, Dict

# noinspection PyPackageRequirements,PyPackageRequirements
import progressbar

# add_module_to_sys_path
directory = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, directory)

import settings
import data.db_session as db_session
from data.models.users import User
from utils import py as py_utils

def main():
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    init_db()

    with db_session.session() as session:
        user_count = session.query(User).count()

    if user_count == 0:
        packages_data: List[dict] = load_top_packages_data_from_json_files(
            'top_packages')

        users_data: dict = get_users_data_from_packages_data(packages_data)

        db_users = insert_users_data(users_data)
    #     do_import_packages(packages_data, db_users)
    #
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
        for package_id, package_data in enumerate(packages_data, start=1):
            p_info = package_data.get('info')
            email_name_map = {
                'author_email': 'author',
                'maintainer_email': 'maintainer',
            }
            got_users_data.update(
                get_email_and_name_from_package_info(p_info, email_name_map))
            bar.update(package_id)

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


def insert_users_data(users_data: Dict[str, str]) -> Dict[str, User]:
    logging.info("Inserting users data to DB ...")

    with db_session.session(expire_on_commit=True) as session:
        num_users = len(users_data)
        with progressbar.ProgressBar(max_value=num_users) as bar:

            for user_data_idx, (u_email, u_name) in enumerate(
                    users_data.items(), start=1):
                u = User(name=u_name, email=u_email)
                session.add(u)
                session.commit()
                bar.update(user_data_idx)

    sys.stderr.flush()
    sys.stdout.flush()
    logging.info("Inserted {:,} users to DB".format(num_users))

    return {u.email: u for u in session.query(User)}


def init_db():
    db_session.global_init(settings.DB_CONNECTION)


if __name__ == '__main__':
    main()
