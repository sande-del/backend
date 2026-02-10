# Challenge 1 — Basic Class & Object
# 1. Create a class Student with two attributes: name and marks
# 2. Add a method display() that prints the name and marks of the student
# 3. Create two Student objects with different names and marks
# 4. Call display() for both objects
class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def display(self):
        print(f"The name of the student is {self.name}, and his marks is {self.marks}")
a1 = student("Ram",78)
a2 = student("hari",90)
a1.display()
a2.display()
        