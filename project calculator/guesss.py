import random
secretenumber  = random.randint(1,20)
guess = int(input("enter a number from 1 to 20 ")) 
if guess == secretenumber:
    print("you picked right number")
else:
    print("Try again")
