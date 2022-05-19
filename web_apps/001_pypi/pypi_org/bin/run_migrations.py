import os

import sys
from alembic import command
from alembic import config

directory = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, directory)
import settings
import data.db_session as db_session

directory = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../..'))
sys.path.insert(0, directory)
from migrations import utils as migrations_utils

def run():
    alembic_cfg = config.Config(settings.ALEMBIC_INI)
    if not migrations_utils.is_current_rev_is_latest():
        command.upgrade(alembic_cfg, 'head')


def setup_db():
    db_session.init_sql(settings.DB_CONNECTION)


if __name__ == '__main__':
    run()
