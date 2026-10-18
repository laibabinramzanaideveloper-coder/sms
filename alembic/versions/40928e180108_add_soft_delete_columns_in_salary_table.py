"""add_soft_delete_columns_in_salary table

Revision ID: 40928e180108
Revises: 4492495fb126
Create Date: 2026-10-12 13:17:57.834591

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '40928e180108'
down_revision: Union[str, Sequence[str], None] = '4492495fb126'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""
ALTER TABLE salary ADD COLUMN is_deleted BOOL DEFAULT FALSE;
ALTER TABLE salary ADD COLUMN deleted_at TIMESTAMP;
""")


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("""
ALTER TABLE salary
DROP COLUMN is_deleted;
ALTER TABLE salary
DROP COLUMN deleted_at;
""")
