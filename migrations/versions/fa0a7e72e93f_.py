"""empty message

Revision ID: fa0a7e72e93f
Revises: 
Create Date: 2022-02-17 18:27:43.027269

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa0a7e72e93f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=151), nullable=True),
    sa.Column('description', sa.String(length=251), nullable=True),
    sa.Column('directions', sa.String(length=4096), nullable=True),
    sa.Column('ing1', sa.Numeric(), nullable=True),
    sa.Column('ingu1', sa.String(length=28), nullable=True),
    sa.Column('ingn1', sa.String(length=28), nullable=True),
    sa.Column('ing2', sa.Numeric(), nullable=True),
    sa.Column('ingu2', sa.String(length=28), nullable=True),
    sa.Column('ingn2', sa.String(length=28), nullable=True),
    sa.Column('ing3', sa.Numeric(), nullable=True),
    sa.Column('ingu3', sa.String(length=28), nullable=True),
    sa.Column('ingn3', sa.String(length=28), nullable=True),
    sa.Column('ing4', sa.Numeric(), nullable=True),
    sa.Column('ingu4', sa.String(length=28), nullable=True),
    sa.Column('ingn4', sa.String(length=28), nullable=True),
    sa.Column('ing5', sa.Numeric(), nullable=True),
    sa.Column('ingu5', sa.String(length=28), nullable=True),
    sa.Column('ingn5', sa.String(length=28), nullable=True),
    sa.Column('ing6', sa.Numeric(), nullable=True),
    sa.Column('ingu6', sa.String(length=28), nullable=True),
    sa.Column('ingn6', sa.String(length=28), nullable=True),
    sa.Column('ing7', sa.Numeric(), nullable=True),
    sa.Column('ingu7', sa.String(length=28), nullable=True),
    sa.Column('ingn7', sa.String(length=28), nullable=True),
    sa.Column('ing8', sa.Numeric(), nullable=True),
    sa.Column('ingu8', sa.String(length=28), nullable=True),
    sa.Column('ingn8', sa.String(length=28), nullable=True),
    sa.Column('ing9', sa.Numeric(), nullable=True),
    sa.Column('ingu9', sa.String(length=28), nullable=True),
    sa.Column('ingn9', sa.String(length=28), nullable=True),
    sa.Column('ing10', sa.Numeric(), nullable=True),
    sa.Column('ingu10', sa.String(length=28), nullable=True),
    sa.Column('ingn10', sa.String(length=28), nullable=True),
    sa.Column('ing11', sa.Numeric(), nullable=True),
    sa.Column('ingu11', sa.String(length=28), nullable=True),
    sa.Column('ingn11', sa.String(length=28), nullable=True),
    sa.Column('avocado', sa.Boolean(), nullable=True),
    sa.Column('pepper', sa.Boolean(), nullable=True),
    sa.Column('carrots', sa.Boolean(), nullable=True),
    sa.Column('celery', sa.Boolean(), nullable=True),
    sa.Column('cabbage', sa.Boolean(), nullable=True),
    sa.Column('cucumber', sa.Boolean(), nullable=True),
    sa.Column('grapetom', sa.Boolean(), nullable=True),
    sa.Column('kale', sa.Boolean(), nullable=True),
    sa.Column('lemon', sa.Boolean(), nullable=True),
    sa.Column('lettuce', sa.Boolean(), nullable=True),
    sa.Column('lime', sa.Boolean(), nullable=True),
    sa.Column('mushroom', sa.Boolean(), nullable=True),
    sa.Column('peas', sa.Boolean(), nullable=True),
    sa.Column('poblano', sa.Boolean(), nullable=True),
    sa.Column('potatoes', sa.Boolean(), nullable=True),
    sa.Column('redcab', sa.Boolean(), nullable=True),
    sa.Column('scallion', sa.Boolean(), nullable=True),
    sa.Column('snowpea', sa.Boolean(), nullable=True),
    sa.Column('spinach', sa.Boolean(), nullable=True),
    sa.Column('sweetpotato', sa.Boolean(), nullable=True),
    sa.Column('tomato', sa.Boolean(), nullable=True),
    sa.Column('zucchini', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book')
    # ### end Alembic commands ###
