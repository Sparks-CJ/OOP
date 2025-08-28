# Base class
class Vehicle:
    def move(self):
        pass  # Base method

# Derived classes with polymorphic behavior
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵️")

# Demonstrate polymorphism
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()
