import PySimpleGUI as sg
from SimConnect import *
import time
import math
import folium
from tkinterweb import HtmlFrame

sm = SimConnect()
aq = AircraftRequests(sm, _time=2000)
my_list = {}
LONG = ''
LAT = ''
my_map = {}

#frame = HtmlFrame(sg)

#my_l = frame.load_website("http://www.google.com")

def simconnect_test():
    
    global my_map
    
    pi = 22/7
    altitude = aq.get("PLANE_ALTITUDE")
    speed = aq.get("AIRSPEED_INDICATED")
    hdg = aq.get("PLANE_HEADING_DEGREES_TRUE")
    LAT = aq.get("PLANE_LATITUDE")
    LONG = aq.get("PLANE_LONGITUDE")
    map = folium.Map(location=[LAT, LONG], zoom_start=14)
    map.save('index.html')
    my_map = map
    radian = hdg
    degree = radian*(180/pi)
    my_list['altitude'] = math.trunc(altitude)
    my_list['speed'] = math.trunc(speed)
    my_list['hdg'] = degree
    

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
#mapview = window['html']
while True:
    simconnect_test()
    event, values = window.read(timeout=10)
    current_time = int(round(time.time() * 500)) - start_time
    window['Input2'].update(my_list["altitude"])
    window['Input3'].update(my_list["speed"])
    window['Input4'].update(my_list["hdg"])
    #mapview.update(my_l)
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