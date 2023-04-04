"""empty message

Revision ID: c8b98326ddb3
Revises: fb2879a70015
Create Date: 2023-04-04 11:29:13.255431

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c8b98326ddb3'
down_revision = 'fb2879a70015'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_payments', schema=None) as batch_op:
        batch_op.alter_column('status',
               existing_type=mysql.ENUM('aprovade', 'reprovade', 'pading', 'canceled', 'extoted'),
               type_=sa.Enum('aprovade', 'reprovade', 'panding', 'canceled', 'extoted', name='status'),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_payments', schema=None) as batch_op:
        batch_op.alter_column('status',
               existing_type=sa.Enum('aprovade', 'reprovade', 'panding', 'canceled', 'extoted', name='status'),
               type_=mysql.ENUM('aprovade', 'reprovade', 'pading', 'canceled', 'extoted'),
               existing_nullable=False)

    # ### end Alembic commands ###
