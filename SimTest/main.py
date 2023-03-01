from SimConnect import *
import math

sm = SimConnect()

aq = AircraftRequests(sm, _time=2000)

URL = 'http://maps.google.com/?q='

altitude = aq.find("PLANE_ALTITUDE")
altitude.time = 200


altitude = aq.get("PLANE_ALTITUDE")
altitude = altitude + 1000

latitude = aq.get("PLANE_LATITUDE")
longitude = aq.get("PLANE_LONGITUDE")
title = aq.get("TITLE")
throttle = aq.get("GENERAL_ENG_THROTTLE_LEVER_POSITION:1")

print(f'Latitude: {latitude} | longitude: {longitude}')
print(f'http://maps.google.com/?q={latitude},{longitude}')
print(title)
print(f'Throttle: {math.trunc(throttle)}%')

sm.exit()
quit()