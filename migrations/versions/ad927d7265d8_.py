"""empty message

Revision ID: ad927d7265d8
Revises: 
Create Date: 2020-08-28 15:49:25.349369

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad927d7265d8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cliente',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=True),
    sa.Column('mci', sa.String(length=50), nullable=True),
    sa.Column('contato', sa.String(length=100), nullable=True),
    sa.Column('telefone1', sa.String(length=100), nullable=True),
    sa.Column('telefone2', sa.String(length=100), nullable=True),
    sa.Column('email1', sa.String(length=100), nullable=True),
    sa.Column('email2', sa.String(length=100), nullable=True),
    sa.Column('razao_social', sa.String(length=200), nullable=True),
    sa.Column('endereco', sa.String(length=400), nullable=True),
    sa.Column('equipamentos', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('mci')
    )
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('senha', sa.String(length=50), nullable=True),
    sa.Column('nome', sa.String(length=50), nullable=True),
    sa.Column('up_uo', sa.String(length=50), nullable=True),
    sa.Column('privilegio', sa.String(length=50), nullable=True),
    sa.Column('matricula', sa.String(length=50), nullable=True),
    sa.Column('ramal', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('equipamento',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('equipamento', sa.String(length=100), nullable=True),
    sa.Column('codigo', sa.String(length=100), nullable=True),
    sa.Column('fabricante', sa.String(length=100), nullable=True),
    sa.Column('modelo', sa.String(length=100), nullable=True),
    sa.Column('serie', sa.String(length=100), nullable=True),
    sa.Column('certificado', sa.String(length=100), nullable=True),
    sa.Column('periodicidade', sa.Integer(), nullable=True),
    sa.Column('descricao', sa.Text(), nullable=True),
    sa.Column('data_ultima_calibracao', sa.DateTime(), nullable=True),
    sa.Column('data_proxima_calibracao', sa.DateTime(), nullable=True),
    sa.Column('data_registro', sa.DateTime(), nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('codigo')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('equipamento')
    op.drop_table('usuario')
    op.drop_table('cliente')
    # ### end Alembic commands ###