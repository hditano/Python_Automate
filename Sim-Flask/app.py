from SimConnect import *
from flask import Flask, render_template
import math

app = Flask(__name__)
sm = SimConnect()

my_variable = 0

@app.route('/my_variable')
def get_my_variable():
    global my_variable
    aq = AircraftRequests(sm, _time=0)
    my_variable = aq.get("PLANE_ALTITUDE")
    return str(math.trunc(my_variable))

@app.route('/data')
def index():
    return render_template('data.html')

@app.route('/')

@app.route('/simtracker')
def simtracker_load():
    return render_template('simtracker.html', variable=my_variable)


if __name__ == '__main__':
    app.run()


