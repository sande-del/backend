# Task 2:
# Write a recursive function print_up(n)
# It should print numbers from 1 to n
# Example: print_up(4) → 1 2 3 4
def up(n):
    if n==0:
        return
    up(n-1)
    print(n)
up(4)
