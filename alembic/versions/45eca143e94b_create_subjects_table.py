"""create subjects table

Revision ID: 45eca143e94b
Revises: d6755e29194c
Create Date: 2026-10-10 13:38:36.196756

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '45eca143e94b'
down_revision: Union[str, Sequence[str], None] = 'd6755e29194c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""
CREATE TABLE subject (
    id SERIAL PRIMARY KEY,
    subject_name VARCHAR (45),
    teacher_name VARCHAR (67)
);    
""")


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("""DROP TABLE subjects""")
