"""nullable false -> quantity

Revision ID: b63307233adf
Revises: 32e733dd9026
Create Date: 2024-01-17 10:54:11.855719

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b63307233adf'
down_revision = '32e733dd9026'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('purchase_order', schema=None) as batch_op:
        batch_op.alter_column('quantity',
               existing_type=sa.INTEGER(),
               nullable=False)

    with op.batch_alter_table('purchase_order_items', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=2),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('purchase_order_items', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.Float(precision=2),
               type_=sa.REAL(),
               existing_nullable=False)

    with op.batch_alter_table('purchase_order', schema=None) as batch_op:
        batch_op.alter_column('quantity',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###