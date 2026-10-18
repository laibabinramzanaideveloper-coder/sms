"""add_soft_delete_columns_in_employees table

Revision ID: 59ec8265db1f
Revises: d8fccef63e3e
Create Date: 2026-10-11 20:58:20.003859

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '59ec8265db1f'
down_revision: Union[str, Sequence[str], None] = 'd8fccef63e3e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""
ALTER TABLE employees ADD COLUMN is_deleted BOOL DEFAULT FALSE;
ALTER TABLE employees ADD COLUMN deleted_at TIMESTAMP;
""")


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("""
ALTER TABLE employees
DROP COLUMN is_deleted;
ALTER TABLE employees
DROP COLUMN deleted_at;

""")
