class Levels:
    def __init__(self, level_id, slots):
        self.level_id = level_id
        self.slots = slots

    def is_available(self, vehicle_type):
        for slot in self.slots:
            if not slot.is_occupied and slot.vehicle_type == vehicle_type:
                return True
        return False

    def park_vehicle(self, vehicle):
        for slot in self.slots:
            if not slot.is_occupied and slot.vehicle_type == vehicle.vehicleType:
                return slot.park_vehicle(vehicle)
        return False

    def unpark_vehicle(self, slot_id):
        for slot in self.slots:
            if slot.slot_id == slot_id:
                return slot.unpark_vehicle()
        return False
