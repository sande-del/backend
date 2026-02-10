# Task:
# 1. Create a class Laptop
# 2. Use __init__ to accept brand, model, and price
# 3. Store them in self
# 4. Add a method show() to print all details
# 5. Create two Laptop objects with different values
# 6. Call show() on both objects
class laptop:
    def __init__(self,brand,model,price):
        self.brand =brand
        self.model = model
        self.price = price
    def show(self):
        print(f"The brand of laptop is { self.brand} the model is {self.model}price is {self.price}")
        #  print(self.brand,self.model,self.price)
    
a1=laptop("dell", "xbs",6000)
a2=laptop("asus","mp22n",1009)
a1.show()
a2.show()

