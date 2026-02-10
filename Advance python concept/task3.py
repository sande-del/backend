# Task:
# 1. Create a decorator `trace_call`
# 2. It should print "Function is called" before running the function
# 3. Use names `*a` for positional arguments, `**b` for keyword arguments
# 4. Apply it to a function `person_info(name, age)` that returns "{name} is {age} years old"
# 5. Call person_info("Champ", 22) and print the return value
def trace_call(func):
    def wrapper(*a,**b):
        print("Function is called")
        result = func(*a,**b)
        print("function called")
        return result
    return wrapper
@trace_call
def person_info(name,age):
    print(f"the name of person is {name},age is {age}")
(person_info("ram",20))