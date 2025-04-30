import time
import uuid
from Users import Users
from Loaction import location
from Rider import Rider
from Driver import Driver
from RideService import RideService
class Ride:
    def __init__(self, rider,driver, source,destination):
        self.ride_id= str(uuid.uuid4())
        self.rider= rider
        self.driver= driver
        self.source= source
        self.destination= destination
        self.start_time=None
        self.end_time=None
        self.fare=0
    
    def start_ride(self):
        self.start_time= time.time()
    
    def end_ride(self):
        self.end_time= time.time()
        distance= self.source.distance_to(self.destination)
        duration= self.end_time- self.start_time
        self.fare = round(10 + distance * 5 + duration * 0.1, 2)
        self.rider.ride_history.append(self)
        self.driver.ride_history.append(self)
        return self.fare

if __name__ == "__main__":
    service = RideService()

    rider = Rider("r1", "rider@email.com", "Rider1")
    d1 = Driver("d1", "d1@email.com", "Driver1")
    d2 = Driver("d2", "d2@email.com", "Driver2")

    service.register_rider(rider)
    service.register_drivers(d1, location(1, 1))
    service.register_drivers(d2, location(10, 10))

    source = location(0, 0)
    destination = location(4, 3)

    ride = service.request_ride(rider, source, destination)

    if ride:
        ride.start_ride()
        time.sleep(2)
        fare = ride.end_ride()
        print(f" Fare for the ride: ₹{fare}")
        print(f"Rider History: {[r.ride_id for r in rider.ride_history]}")
        print(f"Driver History: {[r.ride_id for r in d1.ride_history]}")