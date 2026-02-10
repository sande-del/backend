# Task 3:
# Write a recursive function sum_n(n)
# It should return the sum of numbers from 1 to n
# Example: sum_n(5) → 15
def sum(n):
    if n == 0:
        return 0
    return n + sum(n-1)
print(sum(5))
   

