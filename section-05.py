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


# The __init__ of the Car and Flyable classes accept a different number of parameters.
# If the FlyingCar class inherits from the Car and Flyable classes, its __init__ method needs to
# call the right __init__ method specified in the method order resolution __mro__ of the FlyingCar class.


class FlyingCar(Flyable, Car):
    def __init__(self, wing, door, wheel):
        super().__init__(wing)
        self.door = door
        self.wheel = wheel

    def start(self):
        return super().start()


# The super().__init__() calls the __init__ of the FlyingCar class.
# Therefore, you need to pass the wing argument to the __init__ method.
# Because the FlyingCar class cannot access the __init__ method of the Car class,
# you need to initialize the door and wheel attributes individually.
