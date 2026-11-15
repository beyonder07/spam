class Vehicle:
    def general(self):
        print("vehicle")

class Car(Vehicle):
    def __init__(self):
        self.wheels = 4
        self.general()
        print("car")
        print("wheels:", self.wheels)

c = Car()

