"""update database

Revision ID: 3a93c35613c8
Revises: 79dd4491d2b8
Create Date: 2021-11-22 08:07:24.202274

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a93c35613c8'
down_revision = '79dd4491d2b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('email', table_name='customer')
    op.create_foreign_key(None, 'customer', 'prov', ['prov_domisili'], ['kode_prov'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'customer', 'kabkot', ['kab_domisili'], ['id_kabkot'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'customer', 'pendidikan', ['pendidikan'], ['id_pendidikan'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'customer', 'pekerjaan', ['jenis_pekerjaan'], ['id_pekerjaan'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'kabkot', 'prov', ['kode_prov'], ['kode_prov'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'log', 'customer', ['customer'], ['id_customer'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'log', 'template', ['template_email'], ['id_template'])
    op.create_foreign_key(None, 'log', 'status', ['status'], ['id_status'], onupdate='CASCADE', ondelete='CASCADE')
    op.add_column('template', sa.Column('progress_send', sa.Integer(), nullable=True))
    op.add_column('template', sa.Column('succeed_send', sa.Integer(), nullable=True))
    op.add_column('template', sa.Column('failed_send', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'template', 'status', ['status'], ['id_status'], onupdate='CASCADE', ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'template', type_='foreignkey')
    op.drop_column('template', 'failed_send')
    op.drop_column('template', 'succeed_send')
    op.drop_column('template', 'progress_send')
    op.drop_constraint(None, 'log', type_='foreignkey')
    op.drop_constraint(None, 'log', type_='foreignkey')
    op.drop_constraint(None, 'log', type_='foreignkey')
    op.drop_constraint(None, 'kabkot', type_='foreignkey')
    op.drop_constraint(None, 'customer', type_='foreignkey')
    op.drop_constraint(None, 'customer', type_='foreignkey')
    op.drop_constraint(None, 'customer', type_='foreignkey')
    op.drop_constraint(None, 'customer', type_='foreignkey')
    op.create_index('email', 'customer', ['email'], unique=False)
    # ### end Alembic commands ###