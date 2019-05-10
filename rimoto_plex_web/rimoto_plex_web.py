
from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rimotot.sqlite'
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
db = SQLAlchemy(app)

