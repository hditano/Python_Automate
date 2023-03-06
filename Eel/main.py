import eel
import webview
from SimConnect import *


eel.init('web', allowed_extensions=['.js', '.html'])
#eel.init('web')
#eel.start('hello.html', size=(1216, 739),mode=None, block=False)
sm = SimConnect()
aq = AircraftRequests(sm, _time=2000)

@eel.expose
def test_simconnect():
    altitude = aq.get("PLANE_ALTITUDE")
    return altitude

#webview.create_window('Title', 'web/hello.html', frameless=True, easy_drag=False)

#webview.start()

eel.start('hello.html')