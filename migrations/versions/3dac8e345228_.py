"""empty message

Revision ID: 3dac8e345228
Revises: e6318b4b2ed8
Create Date: 2019-07-29 13:14:12.683136

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3dac8e345228'
down_revision = 'e6318b4b2ed8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_column('merchants', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('merchants', sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_table('profiles')
    # ### end Alembic commands ###
