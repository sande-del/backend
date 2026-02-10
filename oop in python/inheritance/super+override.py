# Task:
# 1. Create a class Animal with __init__(name) and method sound() that prints "Animal makes sound"
# 2. Create class Dog inheriting Animal
# 3. In Dog.__init__, use super().__init__(name) and add attribute breed
# 4. Override sound() in Dog: first call super().sound(), then print "Dog barks"
# 5. Create object of Dog and call sound()
class animal:
    def __init__(self,name):
        self.name = name
    def sound(self):
        print(f"{self.name} makes sound")

class dog(animal):
    def __init__(self, name,breed):
        super().__init__(name)
        self.breed =breed
    def sound(self):
        super().sound()
        print(f"Its breed is {self.breed} ")
a1 = dog("kanxu","tibetian mastif")
a1.sound()
a2 =dog("kancho","sallisha")
a2.sound()
    

