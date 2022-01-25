"""Add last_updated column to Package cls

Revision ID: ffd2e0438799
Revises: 
Create Date: 2022-01-25 16:37:17.581161

"""
import sqlalchemy as sa
from alembic import op
from migrations.alembic import utils as alembic_utils

# revision identifiers, used by Alembic.
revision = 'ffd2e0438799'
down_revision = None
branch_labels = None
depends_on = None

TABLE, COLUMN = 'packages', 'last_updated_date'


def upgrade():
    if not alembic_utils.table_has_column(TABLE, COLUMN):
        op.add_column(TABLE,
                      sa.Column(COLUMN, sa.DateTime(),
                                nullable=True))
        op.create_index(op.f('ix_packages_last_updated_date'), TABLE,
                        [COLUMN], unique=False)


def downgrade():
    if not alembic_utils.table_has_column(TABLE, COLUMN):
        op.drop_index(op.f('ix_packages_last_updated_date'),
                      table_name=TABLE)
        op.drop_column(TABLE, COLUMN)
