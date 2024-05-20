"""empty message

Revision ID: 37f1ee82c63c
Revises: b5a8cff8aa16
Create Date: 2024-05-12 22:34:51.282310

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37f1ee82c63c'
down_revision = 'b5a8cff8aa16'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('file', sa.String(length=200), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.drop_column('file')

    # ### end Alembic commands ###
