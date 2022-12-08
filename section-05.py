class Car:
    def __init__(self, door, wheel):
        self.door = door
        self.wheel = wheel

    def start(self):
        print("Start the car")

    def go(self):
        print("Going")


class Flyable:
    def __init__(self, wing):
        self.wing = wing

    def start(self):
        print("Start the Flyable object")

    def fly(self):
        print("Flying")
