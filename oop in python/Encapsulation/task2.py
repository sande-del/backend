# Task: BankAccount (Encapsulation)
# 1. Create class BankAccount
# 2. Private variable __balance
# 3. __init__ should validate initial balance (>= 0)
# 4. get_balance() → return balance
# 5. deposit(amount) → add amount if amount > 0
# 6. withdraw(amount) → subtract only if amount <= balance
# 7. Create object with balance 1000
# 8. deposit 500
# 9. withdraw 300
# 10. print final balance
class bankaccount:
    def __init__(self,balance):
        if balance >=0:
         self.__balance =balance
        else:
           self.__balance = 0

    def get_balance(self):
       return self.__balance
    def deposite(self,amount):
       if amount >0 :
          self.__balance = self.__balance + amount
    def withdraw(self,amount):
       if amount <= self.__balance:
          self.__balance = self.__balance - amount
       
a1 = bankaccount(1000)
print(a1.get_balance())
a1.deposite(500)
print(a1.get_balance())
a1.withdraw(300)
print(a1.get_balance())