"""company user model creation

Revision ID: 265f7a0a7288
Revises: 70b99e09f078
Create Date: 2023-09-01 02:23:24.727861

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '265f7a0a7288'
down_revision: Union[str, None] = '70b99e09f078'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('companies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('office_location', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_companies_id'), 'companies', ['id'], unique=False)
    op.create_table('company_users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_status', sa.String(), nullable=False),
    sa.Column('company', sa.Integer(), nullable=True),
    sa.Column('user', sa.Integer(), nullable=True),
    sa.Column('member_since', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['company'], ['companies.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_company_users_id'), 'company_users', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_company_users_id'), table_name='company_users')
    op.drop_table('company_users')
    op.drop_index(op.f('ix_companies_id'), table_name='companies')
    op.drop_table('companies')
    # ### end Alembic commands ###
