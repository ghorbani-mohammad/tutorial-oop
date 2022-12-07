# Polymorphism is the ability to take many forms
# Suppose we start with the following code:
class Vehicle:
    def __str__(self) -> str:
        return "Object: Vehicle"


class Car:
    def __str__(self) -> str:
        return "Object: Car"
