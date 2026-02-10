# Task: Polymorphism
# 1. Create class Vehicle with method move() → "Vehicle is moving"
# 2. Create class Car inheriting Vehicle → override move() → "Car is driving"
# 3. Create class Bike inheriting Vehicle → override move() → "Bike is riding"
# 4. Create objects of Vehicle, Car, Bike
# 5. Call move() on all objects
class vehicle:
    def move(self):
        print("vehicle is moving")
    
class car (vehicle):
    def move(self):
        print("car is driving")

class bike(vehicle):
    def move(self):
        print("bike is riding")
a = vehicle()
b = car()
c = bike()
a.move()
b.move()
c.move()