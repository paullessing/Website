"""

Revision ID: 22a5c655da33
Revises: 74e2aff2838b
Create Date: 2017-12-10 17:22:51.139796

"""

# revision identifiers, used by Alembic.
revision = '22a5c655da33'
down_revision = '74e2aff2838b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('price_tier', schema=None) as batch_op:
        batch_op.add_column(sa.Column('product_id', sa.Integer(), nullable=False))
        batch_op.drop_constraint('uq_price_tier_name', type_='unique')
        batch_op.create_unique_constraint(batch_op.f('uq_price_tier_name'), ['name', 'product_id'])
        batch_op.drop_constraint('fk_price_tier_parent_id_product', type_='foreignkey')
        batch_op.create_foreign_key(batch_op.f('fk_price_tier_product_id_product'), 'product', ['product_id'], ['id'])
        batch_op.drop_column('parent_id')

    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('group_id', sa.Integer(), nullable=False))
        batch_op.drop_constraint('uq_product_name', type_='unique')
        batch_op.create_unique_constraint(batch_op.f('uq_product_name'), ['name', 'group_id'])
        batch_op.drop_constraint('fk_product_parent_id_product_group', type_='foreignkey')
        batch_op.create_foreign_key(batch_op.f('fk_product_group_id_product_group'), 'product_group', ['group_id'], ['id'])
        batch_op.drop_column('parent_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('parent_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(batch_op.f('fk_product_group_id_product_group'), type_='foreignkey')
        batch_op.create_foreign_key('fk_product_parent_id_product_group', 'product_group', ['parent_id'], ['id'])
        batch_op.drop_constraint(batch_op.f('uq_product_name'), type_='unique')
        batch_op.create_unique_constraint('uq_product_name', ['name', 'parent_id'])
        batch_op.drop_column('group_id')

    with op.batch_alter_table('price_tier', schema=None) as batch_op:
        batch_op.add_column(sa.Column('parent_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(batch_op.f('fk_price_tier_product_id_product'), type_='foreignkey')
        batch_op.create_foreign_key('fk_price_tier_parent_id_product', 'product', ['parent_id'], ['id'])
        batch_op.drop_constraint(batch_op.f('uq_price_tier_name'), type_='unique')
        batch_op.create_unique_constraint('uq_price_tier_name', ['name', 'parent_id'])
        batch_op.drop_column('product_id')

    # ### end Alembic commands ###