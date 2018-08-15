"""empty message

Revision ID: 0a8462397dcf
Revises: 
Create Date: 2018-08-14 14:00:08.053366

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a8462397dcf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('project_title', sa.String(length=64), nullable=True),
    sa.Column('year_1', sa.Float(), nullable=True),
    sa.Column('year_2', sa.Float(), nullable=True),
    sa.Column('year_3', sa.Float(), nullable=True),
    sa.Column('year_4', sa.Float(), nullable=True),
    sa.Column('year_5', sa.Float(), nullable=True),
    sa.Column('justification', sa.String(length=64), nullable=True),
    sa.Column('comments', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('project')
    # ### end Alembic commands ###