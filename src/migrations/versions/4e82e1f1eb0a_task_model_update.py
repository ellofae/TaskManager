"""task model update

Revision ID: 4e82e1f1eb0a
Revises: fb3b86bcdcca
Create Date: 2023-09-03 23:13:31.571987

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '4e82e1f1eb0a'
down_revision: Union[str, None] = 'fb3b86bcdcca'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('created_by', sa.Integer(), nullable=False))
    op.drop_column('tasks', 'user_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_column('tasks', 'created_by')
    # ### end Alembic commands ###
