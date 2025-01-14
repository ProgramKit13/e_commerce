"""empty message

Revision ID: dfb176e73a52
Revises: 
Create Date: 2023-06-23 09:38:51.182956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dfb176e73a52'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('prodName', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('sector', sa.String(length=100), nullable=True),
    sa.Column('supplier', sa.String(length=100), nullable=True),
    sa.Column('supplierCode', sa.String(length=100), nullable=True),
    sa.Column('manufacturer', sa.String(length=100), nullable=True),
    sa.Column('valueResale', sa.Numeric(precision=8, scale=2), nullable=False),
    sa.Column('cust', sa.Numeric(precision=8, scale=2), nullable=True),
    sa.Column('tax', sa.Numeric(precision=8, scale=2), nullable=True),
    sa.Column('qt', sa.Integer(), nullable=False),
    sa.Column('discount', sa.Numeric(precision=4, scale=2), nullable=True),
    sa.Column('weight', sa.Numeric(precision=8, scale=2), nullable=True),
    sa.Column('weightUnit', sa.String(length=50), nullable=True),
    sa.Column('dimensions', sa.String(length=100), nullable=True),
    sa.Column('dimensionsUnit', sa.String(length=50), nullable=True),
    sa.Column('barcode', sa.String(length=50), nullable=True),
    sa.Column('datePurchase', sa.Date(), nullable=True),
    sa.Column('lastUpdated', sa.Date(), nullable=True),
    sa.Column('reorderPoint', sa.Integer(), nullable=True),
    sa.Column('restockTime', sa.Integer(), nullable=True),
    sa.Column('warrantyInfo', sa.Text(), nullable=True),
    sa.Column('batchInfo', sa.String(length=100), nullable=True),
    sa.Column('expiryDate', sa.Date(), nullable=True),
    sa.Column('materialOrIngredients', sa.Text(), nullable=True),
    sa.Column('safetyRating', sa.String(length=100), nullable=True),
    sa.Column('shippingRestrictions', sa.Text(), nullable=True),
    sa.Column('token', sa.String(length=16), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('sectors',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('token', sa.String(length=16), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('suppliers',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('supplierName', sa.String(length=50), nullable=False),
    sa.Column('supplierEmail', sa.String(length=50), nullable=False),
    sa.Column('supplierState', sa.String(length=2), nullable=False),
    sa.Column('supplierCity', sa.String(length=50), nullable=False),
    sa.Column('supplierNeighborhood', sa.String(length=50), nullable=False),
    sa.Column('supplierStreet', sa.String(length=100), nullable=False),
    sa.Column('supplierNumber', sa.Integer(), nullable=False),
    sa.Column('supplierComplement', sa.String(length=100), nullable=True),
    sa.Column('supplierZipCode', sa.String(length=9), nullable=False),
    sa.Column('supplierCnpj', sa.String(length=18), nullable=False),
    sa.Column('supplierPhone_01', sa.String(length=13), nullable=True),
    sa.Column('supplierPhone_02', sa.String(length=13), nullable=True),
    sa.Column('token', sa.String(length=16), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('dateCreation', sa.DateTime(), nullable=False),
    sa.Column('token', sa.String(length=16), nullable=False),
    sa.Column('adminAccess', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('adminPreferences',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('productsPerPage', sa.Enum('fifty', 'hundred', 'hundredFifty', 'twoHundred', name='productsperpage'), nullable=False),
    sa.Column('suppliersPerPage', sa.Enum('fifty', 'hundred', 'hundredFifty', 'twoHundred', name='suppliersperpage'), nullable=False),
    sa.Column('tokenUser', sa.String(length=16), nullable=False),
    sa.ForeignKeyConstraint(['tokenUser'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('adresses',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('neighborhood', sa.String(length=100), nullable=False),
    sa.Column('complement', sa.String(length=100), nullable=True),
    sa.Column('street', sa.String(length=100), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('state', sa.String(length=2), nullable=False),
    sa.Column('city', sa.String(length=100), nullable=False),
    sa.Column('zipCode', sa.String(length=9), nullable=False),
    sa.Column('activate', sa.Enum('active', 'inative', name='active'), nullable=False),
    sa.Column('tokenUser', sa.String(length=16), nullable=False),
    sa.ForeignKeyConstraint(['tokenUser'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('carts',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('tokenUser', sa.String(length=16), nullable=False),
    sa.Column('token', sa.String(length=64), nullable=False),
    sa.Column('discountTotal', sa.Numeric(precision=4, scale=2), nullable=True),
    sa.Column('valueTtotal', sa.Numeric(precision=8, scale=2), nullable=True),
    sa.Column('openCart', sa.Boolean(), nullable=False),
    sa.Column('status', sa.Enum('confirmed', 'panding', 'canceled', name='status'), nullable=False),
    sa.ForeignKeyConstraint(['tokenUser'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('service_order',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('tokenProduct', sa.String(length=16), nullable=False),
    sa.Column('tokenUser', sa.String(length=16), nullable=False),
    sa.Column('tokenCart', sa.String(length=64), nullable=False),
    sa.Column('token', sa.String(length=64), nullable=False),
    sa.Column('qt', sa.Integer(), nullable=False),
    sa.Column('value', sa.Numeric(precision=8, scale=2), nullable=False),
    sa.Column('discount', sa.Numeric(precision=4, scale=2), nullable=True),
    sa.ForeignKeyConstraint(['tokenCart'], ['carts.token'], ),
    sa.ForeignKeyConstraint(['tokenProduct'], ['products.token'], ),
    sa.ForeignKeyConstraint(['tokenUser'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('user_payments',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('userToken', sa.String(length=16), nullable=False),
    sa.Column('cartToken', sa.String(length=16), nullable=False),
    sa.Column('typePayment', sa.Enum('debit', 'credt', 'ticket', 'pix', name='type'), nullable=False),
    sa.Column('value', sa.Float(), nullable=False),
    sa.Column('status', sa.Enum('aprovade', 'reprovade', 'panding', 'canceled', 'extoted', name='status'), nullable=False),
    sa.Column('datePayment', sa.DateTime(), nullable=False),
    sa.Column('dateStatus', sa.DateTime(), nullable=False),
    sa.Column('token', sa.String(length=64), nullable=False),
    sa.ForeignKeyConstraint(['cartToken'], ['carts.token'], ),
    sa.ForeignKeyConstraint(['userToken'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('token')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_payments')
    op.drop_table('service_order')
    op.drop_table('carts')
    op.drop_table('adresses')
    op.drop_table('adminPreferences')
    op.drop_table('user')
    op.drop_table('suppliers')
    op.drop_table('sectors')
    op.drop_table('products')
    # ### end Alembic commands ###
