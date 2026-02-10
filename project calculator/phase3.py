# Task: Create an OOP Calculator

# 1. Make a class named Calculator
# 2. Implement methods for +, -, *, / (handle division by zero)
# 3. Implement a run() method to take user input and perform the operation
# 4. Outside the class, create an instance and call run()
class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mult(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            return "This operation is impossible"
        else:
            return a / b

    def run(self):
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        operator = input("Enter an operator (+, -, *, /): ")

        if operator == "+":
            print(self.add(a, b))
        elif operator == "-":
            print(self.sub(a, b))
        elif operator == "*":
            print(self.mult(a, b))
        elif operator == "/":
            print(self.div(a, b))
        else:
            print("You entered wrong operator")

# Create an instance and run the calculator
calc = Calculator()
calc.run()