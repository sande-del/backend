def print_1_to_n(n):
    if n == 0:       # base case
        return
    print_1_to_n(n - 1)
    print(n)

print_1_to_n(3)
