from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate , MigrateCommand
from flask_script import Manager
from flask_login import LoginManager
import os.path




app = Flask(__name__,template_folder='../app/templates',static_folder='../app/static')

app.config.from_object('SGI_v0.config')

db = SQLAlchemy(app)


#migrate = Migrate(app,db,render_as_batch=True)

#manager = Manager(app)
#manager.add_command('db',MigrateCommand)


lm = LoginManager()
lm.login_view = 'auth.login'
lm.init_app(app)
#lm = LoginManager(app)



from app.models import usuario,equipamento, forms
from app.controllers import main
from app.controllers.main import main as main_blueprint
from app.controllers.auth import auth as auth_blueprint
from app.controllers.equipamento import equip as equip_blueprint
from app.controllers.laeta import laeta as laeta_blueprint
from app.controllers.dimci import dimci as dimci_blueprint
from app.controllers.cliente import cliente as cliente_blueprint
from app.controllers.agendamento import agendamento as agendamento_blueprint
from app.controllers.indice_geral import indice as indice_blueprint
from app.controllers.informativo_dimci import informativo_dimci as informativo_dimci_blueprint
app.register_blueprint(main_blueprint)
app.register_blueprint(auth_blueprint)
app.register_blueprint(equip_blueprint)
app.register_blueprint(laeta_blueprint)
app.register_blueprint(dimci_blueprint)
app.register_blueprint(cliente_blueprint)
app.register_blueprint(agendamento_blueprint)
app.register_blueprint(indice_blueprint)
app.register_blueprint(informativo_dimci_blueprint)


#from app.models.tables import User

# @lm.user_loader
# def load_user(user_id):
# # since the user_id is just the primary key of our user table, use it in the query for the user
#     return User.query.get(int(user_id))

def create_app():
 db.create_all()
 return app





