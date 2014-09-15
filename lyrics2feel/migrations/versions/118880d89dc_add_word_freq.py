"""add Word.freq

Revision ID: 118880d89dc
Revises: 446136f288
Create Date: 2014-09-15 15:22:12.778192

"""

# revision identifiers, used by Alembic.
revision = '118880d89dc'
down_revision = '446136f288'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('words', sa.Column('freq', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('words', 'freq')
    ### end Alembic commands ###
