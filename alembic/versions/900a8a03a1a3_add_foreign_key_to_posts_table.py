"""add foreign-key to posts table

Revision ID: 900a8a03a1a3
Revises: 06a2a870fb1e
Create Date: 2026-05-30 13:02:32.583628

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '900a8a03a1a3'
down_revision: Union[str, Sequence[str], None] = '06a2a870fb1e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('posts_users_fk',source_table="posts",referent_table="users",local_cols=['owner_id'],remote_cols=['id'],ondelete="CASCADE")
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint("post_users_fk",table_name="posts")
    op.drop_column("posts","owner_id")
    pass
