"""empty message

Revision ID: 2e06030fcc7e
Revises: c543cb2c4946
Create Date: 2020-09-03 13:57:59.727951

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e06030fcc7e'
down_revision = 'c543cb2c4946'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('indice_geral',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('data_realizacao_calibracao', sa.DateTime(), nullable=True),
    sa.Column('data_registro', sa.DateTime(), nullable=False),
    sa.Column('certificado', sa.String(length=50), nullable=True),
    sa.Column('descricao', sa.Text(), nullable=True),
    sa.Column('agendamento_id', sa.Integer(), nullable=True),
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['agendamento_id'], ['agendamento.id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('indice_geral')
    # ### end Alembic commands ###
