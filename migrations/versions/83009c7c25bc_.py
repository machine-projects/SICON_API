"""empty message

Revision ID: 83009c7c25bc
Revises: 
Create Date: 2020-04-29 19:03:13.802239

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83009c7c25bc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
