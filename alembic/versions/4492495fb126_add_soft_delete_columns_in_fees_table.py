"""add_soft_delete_columns_in fees table

Revision ID: 4492495fb126
Revises: 59ec8265db1f
Create Date: 2026-10-12 12:13:02.527857

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4492495fb126'
down_revision: Union[str, Sequence[str], None] = '59ec8265db1f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""
ALTER TABLE fees ADD COLUMN is_deleted BOOL DEFAULT FALSE;
ALTER TABLe fees ADD COLUMN deleted_at TIMESTAMP;
""")


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("""
ALTER TABLE fees
DROP COLUMN is_deleted;
ALTER TABLE fees
DROP COLUMN deleted_at;

""")
