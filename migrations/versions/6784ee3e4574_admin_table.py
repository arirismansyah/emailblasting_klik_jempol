"""admin table

Revision ID: 6784ee3e4574
Revises: 2aaefdae04ec
Create Date: 2021-10-19 14:51:53.192873

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6784ee3e4574'
down_revision = '2aaefdae04ec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('admin', sa.Column('id_admin', sa.Integer(), nullable=False))
    op.drop_column('admin', 'id_faq')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('admin', sa.Column('id_faq', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False))
    op.drop_column('admin', 'id_admin')
    # ### end Alembic commands ###
