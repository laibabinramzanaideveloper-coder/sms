"""create employees table

Revision ID: dae9c3268697
Revises: 75c24a096df1
Create Date: 2026-10-10 13:04:48.277084

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dae9c3268697'
down_revision: Union[str, Sequence[str], None] = '75c24a096df1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    employee_name VARCHAR(100),
    phone_number VARCHAR(15),
    work VARCHAR (19),
    education VARCHAR (45),
    date_of_birth TIMESTAMP,
    father_name VARCHAR (44),
    year TIMESTAMP,
    role VARCHAR (66) 
);
""")

                    #   ( employee_name,phone_number,work,education,date_of_birth,father_name,year,role,uu_id)
def downgrade() -> None:
    """Downgrade schema."""
    op.execute("""DROP TABLE employees""")
