# Project: Student Account System (OOP Revision)
#
# Goal:
# Build a small console-based system using ONLY the OOP concepts you have learned so far.
#
# Concepts to use:
# - Class & Object
# - __init__
# - Methods
# - Encapsulation (private variables + getter/setter)
# - Inheritance
# - super()
# - Method Overriding
# - Polymorphism
# - Abstraction (ABC, abstractmethod)
#
# Structure:
# Student (Abstract Base Class)
# ├── SchoolStudent
# └── CollegeStudent
#
# Tasks:
#
# 1. Create an abstract class Student
#    - __init__(name, marks)
#    - marks must be private
#    - abstract method get_grade()
#    - method show_info() → prints name and marks
#
# 2. Create class SchoolStudent inheriting Student
#    - use super().__init__()
#    - implement get_grade():
#        marks >= 60 → "Pass"
#        else → "Fail"
#
# 3. Create class CollegeStudent inheriting Student
#    - use super().__init__()
#    - implement get_grade():
#        marks >= 75 → "Distinction"
#        marks >= 40 → "Pass"
#        else → "Fail"
#
# 4. Create objects:
#    - one SchoolStudent
#    - one CollegeStudent
#
# 5. Store both objects in a list
#
# 6. Loop through the list and call:
#    - show_info()
#    - get_grade()
#
# Rules:
# - Do NOT create an object of abstract Student
# - Do NOT access marks directly
# - Errors are allowed; learning comes from fixing them
#
# Start with Brick 1 first. Build step by step.



                    # PHASE ONE
# 1. Create abstract class Student
# 2. __init__(name, marks) → marks must be protected
# 3. abstract method get_grade()
# 4. method show_info() → prints name & marks
from abc import ABC, abstractmethod
class student(ABC):
    def __init__(self,name,marks):
        self._name = name
        self._marks = marks
        
    @abstractmethod
    def get_grade(self):
        pass
    def show_info(self):
        print(f"The name of student is {self._name} and his marks is {self._marks}")
    
    def get_marks(self):
        return self._marks
             
      
class school_student(student):
    def __init__(self, name, marks):
        super().__init__(name, marks)
    def get_grade(self):
        if self._marks >= 60:
            print("pass")
        else:
            print("Fail")

class collage_student(student):
    def __init__(self, name, marks):
        super().__init__(name, marks)
    def get_grade(self):
        if self._marks >= 75:
            print("you got distinction")
        elif self._marks >= 40:
            print("you are pass")
        else:
            print("sorry you failed")

a1 = school_student("RAM",50)
a2 = collage_student("hari",27)
collection = [a1,a2]
for  item in collection:
    item.show_info()
    item.get_grade()


        
        


