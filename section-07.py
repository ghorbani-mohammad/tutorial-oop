class Base:
    def __init__(self):
        self._a = 2


class Derived(Base):
    def __init__(self):
        super().__init__()
        print("Calling protected member of base class: ", self._a)

        self._a = 3
        print("Calling modified protected member outside class: ", self._a)


obj1 = Derived()


obj2 = Base()

# Calling protected member
# Can be accessed but should not be done due to convention
print("Accessing protected member of obj1: ", obj1._a)

# Accessing the protected variable outside
print("Accessing protected member of obj2: ", obj2._a)


# Output:
#   Calling protected member of base class:  2
#   Calling modified protected member outside class:  3
#   Accessing protected member of obj1:  3
#   Accessing protected member of obj2:  2


class Base:
    def __init__(self):
        self.a = "public_member"
        self.__c = "private_member"


class Derived(Base):
    def __init__(self):
        super().__init__()
        print("Calling private member of base class: ", self.__c)
