"""enum added in priority field

Revision ID: 87b33e419194
Revises: 48a153e341a8
Create Date: 2024-07-07 00:27:25.703185

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '87b33e419194'
down_revision: Union[str, None] = '48a153e341a8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Создаем тип Enum 'taskpriority', если его еще нет
    taskpriority_enum = sa.Enum('LOW', 'MEDIUM', 'HIGH', name='taskpriority')
    taskpriority_enum.create(op.get_bind())

    # Меняем тип столбца 'priority' на тип Enum 'taskpriority', указывая USING для преобразования значений
    op.alter_column('tasks', 'priority',
                    existing_type=sa.Integer(),
                    type_=taskpriority_enum,
                    existing_nullable=True,
                    postgresql_using='priority::text::taskpriority')


def downgrade() -> None:
    # Меняем тип столбца 'priority' обратно на Integer
    op.alter_column('tasks', 'priority',
                    existing_type=sa.Enum('LOW', 'MEDIUM', 'HIGH', name='taskpriority'),
                    type_=sa.Integer(),
                    existing_nullable=True)

    # Удаляем тип Enum 'taskpriority'
    sa.Enum('LOW', 'MEDIUM', 'HIGH', name='taskpriority').drop(op.get_bind())
