import json
import logging
import os
import sys
import time
from typing import List, Optional, Dict

# noinspection PyPackageRequirements,PyPackageRequirements
import progressbar
from dateutil.parser import parse

# add_module_to_sys_path
directory = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, directory)

import settings
from utils import py as py_utils
import data.db_session as db_session
from data.models.languages import ProgrammingLanguage
from data.models.licenses import License
from data.models.maintainers import Maintainer
from data.models.package import Package
from data.models.releases import Release
from data.models.users import User


def main():
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    init_db()

    session = db_session.create_session()
    user_count = session.query(User).count()
    session.close()

    if user_count == 0:
        packages_data: List[dict] = load_top_packages_data_from_json_files(
            'top_packages')

    #     users = find_users(packages_data)
    #
    #     db_users = do_user_import(users)
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

    logging.info("Loading top packages json data from the dir: '{}'".format(
        top_packages_dir))
    file_paths = get_file_paths(top_packages_dir)
    logging.info("Found {:,} files, loading ...".format(len(file_paths)))
    time.sleep(.1)

    files_data = []
    with progressbar.ProgressBar(max_value=len(file_paths)) as bar:
        for file_id, file_path in enumerate(file_paths, start=1):
            files_data.append(load_file_data(file_path))
            bar.update(file_id)

    sys.stderr.flush()
    sys.stdout.flush()

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


def init_db():
    db_session.global_init(settings.DB_CONNECTION)


if __name__ == '__main__':
    main()
