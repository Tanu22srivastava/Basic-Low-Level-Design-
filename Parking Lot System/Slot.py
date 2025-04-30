class Slot:
    def __init__(self, slot_id, vehicle_type):
        self.slot_id = slot_id
        self.vehicle_type = vehicle_type
        self.is_occupied = False
        self.parked_vehicle = None

    def park_vehicle(self, vehicle):
        if self.is_occupied:
            return False
        self.parked_vehicle = vehicle
        self.is_occupied = True
        return True

    def unpark_vehicle(self):
        if not self.is_occupied:
            return False
        vehicle = self.parked_vehicle
        self.parked_vehicle = None
        self.is_occupied = False
        return vehicle
