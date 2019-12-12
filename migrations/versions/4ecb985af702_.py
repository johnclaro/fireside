"""empty message

Revision ID: 4ecb985af702
Revises: 21949151629c
Create Date: 2019-07-04 16:06:50.389202

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ecb985af702'
down_revision = '21949151629c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products', 'uid')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('uid', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
