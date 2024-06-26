"""empty message

Revision ID: 698ac4b8b726
Revises: 76d9ed06d361
Create Date: 2023-05-10 03:04:59.357995

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '698ac4b8b726'
down_revision = '76d9ed06d361'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('goal_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'task', 'goal', ['goal_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'task', type_='foreignkey')
    op.drop_column('task', 'goal_id')
    # ### end Alembic commands ###
