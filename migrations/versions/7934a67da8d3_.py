"""empty message

Revision ID: 7934a67da8d3
Revises: f37bc33a2a49
Create Date: 2024-02-05 10:42:04.666355

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7934a67da8d3'
down_revision = 'f37bc33a2a49'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('purchase_order_items', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=2),
               existing_nullable=False)
        batch_op.drop_constraint('purchase_order_items_quantity_fkey', type_='foreignkey')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('purchase_order_items', schema=None) as batch_op:
        batch_op.create_foreign_key('purchase_order_items_quantity_fkey', 'purchase_order', ['quantity'], ['id'])
        batch_op.alter_column('price',
               existing_type=sa.Float(precision=2),
               type_=sa.REAL(),
               existing_nullable=False)

    # ### end Alembic commands ###
