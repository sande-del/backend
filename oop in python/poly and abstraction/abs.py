# Task: Abstraction (Simple)
# 1. Create an abstract class Device using ABC
# 2. Add an abstract method turn_on() → no implementation
# 3. Create a concrete class Laptop that inherits Device
#    - Implement turn_on() → print "Laptop is starting"
# 4. Create a concrete class Mobile that inherits Device
#    - Implement turn_on() → print "Mobile is starting"
# 5. Create objects of Laptop and Mobile and call turn_on() on each
# 6. Note: You cannot create an object of Device directly
from abc import ABC, abstractmethod
class device(ABC):
    @abstractmethod
    def turn_on(self):
        pass
class laptop(device) :
    def turn_on(self):
        print("laptop is starting")
class mobile(device) :
    def turn_on(self):
        print("mobile is starting")
class ps5(device) :
    def turn_on(self):
        print("ps5 is starting")
a =laptop()
a.turn_on()
b =mobile()
b.turn_on() 
c =ps5()
c.turn_on()       

 