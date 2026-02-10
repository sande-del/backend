# Task:
# 1. Create a class Counter
# 2. Start value at 0 in __init__
# 3. Add method increase() → add 1
# 4. Add method show() → print value
# 5. Call increase twice, then show
class conter:
    def __init__(self):
        self.count = 0
    def increase(self):
          self.count = self.count + 1
    def show(self):
        print(self.count)
a1 = conter()
a1.increase()
a1.increase()
a1.show()


