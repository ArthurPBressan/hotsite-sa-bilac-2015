"""retira security

Revision ID: 415c31d38d15
Revises: 47e2b7da19b1
Create Date: 2015-10-27 23:25:57.172408

"""

# revision identifiers, used by Alembic.
revision = '415c31d38d15'
down_revision = '47e2b7da19b1'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.drop_table('roles_alunos')
    op.drop_table('role')
    op.drop_column('aluno', 'active')
    op.drop_column('aluno', 'email')


def downgrade():
    op.add_column('aluno', sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('aluno', sa.Column('active', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.create_table('role',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=u'role_pkey'),
    sa.UniqueConstraint('name', name=u'role_name_key')
    )
    op.create_table('roles_alunos',
    sa.Column('aluno_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('role_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['aluno_id'], [u'aluno.id'], name=u'roles_alunos_aluno_id_fkey'),
    sa.ForeignKeyConstraint(['role_id'], [u'role.id'], name=u'roles_alunos_role_id_fkey')
    )
