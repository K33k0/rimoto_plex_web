
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rimototo.db'
#app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html', port=5123, domain='127.0.0.1')


@socketio.on('my_ping')
def ping_pong():
    emit('my_pong')

socketio.run(app,port=5123, debug=True)