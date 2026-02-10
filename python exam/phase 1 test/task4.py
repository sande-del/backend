# Q4 — Functions
# Write a function factorial(n) that returns the factorial of a number n
# Test the function with n = 5 and print the result
def func(n):
    if n == 0:
     return 1 
    return n* func(n-1)
print(func(5))