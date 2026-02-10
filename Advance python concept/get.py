class employee :
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def first_name(self):
        l = self.name.split(" ")
        return l[1]
e = employee("shree ram", 45000)
print(e.first_name())
        