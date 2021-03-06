"""admin table

Revision ID: 2aaefdae04ec
Revises: a1240fa16ccb
Create Date: 2021-10-19 14:50:30.078362

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2aaefdae04ec'
down_revision = 'a1240fa16ccb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('id_faq', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=200), nullable=True),
    sa.Column('password', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id_faq')
    )
    op.add_column('log', sa.Column('status', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'log', 'status', ['status'], ['id_status'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'log', type_='foreignkey')
    op.drop_column('log', 'status')
    op.drop_table('admin')
    # ### end Alembic commands ###
