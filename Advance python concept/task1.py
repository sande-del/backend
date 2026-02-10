# Task:
# 1. Write a decorator named `auth_required`
# 2. The decorator should:
#    - Print "Checking authentication..." before the function runs
#    - Print "Access granted" after the function runs
# 3. Apply the decorator to a function `view_dashboard`
# 4. `view_dashboard` should print: "Dashboard data"
# 5. Call `view_dashboard()`
def auth_required(func):
    def wrapper():
        print("Checking authentication...")
        func()
        print("Access granted")
    return wrapper
@auth_required
def viewe_dashboard():
    print("Dashboard data")
viewe_dashboard()