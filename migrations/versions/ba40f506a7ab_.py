"""empty message

Revision ID: ba40f506a7ab
Revises: 94263d94edeb
Create Date: 2019-06-14 16:24:54.879407

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ba40f506a7ab'
down_revision = '94263d94edeb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('contact_list', 'email',
               existing_type=mysql.VARCHAR(length=80),
               nullable=True)
    op.alter_column('contact_list', 'phone',
               existing_type=mysql.VARCHAR(length=120),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('contact_list', 'phone',
               existing_type=mysql.VARCHAR(length=120),
               nullable=False)
    op.alter_column('contact_list', 'email',
               existing_type=mysql.VARCHAR(length=80),
               nullable=False)
    # ### end Alembic commands ###
