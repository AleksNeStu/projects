import csv
import datetime
import logging
import os
import sys
import time
from typing import List, Optional

# noinspection PyPackageRequirements,PyPackageRequirements
import progressbar
from codetiming import Timer

# add_module_to_sys_path
directory = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, directory)

import settings
import data.db_session as db_session
from enums.sa import SyncStatus, SyncEndReason, SyncType
from utils import py as py_utils
from data.models.syncs import Sync, NotSyncedItem


last_sync, actual_sync, errors, parsing_results = None, None, [], {}


def run(sync_type, forced=False):
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    logging.info("Sync data from input source is started.")
    actual_sync_kwargs = {}
    sync = None

    setup_db()

    with db_session.create_session() as session:
        input_data = get_input_data(session, forced, sync_type)
    if input_data:
        pass


    logging.info("Sync data from input source is finished.")


def get_file_paths(files_dir_path: str) -> List[str]:
    file_paths = []

    for f_name in os.listdir(files_dir_path):
        if f_name.endswith(('.csv', '.CSV')):
            file_paths.append(
                os.path.abspath(os.path.join(files_dir_path, f_name)))

    return sorted(file_paths)


def read_csv_file_data(file_path: str) -> dict:
    try:
        with open(file_path, 'r', newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            dict_from_csv = dict(list(csv_reader)[0])
            return dict_from_csv

    except Exception as err:
        logging.error(
            "Error on try to read CSV file: {}, details: {}".format(
                file_path, err))
        raise err


def get_input_data_from_csv_files(input_dir_path_part) -> List[dict]:
    input_data_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', input_dir_path_part))

    logging.info(
        "Getting input data the dir: '{}' ...".format(input_data_dir))
    file_paths = get_file_paths(input_data_dir)

    logging.info("Found {:,} file paths, loading files data...".format(
        len(file_paths)))
    files_data = []

    bar = progressbar.ProgressBar(maxval=len(file_paths)).start()
    for file_idx, file_path in enumerate(file_paths, start=1):
        files_data.append(read_csv_file_data(file_path))
        bar.update(file_idx)

    sys.stderr.flush()
    sys.stdout.flush()
    logging.info("Loaded {:,} input data CSV files".format(len(files_data)))

    return files_data


def is_new_input_data(session, forced, sync_type):
    global last_sync, actual_sync, errors
    actual_sync = Sync(
        start_date=datetime.datetime.now(),
        status=SyncStatus.started,
        type=sync_type,
    )
    session.add(actual_sync)

    #TODO: Implement
    session.commit()

    res = True
    logging.info(f"Is new input data for sync: {res}.")

    return res


@Timer(text=f"Time consumption for {'get_input_data'}: {{:.3f}}")
def get_input_data(session, forced, sync_type) -> Optional[List[dict]]:
    global last_sync, actual_sync, errors, parsing_results

    logging.info("Get input data is started.")
    if is_new_input_data(session, forced, sync_type):
        parsing_results.update({
            'sync_id': actual_sync.id,
            'sync_type': sync_type,
        })
        actual_sync_kwargs = {}
        try:
            input_data = get_input_data_from_csv_files(
                input_dir_path_part=settings.INPUT_DATA_DIR)
            py_utils.set_obj_attr_values(
                actual_sync, dict(status=SyncStatus.got_data))
            session.commit()

            logging.info("Get input data is finished.")
            return input_data

        except Exception as err:
            error_msg = (
                f'Error on try to get input data: {err}')
            errors.append(error_msg)
            logging.error(error_msg)

            actual_sync_kwargs.update(**dict(
                end_date=datetime.datetime.now(),
                status=SyncStatus.errors,
                end_reason=SyncEndReason.get_data_errors,
                parsing_results=parsing_results,
            ))
            py_utils.set_obj_attr_values(actual_sync, actual_sync_kwargs)
            py_utils.update_obj_attr_values(
                actual_sync, dict(errors=[error_msg]))
            session.commit()

    logging.info("Get input data is finished.")
    return


def setup_db():
    logging.info("Init db.")
    db_session.init_sql(settings.DB_CONNECTION)


if __name__ == '__main__':
    run(sync_type=SyncType.manual.value)