from enum import Enum

class vehicleType(Enum):
    Bike=1
    Car=2
    Truck=3

class Vehicle:
    def __init__(self, vehicleType):
        self.vehicleType= vehicleType