"""add the content column

Revision ID: 6f638a4d290b
Revises: f6ab5cd00896
Create Date: 2026-05-30 11:42:02.293966

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6f638a4d290b'
down_revision: Union[str, Sequence[str], None] = 'f6ab5cd00896'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts",sa.Column("content",sa.String(),nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts",'content')
    pass
