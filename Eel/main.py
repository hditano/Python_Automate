import eel
import webview
from SimConnect import *
import math

eel.init('web', allowed_extensions=['.js', '.html'])
eel.init('web')
#eel.start('hello.html', size=(1216, 739),mode=None, block=False)
#sm = SimConnect()
#aq = AircraftRequests(sm, _time=2000)

# CONST
dict = {}

@eel.expose
def test_simconnect():
    global map
    
    altitude = aq.get("PLANE_ALTITUDE")
    speed = aq.get('AIRSPEED_INDICATED')
    longitude = aq.get('PLANE_LONGITUDE')
    latitude = aq.get('PLANE_LATITUDE')
    dict.update({'altitude':altitude,'speed':speed, 'longitude': longitude, 'latitude': latitude})
    print(dict)
    return dict

webview.create_window('Title', 'web/hello.html', frameless=True, easy_drag=False)

webview.start()

#eel.start('hello.html')