import os.path

#basedir = os.path.abspath(os.path.dirname(__file__))
#SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(basedir,' sgi_storage.db')

basedir = '../SGI_v0'

SQLALCHEMY_DATABASE_URI = 'sqlite:////home/ebpinto/SGI_v0/sgi_banco_de_dados.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

DEBUG = True

SECRET_KEY = 'uma-chave-bem-segura'