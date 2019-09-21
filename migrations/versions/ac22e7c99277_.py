"""empty message

Revision ID: ac22e7c99277
Revises: 255ae5521a78
Create Date: 2019-07-03 19:56:19.357436

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac22e7c99277'
down_revision = '255ae5521a78'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('listings', sa.Column('channel_id', sa.Integer(), nullable=True))
    op.add_column('listings', sa.Column('inventory_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'listings', 'channels', ['channel_id'], ['id'])
    op.create_foreign_key(None, 'listings', 'inventories', ['inventory_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'listings', type_='foreignkey')
    op.drop_constraint(None, 'listings', type_='foreignkey')
    op.drop_column('listings', 'inventory_id')
    op.drop_column('listings', 'channel_id')
    # ### end Alembic commands ###
