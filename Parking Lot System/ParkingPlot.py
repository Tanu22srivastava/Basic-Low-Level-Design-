from levels import Levels
from Slot import Slot
from Vehicle import Vehicle, vehicleType

class ParkingPlot:
    def __init__(self,levels):
        self.levels= levels

    def park_vehicle(self, vehicle):
        for level in self.levels:
            if level.is_available(vehicle.vehicleType):
                if level.park_vehicle(vehicle):
                    return (level.level_id, vehicle)
        return None
    
    def unpark_vehicle(self,level_id, slot_id):
        for level in self.levels:
            if level.level_id==level_id:
                return level.unpark_vehcile(slot_id)
        return None
    
slot1 = Slot(slot_id=1, vehicle_type=vehicleType.Bike)
slot2 = Slot(slot_id=2, vehicle_type=vehicleType.Car)
slot3 = Slot(slot_id=3, vehicle_type=vehicleType.Truck)

level= Levels(level_id=1, slots=[slot1,slot2,slot3])
parkingPlot= ParkingPlot(levels=[level])

bike= Vehicle(vehicleType = vehicleType.Bike)
car= Vehicle(vehicleType= vehicleType.Car)
truck= Vehicle(vehicleType= vehicleType.Truck)
car1= Vehicle(vehicleType= vehicleType.Car)

print("parking bike :", parkingPlot.park_vehicle(bike))
print("parking car :", parkingPlot.park_vehicle(car))
print("parking truck :", parkingPlot.park_vehicle(truck))
print("parking car :", parkingPlot.park_vehicle(car1))