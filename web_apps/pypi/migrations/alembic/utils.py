import sqlalchemy as sa
from alembic import migration
from alembic import op

import pypi_org.data.db_session as db_session


def get_insp(from_alembic=True):
    if from_alembic:
        config = op.get_context().config
        engine = sa.engine_from_config(
            config.get_section(
                config.config_ini_section), prefix='sqlalchemy.')
        return sa.engine.reflection.Inspector.from_engine(engine)

    else:
        engine = db_session.create_engine()
        return sa.inspect(engine)


def is_current_rev_is_latest():
    # using alembic context
    engine = db_session.create_engine()
    conn = engine.connect()
    context = migration.MigrationContext.configure(conn)
    #TODO: Add example with getting current_rev from DB via SA
    current_rev = context.get_current_revision()
    current_heads = context.get_current_heads()

    alembic_version_row = conn.execute('SELECT * FROM alembic_version').one()
    current_rev_sa = alembic_version_row['version_num']

    assert current_rev == current_rev_sa

    return current_rev in current_heads

def table_has_column(table, column):
    insp = get_insp()
    column_names = [c['name'] for c in insp.get_columns(table)]
    return column in column_names

def has_table(table):
    insp = get_insp()
    return insp.has_table(table)