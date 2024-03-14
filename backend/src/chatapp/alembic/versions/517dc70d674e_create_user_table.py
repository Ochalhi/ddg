"""create user table

Revision ID: 517dc70d674e
Revises: 
Create Date: 2024-03-12 11:36:11.373724

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from chatapp.models.User import User

# revision identifiers, used by Alembic.
revision: str = '517dc70d674e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        User.__table__,
        sa.Column('id', sa.Integer, primary_key=True)
    )
    seed()


def seed():
    op.bulk_insert(User.__table__, [{'id': 1}, {'id': 2}])


def downgrade() -> None:
    op.drop_table('user')
