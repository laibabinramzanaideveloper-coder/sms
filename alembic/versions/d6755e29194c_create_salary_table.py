"""create salary table

Revision ID: d6755e29194c
Revises: dae9c3268697
Create Date: 2026-10-10 13:35:25.077603

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd6755e29194c'
down_revision: Union[str, Sequence[str], None] = 'dae9c3268697'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""
CREATE TABLE salary (
    id SERIAL PRIMARY KEY,
    employee_id INT REFERENCES employees(id),
    amount INT 
);    
""")


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("""DROP TABLE salary""")
