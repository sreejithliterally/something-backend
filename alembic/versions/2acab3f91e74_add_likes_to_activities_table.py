"""Add likes to activities table

Revision ID: 2acab3f91e74
Revises: 3147cb06dc5b
Create Date: 2024-02-05 19:17:41.247038

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2acab3f91e74'
down_revision: Union[str, None] = '3147cb06dc5b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('activities', sa.Column('likes', sa.Integer(), nullable=True))
    op.drop_column('bookings', 'payment_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bookings', sa.Column('payment_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('activities', 'likes')
    # ### end Alembic commands ###