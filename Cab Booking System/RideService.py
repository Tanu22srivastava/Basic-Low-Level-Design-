class RideService:
    def __init__(self):
        self.riders=[]
        self.drivers={}

    def register_rider(self,rider):
        self.riders.append(rider)

    def register_drivers(self,driver,location):
        self.drivers[driver]=location

    def request_ride(self, rider, source, destination):
        from Ride import Ride
        nearest_driver= None
        max_distance= float('inf')

        for driver,location in self.drivers.items():
            if driver.is_available:
                distance= location.distance_to(source)
                if distance < max_distance:
                    max_distance= distance
                    nearest_driver= driver

        if not nearest_driver:
            return "no driver available!" 
        
        nearest_driver.is_available= False
        ride= Ride(rider, nearest_driver, source, destination)
        print(f"Ride stated with driver : {nearest_driver}")
        return ride
    
    def cancel_ride(self,ride):
        ride.driver.is_available=True
        print(f"rider with  id {ride.ride_id} is cancelled")