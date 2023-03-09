from SimConnect import *
import math
import time


sm = SimConnect()

aq = AircraftRequests(sm, _time=2000)

URL = 'http://maps.google.com/?q='

altitude = aq.find("PLANE_ALTITUDE")
altitude.time = 200

while True:

    altitude = aq.get("PLANE_ALTITUDE")
    altitude = altitude + 1000



    latitude = aq.get("PLANE_LATITUDE")
    longitude = aq.get("PLANE_LONGITUDE")
    title = aq.get("TITLE")
    throttle = aq.get("GENERAL_ENG_THROTTLE_LEVER_POSITION:1")
    altitude = aq.get("PLANE_ALTITUDE")

    starttime = time.time()


    print(f'Latitude: {latitude} | longitude: {longitude}')
    print(f'http://maps.google.com/?q={latitude},{longitude}')
    print(f'Altitude: {math.trunc(altitude)}ft')
    print(title)
    print(f'Throttle: {math.trunc(throttle)}%')
    time.sleep(5.0 - ((time.time() - starttime) % 5.0))
sm.exit()
quit()