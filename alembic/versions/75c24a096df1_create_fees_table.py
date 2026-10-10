"""create fees table

Revision ID: 75c24a096df1
Revises: 65d2e9385713
Create Date: 2026-10-10 12:42:23.943627

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '75c24a096df1'
down_revision: Union[str, Sequence[str], None] = '65d2e9385713'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""
CREATE TABLE fees (
    id SERIAL PRIMARY KEY,
    student_id INT REFERENCES students(id),
    amount INT 
);    
""")
# student_id, amount

def downgrade() -> None:
    """Downgrade schema."""
    op.execute("""DROP TABLE fees""")
