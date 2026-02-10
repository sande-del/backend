# Task: Practice super() only
# 1. Create class Person with __init__(name, age)
# 2. Create class Student inheriting Person
# 3. In Student.__init__, use super().__init__(name, age)
# 4. Add extra attribute grade in Student
# 5. Create a Student object and print name, age, grade

# Write your code below this line
class person:
    def __init__(self,name,age):
        self.name =name
        self.age=age
class student(person):
    def __init__(self, name, age,subject):
        super().__init__(name, age)
        self.subject =subject
    def show(self):
        print(f"the name of student is {self.name},the age of student is {self.age} and is fav subject is {self.subject}")
a1 = student("ram",20,"python")
a1.show()