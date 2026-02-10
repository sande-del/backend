# Challenge 2 — Inheritance
# 1. Create a parent class Employee with attributes: name and salary
# 2. Add a method display_info() to print name and salary
# 3. Create a child class Manager that inherits Employee and adds department
# 4. Override display_info() in Manager to also print the department
# 5. Create one Employee and one Manager object and call their display_info() methods
class employee:
    def __init__(self,name ,salary):
        self.name = name
        self.salary = salary
    def display_info(self):
        print(f"The name of employee is {self.name} and his salary is {self.salary}")
class manager(employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department = department
    def display_info(self):
         super().display_info()
         print(f"the department of the emloyee is {self.department}")
a1 = manager('ram',45000,"coldstore")
a1.display_info()