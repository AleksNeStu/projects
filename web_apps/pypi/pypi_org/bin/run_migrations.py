import os

import sys
from alembic import command
from alembic import config
from alembic import migration

# add_module_to_sys_path
directory = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, directory)

import settings
import data.db_session as db_session

def is_migration_latest_rev():
    engine = db_session.create_engine()
    conn = engine.connect()
    context = migration.MigrationContext.configure(conn)
    #TODO: Add example with getting current_rev from DB via SA
    current_rev = context.get_current_revision()
    current_heads = context.get_current_heads()
    return current_rev in current_heads

def run():
    alembic_cfg = config.Config(settings.ALEMBIC_INI)
    if not is_migration_latest_rev():
        command.upgrade(alembic_cfg, 'head')


def setup_db():
    db_session.global_init(settings.DB_CONNECTION)


if __name__ == '__main__':
    run()
