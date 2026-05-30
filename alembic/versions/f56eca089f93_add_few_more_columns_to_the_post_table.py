"""add few more columns to the post table 

Revision ID: f56eca089f93
Revises: 900a8a03a1a3
Create Date: 2026-05-30 13:15:00.111322

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f56eca089f93'
down_revision: Union[str, Sequence[str], None] = '900a8a03a1a3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts",
                  
                  sa.Column("published",sa.Boolean(),nullable=False,server_default='TRUE'),
                  )
    
    op.add_column("posts",
        sa.Column("created_at",sa.TIMESTAMP(timezone=True),server_default=sa.text('NOW()'),nullable=False)
        )
    
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts","published")
    op.drop_column("posts","created_at")

    pass
