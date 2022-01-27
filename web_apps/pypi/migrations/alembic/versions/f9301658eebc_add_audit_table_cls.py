"""Add Audit table cls

Revision ID: f9301658eebc
Revises: ffd2e0438799
Create Date: 2022-01-25 18:09:17.960504

"""
import sqlalchemy as sa
from alembic import op
from migrations import utils as migrations_utils

# revision identifiers, used by Alembic.
revision = 'f9301658eebc'
down_revision = 'ffd2e0438799'
branch_labels = None
depends_on = None

TABLE = 'audit'

def upgrade():
    if not migrations_utils.has_table(TABLE):
        op.create_table(TABLE,
                        sa.Column('id', sa.String(), nullable=False),
                        sa.Column('created_date', sa.DateTime(),
                                  nullable=True),
                        sa.Column('description', sa.String(), nullable=True),
                        sa.PrimaryKeyConstraint('id')
                        )
        op.create_index(op.f('ix_audit_created_date'), TABLE,
                        ['created_date'],
                        unique=False)


def downgrade():
    if migrations_utils.has_table(TABLE):
        op.drop_index(op.f('ix_audit_created_date'), table_name=TABLE)
        op.drop_table(TABLE)