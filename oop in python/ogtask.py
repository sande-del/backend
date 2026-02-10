# Task: OOP Revision (no encapsulation)
# 1. Create class Person with __init__(name, age)
# 2. Add method show_info() → print name and age
# 3. Create class Student inheriting Person
# 4. In Student.__init__, use super() and add subject
# 5. Override show_info():
#    - call parent show_info() using super()
#    - then print subject
# 6. Create Student object and call show_info()
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(f"The name of person {self.name} and his age is {self.age}")
        
class student(person):
    def __init__(self, name, age,subject):
        super().__init__(name, age)
        self.subject =subject
    def show(self):
        super().show()
        print(f"The subject of student is {self.subject} ")
a2 =student("ram",20,"generative AI")
a2.show()