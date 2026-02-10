# Task 1: Write a function greet_person(name="Friend") that prints "Hello, <name>!"
# Call it with no argument and with a name
# def greet_person(name = "friend"):
#     print("hello",name)
# greet_person()

# Task 3: Write a function describe_student(name="Unknown", grade="A", city="Kathmandu")
# Print a description using f-string
# Call it with no arguments, with one argument, and using keyword arguments
# def des_std(name="Unknown", grade="A", city="Kathmandu"):
#     print(f"The name of student is {name}.He studies in grade {grade} and he lives in {city}")
# des_std()
# des_std(name="ram", grade=5)


# Task 2: Write a function calculate_power(base, exponent=2) that returns base^exponent
# Call it with one and two arguments
def calc(base,expo =2):
    return base**expo
result = calc(4)
print(result)