sen = "hello is name is drake"
sum =0
vowels =['a','e','i','o','u']
for char in sen.lower():
    if(char in vowels):
        sum += 1
        
print(f"there are {sum} vowels in this sentense")