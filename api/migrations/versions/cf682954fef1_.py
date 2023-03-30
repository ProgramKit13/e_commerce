"""empty message

Revision ID: cf682954fef1
Revises: 
Create Date: 2023-03-30 13:29:45.133815

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf682954fef1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('prodName', sa.String(length=100), nullable=False),
    sa.Column('valueResale', sa.Float(precision=9), nullable=False),
    sa.Column('cust', sa.Float(precision=9), nullable=False),
    sa.Column('tax', sa.Float(precision=9), nullable=True),
    sa.Column('qt', sa.Integer(), nullable=False),
    sa.Column('alterResale', sa.Float(precision=9), nullable=True),
    sa.Column('discount', sa.Float(precision=9), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('datePurchase', sa.DateTime(), nullable=False),
    sa.Column('dateShelf', sa.DateTime(), nullable=False),
    sa.Column('token', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=64), nullable=False),
    sa.Column('cpf', sa.String(length=11), nullable=False),
    sa.Column('genre', sa.Enum('masculino', 'feminino', 'outros', name='genre'), nullable=False),
    sa.Column('dateCreation', sa.DateTime(), nullable=False),
    sa.Column('token', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('adresses',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('neighborhood', sa.String(length=100), nullable=False),
    sa.Column('street', sa.String(length=100), nullable=False),
    sa.Column('number', sa.String(length=9), nullable=False),
    sa.Column('state', sa.String(length=2), nullable=False),
    sa.Column('city', sa.String(length=100), nullable=False),
    sa.Column('zipCode', sa.String(length=9), nullable=False),
    sa.Column('activate', sa.Enum('active', 'inative', name='active'), nullable=False),
    sa.Column('idUser', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['idUser'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('phones',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('type', sa.Enum('fixed', 'cellphone', name='type'), nullable=False),
    sa.Column('ddd', sa.String(length=2), nullable=False),
    sa.Column('number', sa.String(length=9), nullable=False),
    sa.Column('idUser', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['idUser'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('suppliers',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('uf', sa.String(length=2), nullable=False),
    sa.Column('city', sa.String(length=50), nullable=False),
    sa.Column('neighborhood', sa.String(length=50), nullable=False),
    sa.Column('number', sa.String(length=9), nullable=False),
    sa.Column('complement', sa.String(length=100), nullable=False),
    sa.Column('cnpj', sa.String(length=14), nullable=False),
    sa.Column('idProduct', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['idProduct'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('user_payments',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('typePayment', sa.Enum('debit', 'credt', 'ticket', 'pix', name='type'), nullable=False),
    sa.Column('value', sa.Float(), nullable=False),
    sa.Column('status', sa.Enum('aprovade', 'reprovade', 'pading', 'canceled', 'extoted', name='status'), nullable=False),
    sa.Column('idUser', sa.Integer(), nullable=False),
    sa.Column('datePayment', sa.DateTime(), nullable=False),
    sa.Column('dateStatus', sa.DateTime(), nullable=False),
    sa.Column('token', sa.String(length=64), nullable=False),
    sa.ForeignKeyConstraint(['idUser'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('carts',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('qt', sa.Integer(), nullable=False),
    sa.Column('value', sa.Float(), nullable=False),
    sa.Column('confirm', sa.Enum('confirmation', 'canceled', name='confirmationoption'), nullable=False),
    sa.Column('totalDiscount', sa.Float(precision=9), nullable=True),
    sa.Column('idUser', sa.Integer(), nullable=False),
    sa.Column('idProduct', sa.Integer(), nullable=False),
    sa.Column('idPayment', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(length=64), nullable=False),
    sa.ForeignKeyConstraint(['idPayment'], ['user_payments.id'], ),
    sa.ForeignKeyConstraint(['idProduct'], ['products.id'], ),
    sa.ForeignKeyConstraint(['idUser'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('suppliers_phones',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('type', sa.Enum('fixed', 'cellphone', name='type'), nullable=False),
    sa.Column('ddd', sa.String(length=2), nullable=False),
    sa.Column('number', sa.String(length=9), nullable=False),
    sa.Column('idSups', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['idSups'], ['suppliers.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('suppliers_phones')
    op.drop_table('carts')
    op.drop_table('user_payments')
    op.drop_table('suppliers')
    op.drop_table('phones')
    op.drop_table('adresses')
    op.drop_table('user')
    op.drop_table('products')
    # ### end Alembic commands ###
