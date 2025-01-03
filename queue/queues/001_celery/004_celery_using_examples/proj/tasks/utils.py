import csv
import datetime
import os
from os.path import isfile, join
from time import mktime


def is_exists(filename):
    return os.path.isfile(filename)


def make_csv(filename, lines):
    dirname = os.path.dirname(filename)
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    with open(filename, 'w') as csvfile:
        trending_csv = csv.writer(csvfile)
        for line in lines:
            trending_csv.writerow(line)
    return filename


def strf_date(mixed_date, ref_date=None):
    dt_str = None
    if ref_date is None:
        ref_date = datetime.date.today()
    if mixed_date in ('day', 'week', 'month'):
        delta = None
        if mixed_date == 'day':
            delta = datetime.timedelta(days=1)
        elif mixed_date == 'week':
            delta = datetime.timedelta(weeks=1)
        else:
            delta = datetime.timedelta(days=30)
        dt_str = (ref_date - delta).isoformat()

    elif type(ref_date) in (str,):
        dt_str = ref_date

    elif type(ref_date) in (datetime.date, datetime.datetime):
        dt_str = ref_date.isoformat()
    return dt_str


def list_files(folder):
    err_files = [(folder, f) for f in os.listdir(folder) if isfile(join(folder, f))]
    return err_files


def interval_timestamp(interval, t=None):
    if t is None:
        t = ts()
    return t - (t % interval)


def ts():
    return int(mktime(datetime.datetime.utcnow().timetuple()))
