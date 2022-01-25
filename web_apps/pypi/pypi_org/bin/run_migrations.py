import os

import sys
from alembic import command
from alembic import config

# add_module_to_sys_path
from migrations.alembic import utils as alembic_utils

directory = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, directory)

import settings
import data.db_session as db_session

def run():
    alembic_cfg = config.Config(settings.ALEMBIC_INI)
    if not alembic_utils.is_migration_latest_rev():
        command.upgrade(alembic_cfg, 'head')


def setup_db():
    db_session.global_init(settings.DB_CONNECTION)


if __name__ == '__main__':
    run()
