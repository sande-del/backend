def decorator(func):
    def wrapper():
        print("iam about to exxute function")
        func()
        print("i have executed the function")
    return wrapper
@decorator
def say_hello():
    print("hello")
say_hello()
# say_hello()
# f = decorator(say_hello)
# f()
