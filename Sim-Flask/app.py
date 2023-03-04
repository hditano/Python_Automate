import threading
import time
from SimConnect import *
from flask import Flask, render_template
from turbo_flask import Turbo

app = Flask(__name__)
turbo = Turbo(app)
sm = SimConnect()

my_variable = 0

@app.route('/my_variable')
def get_my_variable():
    global my_variable
    my_variable += 1
    return str(my_variable)

@app.route('/data')
def index():
    return render_template('data.html')


@app.before_first_request
def before_first_request():
    threading.Thread(target=update_load).start()


def update_load():
    with app.app_context():
        while True:
            time.sleep(5)
            turbo.push(turbo.replace(render_template('simtracker.html'), 'load'))


@app.route('/simtracker')
def simtracker_load():
    aq = AircraftRequests(sm, _time=0)

    altitude = aq.get("PLANE_ALTITUDE")

    return render_template('simtracker.html', altitude=altitude)


if __name__ == '__main__':
    app.run()
