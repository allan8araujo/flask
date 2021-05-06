from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f9ab7221cb7e60be8233b442ec95d00e'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
login_manager=LoginManager(app)
db= SQLAlchemy(app)
bcrypt= Bcrypt(app)
from aplicativo import routes