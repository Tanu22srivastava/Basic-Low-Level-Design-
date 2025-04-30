# 🚗 Parking Lot System – Low Level Design (LLD)

This project is a basic Low-Level Design (LLD) implementation of a Parking Lot System in Python. It is designed using object-oriented principles to simulate multi-floor parking with support for different vehicle types.

---

## 📚 Features

- Multiple floors, each with multiple slots
- Slots designated for specific vehicle types (Car, Bike, Truck)
- Parking and unparking of vehicles
- Check available slots
- Enums used for vehicle type consistency

---

## 🏗️ Design Overview

### Classes Implemented:

- `Slot`: Represents a parking slot. Knows if it's occupied and what vehicle is parked.
- `Floor`: Contains multiple slots and handles parking/unparking logic at the floor level.
- `Vehicle`: Base class with type (Car, Bike, Truck).
- `Parking_lot`: Aggregates all floors. Handles system-level operations like finding available slots and managing vehicle entry/exit.

---

## 🧪 Example Flow

```python
# Create slots
slot1 = Slot(slot_id=1, vehicle_type=vehicle_type.CAR)
slot2 = Slot(slot_id=2, vehicle_type=vehicle_type.BIKE)

# Create a floor and add slots
floor = Floor(floor_id=1, slots=[slot1, slot2])

# Create parking lot with the floor
parkingLot = Parking_lot(floors=[floor])

# Create vehicles
bike = Vehicle(vehicle_type=vehicle_type.BIKE)
car = Vehicle(vehicle_type=vehicle_type.CAR)

# Park vehicles
parkingLot.park_vehicle(bike)
parkingLot.park_vehicle(car)

# Display available slots
parkingLot.available_slots()
