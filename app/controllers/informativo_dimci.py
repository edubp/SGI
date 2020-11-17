from flask import Blueprint, render_template,request,redirect,url_for,send_file
from flask_login import login_required, current_user
from app.models.informativo_dimci import Informativo_Dimci
from app import db

informativo_dimci = Blueprint('informativo_dimci', __name__)

@informativo_dimci.route('/informativos_dimci')
@login_required
def informativos_dimci():
    informativos = Informativo_Dimci.query.all()
    return render_template('informativos_dimci.html',informativos = informativos)

@informativo_dimci.route('/adicionarInformativo_Dimci', methods = ['GET', 'POST'])
@login_required
def adicionarInformativo_Dimci():
    if request.method == 'POST':
        informacao = request.form['informacao']
        #data_registro = request.form['data_registro']
        usuario = current_user

        informativo = Informativo_Dimci(informacao = informacao, usuario = usuario)
        db.session.add(informativo)
        db.session.commit()
        return redirect(url_for('informativo_dimci.informativos_dimci'))

    return render_template('informativo_dimci.html')

@informativo_dimci.route('/editarInformativo_Dimci/<int:id>', methods= ['GET', 'POST'])
def editarInformativo_Dimci(id):
    informativo = Informativo_Dimci.query.get(id)

    if request.method == 'POST':
        informativo.informacao= request.form['informacao']
        db.session.commit()
        return redirect(url_for('informativo_dimci.informativos_dimci'))

    return render_template('editar_informativo_dimci.html', i = informativo)

@informativo_dimci.route('/deletarInformativo_Dimci/<int:id>')
def deletar(id):
    informativo = Informativo_Dimci.query.get(id)
    db.session.delete(informativo)
    db.session.commit()
    return redirect(url_for('informativo_dimci.informativos_dimci'))

