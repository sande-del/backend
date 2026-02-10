# Task (Hour 1 – Task 1):
# 1. Create a class Account
# 2. __init__ should take owner name and balance
# 3. Add method deposit(amount) → add to balance
# 4. Add method withdraw(amount) → subtract from balance
# 5. Add method show_balance() → print owner and balance
# 6. Create one object and call methods in this order:
#    deposit → deposit → withdraw → show_balance
class account:
    def __init__(self,name,balance):
        self.name = name
        self. balance =balance
    def deposit(self,amount):
            self.balance =  self.balance + amount
    def withdraw(self,amount):
         self.balance = self.balance - amount
    def show(self):
         print(f"The name of owner is {self.name} and his blance is {self.balance}")
        

a1 = account("ram",60000)
a1.deposit(5000)
a1.deposit(5000)
a1.withdraw(15000)
a1.show()

         

       