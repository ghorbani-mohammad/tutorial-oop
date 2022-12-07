# Polymorphism is the ability to take many forms
# Suppose we start with the following code:
class Vehicle:
    def __str__(self):
        return "Object: Vehicle"


class Car(Vehicle):
    def __str__(self):
        return "Object: Car"


class Airplane(Vehicle):
    def __str__(self):
        return "Object: Airplane"


# Doesn't that feel like a lot of repetition? We should do better!
class Vehicle:
    def __str__(self) -> str:
        return f"Object: {self.__class__.__name__}"


class Car(Vehicle):
    pass


class Airplane(Vehicle):
    pass


obj = Car()
print(obj)
# Output: Object: Car
obj = Airplane()
print(obj)
# Output: Object: Airplane


# Notice the line 21, self dynamically has different shapes Car and Airplane
# Having different shapes in runtime called polymorphism
