# Polymorphism is the ability to take many forms
# Suppose we start with the following code:
class Vehicle:
    def __str__(self):
        return "Object: Vehicle"


class Car:
    def __str__(self):
        return "Object: Car"


class Airplane:
    def __str__(self):
        return "Object: Airplane"
