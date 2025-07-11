"""add user_id to photo

Revision ID: 7c95b0c77385
Revises: d78980c10341
Create Date: 2025-06-10 17:34:07.300393

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '7c95b0c77385'
down_revision: Union[str, None] = 'd78980c10341'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('conversations', sa.Column('summary_text', sa.Text(), nullable=True))
    op.add_column('conversations', sa.Column('summary_voice', sa.Text(), nullable=True))
    op.add_column('photos', sa.Column('user_id', sa.UUID(), nullable=True))
    op.create_foreign_key(None, 'photos', 'users', ['user_id'], ['id'])
    op.drop_column('photos', 'summary_text')
    op.drop_column('photos', 'summary_voice')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('photos', sa.Column('summary_voice', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True))
    op.add_column('photos', sa.Column('summary_text', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'photos', type_='foreignkey')
    op.drop_column('photos', 'user_id')
    op.drop_column('conversations', 'summary_voice')
    op.drop_column('conversations', 'summary_text')
    # ### end Alembic commands ###
