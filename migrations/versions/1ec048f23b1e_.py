"""empty message

Revision ID: 1ec048f23b1e
Revises: 48f1693b9933
Create Date: 2019-07-04 23:51:42.103339

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ec048f23b1e'
down_revision = '48f1693b9933'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('channels_etsy_channel_id_fkey', 'channels_etsy', type_='foreignkey')
    op.create_foreign_key(None, 'channels_etsy', 'channels', ['channel_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'channels_etsy', type_='foreignkey')
    op.create_foreign_key('channels_etsy_channel_id_fkey', 'channels_etsy', 'channels', ['channel_id'], ['id'])
    # ### end Alembic commands ###
