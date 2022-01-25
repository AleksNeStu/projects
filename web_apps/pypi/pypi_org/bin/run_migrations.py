import os

import sys
from alembic import command
from alembic import context
from alembic.config import Config

# add_module_to_sys_path
directory = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, directory)

import settings
import data.db_session as db_session


def run():
    alembic_cfg = Config(settings.ALEMBIC_INI)
    command.upgrade(alembic_cfg, 'head')


def setup_db():
    db_session.global_init(settings.DB_CONNECTION)


if __name__ == '__main__':
    run()
