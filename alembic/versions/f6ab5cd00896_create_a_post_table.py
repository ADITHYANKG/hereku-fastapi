"""create a post table

Revision ID: f6ab5cd00896
Revises: 
Create Date: 2026-05-30 11:28:57.020787

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f6ab5cd00896'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table("posts",sa.Column("id",sa.Integer(),nullable=False,primary_key=True),sa.Column("title",sa.String(),nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('posts')
    pass
