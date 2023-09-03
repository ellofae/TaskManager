"""task model update

Revision ID: fb3b86bcdcca
Revises: 265f7a0a7288
Create Date: 2023-09-03 23:07:16.433188

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'fb3b86bcdcca'
down_revision: Union[str, None] = '265f7a0a7288'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('company', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'tasks', 'companies', ['company'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tasks', type_='foreignkey')
    op.drop_column('tasks', 'company')
    # ### end Alembic commands ###
