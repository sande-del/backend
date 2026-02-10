# 1. Take input from the user
# 2. Convert it to int
# 3. Handle error if user enters non-number
# 4. Print the number if valid
# try:
#     num = int(input("Enter a number: "))
#     print(10 / num)
# except ValueError:
#     print("You must enter a number")
# except ZeroDivisionError:
#     print("Cannot divide by zero")
try:
    a = input("enter a number")
    num = int(a)
except:
    print("you entered no numeric value")