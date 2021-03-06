"""create table character

Revision ID: 91d0bbaea880
Revises: 91a92ecf3568
Create Date: 2020-01-08 11:33:37.607972

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91d0bbaea880'
down_revision = '91a92ecf3568'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=127), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('xp', sa.SmallInteger(), nullable=False),
    sa.Column('agility', sa.SmallInteger(), nullable=False),
    sa.Column('smarts', sa.SmallInteger(), nullable=False),
    sa.Column('spirit', sa.SmallInteger(), nullable=False),
    sa.Column('strength', sa.SmallInteger(), nullable=False),
    sa.Column('vigor', sa.SmallInteger(), nullable=False),
    sa.Column('pace', sa.SmallInteger(), nullable=False),
    sa.Column('parry', sa.SmallInteger(), nullable=False),
    sa.Column('toughness', sa.SmallInteger(), nullable=False),
    sa.Column('charisma', sa.SmallInteger(), nullable=False),
    sa.Column('wounds', sa.SmallInteger(), nullable=False),
    sa.Column('fatigue', sa.SmallInteger(), nullable=False),
    sa.Column('scenario_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['scenario_id'], ['scenario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('character')
    # ### end Alembic commands ###
