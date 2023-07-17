"""users table

Revision ID: 46d721ba70e5
Revises: 
Create Date: 2023-07-11 11:43:55.110030

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46d721ba70e5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('username', sa.String(length=25), nullable=False),
        sa.Column('password', sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint('id')                
    )


def downgrade():
    op.drop_table('users')
