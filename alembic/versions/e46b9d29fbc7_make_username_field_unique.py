"""make username field unique

Revision ID: e46b9d29fbc7
Revises: 5c70e8683b5d
Create Date: 2024-07-07 15:11:57.098599

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e46b9d29fbc7'
down_revision: Union[str, None] = '5c70e8683b5d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'hashed_password',
               existing_type=sa.VARCHAR(length=60),
               type_=sa.String(length=1024),
               existing_nullable=False)
    op.drop_index('ix_users_username', table_name='users')
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.create_index('ix_users_username', 'users', ['username'], unique=False)
    op.alter_column('users', 'hashed_password',
               existing_type=sa.String(length=1024),
               type_=sa.VARCHAR(length=60),
               existing_nullable=False)
    # ### end Alembic commands ###