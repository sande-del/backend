# 1. Create a decorator `log_call`
# 2. It should print "Calling function..."
# 3. It must work with functions that take arguments
# 4. Apply it to a function `add(a, b)` that prints the sum
# 5. Call add(5, 10)
def log_call(func):
    def wrapper(*a,**b):
        print("Calling function...")
        result = func(*a,**b)
        return result
    return wrapper
@log_call 
def add(a,b):
    return a + b
add(5,5)       