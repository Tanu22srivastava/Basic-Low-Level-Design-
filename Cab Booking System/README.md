# 🚖 Cab Booking System – Low Level Design (LLD)

A Python-based simulation of a simplified **cab booking system**, inspired by ride-hailing services like Uber and Ola. This system demonstrates core OOPS concepts, ride lifecycle management, driver allocation based on location, and fare calculation.

---

## 📦 Modules & Classes

### 👤 Users (Base Class)
- `Users`: Common base for `Rider` and `Driver`
  - `user_id`, `email`, `name`

### 👨‍✈️ Driver (inherits `Users`)
- Has availability status
- Maintains `ride_history`

### 🧍 Rider (inherits `Users`)
- Can request rides
- Maintains `ride_history`

### 📍 Location
- Represents coordinates `(x, y)`
- Method: `distance_to()` to calculate Euclidean distance

### 🚗 Ride
- Represents a ride from source to destination
- Tracks:
  - `ride_id` (UUID)
  - `start_time`, `end_time`
  - `fare`
  - Rider & driver
- `start_ride()` and `end_ride()` methods manage the ride lifecycle and fare computation.

### 🛠 RideService
- Registers riders and drivers
- Allocates the nearest available driver to a rider
- Cancels rides and resets driver availability

---

