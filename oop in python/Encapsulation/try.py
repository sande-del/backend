class Student:
    def __init__(self, marks):
        self.__marks = marks   # private

    # Getter
    def get_marks(self):
        return self.__marks

    # Setter with validation
    def set_marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self.__marks = new_marks
        else:
            print("Invalid marks")
s = Student(90)
print(s.get_marks())      # 90

s.set_marks(95)
print(s.get_marks())      # 95

s.set_marks(120)          # Invalid marks
print(s.get_marks())      # still 95
