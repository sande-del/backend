# Task:
# 1. Ask user for two numbers
# 2. Ask user for operation (+, -, *, /)
# 3. Perform the operation using if/elif
# 4. Print the result
# 5. Handle division by zero
a =int(input("enter a number"))
b =int(input("enter a number"))
sign = input("enter a sign "+" ,-,*,/")
if sign == "+": 
   print(a+b)
elif sign == "-":
   print(a-b)
elif sign == "*":
   print(a*b)