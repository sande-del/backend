# 1. Create a class Student with attributes: name, roll_number
# 2. Implement __str__ to return "Student: {name}, Roll No: {roll_number}"
# 3. Create a Student object and print it
class studet:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
    def __str__(self):
      return f" The name of the student is {self.name},and his roll number is {self.roll}"
a = studet('ram',34)
print (a)