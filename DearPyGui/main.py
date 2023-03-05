import PySimpleGUI as sg
from SimConnect import *
import time
import math

sm = SimConnect()
aq = AircraftRequests(sm, _time=2000)
my_list = {}

def simconnect_test():
    
    altitude = aq.get("PLANE_ALTITUDE")
    speed = aq.get("AIRSPEED_INDICATED")
    hdg = aq.get("PLANE_HEADING_DEGREES_TRUE")
    my_list['altitude'] = math.trunc(altitude)
    my_list['speed'] = math.trunc(speed)
    my_list['hdg'] = hdg

sg.theme('DarkAmber')   # General Theme
# Window Layout
layout = [  [sg.Text('', size=(60, 1)),sg.Text('🗖', enable_events=True, key='Max'),sg.Text('X',enable_events=True ,key='Input1')],
            [sg.Text('Altitude:'),sg.Text('', key='Input2'),sg.Text('ft')],
            [sg.Text('Speed: '), sg.Text('', key='Input3'), sg.Text('kt')],
            [sg.Text('Heading: '), sg.Text('', key='Input4'), sg.Text('dg')],
            [sg.Button('Ok'), sg.Button('Cancel')]
        ]

# create Window
window = sg.Window('Window Title', layout, no_titlebar=True, grab_anywhere=True, keep_on_top=True)
# Main Event Loop

start_time = int(round(time.time() * 500))
while True:
    simconnect_test()
    event, values = window.read(timeout=10)
    current_time = int(round(time.time() * 500)) - start_time
    window['Input2'].update(my_list["altitude"])
    window['Input3'].update(my_list["speed"])
    window['Input4'].update(my_list["hdg"])
    if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Input1': # if user closes window or clicks cancel
        break
    elif event == 'Max':
        window.maximize()
        state = window.TKroot.state()
        print(state)
        if state == 'zoomed':
            window.minimize()
    elif event == 'Ok':
        window['Input2'].update(simconnect_test())
        

window.close()