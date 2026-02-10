# Task:
# 1. Create class Light
# 2. __init__ sets state = "OFF"
# 3. method turn_on() sets state = "ON"
# 4. method turn_off() sets state = "OFF"
# 5. method show() prints state
# 6. Create object and call: turn_on → show
class light:
    def __init__(self):
        self.state = "off"
    def turn_on(self):
        self.state ="on"
    def turn_off(self):
        self.state = "off"
    def show(self):
        print(f"The light is {self.state}")
a1 = light()
a1.turn_on()
a1.show()

        