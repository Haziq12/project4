"""empty message

Revision ID: 0783e7c84e04
Revises: 1d2908be0887
Create Date: 2022-04-10 23:47:07.410656

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0783e7c84e04'
down_revision = '1d2908be0887'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('country', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'country')
    # ### end Alembic commands ###
