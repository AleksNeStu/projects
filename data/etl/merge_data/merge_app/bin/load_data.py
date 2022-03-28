import csv
import datetime
import logging
import os
import sys
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
from data.models.syncs import Sync

last_sync, actual_sync, errors, parsing_results = None, None, [], {}

# Not checked enums due to ORM SA is performing that
# Not used parse module to parse expected date format to check data consistency
def get_normalized_dicts_csv_1(csv_reader):
    normalized_dicts = []
    for row in csv_reader:
        row = py_utils.DictToObj(default_val=None, **row)
        normalized_dicts.append(dict(
            date=py_utils.parse_date(
                row.timestamp, settings.DATE_FORMAT_CSV_1),
            operation_type=row.type,
            currency_type=None,
            money_amount=float(row.amount),
            sender_id=int(getattr(row, 'from')),  # registered word from
            recipient_id=int(row.to),
        ))

    return normalized_dicts

def get_normalized_dicts_csv_2(csv_reader):
    normalized_dicts = []
    for row in csv_reader:
        row = py_utils.DictToObj(default_val=None, **row)
        normalized_dicts.append(dict(
            date=py_utils.parse_date(
                row.date, settings.DATE_FORMAT_CSV_2),
            operation_type=row.transaction,
            currency_type=None,
            money_amount=float(row.amounts),
            sender_id=int(getattr(row, 'from')),  # registered word from
            recipient_id=int(row.to),
        ))

    return normalized_dicts

def get_normalized_dicts_csv_3(csv_reader):
    normalized_dicts = []
    for row in csv_reader:
        row = py_utils.DictToObj(default_val=None, **row)
        normalized_dicts.append(dict(
            date=py_utils.parse_date(
                row.date, settings.DATE_FORMAT_CSV_3),
            operation_type=row.type,
            currency_type=None,
            money_amount=float(row.amount),
            sender_id=int(getattr(row, 'from')),  # registered word from
            recipient_id=int(row.to),
        ))

    return normalized_dicts

CSV_NORMALIZATION_MAP = {
    # CSV1 format
    py_utils.get_unique_from_list_of_str(
        ['timestamp', 'type', 'amount', 'to', 'from']): get_normalized_dicts_csv_1,
    # CSV2 format
    py_utils.get_unique_from_list_of_str(
        ['date', 'transaction', 'amounts', 'to', 'from']): get_normalized_dicts_csv_2,
    # CSV3 format
    py_utils.get_unique_from_list_of_str(
        ['date_readable', 'type', 'euro', 'cents', 'to', 'from']): get_normalized_dicts_csv_3,
}


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


def get_normalized_dicts_from_csv(file_path: str) -> List[dict]:
    try:
        with open(file_path, 'r', newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            columns_unique = py_utils.get_unique_from_list_of_str(
                csv_reader.fieldnames)
            get_normalized_dicts_func = CSV_NORMALIZATION_MAP.get(
                columns_unique)
            if not get_normalized_dicts_func:
                #TODO: Add data to failed syncs to DB
                raise Exception(
                    f"Not recognized format of CSV columns, "
                    f"file: {file_path}, columns: {csv_reader.fieldnames}.")

            normalized_dicts_from_csv = get_normalized_dicts_func(csv_reader)
            return normalized_dicts_from_csv

    except Exception as err:
        logging.error(
            "Error on try to read CSV file: {}, details: {}".format(
                file_path, err))
        raise err


def get_normalized_dicts_from_input_csv_files(
        input_dir_path_part) -> List[dict]:
    input_data_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', input_dir_path_part))

    logging.info(
        "Getting input data the dir: '{}' ...".format(input_data_dir))
    file_paths = get_file_paths(input_data_dir)

    logging.info("Found {:,} file paths, loading files data...".format(
        len(file_paths)))
    all_normalized_dicts = []

    bar = progressbar.ProgressBar(maxval=len(file_paths)).start()
    for file_idx, file_path in enumerate(file_paths, start=1):
        csv_normalized_dicts = get_normalized_dicts_from_csv(file_path)
        all_normalized_dicts.extend(csv_normalized_dicts)
        bar.update(file_idx)

    sys.stderr.flush()
    sys.stdout.flush()
    logging.info("Loaded {:,} input data CSV files".format(
        len(all_normalized_dicts)))

    return all_normalized_dicts


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
            all_normalized_dicts = get_normalized_dicts_from_input_csv_files(
                input_dir_path_part=settings.INPUT_DATA_DIR)
            py_utils.set_obj_attr_values(
                actual_sync, dict(status=SyncStatus.got_data))
            session.commit()

            logging.info("Get input data is finished.")
            return all_normalized_dicts

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