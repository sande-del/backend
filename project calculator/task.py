# Task:
# 1. Take two numbers from user
# 2. Take operator (+, -, *, /)
# 3. Use if / elif / else
# 4. Handle division by zero
# 5. Print result or error
a = int(input("Enter a first number "))
b = int(input("Enter a second number "))
operator = input('Enter a operator +, -, *, / ')
if operator == "+":
    print(a+b)
elif operator == "-":
    print(a-b)
elif operator == "*":
    print(a*b)
# if operator == "/" and  b==0:
#      print("this operation is impossible")
elif operator == "/":
    if b == 0:
       print("this operation is imposible")
    else:
     print(a/b)
else:
 print("you entered wrong operato")