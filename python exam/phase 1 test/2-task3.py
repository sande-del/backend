# Challenge 3 — Encapsulation & Getters/Setters
# 1. Create a class BankAccount with a private attribute __balance
# 2. Add a method deposit(amount) to add money to balance
# 3. Add a method withdraw(amount) to subtract money if balance is enough
# 4. Add a method get_balance() to return the current balance
# 5. Create an account, deposit 5000, withdraw 2000, and print the balance
class bank_acc:
    def __init__(self,balance):
        self.__balance = balance
    def deposit(self,amount):
        self.__balance += amount
    def withdraw(self,amount):
        if self.__balance >= amount:
         self.__balance -= amount 
         return self.__balance 
        else:
           print("tappai sanga paryapta balance xaina")
    def get_balance(self):
       return self.__balance
a1 = bank_acc(0) 
a1.deposit(5000) 
a1.withdraw(2000)
print(a1.get_balance())