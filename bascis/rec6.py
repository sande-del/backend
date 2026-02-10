# Write a recursive function count_digits(n)
# It should return how many digits are in the number
# Example: count_digits(3456) → 4
def count(n):
    if n==0:
        return 0
    return 1 + count(n//10)
print(count(8876))