"""add_soft_delete_columns_in_subject table

Revision ID: 595e109c9ef8
Revises: 40928e180108
Create Date: 2026-10-12 19:05:56.447711

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '595e109c9ef8'
down_revision: Union[str, Sequence[str], None] = '40928e180108'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""
ALTER TABLE subject ADD COLUMN is_deleted BOOL DEFAULT FALSE;
ALTER TABLE subject ADD COLUMN deleted_at TIMESTAMP;
""")


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("""
ALTER TABLE subject
DROP COLUMN is_deleted;
ALTER TABLE subject
DROP COLUMN deleted_at;
""")
