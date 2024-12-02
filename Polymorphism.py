# Base class for Vehicle
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Car class inheriting from Vehicle
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

# Plane class inheriting from Vehicle
class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

# Example of polymorphism
def demonstrate_move(vehicle: Vehicle):
    print(vehicle.move())

# Creating instances
car = Car()
plane = Plane()

# Demonstrating polymorphism
demonstrate_move(car)   # Should print "Driving 🚗"
demonstrate_move(plane) # Should print "Flying ✈️"
