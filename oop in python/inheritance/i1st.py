# Task:
# 1. Create class Vehicle with __init__(brand, year) and method show()
# 2. Create class Car that inherits Vehicle
# 3. Add method drive() to Car
# 4. Create a Car object and call both show() and drive()
class vehicle:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year
    def show(self):
        print(self.brand,self.year)
class car(vehicle):
    def drive(self):
        print(f"this car is good brand is {self.brand}")

a1 =vehicle("tesla",2025)
a1.show()
a2=car("bmw",2026)
a2.drive()
 