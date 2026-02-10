# 1. Create a class `Person` with a protected attribute _name
# 2. Add a getter for _name using @property
# 3. Create a Person object and print the name using the getter
class person:
    def __init__(self,name):
        self.name = name
    @property
    def name(self):
     return self._name
    @name.setter
    def name(self,value):
       if len(value)>= 3:
          self.name = value
       else:
          print("name is too short")
p1 = person("ra")
print(p1.name) 