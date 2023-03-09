from fastapi import FastAPI
from flaskwebgui import FlaskUI

from nicegui import ui
from SimConnect import *

# INITIALIZATION
app = FastAPI()
sm = SimConnect()
aq = AircraftRequests(sm, _time=2000)
# Global Variables
sim_data = {}



def handle_simtracker():
    global sim_data
    altitude = aq.get("PLANE_ALTITUDE")
    sim_data['altitude'] = altitude
    print('data going on')
    

with ui.tabs() as tabs:
        ui.tab('Home', icon='home')
        ui.tab('About', icon='info')

with ui.tab_panels(tabs, value='Home'):
    with ui.tab_panel('Home'):
        toggle1 = ui.label('Altitude')
        t = ui.timer(interval=4, callback=handle_simtracker)
        a = ui.timer(interval=5, callback=lambda: toggle1.set_text(
            sim_data['altitude']))
        ui.label('Speed')
        ui.label('Heading')
        ui.button('Call Data', on_click=handle_simtracker)

    def handle_change(e):
        global toggle_value
        toggle_value = e.value

    def handle_simtracker(e):
        global toggle_simtrack
        toggle_simtrack = e.value

ui.run_with(app, dark=True)

if __name__ == "__main__":
    FlaskUI(app=app, server="fastapi", width=800, height=600).run()