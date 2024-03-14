"""create message table

Revision ID: b18842995c1d
Revises: 517dc70d674e
Create Date: 2024-03-12 11:40:48.421222

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from chatapp.models.Message import Message

# revision identifiers, used by Alembic.
revision: str = 'b18842995c1d'
down_revision: Union[str, None] = '517dc70d674e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        Message.__table__,
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('sender_id', sa.Integer),
        sa.ForeignKeyConstraint(('sender_id',), ['user.id']),
        sa.Column('receiver_id', sa.Integer),
        sa.ForeignKeyConstraint(('receiver_id',), ['user.id']),
        sa.Column('content', sa.String),
        sa.Column('timestamp', sa.DateTime, server_default=sa.func.now())
    )


def downgrade() -> None:
    op.drop_table('message')
