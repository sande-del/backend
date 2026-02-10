# Task 1:
# Write a recursive function print_down(n)
# It should print numbers from n to 1
# Example: print_down(4) → 4 3 2 
def  down(n):
    if n==1:
        return
    print(n)
    down(n-1)
down(4)