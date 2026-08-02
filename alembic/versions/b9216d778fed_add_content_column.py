"""add content column

Revision ID: b9216d778fed
Revises: f975bc8cfb6d
Create Date: 2026-08-02 13:12:37.751175

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b9216d778fed'
down_revision: Union[str, Sequence[str], None] = 'f975bc8cfb6d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts',sa.Column('content',sa.String,nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts','content')
    pass
