# Task:
# 1. Create a class Person
# 2. Use __init__ to accept name and age
# 3. Store them using self
# 4. Add a method show() to print name and age
# 5. Create two objects and call show()
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(self.name ,self.age)

a= person("ram",30)
b = person("shyam" ,20)
a.show()
b.show()

    