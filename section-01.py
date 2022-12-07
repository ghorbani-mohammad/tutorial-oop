class Employee:
    def __init__(self, name, base_salary, years):
        self.name = name
        self.base_salary = base_salary
        self.years = years

    def salary(self):
        return self.base_salary + (self.years * 1000)


class Developer(Employee):
    """Developers are just regular employees

    Args:
        Employee (Employee): employee
    """

    pass
