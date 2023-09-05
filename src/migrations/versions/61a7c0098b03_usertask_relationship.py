"""UserTask relationship

Revision ID: 61a7c0098b03
Revises: 43bc80fc3269
Create Date: 2023-09-04 20:11:51.103918

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '61a7c0098b03'
down_revision: Union[str, None] = '43bc80fc3269'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_task',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('task_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
    )
    op.add_column('tasks', sa.Column('company_id', sa.Integer(), nullable=True))
    op.drop_constraint('tasks_company_fkey', 'tasks', type_='foreignkey')
    op.create_foreign_key(None, 'tasks', 'companies', ['company_id'], ['id'], ondelete='CASCADE')
    op.drop_column('tasks', 'company')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('company', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'tasks', type_='foreignkey')
    op.create_foreign_key('tasks_company_fkey', 'tasks', 'companies', ['company'], ['id'], ondelete='CASCADE')
    op.drop_column('tasks', 'company_id')
    op.drop_table('user_task')
    # ### end Alembic commands ###
