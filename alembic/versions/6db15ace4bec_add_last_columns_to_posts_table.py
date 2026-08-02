"""add last columns to posts table

Revision ID: 6db15ace4bec
Revises: 1af15ba77f8f
Create Date: 2026-08-02 14:19:31.312729

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6db15ace4bec'
down_revision: Union[str, Sequence[str], None] = '1af15ba77f8f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts",sa.Column('published',sa.Boolean(),server_default="TRUE",nullable=False))
    op.add_column("posts",sa.Column('created_at',sa.TIMESTAMP(timezone=True),server_default=sa.text("NOW()"),nullable=False))

    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts","published")
    op.drop_column("posts","created_at")
    pass
