# Here we have another example about using super and overriding (check the previous section) but
# We also want to add polymorphism into it.


class Employee:
    BONUS_PER_YEAR = 1000

    def __init__(self, name, base_salary, years):
        self.name = name
        self.base_salary = base_salary
        self.years = years

    def salary(self):
        return self.base_salary + (self.years * self.BONUS_PER_YEAR)


class Developer(Employee):
    pass


class Manager(Employee):
    BONUS_PER_YEAR = 1500

    def salary(self):
        return super().salary() * 1.1

