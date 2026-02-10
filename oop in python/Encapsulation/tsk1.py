# Task: Easy Encapsulation
# 1. Create class Student
# 2. Private attribute __marks
# 3. Getter get_marks() → returns marks
# 4. Setter set_marks(m) → updates marks only if 0 <= m <= 100
# 5. Create object with marks 80
# 6. Print marks using getter
# 7. Update marks to 90 using setter
# 8. Print marks again
class student:
    def __init__(self,marks):
        if 0<= marks <=100:
         self.__marks =marks
        else:
            self.__marks = 0
            print("The marks is in negtive so it changed into 0")
    def get_marks(self):
        return self.__marks
    def set_marks(self,n_marks):
        if 0 <= n_marks <=100 :
            self.__marks = n_marks
        else:
            print("Invalid marks")
a1 = student(-9)
print(a1.get_marks())
a1.set_marks(90)
print(a1.get_marks())