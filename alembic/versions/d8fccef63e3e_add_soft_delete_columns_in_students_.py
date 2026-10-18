"""add soft delete columns in students table

Revision ID: d8fccef63e3e
Revises: 45eca143e94b
Create Date: 2026-10-11 17:11:27.696494

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd8fccef63e3e'
down_revision: Union[str, Sequence[str], None] = '45eca143e94b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""
ALTER TABLE students ADD COLUMN is_deleted BOOL DEFAULT FALSE;
ALTER TABLE students ADD COLUMN deleted_at TIMESTAMP;
""")


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("""
ALTER TABLE students
DROP COLUMN is_deleted;
ALTER TABLE students
DROP COLUMN deleted_at;

""")
