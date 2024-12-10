# Base class Animal
class Animal:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Subclass for Car
class Car(Animal):
    def move(self):
        print("Driving 🚗")

# Subclass for Plane
class Plane(Animal):
    def move(self):
        print("Flying ✈️")

# Subclass for Bike
class Bike(Animal):
    def move(self):
        print("Riding 🚲")

# Creating objects for each class
car = Car()
plane = Plane()
bike = Bike()

# Demonstrating Polymorphism: Each object calls the same move() method, but each does it differently
def demonstrate_movement(vehicle):
    vehicle.move()

# Demonstrating the polymorphic behavior
demonstrate_movement(car)  # Output: Driving 🚗
demonstrate_movement(plane)  # Output: Flying ✈️
demonstrate_movement(bike)  # Output: Riding 🚲
