from app import db
from datetime import datetime

class Informativo_Dimci(db.Model):
    __tablename__ = 'informativo_dimci'

    id = db.Column('id',db.Integer,primary_key = True, autoincrement = True)
    informacao = db.Column(db.Text(),nullable=True)
    data_registro = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=True)
    usuario = db.relationship('Usuario', back_populates="informativo_dimci")