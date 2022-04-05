"""empty message

Revision ID: 5b7082a03466
Revises: 29d51ac91808
Create Date: 2022-04-01 16:00:42.107170

"""

# revision identifiers, used by Alembic.
revision = '5b7082a03466'
down_revision = '29d51ac91808'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('default', sa.Boolean(), nullable=True))
    op.create_index(op.f('ix_roles_default'), 'roles', ['default'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_roles_default'), table_name='roles')
    op.drop_column('roles', 'default')
    # ### end Alembic commands ###
