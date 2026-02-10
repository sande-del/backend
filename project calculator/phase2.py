# Task:
# 1. Create four functions: add(a,b), sub(a,b), mul(a,b), div(a,b)
# 2. Each function performs its operation and returns the result
# 3. Create a run_calculator() function:
#    - Take two numbers
#    - Take operator
#    - Call the correct function
#    - Handle division by zero
# 4. Print the final result
# 5. Program runs only once
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    if b == 0:
     return "this operation is impossible"
    else:
       return a/b
def run_calc():
    a = int(input('enter a first number '))
    b = int(input("Enter a second number "))
    operator = input(' enter a operatr +,-,*,/ ')
    if operator == "+":
        print(add(a,b))
    elif operator == "-":
        print(sub(a,b))
    elif operator == "*":
        print(mult(a,b))
    elif operator == "/":
        print(div(a,b)) 
    else:
        print("You entered wrong operator ")
run_calc()