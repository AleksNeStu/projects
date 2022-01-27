import os

import sys
from alembic import command
from alembic import config

# add_module_to_sys_path
from migrations import utils as migrations_utils

directory = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, directory)

import settings
import data.db_session as db_session

def run():
    alembic_cfg = config.Config(settings.ALEMBIC_INI)
    if not migrations_utils.is_current_rev_is_latest():
        command.upgrade(alembic_cfg, 'head')


def setup_db():
    db_session.global_init(settings.DB_CONNECTION)


if __name__ == '__main__':
    run()
