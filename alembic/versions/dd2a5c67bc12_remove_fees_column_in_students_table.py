"""remove_fees_column_in_students table

Revision ID: dd2a5c67bc12
Revises: 595e109c9ef8
Create Date: 2026-10-14 13:30:09.484818

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dd2a5c67bc12'
down_revision: Union[str, Sequence[str], None] = '595e109c9ef8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""ALTER TABLE students
DROP COLUMN fees;""")


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("""ALTER TABLE students
      ADD COLUMN fees int;""")
