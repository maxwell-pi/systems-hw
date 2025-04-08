import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '928dc7c3e8db2b0ea72c9a499d64ac28'
db_path = os.environ.get("DATABASE_PATH", 'instance/notes.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from notebook import routes  # just to register routes