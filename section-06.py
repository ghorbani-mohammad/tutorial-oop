# Encapsulation

# Using OOP in Python, we can restrict access to methods and variables.
# This prevents data from direct modification which is called encapsulation.
# In Python, we denote private attributes using underscore as the prefix i.e single _ or double __.
# Single _ means protected variables
# Double __ means private variables


class Computer:
    def __init__(self):
        self.__max_price = 900

    def sell(self):
        print(f"Selling Price: {self.__max_price}")

    def setMaxPrice(self, price):
        self.__max_price = price


c = Computer()
c.sell()

# change the price
c.__max_price = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()

# Output:
#   Selling Price: 900
#   Selling Price: 900
#   Selling Price: 1000


# Note that you can read the private variables but you can't write them directly
