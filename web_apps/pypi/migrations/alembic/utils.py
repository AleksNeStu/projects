from alembic import migration

import data.db_session as db_session


def is_migration_latest_rev():
    engine = db_session.create_engine()
    conn = engine.connect()
    context = migration.MigrationContext.configure(conn)
    #TODO: Add example with getting current_rev from DB via SA
    current_rev = context.get_current_revision()
    current_heads = context.get_current_heads()
    return current_rev in current_heads