from SimConnect import *

class Simtracker():
    def __init__(self) -> None:
        self.sm = SimConnect()
        self.aq = AircraftRequests(self.sm, _time=2000)
        
    def altitude_timer(self):
        altitude = self.aq.find("PLANE_ALTITUDE")
        altitude = self.aq.get("PLANE_ALTITUDE")
        
        return str(altitude)
    
    

my_sim = Simtracker()
print(my_sim.altitude_timer())


        