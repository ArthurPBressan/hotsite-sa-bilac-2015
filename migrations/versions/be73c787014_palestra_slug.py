"""palestra slug

Revision ID: be73c787014
Revises: 415c31d38d15
Create Date: 2015-11-04 21:00:47.624017

"""

# revision identifiers, used by Alembic.
revision = 'be73c787014'
down_revision = '415c31d38d15'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('palestra', sa.Column('titulo_slug', sa.String(length=255), nullable=True))


def downgrade():
    op.drop_column('palestra', 'titulo_slug')
