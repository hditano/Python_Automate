from threading import Lock
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from SimConnect import *

app = Flask(__name__)
app.secret_key = 'your secret here'
sio = SocketIO(app)

thread = None
thread_lock = Lock()

my_list = {}


@app.route('/')
def index():
    SimConnect()
    return render_template('index.html')


def background_task():
    while True:
        sio.sleep(10)
        sio.emit('my_response', my_list)


@sio.on('connect')
def connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = sio.start_background_task(background_task)
    emit('my_response', {'data': 'connected'})


def SimConnect():
    global my_list
    sm = SimConnect()
    aq = AircraftRequests(sm, _time=2000)
    altitude = aq.find("PLANE_ALTITUDE")
    my_list.append(altitude)

if __name__ == '__main__':
    sio.run(app)