# Task 4:
# Write a recursive function factorial(n)
# It should return n factorial
# Example: factorial(5) → 120
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)
print(fact(5))






    