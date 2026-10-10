"""create students table

Revision ID: 65d2e9385713
Revises: ca67e5efac88
Create Date: 2026-10-10 12:30:54.525401

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '65d2e9385713'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    student_name VARCHAR(100),
    phone_number VARCHAR(15),
    fees INT 
);
""")

def downgrade() -> None:
    """Downgrade schema."""
    op.execute("""DROP TABLE students""")
